

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

    
    pocao  = f.newConsumableItem(idd.consumableItems,"pocaoVidaM")
    pocao2 = f.newConsumableItem(idd.consumableItems,"pocaoVidaM")
    
    espada = f.newConsumableItem(edd,"espadaComum")
    
    capacete = f.newEquipableItem(edd,"capaceteComum")
    peitoral = f.newEquipableItem(edd,"peitoralComum")
    calça    = f.newEquipableItem(edd,"calçaComum")
    bota     = f.newEquipableItem(edd,"botasComum")
    
    espada.equip(j)

    capacete.equip(j)
    peitoral.equip(j)
    calça.equip(j)
    bota.equip(j)

    j.addItems(pocao,10)

    while j.stats["Vida"] > 0:
        
        f.batlleEvent(j.stats["Nivel"],ed,e,j)

 
        