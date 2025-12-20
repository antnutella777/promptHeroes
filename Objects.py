class Jogador:
    def __init__(self):
        self.prop   = {}
        self.stats  = {}
        self.items  = {}

        self.inventario = []
        for l in range(4):
            linha = []
            for c in range(6):
                linha.append(None)
            self.inventario.append(linha)

        self.prop   ["Raca"] = None
        self.prop   ["Nome"] = None
        self.prop   ["Sexo"] = None
        self.prop   ["Cofirm"] = None

        self.stats  ["Vida"]= None
        self.stats  ["MXVida"]= None
        self.stats  ["Mana"]= None
        self.stats  ["MXMana"]= None
        self.stats  ["Nivel"]= None
        self.stats  ["XP"]= None
        self.stats  ["MXDamage"] = None
        self.stats  ["Damage"] = None

        self.items  ["Arma"]        = None
        self.items  ["Capacete"]    = None
        self.items  ["Peitoral"]    = None
        self.items  ["Pernas"]      = None
        self.items  ["Botas"]       = None
        self.items  ["Anel"]        = None
        self.items  ["Colar"]       = None

    def atack():
        damage = self.stats["Damage"] 

class Enemy:
    def __init__(self):
        self.prop   = {}
        self.stats  = {}

        self.prop   ["Nome"]    = None
        self.prop   ["Raça"]    = None
        self.stats  ["Vida"]    = None
        self.stats  ["Damage"]  = None
        self.stats  ["LVL"]     = None



class Items:
    def __init__(self):
        self.prop   = {}
        self.stats  = {}

        self.prop   ["Nome"] = None
        self.prop   ["Tipo"] = None
        self.prop   ["Corfirm"] = None
        self.stats  ["DEF"]  = None
        self.stats  ["MXDEF"]  = None
        self.stats  ["MXATK"]  = None
        self.stats  ["ATK"]  = None
        self.stats  ["LVL"]  = None
