from datetime import datetime
football = []
def strcmp_and_sort(football, s):
    i = 0
    while i < len(football):
        j = 0
        while j < len(football) - i - 1:
            if football[j][s] > football[j + 1][s]:
                    football[j], football[j + 1] = football[j + 1], football[j]
            j += 1
        i += 1

def addplayer(football):
    while true:
    print("------------------search---------------------")
    id1 = int(input("enter id of player:"))
    name =  input("enter name: ")
    nakename = input("enter nickname: ")
    numeroMaillot = int(input("enter numeroMaillot: "))
    poste = input("enter position of this player: ")
    age = int(input("enter age of this player: "))
    goals = int(input("enter how many goals this palyer have: "))
    now = datetime.now()
    status = input("titulaire(T) or remplaçant(r): ")
    if status == 'T' or  status == 't':
        status = "titulaire"
    elif status == 'R' or status == 'r':
        status = "remplaçant"
    fot = {"id": id1, "name": name,  "nakename": nakename, "numeroMaillot": numeroMaillot, "poste": poste, "age": age, "goals": goals, "now": now, "status": status}
    football.append(fot)
    print("saved successfully")
    answer = input("do you want to add more palayers,enter(Y/N): ")
    if answer == 'N' or answer == 'n':
        break
def printinfo(zoo, a):
    print("-----------------------------------")
    print( "id : ", a["id"])
    print("name : ",a["name"])
    print("nickname : ", a["nickname"])
    print("numeroMaillot :", a["numeroMaillot"])
    print("age : ", a["age"])
    print("poste: ", a["poste"])
    print("goals: ", a["goals"])
    print("status", a["status"])
    print("-----------------------------------\n")
def showplayers(football):
    call = input("show by name or age or poste: ")
    if call == "name":
        strcmp_and_sort(football, "name")
        for n in football:
            printinfo(football, n)
    elif call == "age":
        strcmp_and_sort(football, "age")
        for j in football:
            printinfo(football, j)
    elif call == "poste":
        ps = input("enter the poste: ")
        for r in football:
            if r["poste"] == ps:
                printinfo(football, r)

def update(football):
    while true:
        rtx = input("enter id to update")
        for j in football:
            if rtx == j["id"]:
            j["poste"] = input("enter new poste: ")
            j["age"] = input("enter new age: ")
            j["goals"] = int(input("enter number of goals"))
            print("saved successfully")
        ans = input("do you want to update more players Y/N: ")
        if ans == 'N' or ans == 'n':
            break
def removeinfo(football):
    while True:
        found = False
        idx = int(input("enter id: "))
        for i in football:
            if idx == i["id"]:
                football.remove(i)
                print("player removed successfully!")
                found = True
                os.system("clear")
                answer = input("do you want to remove more players Y/N: ")
                if(answer == 'N' or answer == 'n'):
                    return
        if found == False:
            os.system("clear")
            print("this id is not exist try again")
def search(football):
    os.system("clear")
    print("------------------search---------------------")
    answer = input("do you want search by id  or name: ")
    if answer == "name":
        while True:
            ans = input("enter name :")
            for a in football:
                if a["name"] == ans:
                    printinfo(football, a)
                    return
            os.system("clear")
            print("this name is not exist try again")
    if answer == "id":
        while True:
            ans2 = int(input("enter id: "))
            for i in football:
                if i["id"] == ans2:
                    printinfo(fotball, i)
                    return
            os.system("clear")
            print("this id is not exist try again")

