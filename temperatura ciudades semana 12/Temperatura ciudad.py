#matriz 3D

temperaturas = [
    [   #Quito
        [   # Semana 1
            {"día": "Lunes", "temp": 10},
            {"día": "Martes", "temp": 8},
            {"día": "Miércoles", "temp": 14},
            {"día": "Jueves", "temp": 12},
            {"día": "Viernes", "temp": 22},
            {"día": "Sábado", "temp": 18},
            {"día": "Domingo", "temp": 20}
    ],
        [   # Semana 2
            {"día": "Lunes", "temp": 25},
            {"día": "Martes", "temp": 27},
            {"día": "Miércoles", "temp": 18},
            {"día": "Jueves", "temp": 14},
            {"día": "Viernes", "temp": 20},
            {"día": "Sábado", "temp": 21},
            {"día": "Domingo", "temp": 16}
        ],
        [   # Semana 3
            {"día": "Lunes", "temp": 13},
            {"día": "Martes", "temp": 15},
            {"día": "Miércoles", "temp": 23},
            {"día": "Jueves", "temp": 17},
            {"día": "Viernes", "temp": 25},
            {"día": "Sábado", "temp": 21},
            {"día": "Domingo", "temp": 16}
        ],
        [   # Semana 4
            {"día": "Lunes", "temp": 15},
            {"día": "Martes", "temp": 17},
            {"día": "Miércoles", "temp": 13},
            {"día": "Jueves", "temp": 22},
            {"día": "Viernes", "temp": 24},
            {"día": "Sábado", "temp": 26},
            {"día": "Domingo", "temp": 20}
        ]
    ],
    [   # Guayaquil
        [   # Semana 1
            {"día": "Lunes", "temp": 22},
            {"día": "Martes", "temp": 25},
            {"día": "Miércoles", "temp": 30},
            {"día": "Jueves", "temp": 34},
            {"día": "Viernes", "temp": 26},
            {"día": "Sábado", "temp": 29},
            {"día": "Domingo", "temp": 27}
        ],
        [   # Semana 2
            {"día": "Lunes", "temp": 23},
            {"día": "Martes", "temp": 32},
            {"día": "Miércoles", "temp": 33},
            {"día": "Jueves", "temp": 24},
            {"día": "Viernes", "temp": 29},
            {"día": "Sábado", "temp": 26},
            {"día": "Domingo", "temp": 20}
        ],
        [   # Semana 3
            {"día": "Lunes", "temp": 36},
            {"día": "Martes", "temp": 27},
            {"día": "Miércoles", "temp": 21},
            {"día": "Jueves", "temp": 35},
            {"día": "Viernes", "temp": 24},
            {"día": "Sábado", "temp": 29},
            {"día": "Domingo", "temp": 30}
        ],
        [   # Semana 4
            {"día": "Lunes", "temp": 26},
            {"día": "Martes", "temp": 27},
            {"día": "Miércoles", "temp": 29},
            {"día": "Jueves", "temp": 35},
            {"día": "Viernes", "temp": 20},
            {"día": "Sábado", "temp": 28},
            {"día": "Domingo", "temp": 36}
        ]
    ],
    [   # San Miguel de los Bancos
        [   # Semana 1
            {"día": "Lunes", "temp": 16},
            {"día": "Martes", "temp": 18},
            {"día": "Miércoles", "temp": 21},
            {"día": "Jueves", "temp": 24},
            {"día": "Viernes", "temp": 20},
            {"día": "Sábado", "temp": 15},
            {"día": "Domingo", "temp": 17}
        ],
        [   # Semana 2
            {"día": "Lunes", "temp": 22},
            {"día": "Martes", "temp": 19},
            {"día": "Miércoles", "temp": 14},
            {"día": "Jueves", "temp": 23},
            {"día": "Viernes", "temp": 16},
            {"día": "Sábado", "temp": 24},
            {"día": "Domingo", "temp": 18}
        ],
        [   # Semana 3
            {"día": "Lunes", "temp": 23},
            {"día": "Martes", "temp": 18},
            {"día": "Miércoles", "temp": 19},
            {"día": "Jueves", "temp": 22},
            {"día": "Viernes", "temp": 21},
            {"día": "Sábado", "temp": 23},
            {"día": "Domingo", "temp": 20}
        ],
        [   # Semana 4
            {"día": "Lunes", "temp": 15},
            {"día": "Martes", "temp": 18},
            {"día": "Miércoles", "temp": 23},
            {"día": "Jueves", "temp": 17},
            {"día": "Viernes", "temp": 20},
            {"día": "Sábado", "temp": 25},
            {"día": "Domingo", "temp": 19}
        ]
    ]
]

ciudades = ["Quito ", "Guayaquil", "San Miguel de los Bancos"]
for ciudad_idx, ciudad  in enumerate(temperaturas):
    for semana_idx, semana in enumerate(ciudad):
        suma_temperaturas =sum([dia["temp"] for dia in semana])
        promedio= suma_temperaturas / len(semana)
        print(f"promedio de temperatura en {ciudades[ciudad_idx]}, semana {semana_idx + 1}: {promedio:.2f}°c")