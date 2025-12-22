import random, math, Funcs

f = Funcs

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
        self.stats  ["critPercent"] = None

        self.items  ["Arma"]        = None
        self.items  ["Capacete"]    = None
        self.items  ["Peitoral"]    = None
        self.items  ["Pernas"]      = None
        self.items  ["Botas"]       = None
        self.items  ["Anel"]        = None
        self.items  ["Colar"]       = None

    def atack(self,obj):
        critChance = random.randint(0,100)
        dano = 0
        chance = ""

        match critChance:
            case x if x <=20:
                dano = 0
                chance = "Voce Errou"
            case x if x <= 84:
                dano = self.stats["Damage"] 
                chance = "Acertou {} !!".format(dano)
            case _:
                dano = self.stats["Damage"]  + (self.stats["Damage"] * (self.stats["critPercent"] / 100))    
                chance = "Critico {} !!".format(dano)
        obj.stats["Vida"] -= dano
        f.typeTx(chance)

class Enemy:
    def __init__(self):
        self.prop   = {}
        self.stats  = {}

        self.prop   ["Nome"]    = None
        self.prop   ["Raça"]    = None
        self.stats  ["Vida"]    = None
        self.stats  ["Damage"]  = None
        self.stats  ["LVL"]     = None
    
    def atack(self,obj):
        critChance = random.randint(0,100)
        dano = 0
        chance = ""

        match critChance:
            case x if x <=20:
                dano = 0
                chance = "Voce Errou"
            case x if x <= 84:
                dano = self.stats["Damage"] 
                chance = "Acertou {} !!".format(dano)
            case _:
                dano = self.stats["Damage"]  + (self.stats["Damage"] * (critPercent / 100))    
                chance = "Critico {} !!".format(dano)
        obj.stats["Vida"] -= dano
        f.typeTx(chance)


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
