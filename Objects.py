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
    def addItems(self,item,amount): 
        for l in range(len(self.inventario)):  
            for c in range(len(self.inventario[l])):
                slot = self.inventario[l][c]
                if slot is not None and slot.prop["Name"] == item.prop["Name"]:
                    if not slot.prop["Stack"]:
                        continue
                    maxStack = slot.stats["maxStack"]
                    curent = slot.stats["Amount"]

                    space = maxStack - curent

                    if space <= 0:
                        continue

                    toAdd = min(space,amount)

                    slot.stats["Amount"] += toAdd

                    amount -= toAdd

                    if amount == 0:
                        return
        
        for l in range(len(self.inventario)):  
            for c in range(len(self.inventario[l])):
                if self.inventario[l][c] is None:
                    newItem = item
                    maxStack = item.stats["maxStack"]

                    toAdd = min(amount,maxStack)
                    
                    newItem.stats["Amount"] = toAdd
                    self.inventario[l][c] = newItem

                    amount -= toAdd

                    if amount == 0:
                        return

                             
                            
                                
                      
    def listarItens(self):
        print("=== ITENS NO INVENTÁRIO ===")

        for linha in self.inventario:
            for item in linha:
                if item != None:
                    print("-{} ({})".format(item.prop["Name"],item.stats["Amount"]))
    def playerInfo(self):
        f.typeTx("======{}======\n".format(self.prop["Nome"]))
        f.typeTx("Raca: {}\n".format(self.prop["Raca"]))
        f.typeTx("Nivel {}\n".format(self.stats["Nivel"]))
        f.typeTx("XP:   {}/{}\n".format(self.stats["XP"],self.stats["mxXP"]))
        f.typeTx("Vida: {}/{}\n".format(self.stats["Vida"],self.stats["MXVida"]))
        f.typeTx("Mana: {}/{}\n".format(self.stats["Mana"],self.stats["MXMana"]))
        f.typeTx("Nivel {}\n")
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

        self.prop   ["Name"]            = None
        self.prop   ["Type"]            = None
        self.prop   ["Description"]     = None
        self.prop   ["fxTarget"]        = None
        self.prop   ["Price"]           = None
        self.prop   ["Stack"]           = None

        self.stats  ["maxStack"]        = None
        self.stats  ["Amount"]           = None   
        self.stats  ["DEF"]             = None
        self.stats  ["MXDEF"]           = None
        self.stats  ["MXATK"]           = None
        self.stats  ["ATK"]             = None
        self.stats  ["LVL"]             = None
        self.stats  ["Effects"]         = None
    def use(self,player):
        if self.prop["Type"]== "consumable":
            match self.prop["fxTarget"]:
                case "Life":
                    player.stats["Vida"] += self.stats["Effects"]
                    f.typeTx("Você Recuperou {} de Vida!!!\n".format(self.stats["Effects"]))
    def itemInfo(self):
        f.typeTx("=======Infomaçoes do Item=======\n")
        f.typeTx("Nome: {}\n".format(self.prop["Name"]))
        f.typeTx("Tipo: {}\n".format(self.prop["Type"]))
        f.typeTx("Descrição: {}\n".format(self.prop["Description"]))
        

