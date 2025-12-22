import os,time,Objects



def typeTx(texto):
    for letra in texto:
        print(letra, end="", flush=True)
        time.sleep(0.05)
def typeTxTimer(texto,timer):
    for letra in texto:
        print(letra, end="", flush=True)
        time.sleep(timer)
def clear():
    os.system("cls" if os.name == "nt" else "clear")
def jStats():
    print("     Propiedade do Personagem\n")
    print("Nome: ",j.prop["Nome"] )
    print("Sexo: ",j.prop["Sexo"] )
    print("Raça: ",j.prop["Raca"])
    print("     Seus Status\n")

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
    input(">>> Pressione ENTER para começar <<<")
def userInput(opt,falseTxt):
    loop = False
    while loop == False:
        var = input("{} >>> ".format(opt))
        for index in range(len(opt)):
            if opt[index] == var:
                loop = True
        if loop == False:
            typeTx(falseTxt + "\n")
    return var

def addItemProps(obj,nome,tipo,maxAtk,lvl):
    obj.prop["Nome"] = nome
    obj.prop["Tipo"] = tipo

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