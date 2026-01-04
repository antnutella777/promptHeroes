import random, math, Funcs
from colorData import *
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
        self.prop   ["Skills"]      = None
       

        self.stats  ["Vida"]        = None
        self.stats  ["MXVida"]      = None
        self.stats  ["DEF"]         = None
        self.stats  ["Mana"]        = None
        self.stats  ["MXMana"]      = None
        self.stats  ["Nivel"]       = None
        self.stats  ["mxXP"]        = None
        self.stats  ["XP"]          = None
        self.stats  ["MXDamage"]    = None
        self.stats  ["Damage"]      = None
        self.stats  ["critPercent"] = None

        self.items  ["Arma"]        = None
        self.items  ["Head"]        = None
        self.items  ["Chest"]       = None
        self.items  ["Legs"]        = None
        self.items  ["Foots"]       = None
        self.items  ["Anel"]        = None
        self.items  ["Ring"]        = None

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
        f.clear()
        f.typeTx(chance,"red")
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

                    
                    self.inventario[l][c].stats["Amount"] += toAdd 
                    amount -= toAdd
                    
                    if amount == 0:
                        return
        
        for l in range(len(self.inventario)):  
            for c in range(len(self.inventario[l])):
                if self.inventario[l][c] is None:
                    newItem = item.clone()
                    maxStack = item.stats["maxStack"]

                    toAdd = min(amount,maxStack)
                    
                    newItem.stats["Amount"] = toAdd
                    self.inventario[l][c] = newItem

                    amount -= toAdd

                    if amount == 0:
                        return                                     
    def listarItens(self):
        print("=== INVENTÁRIO ===")
        itemList = []
        for linha in self.inventario:
            for item in linha:
                if item != None:
                    print("-{} ({})".format(item.prop["Name"],item.stats["Amount"]))
                    itemList.append(item)
        return itemList            
    def info(self):
        f.typeTx("======{}======\n".format(self.prop["Nome"]),"red")
        f.typeTx("Raca: {}\n".format(self.prop["Raca"]),"cyan")
        f.typeTx("Nivel {}\n".format(self.stats["Nivel"]),"cyan")
        f.typeTx("XP:   {}/{}\n".format(self.stats["XP"],self.stats["mxXP"]),"yellow")
        f.typeTx("Vida: {}/{}\n".format(self.stats["Vida"],self.stats["MXVida"]),"green")
        f.typeTx("Mana: {}/{}\n".format(self.stats["Mana"],self.stats["MXMana"]),"magenta")      
class Enemy:
    def __init__(self):
        self.prop   = {}
        self.stats  = {}

        self.prop   ["Name"]    = None
        self.prop   ["Raca"]    = None
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
                chance = self.prop["Name"]  + " Errou\n"
            case x if x <= 84:
                dano = self.stats["Damage"]
                chance = self.prop["Name"] + " tirou {} do seu HP !!\n".format(dano)
            case _:
                dano = self.stats["Damage"]  + (self.stats["Damage"] * (self.stats  ["critPercent"] / 100))
                chance = self.prop["Name"] + " te deu um critico {} !!\n".format(dano)
        obj.stats["Vida"] -= dano
        f.typeTx(chance,"red")
    def info(self):
        f.typeTx("======{}======\n".format(self.prop["Name"]),"red")
        f.typeTx("Raca:  {}\n".format(self.prop["Raca"]),"cyan")
        f.typeTx("Nivel: {}\n".format(self.stats["LVL"]),"cyan")
        f.typeTx("Vida:  {}\n".format(self.stats["Vida"]),"blue")
        f.typeTx("Dano:  {}\n".format(self.stats["Damage"]),"blue")
        f.typeTx("Crit(%): %{}\n".format(self.stats["critPercent"]),"blue")    
class Items:
    def __init__(self):
        self.prop   = {}
        self.stats  = {}

        self.prop   ["Name"]            = None
        self.prop   ["Type"]            = None
        self.prop   ["Description"]     = None
        self.prop   ["eqTarget"]        = None
        self.prop   ["fxTarget"]        = None
        self.prop   ["Price"]           = None
        self.prop   ["Stack"]           = None
        self.prop   ["Rarity"]          = None
        self.stats  ["maxStack"]        = None
        self.stats  ["Amount"]          = None   
        self.stats  ["DEF"]             = None
        self.stats  ["ATK"]             = None
        self.stats  ["LVL"]             = None
        self.stats  ["Effects"]         = None
    def use(self,player,l,c):
        if self.prop["Type"]== "consumable":
            match self.prop["fxTarget"]:
                case "Life":
                    player.stats["Vida"] += self.stats["Effects"]
                    f.typeTx("Você Recuperou {} de Vida!!!\n".format(self.stats["Effects"]),"green")
                    if player.inventario[l][c].stats["Amount"] > 0:
                        self.stats["Amount"] -= 1 
                            
                    
                    if player.inventario[l][c].stats["Amount"] <= 0:
                        player.inventario[l][c].stats["Amount"] = None
               
                    
                    if player.stats["Vida"] >= player.stats["MXVida"]:
                        player.stats["Vida"] = player.stats["MXVida"]                                   
        else:
            f.typeTx("Esse item não é concumivel\n","red")
    def equip(self,player):
        if self.prop["Type"] == "equipable":
            match self.prop["eqTarget"]:
                case "Head":
                    if player.items["Head"] is None:
                        player.items["Head"]  = self
                    else:
                        itemAtual = player.items["Head"]
                        player.stats["DEF"] -= itemAtual.stats["DEF"]
                        player.addItems(itemAtual,1)
                        player.items["Head"]  = self
                    player.stats["DEF"] += self.stats["DEF"]    

                case "Chest":
                    if player.items["Chest"] is None:
                        player.items["Chest"]  = self
                    else:
                        itemAtual = player.items["Chest"]
                        player.stats["DEF"] -= itemAtual.stats["DEF"]
                        player.addItems(itemAtual,1)
                        player.items["Chest"]  = self
                    player.stats["DEF"] += self.stats["DEF"] 
                case "Legs":
                    player.items["Legs"] = self 
                    player.items["DEF"]   += self.stats["DEF"]  
                case "Foots":



    def info(self):
        f.clear()
        f.typeTx("=======Infomaçoes do Item=======\n","cyan")
        f.typeTx("Nome: {}\n".format(self.prop["Name"]),"yellow")
        f.typeTx("Tipo: {}\n".format(self.prop["Type"]),"red")
        f.typeTx("Descrição: {}\n".format(self.prop["Description"]),"magenta")
    def clone(self):
        import copy
        return copy.deepcopy(self)           
class Skill:
   def __init__(self):
        self.prop = {}
        self.stasts = {}

        self.prop["Nome"]   = None
        self.prop["Tipo"]   = None
        self.prop["Custo"]  = None
        self.prop["Cool"]   = None
        self.prop["Req"]    = None
        self.prop["Stado"]  = None

