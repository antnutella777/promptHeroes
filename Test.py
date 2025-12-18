
import math, time, os

class Jogador:
    def __init__(self):
        self.prop   = {}
        self.stats  = {}
        self.items  = {}
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

        self.items  ["Arma"] = None
    
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

j = Jogador()
i =  Items()

j.prop   ["Raca"] = "Human"
j.prop   ["Nome"] = "Andre"
j.prop   ["Sexo"] = "Masculino"
j.prop   ["Cofirm"] = "Sim"

j.items["Arma"] = "Lança"
i.prop["Nome"] = "Cajado do Heroi"
i.prop["Tipo"] = j.items["Arma"]

i.stats["MXATK"] = 20
i.stats["ATK"]   = i.stats["MXATK"]
i.stats["LVL"]= 1

os.system("cls" if os.name == "nt" else "clear")

def addPlayerProps(maxVida,maxMana,lvl):
    j.stats["MXVida"] = maxVida
    j.stats["Vida"] = j.stats["MXVida"]
    j.stats["MXMana"] = maxMana
    j.stats["Mana"] = j.stats["MXMana"]
    j.stats["Nivel"]  = lvl


def jStats():
    input("     Propiedade do Personagem\n")
    print("Nome: ",j.prop["Nome"] )
    print("Sexo: ",j.prop["Sexo"] )
    print("Raça: ",j.prop["Raca"])
    input("     Seus Status\n")
   
    match j.prop["Raca"]:
        case "Human":
            j.stats["MXVida"] = 100
            j.stats["Vida"] = j.stats["MXVida"]
            j.stats["MXMana"] = 60
            j.stats["Mana"] = j.stats["MXMana"]
            j.stats["Nivel"]  = 0
            
            print("Vida: {}".format(j.stats["Vida"]) + "/", j.stats["MXVida"])
            print("Mana: {}".format(j.stats["Mana"]) + "/", j.stats["MXMana"])
           
            print("Level: {}".format(j.stats["Nivel"]) )
        case "Elf":   
            j.stats["MXVida"] = 80
            j.stats["Vida"] = j.stats["MXVida"]
            j.stats["MXMana"] = 120
            j.stats["Mana"] = j.stats["MXMana"]
            j.stats["Nivel"]  = 0
            
            print("Vida: {}".format(j.stats["Vida"]) + "/", j.stats["MXVida"])
            print("Mana: {}".format(j.stats["Mana"]) + "/", j.stats["MXMana"])
        
            print("Level: {}".format(j.stats["Nivel"]) )
        case "Giant":    
            j.stats["MXVida"] = 180
            j.stats["Vida"] = j.stats["MXVida"]
            j.stats["MXMana"] = 20
            j.stats["Mana"] = j.stats["MXMana"]
            j.stats["Nivel"]  = 0
            
            print("Vida: {}".format(j.stats["Vida"]) + "/", j.stats["MXVida"])
            print("Mana: {}".format(j.stats["Mana"]) + "/", j.stats["MXMana"])
            
            print("Level: {}".format(j.stats["Nivel"]) ) 
    
    match j.items["Arma"]:
            case "Espada":
                
                i.prop["Nome"] = "Espada do Heroi"
                i.prop["Tipo"] = j.items["Arma"]

                i.stats["MXATK"] = 15
                i.stats["ATK"]   = i.stats["MXATK"]
                i.stats["LVL"]= 1

                print(f" ATK:  {i.stats["ATK"]}                                   ||          ")
                print(f" DEF:  0                                   ||||         ")
                print(f" LVL:  {i.stats["LVL"]}                                   ||||         ")
                print("                                           ||||         ")
                print(f" Nome: {i.prop["Nome"]}                     ||||         ")
                print(f" Tipo: {i.prop["Tipo"]}                              ||||         ")
                print("                                           ||||         ")
                print("                                        ==========      ")
                print("                                            ##          ")
                print("                                            ##          ")
                print("                                           ====         ")
            case "Arco":

                i.prop["Nome"] = "Arco do Heroi"
                i.prop["Tipo"] = j.items["Arma"]

                i.stats["MXATK"] = 5
                i.stats["ATK"]   = i.stats["MXATK"]
                i.stats["LVL"]= 1

                print(f" ATK: {i.stats["ATK"]}                                        (         ")
                print(f" DEF: {i.stats["DEF"]}                                    ((         ")
                print(f" LVL: {i.stats["LVL"]}                                      (((         ")
                print("                                            ((((         ")
                print(f" Nome: {i.prop["Nome"]}                        ||  \        ")
                print(f" Tipo: {i.prop["Tipo"]}                                 ||   \       ")
                print("                                            ||    >      ") 
                print("                                            ||   /       ")
                print("                                            ||  /        ")
                print("                                            ((((         ")
                print("                                             (((          ")
                print("                                              ((          ")
                print("                                               (          ")
            case "Cajado":

                i.prop["Nome"] = "Cajado do Heroi"
                i.prop["Tipo"] = j.items["Arma"]

                i.stats["MXATK"] = 10
                i.stats["ATK"]   = i.stats["MXATK"]
                i.stats["LVL"]= 1

                print(f' ATK: {i.stats["ATK"]}                               ◎◎          ')
                print(f' DEF: {i.stats["DEF"]}                             ||          ') 
                print(f' LVL: {i.stats["LVL"]}                                ||          ') 
                print('                                   |---◎◎---|      ')
                print(f' Nome: {i.prop["Nome"]}                 ||          ')
                print(f' Tipo: {i.prop["Tipo"]}                          ||          ')
                print('                                       ||          ')
                print('                                       ||          ')
                print('                                       ||          ')
                print('                                       ||          ')
                print('                                     |====|        ')
                print('                                    |======|       ')    
            case "Lança":

                i.prop["Nome"] = "Cajado do Heroi"
                i.prop["Tipo"] = j.items["Arma"]

                i.stats["MXATK"] = 20
                i.stats["ATK"]   = i.stats["MXATK"]
                i.stats["LVL"]= 1    
                print(f" ATK: {i.stats["ATK"]}                                 /\      ")
                print(f" DEF: {i.stats["DEF"]}                              /**\     ")
                print(f" LVL: {i.stats["LVL"]}                                  ||      ")
                print("                                         ||      ")
                print(f" Nome: {i.prop["Nome"]}                   ||      ")
                print(f" Tipo: {j.items["Arma"]}                             ||      ")
                print("                                         ||      ")
                print("                                         ||      ")
                print("                                         ||      ")
                print("                                       /====\    ")        
jStats()
