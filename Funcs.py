import os,time,math,random
from Objects import *
def typeTx(texto):
    for letra in texto:
        print(letra, end="", flush=True)
        time.sleep(0.05)
    texto += "\n"
def typeTxTimer(texto,timer):
    for letra in texto:
        print(letra, end="", flush=True)
        time.sleep(timer)
def clear():
    os.system("cls" if os.name == "nt" else "clear")
def jStats(j,i):
    print("     Propiedade do Personagem\n")
    print("Nome: ",j.prop["Name"] )
    print("Sexo: ",j.prop["Sexo"] )
    print("Raca: ",j.prop["Raca"])
    print("     Seus Status\n")

    match j.prop["Raca"]:
        case "Human":

            print("Vida: {}".format(j.stats["Vida"]) + "/", j.stats["MXVida"])
            print("Mana: {}".format(j.stats["Mana"]) + "/", j.stats["MXMana"])
            print
            print("Level: {}".format(j.stats["Nivel"]) )
        case "Elf":

            print("Vida: {}".format(j.stats["Vida"]) + "/", j.stats["MXVida"])
            print("Mana: {}".format(j.stats["Mana"]) + "/", j.stats["MXMana"])

            print("Level: {}".format(j.stats["Nivel"]) )
        case "Giant":

            print("Vida: {}".format(j.stats["Vida"]) + "/", j.stats["MXVida"])
            print("Mana: {}".format(j.stats["Mana"]) + "/", j.stats["MXMana"])

            print("Level: {}".format(j.stats["Nivel"]) )

    match j.items["Arma"]:
            case "Espada":

                print(f" ATK:  {i.stats["ATK"]}                                   ||          ")
                print(f"                                           ||||         ")
                print(f" LVL:  {i.stats["LVL"]}                                   ||||         ")
                print("                                           ||||         ")
                print(f" Nome: {i.prop["Name"]}                     ||||         ")
                print(f" Tipo: {i.prop["Type"]}                              ||||         ")
                print("                                           ||||         ")
                print("                                        ==========      ")
                print("                                            ##          ")
                print("                                            ##          ")
                print("                                           ====         ")
            case "Arco":

                print(f" ATK: {i.stats["ATK"]}                                        (         ")
                print(f"                                                          ((         ")
                print(f" LVL: {i.stats["LVL"]}                                      (((         ")
                print("                                            ((((         ")
                print(f" Nome: {i.prop["Name"]}                        ||  \        ")
                print(f" Tipo: {i.prop["Type"]}                                 ||   \       ")
                print("                                            ||    >      ")
                print("                                            ||   /       ")
                print("                                            ||  /        ")
                print("                                            ((((         ")
                print("                                             (((          ")
                print("                                              ((          ")
                print("                                               (          ")
            case "Cajado":

                print(f' ATK: {i.stats["ATK"]}                               ◎◎          ')
                print(f'                                                   ||          ')
                print(f' LVL: {i.stats["LVL"]}                                ||          ')
                print('                                   |---◎◎---|      ')
                print(f' Nome: {i.prop["Name"]}                 ||          ')
                print(f' Tipo: {i.prop["Type"]}                          ||          ')
                print('                                       ||          ')
                print('                                       ||          ')
                print('                                       ||          ')
                print('                                       ||          ')
                print('                                     |====|        ')
                print('                                    |======|       ')
            case "Lanca":
                print(f" ATK: {i.stats["ATK"]}                                 /\      ")
                print(f"                                                    /**\     ")
                print(f" LVL: {i.stats["LVL"]}                                  ||      ")
                print("                                         ||      ")
                print(f" Nome: {i.prop["Name"]}                   ||      ")
                print(f" Tipo: {j.items["Arma"]}                             ||      ")
                print("                                         ||      ")
                print("                                         ||      ")
                print("                                         ||      ")
                print("                                       /====\    ")
def logo():
    print("""
    ██████╗ ██████╗  ██████╗ ███╗   ███╗██████╗ ████████╗
    ██╔══██╗██╔══██╗██╔═══██╗████╗ ████║██╔══██╗╚══██╔══╝
    ██████╔╝██████╔╝██║   ██║██╔████╔██║██████╔╝   ██║
    ██╔═══╝ ██╔══██╗██║   ██║██║╚██╔╝██║██╔═══╝    ██║
    ██║     ██║  ██║╚██████╔╝██║ ╚═╝ ██║██║        ██║
    ╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝╚═╝        ╚═╝

            ██╗  ██╗███████╗██████╗  ██████╗ ███████╗
            ██║  ██║██╔════╝██╔══██╗██╔═══██╗██╔════╝
            ███████║█████╗  ██████╔╝██║   ██║███████╗
            ██╔══██║██╔══╝  ██╔══██╗██║   ██║╚════██║
            ██║  ██║███████╗██║  ██║╚██████╔╝███████║
            ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝
        """)
    input("> Um RPG forjado no terminal <")
    input(">>> Pressione ENTER para comecar <<<")
def userInput(opt,falseTxt):
    loop = False
    while loop == False:
        var = input("\n>>> ")
        for index in range(len(opt)):
            if opt[index] == var:
                loop = True
        if loop == False:
            typeTx(falseTxt + "\n")
    return var
def addItemProps(obj,nome,tipo,maxAtk,lvl):
    obj.prop["Name"] = nome
    obj.prop["Type"] = tipo

    obj.stats["MXATK"] = maxAtk
    obj.stats["ATK"]   = obj.stats["MXATK"]
    obj.stats["LVL"]   = lvl
def addPlayerProps(obj,maxVida,maxMana,maxDamage,lvl):
    obj.stats     ["MXVida"]      = maxVida
    obj.stats     ["Vida"]        = obj.stats["MXVida"]
    obj.stats     ["MXMana"]      = maxMana
    obj.stats     ["Mana"]        = obj.stats["MXMana"]
    obj.stats     ["Nivel"]       = lvl
    obj.stats     ["MXDamage"]    = maxDamage
    obj.stats     ["Damage"]      = obj.stats  ["MXDamage"]
def fakeLoad(timer,txt):
    for index in range(101):
        print( txt + "{}%" .format(index))
        time.sleep(timer)
def newEneny(obj,E,lvl):
    obj.prop["Name"]        = E["Name"]
    obj.prop["Raca"]        = E["Raca"]
    obj.stats["Vida"]       = E["Vida"] * (lvl / 2)
    obj.stats["Damage"]     = math.floor(E["dano"] * (lvl / 2))
    obj.stats  ["critPercent"] = 10 * lvl
    obj.stats["LVL"]        = lvl
    return obj
def objStats(obj):
    clear()
    typeTx("     Propiedade do {} \n".format(obj.prop["Name"]))
    print("Nome: ",obj.prop["Name"] )
    print("Raca: ",obj.prop["Raca"])

    typeTx("     Seus Status\n")

    print("Vida:    {}".format(obj.stats["Vida"]))
    print("Level:   {}".format(obj.stats["LVL"]) )
    print("Damage:  {}".format(obj.stats["Damage"]))
def addPlayerSlave(obj):
    obj.prop["Raca"] = "Human"
    obj.prop["Nome"] = "Andre"
    obj.prop["Sexo"] = "Masculino"

    obj.stats["critPercent"] = 20

    obj.items["Arma"] = "Espada"
def slaveStats(obj):
    clear()
    typeTx("     Propiedade do {} \n".format(obj.prop["Name"]))
    print("Nome: ",obj.prop["Name"] )
    print("Raca: ",obj.prop["Raca"])

    typeTx("     Seus Status\n")

    print("Vida:    {}".format(obj.stats["Vida"]))
    print("Level:   {}".format(obj.stats["Nivel"]))
    print("Arma:    {}".format(obj.items["Arma"]))
    print("Damage:  {}".format(obj.stats["Damage"]))
def startBattle(enemyList,objEnemy,lvl):
    fakeLoad(0.01,"Carregando Batalha ")

    enemyChoose = random.randint(0,2)

    obj = newEneny(objEnemy,enemyList[enemyChoose],lvl)

    clear()
    return obj
def playerTurn(enemy,player):   

    battleList = ["atacar","defender","item","fujir","info","status","menu"]
    false = "Opcao Invalida"
    
    choose = userInput(battleList,false)
    match choose:
        case "atacar":
            player.atack(enemy)
        case "defender":
            typeTx("Estou Defendendo\n")
        case "item":
            typeTx("Usando item\n")
        case "fujir":
            fulgaChance = random.randint(0,100)
            if fulgaChance > 79:
                typeTx("Voce fugiu\n")
            else:
                typeTx("{} te bloqueou\n".format(enemy.prop["Name"]))
        case "info":
            objStats(enemy)
        case "status":
            slaveStats(player)
    return choose
def checkBattleEnd(choose,enemy,player):
    if choose != "info" and choose != "status" and enemy.stats["Vida"] > 0:
            enemy.atack(player)
    if enemy.stats["Vida"] < 0:
        typeTx("Voce Venceu!!!!\n")
    elif player.stats["Vida"] < 0:
        typeTx("Voce Morreu\n")
def batlleEvent(lvl,ed,enemyObj,j):
    enemys = [ed.Batedor,ed.Gigante,ed.Guarda]
    obj = startBattle(enemys,enemyObj,lvl)
    typeTx(" Um {} bloqueou seu caminho!!!".format(obj.prop["Name"]))
    while (j.stats["Vida"] > 0 and obj.stats["Vida"] > 0) :
        choose = playerTurn(obj,j)
        checkBattleEnd(choose,obj,j)     
def newConsumableItem(itemsData, item):
    obj = Items() 
    obj.prop   ["Name"]             = itemsData[item]["Name"]
    obj.prop   ["Type"]             = itemsData[item]["Type"]
    obj.prop   ["Description"]      = itemsData[item]["Description"]
    obj.prop   ["fxTarget"]         = itemsData[item]["fxTarget"]
    obj.prop   ["Price"]            = itemsData[item]["Price"]
    obj.stats  ["Effects"]          = itemsData[item]["Effects"]
    obj.prop   ["Stack"]            = itemsData[item]["Stack"]
    obj.stats  ["maxStack"]         = itemsData[item]["maxStack"] 
    return obj