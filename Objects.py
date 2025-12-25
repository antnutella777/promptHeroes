import random, math, Funcs

f = Funcs

class Jogador:
    def __init__(self):
        self.prop   = {}
        self.stats  = {}
        self.items  = {}
        self.resorces = {}
        self.inventario = []
        for l in range(4):
            linha = []
            for c in range(6):
                linha.append(None)
            self.inventario.append(linha)

        self.prop   ["Raca"]        = None
        self.prop   ["Nome"]        = None
        self.prop   ["Sexo"]        = None
        self.prop   ["Cofirm"]      = None


        self.stats  ["Vida"]        = None
        self.stats  ["MXVida"]      = None
        self.stats  ["Mana"]        = None
        self.stats  ["MXMana"]      = None
        self.stats  ["Nivel"]       = None
        self.stats  ["mxXP"]        = None
        self.stats  ["XP"]          = None
        self.stats  ["MXDamage"]    = None
        self.stats  ["Damage"]      = None
        self.stats  ["critPercent"] = None

        self.items  ["Arma"]        = None
        self.items  ["Capacete"]    = None
        self.items  ["Peitoral"]    = None
        self.items  ["Pernas"]      = None
        self.items  ["Botas"]       = None
        self.items  ["Anel"]        = None
        self.items  ["Colar"]       = None

        self.resorces   ["cash"]        = 0
        self.resorces   ["couro"]       = 0
        self.resorces   ["ferro"]       = 0
        self.resorces   ["diamante"]    = 0

    def atack(self,obj):
        critChance = random.randint(0,100)
        dano = 0
        chance = ""

        match critChance:
            case x if x <=20:
                dano = 0
                chance = "Voce Errou\n"
            case x if x <= 84:
                dano = self.stats["Damage"]
                chance = "Voce tirou {} de dano!!\n".format(dano)
            case _:
                dano = self.stats["Damage"]  + (self.stats["Damage"] * (self.stats["critPercent"] / 100))
                chance = "Critico {} !!\n".format(dano)
        obj.stats["Vida"] -= dano
        f.typeTx(chance)
    def addItems(self,item):
            for l in range(len(self.inventario)):
                for c in range(len(self.inventario[l])):
                    if self.inventario is None:
                        self.inventario[l][c] = item
    def listarItens(self):
        print("=== ITENS NO INVENTÁRIO ===")

        for linha in self.inventario:
            for item in linha:
                print(f"- {item.prop['Nome']}")

class Enemy:
    def __init__(self):
        self.prop   = {}
        self.stats  = {}

        self.prop   ["Nome"]    = None
        self.prop   ["Raça"]    = None
        self.stats  ["Vida"]    = None
        self.stats  ["Damage"]  = None
        self.stats  ["LVL"]     = None
        self.stats  ["critPercent"] = None

    def atack(self,obj):
        critChance = random.randint(0,100)
        dano = 0
        chance = ""

        match critChance:
            case x if x <=20:
                dano = 0
                chance = self.prop["Nome"]  + " Errou\n"
            case x if x <= 84:
                dano = self.stats["Damage"]
                chance = self.prop["Nome"] + " tirou {} do seu HP !!\n".format(dano)
            case _:
                dano = self.stats["Damage"]  + (self.stats["Damage"] * (self.stats  ["critPercent"] / 100))
                chance = self.prop["Nome"] + " te deu um critico {} !!\n".format(dano)
        obj.stats["Vida"] -= dano
        f.typeTx(chance)

class Items:
    def __init__(self):
        self.prop   = {}
        self.stats  = {}

        self.prop   ["Nome"]    = None
        self.prop   ["Tipo"]    = None
        self.prop   ["Desc"]    = None
        self.prop   ["fxTaget"] = None
        self.prop   ["Preço"]   = None
        self.stats  ["DEF"]     = None
        self.stats  ["MXDEF"]   = None
        self.stats  ["MXATK"]   = None
        self.stats  ["ATK"]     = None
        self.stats  ["LVL"]     = None
        self.stats  ["Efects"]  = None

