

import sys,Funcs,Objects, math,time,os,dictionary, random

j = Objects.Jogador()
i = Objects.Items()
e = Objects.Enemy()
f = Funcs
d = dictionary

DEBUG = False

gameStage = "Intro" 

confirm = False
armaLoop = False
confirma = ["Sim","Nao"]

gameLoopMain = True

def batlleEvent():
    
    f.fakeLoad(0.01,"Carregando Batalha ")

    enemys = [d.Batedor,d.Gigante,d.Guarda]

    enemyChoose = random.randint(0,2)

    obj = f.newEneny(e,enemys[enemyChoose],1)
    
    f.clear()
    
    f.typeTx(" Um {} bloqueou seu caminho!!!".format(obj.prop["Nome"]))
    
    battleList = ["atacar","defender","item","fujir","info","status","menu"]
    false = "Opção Invalida"
    while (j.stats["Vida"] > 0 and obj.stats["Vida"] > 0) :
        choose = f.userInput(battleList,false)
        match choose:
            case "atacar":
                j.atack(obj)
            case "defender":
                f.typeTx("Estou Defendendo\n")
            case "item":
                f.typeTx("Usando item\n")
            case "fujir":
                fulgaChance = random.randint(0,100)
                if fulgaChance > 79:
                    f.typeTx("Você fugiu\n")
                    break
                else:
                    f.typeTx("{} te bloqueou\n".format(obj.prop["Nome"]))
            case "info": 
                f.objStats(obj) 
            case "status":
                f.slaveStats(j)
        if choose != "info" and choose != "status" and obj.stats["Vida"] > 0:
            obj.atack(j)
        if obj.stats["Vida"] < 0:
            f.typeTx("Você Venceu!!!!\n")
        elif j.stats["Vida"] < 0:
            f.typeTx("Voce Morreu")                         

def batlleTutorialEvent():
    f.typeTx("Primeiro vamos aprender o basico de uma batalha, observe:")
    time.sleep(1)
    f.clear()
    f.fakeLoad(0.01,"Carregando Batalha ")

    enemys = [d.Batedor,d.Gigante,d.Guarda]

    enemyChoose = random.randint(0,2)

    obj = f.newEneny(e,enemys[enemyChoose],1)
    
    f.clear()
    
    f.typeTx(" Um {} bloqueou seu caminho!!!\n".format(obj.prop["Nome"]))

    f.typeTx("Um {} está a sua frente. e não perece ser amigavel. ")
    time.sleep(1)
    f.typeTx("Nesse modo você tem duas opçoes iniciais:")
    time.sleep(1)
    f.typeTx(" atacar ")
    time.sleep(1)
    f.typeTx("ou fujir\n ")
    battleList = ["atacar","defender","item","fujir","info","status","menu"]
    false = "Opção Invalida"
    while (j.stats["Vida"] > 0 and obj.stats["Vida"] > 0) :
        choose = f.userInput(battleList,false)
        match choose:
            case "atacar":
                f.typeTx("Ao atacar Voce reduz o HP do um inimigo. ")
                time.sleep(1)
                f.typeTx("Você pode ver suas infos do inimigo digitando o comando --> info\n")
                j.atack(obj)
            case "defender":
                f.typeTx("Estou Defendendo\n")
            case "item":
                f.typeTx("Usando item\n")
            case "fujir":
                fulgaChance = random.randint(0,100)
                
                f.typeTx("Ao fujir você saira da batalha, porém o inimigo pode te bloquear novamente\n")

                if fulgaChance > 79:
                    f.typeTx("Você fugiu\n")
                    break
                else:
                    f.typeTx("{} te bloqueou\n".format(obj.prop["Nome"]))
            case "info": 
                f.objStats(obj) 
            case "status":
                f.slaveStats(j)
                f.typeTx("Aqui você pode ver todas a informaçoes seu pesonagem. Escolha outra opção\n")
        if choose != "info" and choose != "status" and obj.stats["Vida"] > 0:
            obj.atack(j)
            f.typeTx("no turno do inimigo, ele atacará e reduzira o seu HP. ")
            time.sleep(1)
            f.typeTx("Você pode ver seus status digitando o comando --> status\n")
        if obj.stats["Vida"] < 0:
            f.typeTx("Quando o HP do inimigo chega a zero, você vence.\n")
            f.typeTx("Você Venceu!!!!\n")
        elif j.stats["Vida"] < 0:
            f.typeTx("Voce Morreu")
f.clear()
if DEBUG == False:
    while gameLoopMain == True:    
        match gameStage:
            case "Intro":
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

                f.fakeLoad(0.05,"Carregando Mundo \n")


                f.fakeLoad(0.05,"Carregando Criação de personagem ")

                time.sleep(1)
                f.clear()
                f.typeTx("Prontinho")
                time.sleep(1)
                f.clear()
                f.typeTx("Voce, vai precisar de um receptculo para este mundo para este mundo")
                gameStage = "Criação"
                input("[Enter]>>> ")
                
                f.clear()

                
                confirm = False
            case "Criação":    
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
                            f.addPlayerProps(j,100,60,1,1)

                            print("Vida: {}".format(j.stats["Vida"]) + "/", j.stats["MXVida"])
                            print("Mana: {}".format(j.stats["Mana"]) + "/", j.stats["MXMana"])

                            print("Level: {}".format(j.stats["Nivel"]) )
                        case "Elf":

                            f.addPlayerProps(j,80,120,1,1)

                            print("Vida: {}".format(j.stats["Vida"]) + "/", j.stats["MXVida"])
                            print("Mana: {}".format(j.stats["Mana"]) + "/", j.stats["MXMana"])

                            print("Level: {}".format(j.stats["Nivel"]) )
                        case "Giant":

                            f.addPlayerProps(j,180,20,1,1)

                            print("Vida: {}".format(j.stats["Vida"]) + "/", j.stats["MXVida"])
                            print("Mana: {}".format(j.stats["Mana"]) + "/", j.stats["MXMana"])

                            print("Level: {}".format(j.stats["Nivel"]) )

                    f.typeTx("Confima esse Personagem???\n")

                    j.prop["Confirm"] = f.userInput(confirma,"Confima esse Personagem???\n")


                    match j.prop["Confirm"]:
                        case "Sim":
                            confirm = True
                            gameLoop = True
                        case "Nao":
                            f.clear()
                            f.typeTx("Deletando Personagem...\n")
                    gameStage = "Seleção de Arma" 
                    armaLoop = True       
            case "Seleção de Arma":
                while armaLoop == True:
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
                                f.addItemProps(i,"Espada do Heroi",j.items["Arma"],15,1)


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

                                f.addItemProps(i,"Arco do Heroi",j.items["Arma"],5,1)

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

                                f.addItemProps(i,"Cajado do Heroi",j.items["Arma"],10,1)

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

                                f.addItemProps(i,"Lança do Heroi",j.items["Arma"],20,1)

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

                        j.stats["MXDamage"] += i.stats["MXATK"]

                        match i.prop["Confirm"]:
                            case "Sim":
                                confirmArma = True
                            case "Nao":
                                f.clear()
            
                                f.typeTx("Deletando Arma...\n")
                        armaLoop = False          
                    gameStage = "Conclução"        
            case "Conclusão" :                    
                f.clear()
                f.typeTx("      Seu receptaculo:\n")
                f.jStats()
                input("Pressione Enter para continuar...\n")
                f.clear()
                f.logo()
                f.clear()
                f.typeTx("Em uma terra destante nunca antes imaginada.")
         
else:
   
    f.addPlayerSlave(j)
    
    match j.prop["Raca"]:
        case "Human": f.addPlayerProps(j,100,60,1,1)
        case "Elf":   f.addPlayerProps(j,80,120,1,1)
        case "Giant": f.addPlayerProps(j,180,20,1,1)
    match j.items["Arma"]:
        case "Espada":  f.addItemProps(i,"Espada do Heroi",j.items["Arma"],15,1)
        case "Arco":    f.addItemProps(i,"Arco do Heroi",j.items["Arma"],5,1)
        case "Cajado":  f.addItemProps(i,"Cajado do Heroi",j.items["Arma"],10,1)
        case "Lança":   f.addItemProps(i,"Lança do Heroi",j.items["Arma"],20,1)

    j.stats["Damage"] += i.stats["ATK"]


    
    batlleEvent()

   

