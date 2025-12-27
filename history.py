import sys,Funcs,Objects, math,time,os,enemyData,random,itemsData


gameStage = "Intro"

confirm = False
armaLoop = False
confirma = ["Sim","Nao"]

f = Funcs


def gameIntro():

    f.typeTx("Ola")
    time.sleep(3)
    f.clear()
    f.typeTx("Ja faz muito tempo na verdade")
    time.sleep(2)
    f.clear()
    f.typeTx("Voce e novo por aqui")

    resp = input("{}>>> ".format(confirma))
    if resp == "Sim":
        f.clear()
        f.typeTx("Entendi\n")
        time.sleep(1)

    elif resp == "Nao":

        f.typeTx("Entao ja sabe como o que esta por vir")
        time.sleep(1)
        sys.exit()
    else:
        f.typeTx("Acho que nao tem nimguem aqui")
        sys.exit()

    f.clear()
    f.typeTx("Bom, era pra ter algo a mais por aqui\n")
    time.sleep(1)
    f.clear()
    f.typeTx("Mais acho que podemos comecar do mesmo jeito")
    input("[Enter]>>> ")
    f.clear()

    f.fakeLoad(0.05,"Carregando Mundo \n")


    f.fakeLoad(0.05,"Carregando Criacao de personagem ")

    time.sleep(1)
    f.clear()
    f.typeTx("Prontinho")
    time.sleep(1)
    f.clear()
    f.typeTx("Voce, vai precisar de um receptculo para este mundo para este mundo")
    
    input("[Enter]>>> ")

    f.clear()
def createPers(player):
    raca = ["Human","Elf","Giant"]
    sexo = ["Masculino", "Feminino"]

    index = 0

    f.typeTx("Qual e o Nome do Receptaculo ??\n")

    player.prop["Name"] = input('>>> ')

    f.typeTx("Qual e o Sexo do Receptaculo??\n")

    player.prop["Sexo"] = f.userInput(sexo,"Esse Genero nao existe em Etherea\n")

    f.typeTx("Qual e sua Raca??\n")

    player.prop["Raca"] = f.userInput(raca,"Essa Raca nao existe\n")

    f.clear()
    f.typeTx("     Propiedade do Personagem\n")
    print("Nome: ",player.prop["Name"] )
    print("Sexo: ",player.prop["Sexo"] )
    print("Raca: ",player.prop["Raca"])
    f.typeTx("     Seus Status\n")

    match player.prop["Raca"]:
        case "Human":
            f.addPlayerProps(player,100,60,1,1)

            print("Vida: {}".format(player.stats["Vida"]) + "/", player.stats["MXVida"])
            print("Mana: {}".format(player.stats["Mana"]) + "/", player.stats["MXMana"])

            print("Level: {}".format(player.stats["Nivel"]) )
        case "Elf":

            f.addPlayerProps(player,80,120,1,1)

            print("Vida: {}".format(player.stats["Vida"]) + "/", player.stats["MXVida"])
            print("Mana: {}".format(player.stats["Mana"]) + "/", player.stats["MXMana"])

            print("Level: {}".format(player.stats["Nivel"]) )
        case "Giant":

            f.addPlayerProps(player,180,20,1,1)

            print("Vida: {}".format(player.stats["Vida"]) + "/", player.stats["MXVida"])
            print("Mana: {}".format(player.stats["Mana"]) + "/", player.stats["MXMana"])

            print("Level: {}".format(player.stats["Nivel"]) )

    f.typeTx("Confima esse Personagem???\n")

    player.prop["Confirm"] = f.userInput(confirma,"Confima esse Personagem???\n")


    match player.prop["Confirm"]:
        case "Sim":
            return True
          
        case "Nao":
            f.clear()
            f.typeTx("Deletando Personagem...\n")
            return False
def defineWeapon(i,j):
    armas = ["Espada","Lanca","Cajado","Arco"]
    confirmArma = False

    f.typeTxTimer("CARREGANDO",0.5)
    f.clear()
    f.typeTx("Em PromptHeroes voce escolhe apenas um tipo de arma.\nEsta arma sera a sua sua Arma pelo resto da vida deste personagem;\n")
    input("Pressione Enter para continuar...\n")
    f.clear()
    f.typeTx("Nao se preocupe voce podera mudar uma vez a cada capitulo.\nMais recomendado o uso de apenas uma.\n")
    input("Pressione Enter para continuar...\n")
    f.clear()

    while confirmArma == False: 
        f.typeTx("Agora Escolha Sua Arma. Escolha com cuidado!!\n")

        j.items["Arma"] = f.userInput(armas,"Essa Arma nao existe\n")

        f.clear()
        match j.items["Arma"]:
            case "Espada":
                f.addItemProps(i,"Espada do Heroi",j.items["Arma"],15,1)


                print(f" ATK:  {i.stats["ATK"]}                                   ||          ")
                print(f" DEF:  0                                   ||||         ")
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

                f.addItemProps(i,"Arco do Heroi",j.items["Arma"],5,1)

                print(f" ATK: {i.stats["ATK"]}                                        (         ")
                print(f" DEF: {i.stats["DEF"]}                                    ((         ")
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

                f.addItemProps(i,"Cajado do Heroi",j.items["Arma"],10,1)

                print(f' ATK: {i.stats["ATK"]}                               ◎◎          ')
                print(f' DEF: {i.stats["DEF"]}                             ||          ')
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

                f.addItemProps(i,"Lanca do Heroi",j.items["Arma"],20,1)

                print(f" ATK: {i.stats["ATK"]}                                 /\      ")
                print(f" DEF: {i.stats["DEF"]}                              /**\     ")
                print(f" LVL: {i.stats["LVL"]}                                  ||      ")
                print("                                         ||      ")
                print(f" Nome: {i.prop["Name"]}                   ||      ")
                print(f" Tipo: {j.items["Arma"]}                             ||      ")
                print("                                         ||      ")
                print("                                         ||      ")
                print("                                         ||      ")
                print("                                       /====\    ")
        f.typeTx("Confirma??\n")

        i.prop["Confirm"] = f.userInput(confirma,"Confirma??")

        j.stats["MXDamage"] += i.stats["MXATK"]

        match i.prop["Confirm"]:
            case "Sim":
                confirmArma = True
                return False
            case "Nao":
                f.clear()
                return True
                f.typeTx("Deletando Arma...\n")
def presentation(j,i):
        f.clear()
        f.typeTx("      Seu receptaculo:\n")
        f.jStats(j,i)
        input("Pressione Enter para continuar...\n")
        f.clear()
        f.logo()
        f.clear()