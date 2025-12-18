

import math, time, os
import sys,funcs
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
    

class Enemy:
    def __init__(self):
        self.prop   = {}
        self.stats  = {}



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
f = funcs
confirm = False
gameLoop = False
confirma = ["Sim","Nao"]




f.clear()

f.typeTx("Olá")
time.sleep(3)
f.clear()
f.typeTx("Ja faz muito tempo na verdade")
time.sleep(2)
f.clear()
f.typeTx("Voce é novo por aqui")

resp = input("{}>>> ".format(confirma))
if resp == "Sim":
    f.clear()
    f.typeTx("Entendi\n")
    time.sleep(1)
   
elif resp == "Nao":
    
    f.typeTx("Entao já sabe como o que esta por vir")
    time.sleep(1)
    sys.exit()
else:
    f.typeTx("Acho que não tem nimguem aqui")
    sys.exit()

f.clear()
f.typeTx("Bom, era pra ter algo a mais por aqui\n")
time.sleep(1)
f.clear()
f.typeTx("Mais acho que podemos começar do mesmo jeito")
input("[Enter]>>> ")
f.clear()

f.typeTxTimer("Carregando Mundo\n",0.3)
index = 0
for index in range(101):
   print("Carregando Criação de personagem {}%" .format(index))
   time.sleep(0.05)
time.sleep(1)
f.clear()
f.typeTx("Prontinho")
time.sleep(1)
f.clear()
f.typeTx("Voce, vai precisar de um receptculo para este mundo para este mundo")
input("[Enter]>>> ")
f.clear()
while confirm == False:

    raca = ["Human","Elf","Giant"]
    sexo = ["Masculino", "Feminino"]
    
    index = 0

    f.typeTx("Qual é o Nome do Receptaculo ??\n")

    j.prop["Nome"] = input('>>> ')

    f.typeTx("Qual é o Sexo do Receptaculo??\n")

    j.prop["Sexo"] = f.userInput(sexo,"Esse Genero não existe em Etherea\n")

    f.typeTx("Qual é sua Raca??\n")

    j.prop["Raca"] = f.userInput(raca,"Essa Raca não existe\n")

    f.clear()       
    f.typeTx("     Propiedade do Personagem\n")
    print("Nome: ",j.prop["Nome"] )
    print("Sexo: ",j.prop["Sexo"] )
    print("Raça: ",j.prop["Raca"])
    f.typeTx("     Seus Status\n")
   
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

    f.typeTx("Confima esse Personagem???\n")

 
    definePersonagem = False
    while definePersonagem == False:
        j.prop["Confirm"] = input("{} >>> ".format(confirma))
        for index in range(len(confirma)):
            if confirma[index] == j.prop["Confirm"]:
                definePersonagem = True

        if definePersonagem == False:
            f.typeTx("Confima esse Personagem???\n")       
    
    match j.prop["Confirm"]:
        case "Sim":
            confirm = True
            gameLoop = True
        case "Nao":
            clear()
            f.typeTx("Deletando Personagem...\n")         

while gameLoop == True:
    armas = ["Espada","Lança","Cajado","Arco"]
    confirmArma = False
    index = 0
    
    f.typeTxTimer("CARREGANDO",0.5)
    f.clear()
    f.typeTx("Em PromptHeroes você escolhe apenas um tipo de arma.\nEsta arma sera a sua sua Arma pelo resto da vida deste personagem;\n")
    input("Pressione Enter para continuar...\n")
    f.clear()
    f.typeTx("Não se preocupe voce podera mudar uma vez a cada capitulo.\n Mais recomendado o uso de apenas uma.\n")
    input("Pressione Enter para continuar...\n")
    f.clear()

    while confirmArma == False:
        f.typeTx("Agora Escolha Sua Arma. Escolha com cuidado!!\n")
        
        j.items["Arma"] = f.userInput(armas,"Essa Arma não existe\n")
        
        f.clear()
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
        f.typeTx("Confirma??\n")
        
        i.prop["Confirm"] = f.userInput(confirma,"Confirma??")


        match i.prop["Confirm"]:
            case "Sim":
                confirmArma = True
            case "Nao":
                
                f.clear()
                f.typeTx("Deletando Arma...\n") 
    f.clear()
    f.jStats()
    input("Pressione Enter para continuar...\n")
    f.clear()
    f.logo()
    f.clear()
    f.typeTx("Em uma terra destante nunca antes imaginada.")
    gameLoop = False
    

    
    