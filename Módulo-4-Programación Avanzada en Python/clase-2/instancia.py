class Taza:
    sizes = {
        "small": "pequeño",
        "medium": "mediano",
        "large": "grande"
    }
    def __init__(self):
        self.size = self.sizes["small"]

class Maquina:
    def __init__(self, _tipo_cafe, _cantidad_agua, _cantidad_cafe):
        self.tipo_cafe = _tipo_cafe
        self.cantidad_agua = _cantidad_agua
        self.cantidad_cafe = _cantidad_cafe

class Cafe:
    tipos_cafe = {
        "grano_corto": "grano_corto",
        "grano_mocha": "grano_mocha",
        "grano_intenso": "grano_intenso" 
    }

    def __init__(self):
        self.tipo_cafe = self.tipos_cafe["grano_corto"]

class Leche:
    tipos_leche = {
        "entera": "entera",
        "semi_descremada": "semi_descremada",
        "descremada": "descremada",
        "almendra": "almendra"
    }

    def __init__(self):
        self.tipo_leche = self.tipos_leche["entera"]
