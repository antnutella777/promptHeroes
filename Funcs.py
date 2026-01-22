import os,time,math,random,readline
from Objects import *
from colorData import *
historyInput = []

def typeTx(texto,color):
    
    if "brigth_" in color:
        for letra in texto:
            print(bright_colors[color],letra,sep="", end="", flush=True )
            time.sleep(0.05)
        texto += "\n" + main_colors["reset"]
    else:    
        for letra in texto:
            print(main_colors[color],letra,sep="", end="", flush=True )
            time.sleep(0.05)
        texto += "\n" + main_colors["reset"]
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
        var = input(main_colors["blue"]+ "\n>>> ")
        for index in range(len(opt)):
            if opt[index] == var:
                loop = True
        if loop == False:
            typeTx(falseTxt + "\n","blue")
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
    obj.prop    ["Name"]        = E["Nome"]
    obj.prop    ["Raca"]        = E["Raça"]
    obj.stats   ["Vida"]        = E["Vida"] * (lvl / 2)
    obj.stats   ["Damage"]      = math.floor(E["dano"] * (lvl / 2))
    obj.stats   ["critPercent"] = 10 * lvl
    obj.stats   ["LVL"]         = lvl
    return obj
def objStats(obj):
    clear()
    typeTx("     Propiedade do {} \n".format(obj.prop["Name"]),"red")
    print("Nome: ",obj.prop["Name"] )
    print("Raca: ",obj.prop["Raca"])

    typeTx("     Seus Status\n","red")

    print("Vida:    {}".format(obj.stats["Vida"]))
    print("Level:   {}".format(obj.stats["LVL"]) )
    print("Damage:  {}".format(obj.stats["Damage"]))
def addPlayerSlave(obj):
    obj.prop["Raca"] = "Human"
    obj.prop["Nome"] = "Andre"
    obj.prop["Sexo"] = "Masculino"

    obj.stats["critPercent"] = 20
    obj.stats["Nivel"] = 1
    obj.stats["XP"] = 0
    obj.stats["mxXP"] = 100
    obj.items["Arma"] = "Espada"
def slaveStats(obj):
    clear()
    typeTx("     Propiedade do {} \n".format(obj.prop["Name"]),"red")
    print("Nome: ",obj.prop["Name"] )
    print("Raca: ",obj.prop["Raca"])

    typeTx("     Seus Status\n","red")

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
            typeTx("Estou Defendendo\n","yelow")
        case "item":
            f.clear()
            itemList = player.listarItens()
            comando = input(">>>> ")

            if "use" in comando: 
                
                for l in range(len(player.inventario)):
                 
                    for c in range(len(player.inventario[l])):
                   
                        if player.inventario[l][c].prop["Name"] in comando: 
                            player.inventario[l][c].use(player,l,c)
                            return choose
                        else:
                            typeTx("Item não exite")
            elif "equip" in comando:
                for l in range(len(player.inventario)):
                    for c in range(len(player.inventario[l])):
                        if player.inventario[l][c].prop["Name"] in comando: 
                            player.inventario[l][c].equip()
                            return choose
                        else:
                            typeTx("Item não exite")
            elif "info" in comando:
                for item in range(len(itemList)):
                    if itemList[item].prop["Name"] in comando: 
                        itemList[item].info() 
                        return choose 
                    else:
                        typeTx("Item não exite")
            elif "exit" in comando:
                return "status"            
        case "fujir":
            fulgaChance = random.randint(0,100)
            if fulgaChance > 79:
                typeTx("Voce fugiu\n","yellow")
            else:
                typeTx("{} te bloqueou\n".format(enemy.prop["Name"]),"yellow")
        case "info":
            f.clear()
            enemy.info()
        case "status":
            f.clear()
            player.info()
    return choose
def checkBattleEnd(choose,enemy,player):
    if choose != "info" and choose != "status" and choose != "item" and enemy.stats["Vida"] > 0:
            enemy.atack(player)
    if enemy.stats["Vida"] <= 0:
        typeTx("Voce Venceu!!!!\n","blue")
    elif player.stats["Vida"] < 0:
        typeTx("Voce Morreu\n","red")
def batlleEvent(lvl,ed,enemyObj,j):
    enemys = [ed.Batedor,ed.Gigante,ed.Guarda]
    obj = startBattle(enemys,enemyObj,lvl)
    typeTx("{} bloqueou seu caminho!!!".format(obj.prop["Name"]),"yellow")
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
def newEquipableItem(itemsData, item):
    obj = Items() 
    obj.prop   ["Name"]             = itemsData[item]["Name"]
    obj.prop   ["eqTarget"]         = itemsData[item]["eqTarget"]
    obj.prop   ["DEF"]              = itemsData[item]["Defesa"]
    obj.prop   ["Rarity"]           = itemsData[item]["Rarity"]
    obj.prop   ["Type"]             = itemsData[item]["Type"]
    obj.prop   ["Description"]      = itemsData[item]["Description"]
    obj.prop   ["fxTarget"]         = itemsData[item]["fxTarget"]
    obj.prop   ["Price"]            = itemsData[item]["Price"]
    obj.stats  ["Effects"]          = itemsData[item]["Effects"]
    obj.prop   ["Stack"]            = itemsData[item]["Stack"]
    obj.stats  ["maxStack"]         = itemsData[item]["maxStack"] 
    return obj

