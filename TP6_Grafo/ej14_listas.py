ambientes = [
    {"value": "Cocina"},
    {"value": "Comedor"},
    {"value": "Cochera"},
    {"value": "Quincho"},
    {"value": "Baño 1"},
    {"value": "Baño 2"},
    {"value": "Habitación 1"},
    {"value": "Habitación 2"},
    {"value": "Sala de estar"},
    {"value": "Terraza"},
    {"value": "Patio"}
]

conexiones = [
    # Cocina (5 aristas)
    {"origin": "Cocina", "destination": "Comedor", "weight": 4},
    {"origin": "Cocina", "destination": "Quincho", "weight": 12},
    {"origin": "Cocina", "destination": "Baño 1", "weight": 8},
    {"origin": "Cocina", "destination": "Patio", "weight": 15},
    {"origin": "Cocina", "destination": "Cochera", "weight": 18},

    # Comedor (3 aristas)
    {"origin": "Comedor", "destination": "Sala de estar", "weight": 5},
    {"origin": "Comedor", "destination": "Habitación 1", "weight": 10},

    # Cochera (3 aristas)
    {"origin": "Cochera", "destination": "Patio", "weight": 6},
    {"origin": "Cochera", "destination": "Terraza", "weight": 20},

    # Quincho (3 aristas)
    {"origin": "Quincho", "destination": "Patio", "weight": 5},
    {"origin": "Quincho", "destination": "Terraza", "weight": 7},

    # Baño 1 (3 aristas - agregamos una nueva para cumplir la regla)
    {"origin": "Baño 1", "destination": "Habitación 1", "weight": 3},
    {"origin": "Baño 1", "destination": "Baño 2", "weight": 5},

    # Baño 2 (4 aristas)
    {"origin": "Baño 2", "destination": "Habitación 1", "weight": 4},
    {"origin": "Baño 2", "destination": "Habitación 2", "weight": 6},
    {"origin": "Baño 2", "destination": "Sala de estar", "weight": 9},

    # Habitación 1 (4 aristas)
    {"origin": "Habitación 1", "destination": "Habitación 2", "weight": 7},

    # Habitación 2 (4 aristas)
    {"origin": "Habitación 2", "destination": "Sala de estar", "weight": 5},
    {"origin": "Habitación 2", "destination": "Terraza", "weight": 11},

    # Sala de estar (4 aristas)
    {"origin": "Sala de estar", "destination": "Terraza", "weight": 8},

    # Terraza (5 aristas - ya tenía 5 en la original, pero nos aseguramos)
    {"origin": "Terraza", "destination": "Patio", "weight": 4},
]