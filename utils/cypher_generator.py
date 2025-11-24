from typing import Dict, List, Tuple, Optional
from pathlib import Path
from jinja2 import Environment, FileSystemLoader, select_autoescape

# Тип для переходной модели MDP: P[state][action] = [(prob, next_state, reward, done), ...]
MDPTransitionModel = Dict[int, Dict[int, List[Tuple[float, int, float, bool]]]]


def _aggregate_transitions(P: MDPTransitionModel) -> MDPTransitionModel:
    """
    Агрегирует переходы с одинаковыми (state, action, next_state), суммируя вероятности.
    
    Args:
        P: Переходная модель MDP.
        
    Returns:
        Агрегированная переходная модель MDP.
    """
    aggregated_P = {}
    
    for state_id in range(len(P)):
        aggregated_P[state_id] = {}
        
        for action_id, transitions in P[state_id].items():
            # Словарь для агрегации: (next_state, reward, done) -> суммарная вероятность
            aggregated_transitions = {}
            
            for prob, next_state, reward, done in transitions:
                key = (next_state, reward, done)
                
                if key in aggregated_transitions:
                    aggregated_transitions[key] += prob
                else:
                    aggregated_transitions[key] = prob
            
            # Преобразуем обратно в список кортежей
            aggregated_P[state_id][action_id] = [
                (prob, next_state, reward, done)
                for (next_state, reward, done), prob in aggregated_transitions.items()
            ]
    
    return aggregated_P


def _determine_terminal_states(P: MDPTransitionModel) -> List[str]:
    """
    Определяет терминальные состояния в MDP.
    
    Состояние считается терминальным, если:
    - Все переходы из него имеют флаг done=True
    - Или нет исходящих переходов
    
    Args:
        P: Переходная модель MDP.
        
    Returns:
        Список строк 'true'/'false' для использования в Cypher запросе.
    """
    terminal_states = []
    
    for state_id in range(len(P)):
        is_terminal = True
        
        # Проверяем все переходы из состояния
        for action_id in P[state_id].keys():
            for prob, next_state, reward, done in P[state_id][action_id]:
                # Если хотя бы один переход не терминальный, состояние не терминальное
                if not done:
                    is_terminal = False
                    break
            if not is_terminal:
                break
        
        # Преобразуем в строку для Cypher (true/false в нижнем регистре)
        terminal_states.append('true' if is_terminal else 'false')
    
    return terminal_states


def _generate_state_names(
    P: MDPTransitionModel,
    state_names: Optional[Dict[int, str]] = None
) -> Dict[int, str]:
    """
    Генерирует названия состояний.
    
    Args:
        P: Переходная модель MDP.
        state_names: Опциональный словарь с названиями состояний. Если None, генерируются автоматически.
        
    Returns:
        Словарь {state_id: state_name}
    """
    if state_names is None:
        state_names = {state_id: f"State_{state_id}" for state_id in range(len(P))}
    return state_names


def generate_cypher_query(
    P: MDPTransitionModel,
    template_path: str = None,
    state_names: Optional[Dict[int, str]] = None,
    aggregate: bool = True
) -> str:
    """
    Генерирует Cypher запрос для создания графа MDP в Neo4j.
    
    Args:
        P: Переходная модель MDP.
        template_path: Путь к шаблону Jinja2. Если None, используется шаблон по умолчанию.
        state_names: Опциональный словарь с названиями состояний {state_id: name}.
                     Если None, генерируются автоматически как "State_0", "State_1", ...
        aggregate: Если True, агрегирует переходы с одинаковыми (state, action, next_state).
        
    Returns:
        Строка с Cypher запросом.
    """
    # Агрегируем переходы, если нужно
    if aggregate:
        P = _aggregate_transitions(P)
    
    # Определяем путь к шаблону
    if template_path is None:
        project_root = Path(__file__).parent.parent
        template_path = project_root / "templates" / "mdp_to_cypher.j2"
    
    template_dir = Path(template_path).parent
    template_name = Path(template_path).name
    
    # Настраиваем Jinja2 окружение
    env = Environment(
        loader=FileSystemLoader(str(template_dir)),
        autoescape=select_autoescape(['html', 'xml'])
    )
    
    # Загружаем шаблон
    template = env.get_template(template_name)
    
    # Определяем терминальные состояния
    terminal_states = _determine_terminal_states(P)
    
    # Генерируем названия состояний
    state_names_dict = _generate_state_names(P, state_names)
    
    # Создаём список состояний для итерации в шаблоне
    states = list(range(len(P)))
    
    # Рендерим шаблон
    cypher_query = template.render(
        P=P,
        states=states,
        terminal_states=terminal_states,
        state_names=state_names_dict
    )
    
    return cypher_query


def save_cypher_query(
    P: MDPTransitionModel,
    output_path: str,
    template_path: str = None,
    state_names: Optional[Dict[int, str]] = None,
    aggregate: bool = True
) -> None:
    """
    Генерирует и сохраняет Cypher запрос в файл.
    
    Args:
        P: Переходная модель MDP.
        output_path: Путь для сохранения Cypher запроса.
        template_path: Путь к шаблону Jinja2. Если None, используется шаблон по умолчанию.
        state_names: Опциональный словарь с названиями состояний {state_id: name}.
        aggregate: Если True, агрегирует переходы с одинаковыми (state, action, next_state).
    """
    cypher_query = generate_cypher_query(P, template_path, state_names, aggregate)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(cypher_query)


if __name__ == "__main__":
    # Пример использования
    import gym
    
    # Загружаем MDP из gym
    P: MDPTransitionModel = gym.make('FrozenLake-v1').env.P
    
    # Генерируем Cypher запрос с агрегацией
    cypher_query = generate_cypher_query(P, aggregate=True)
    
    print("Сгенерированный Cypher запрос:")
    print("=" * 50)
    print(cypher_query)
    print("=" * 50)
    
    # Сохраняем в файл
    save_cypher_query(P, "mdp_graph.cypher", aggregate=True)
    print("\nЗапрос сохранён в файл: mdp_graph.cypher")

