// Cypher запрос для создания графа MDP из переходной модели
// Генерируется автоматически из MDP переходной модели

// Создаём все узлы (состояния)

CREATE (State_0:State {
    name: 0,
    terminal: false
})

CREATE (State_1:State {
    name: 1,
    terminal: false
})

CREATE (State_2:State {
    name: 2,
    terminal: false
})

CREATE (State_3:State {
    name: 3,
    terminal: false
})

CREATE (State_4:State {
    name: 4,
    terminal: false
})

CREATE (State_5:State {
    name: 5,
    terminal: true
})

CREATE (State_6:State {
    name: 6,
    terminal: false
})

CREATE (State_7:State {
    name: 7,
    terminal: true
})

CREATE (State_8:State {
    name: 8,
    terminal: false
})

CREATE (State_9:State {
    name: 9,
    terminal: false
})

CREATE (State_10:State {
    name: 10,
    terminal: false
})

CREATE (State_11:State {
    name: 11,
    terminal: true
})

CREATE (State_12:State {
    name: 12,
    terminal: true
})

CREATE (State_13:State {
    name: 13,
    terminal: false
})

CREATE (State_14:State {
    name: 14,
    terminal: false
})

CREATE (State_15:State {
    name: 15,
    terminal: true
})


// Создаём все связи (действия/переходы)



CREATE (State_0)-[:`0` {
    probability: 0.6666666666666666,
    reward: 0.0
}]->(State_0)

CREATE (State_0)-[:`0` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_4)



CREATE (State_0)-[:`1` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_0)

CREATE (State_0)-[:`1` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_4)

CREATE (State_0)-[:`1` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_1)



CREATE (State_0)-[:`2` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_4)

CREATE (State_0)-[:`2` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_1)

CREATE (State_0)-[:`2` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_0)



CREATE (State_0)-[:`3` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_1)

CREATE (State_0)-[:`3` {
    probability: 0.6666666666666666,
    reward: 0.0
}]->(State_0)





CREATE (State_1)-[:`0` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_1)

CREATE (State_1)-[:`0` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_0)

CREATE (State_1)-[:`0` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_5)



CREATE (State_1)-[:`1` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_0)

CREATE (State_1)-[:`1` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_5)

CREATE (State_1)-[:`1` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_2)



CREATE (State_1)-[:`2` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_5)

CREATE (State_1)-[:`2` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_2)

CREATE (State_1)-[:`2` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_1)



CREATE (State_1)-[:`3` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_2)

CREATE (State_1)-[:`3` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_1)

CREATE (State_1)-[:`3` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_0)





CREATE (State_2)-[:`0` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_2)

CREATE (State_2)-[:`0` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_1)

CREATE (State_2)-[:`0` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_6)



CREATE (State_2)-[:`1` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_1)

CREATE (State_2)-[:`1` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_6)

CREATE (State_2)-[:`1` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_3)



CREATE (State_2)-[:`2` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_6)

CREATE (State_2)-[:`2` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_3)

CREATE (State_2)-[:`2` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_2)



CREATE (State_2)-[:`3` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_3)

CREATE (State_2)-[:`3` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_2)

CREATE (State_2)-[:`3` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_1)





CREATE (State_3)-[:`0` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_3)

CREATE (State_3)-[:`0` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_2)

CREATE (State_3)-[:`0` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_7)



CREATE (State_3)-[:`1` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_2)

CREATE (State_3)-[:`1` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_7)

CREATE (State_3)-[:`1` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_3)



CREATE (State_3)-[:`2` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_7)

CREATE (State_3)-[:`2` {
    probability: 0.6666666666666666,
    reward: 0.0
}]->(State_3)



CREATE (State_3)-[:`3` {
    probability: 0.6666666666666666,
    reward: 0.0
}]->(State_3)

CREATE (State_3)-[:`3` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_2)





CREATE (State_4)-[:`0` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_0)

CREATE (State_4)-[:`0` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_4)

CREATE (State_4)-[:`0` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_8)



CREATE (State_4)-[:`1` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_4)

CREATE (State_4)-[:`1` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_8)

CREATE (State_4)-[:`1` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_5)



CREATE (State_4)-[:`2` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_8)

CREATE (State_4)-[:`2` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_5)

CREATE (State_4)-[:`2` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_0)



CREATE (State_4)-[:`3` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_5)

CREATE (State_4)-[:`3` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_0)

CREATE (State_4)-[:`3` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_4)





CREATE (State_5)-[:`0` {
    probability: 1.0,
    reward: 0
}]->(State_5)



CREATE (State_5)-[:`1` {
    probability: 1.0,
    reward: 0
}]->(State_5)



CREATE (State_5)-[:`2` {
    probability: 1.0,
    reward: 0
}]->(State_5)



CREATE (State_5)-[:`3` {
    probability: 1.0,
    reward: 0
}]->(State_5)





CREATE (State_6)-[:`0` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_2)

CREATE (State_6)-[:`0` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_5)

CREATE (State_6)-[:`0` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_10)



CREATE (State_6)-[:`1` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_5)

CREATE (State_6)-[:`1` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_10)

CREATE (State_6)-[:`1` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_7)



CREATE (State_6)-[:`2` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_10)

CREATE (State_6)-[:`2` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_7)

CREATE (State_6)-[:`2` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_2)



CREATE (State_6)-[:`3` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_7)

CREATE (State_6)-[:`3` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_2)

CREATE (State_6)-[:`3` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_5)





CREATE (State_7)-[:`0` {
    probability: 1.0,
    reward: 0
}]->(State_7)



CREATE (State_7)-[:`1` {
    probability: 1.0,
    reward: 0
}]->(State_7)



CREATE (State_7)-[:`2` {
    probability: 1.0,
    reward: 0
}]->(State_7)



CREATE (State_7)-[:`3` {
    probability: 1.0,
    reward: 0
}]->(State_7)





CREATE (State_8)-[:`0` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_4)

CREATE (State_8)-[:`0` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_8)

CREATE (State_8)-[:`0` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_12)



CREATE (State_8)-[:`1` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_8)

CREATE (State_8)-[:`1` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_12)

CREATE (State_8)-[:`1` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_9)



CREATE (State_8)-[:`2` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_12)

CREATE (State_8)-[:`2` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_9)

CREATE (State_8)-[:`2` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_4)



CREATE (State_8)-[:`3` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_9)

CREATE (State_8)-[:`3` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_4)

CREATE (State_8)-[:`3` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_8)





CREATE (State_9)-[:`0` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_5)

CREATE (State_9)-[:`0` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_8)

CREATE (State_9)-[:`0` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_13)



CREATE (State_9)-[:`1` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_8)

CREATE (State_9)-[:`1` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_13)

CREATE (State_9)-[:`1` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_10)



CREATE (State_9)-[:`2` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_13)

CREATE (State_9)-[:`2` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_10)

CREATE (State_9)-[:`2` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_5)



CREATE (State_9)-[:`3` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_10)

CREATE (State_9)-[:`3` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_5)

CREATE (State_9)-[:`3` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_8)





CREATE (State_10)-[:`0` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_6)

CREATE (State_10)-[:`0` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_9)

CREATE (State_10)-[:`0` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_14)



CREATE (State_10)-[:`1` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_9)

CREATE (State_10)-[:`1` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_14)

CREATE (State_10)-[:`1` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_11)



CREATE (State_10)-[:`2` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_14)

CREATE (State_10)-[:`2` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_11)

CREATE (State_10)-[:`2` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_6)



CREATE (State_10)-[:`3` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_11)

CREATE (State_10)-[:`3` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_6)

CREATE (State_10)-[:`3` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_9)





CREATE (State_11)-[:`0` {
    probability: 1.0,
    reward: 0
}]->(State_11)



CREATE (State_11)-[:`1` {
    probability: 1.0,
    reward: 0
}]->(State_11)



CREATE (State_11)-[:`2` {
    probability: 1.0,
    reward: 0
}]->(State_11)



CREATE (State_11)-[:`3` {
    probability: 1.0,
    reward: 0
}]->(State_11)





CREATE (State_12)-[:`0` {
    probability: 1.0,
    reward: 0
}]->(State_12)



CREATE (State_12)-[:`1` {
    probability: 1.0,
    reward: 0
}]->(State_12)



CREATE (State_12)-[:`2` {
    probability: 1.0,
    reward: 0
}]->(State_12)



CREATE (State_12)-[:`3` {
    probability: 1.0,
    reward: 0
}]->(State_12)





CREATE (State_13)-[:`0` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_9)

CREATE (State_13)-[:`0` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_12)

CREATE (State_13)-[:`0` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_13)



CREATE (State_13)-[:`1` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_12)

CREATE (State_13)-[:`1` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_13)

CREATE (State_13)-[:`1` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_14)



CREATE (State_13)-[:`2` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_13)

CREATE (State_13)-[:`2` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_14)

CREATE (State_13)-[:`2` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_9)



CREATE (State_13)-[:`3` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_14)

CREATE (State_13)-[:`3` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_9)

CREATE (State_13)-[:`3` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_12)





CREATE (State_14)-[:`0` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_10)

CREATE (State_14)-[:`0` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_13)

CREATE (State_14)-[:`0` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_14)



CREATE (State_14)-[:`1` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_13)

CREATE (State_14)-[:`1` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_14)

CREATE (State_14)-[:`1` {
    probability: 0.3333333333333333,
    reward: 1.0
}]->(State_15)



CREATE (State_14)-[:`2` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_14)

CREATE (State_14)-[:`2` {
    probability: 0.3333333333333333,
    reward: 1.0
}]->(State_15)

CREATE (State_14)-[:`2` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_10)



CREATE (State_14)-[:`3` {
    probability: 0.3333333333333333,
    reward: 1.0
}]->(State_15)

CREATE (State_14)-[:`3` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_10)

CREATE (State_14)-[:`3` {
    probability: 0.3333333333333333,
    reward: 0.0
}]->(State_13)





CREATE (State_15)-[:`0` {
    probability: 1.0,
    reward: 0
}]->(State_15)



CREATE (State_15)-[:`1` {
    probability: 1.0,
    reward: 0
}]->(State_15)



CREATE (State_15)-[:`2` {
    probability: 1.0,
    reward: 0
}]->(State_15)



CREATE (State_15)-[:`3` {
    probability: 1.0,
    reward: 0
}]->(State_15)


