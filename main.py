

import Funcs,Objects,enemyData,itemsData,history,readline
from itemsData  import consumableItems,equpableItems
from colorData  import *
from Objects    import *

j           = Jogador()
i           = Items()
e           = Enemy()
f           = Funcs
h           = history  
ed          = enemyData
idd         = itemsData
edd         = equpableItems
DEBUG       = True     
gameStage   = "Intro"



#temporario para debug
if gameStage != "Intro":
    f.addPlayerSlave(j)

    match j.prop["Raca"]:
        case "Human": f.addPlayerProps(j,100,60,1,1)
        case "Elf":   f.addPlayerProps(j,80,120,1,1)
        case "Giant": f.addPlayerProps(j,180,20,1,1)
    match j.items["Arma"]:
        case "Espada":  f.addItemProps(i,"Espada do Heroi",j.items["Arma"],15,1)
        case "Arco":    f.addItemProps(i,"Arco do Heroi",j.items["Arma"],5,1)
        case "Cajado":  f.addItemProps(i,"Cajado do Heroi",j.items["Arma"],10,1)
        case "Lanca":   f.addItemProps(i,"Lanca do Heroi",j.items["Arma"],20,1)

confirm = False
armaLoop = False
confirma = ["Sim","Nao"]

gameLoopMain = True     
f.clear()
if DEBUG == False:
    while gameLoopMain == True:
        match gameStage:
            case "Intro":
                h.gameIntro()
                confirm = False
                gameStage = "Criacao"
            case "Criacao":
                while confirm == False:
                    confirm = h.createPers(j)    
                armaLoop = True
                gameStage = "Arma"
            case "Arma":
                while armaLoop == True:
                    armaLoop = h.defineWeapon(i,j)
                gameStage = "present"
            case "present" :
                h.presentation(j,i)              
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
        case "Lanca":   f.addItemProps(i,"Lanca do Heroi",j.items["Arma"],20,1)

    j.stats["Damage"] += i.stats["ATK"]

    #f.batlleEvent(2,ed,e,j)
    
    pocao  = f.newConsumableItem(idd.consumableItems,"pocaoVidaM")
    pocao2 = f.newConsumableItem(idd.consumableItems,"pocaoVidaM")
    
    
    capacete = f.newEquipableItem(edd,"capaceteComum")
    peitoral = f.newEquipableItem(edd,"peitoralComum")
    calça    = f.newEquipableItem(edd,"calçaComum")
    bota     = f.newEquipableItem(edd,"botasComum")
    
    capacete.equip(j)
    peitoral.equip(j)
    calça.equip(j)
    bota.equip(j)

    j.addItems(pocao,5)
 
    f.batlleEvent(1,ed,e,j)
 
        