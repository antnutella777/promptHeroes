import sys,Funcs,Objects, math,time,os,dictionary, random

j = Objects.Jogador()
i = Objects.Items()
e = Objects.Enemy()
f = Funcs
d = dictionary



confirm = False
armaLoop = False
confirma = ["Sim","Nao"]

def batlleEvent(obj,enemyLife,playerLife):
    battleList = ["Atacar","Defender","Item","Fujir"]
    false = "Opção Invalida"
    while (enemyLife > 0 and playerLife > 0) :
        match f.userInput(battleList,false):
            case "Atacar":
                j.atack()
            case "Defender":
                f.typeTx("Estou Defendendo")
            case "Item":
                f.typeTx("Usando item")
            case "Fujir":
               break

enemys = [d.Batedor,d.Guarda]

chooseEnemy = random.randint(0,1)

f.newEneny(e,enemys[chooseEnemy],1)

f.objStats(e)
