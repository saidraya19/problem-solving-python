import requests
import os
zoo = [
    {"id": 1, "name": "lion", "espece": "mammifere", "age": 5, "habitat": "savane"},
    {"id": 2, "name": "tigre", "espece": "mammifere", "age": 4, "habitat": "jungle"},
    {"id": 3, "name": "elephant", "espece": "mammifere", "age": 10, "habitat": "savane"},
    {"id": 4, "name": "zebre", "espece": "mammifere", "age": 6, "habitat": "savane"},
    {"id": 5, "name": "girafe", "espece": "mammifere", "age": 7, "habitat": "savane"},
    {"id": 6, "name": "singe", "espece": "mammifere", "age": 3, "habitat": "foret"},
    {"id": 7, "name": "ours", "espece": "mammifere", "age": 8, "habitat": "montagne"},
    {"id": 8, "name": "loup", "espece": "mammifere", "age": 5, "habitat": "foret"},
    {"id": 9, "name": "renard", "espece": "mammifere", "age": 4, "habitat": "foret"},
    {"id": 10, "name": "kangourou", "espece": "mammifere", "age": 6, "habitat": "desert"},
    {"id": 11, "name": "aigle", "espece": "oiseau", "age": 5, "habitat": "montagne"},
    {"id": 12, "name": "perroquet", "espece": "oiseau", "age": 2, "habitat": "foret"},
    {"id": 13, "name": "pigeon", "espece": "oiseau", "age": 3, "habitat": "ville"},
    {"id": 14, "name": "serpent", "espece": "reptile", "age": 4, "habitat": "desert"},
    {"id": 15, "name": "crocodile", "espece": "reptile", "age": 12, "habitat": "riviere"},
    {"id": 16, "name": "tortue", "espece": "reptile", "age": 50, "habitat": "mer"},
    {"id": 17, "name": "requin", "espece": "poisson", "age": 15, "habitat": "mer"},
    {"id": 18, "name": "dauphin", "espece": "poisson", "age": 8, "habitat": "mer"},
    {"id": 19, "name": "chat", "espece": "mammifere", "age": 2, "habitat": "maison"},
    {"id": 20, "name": "chien", "espece": "mammifere", "age": 3, "habitat": "maison"}
]
def strcmp_t(zoo):
    i = 0
    while i < len(zoo):
        j = 0
        while j < len(zoo) - i - 1:
            if zoo[j]["name"] > zoo[j + 1]["name"]:
                zoo[j], zoo[j + 1] = zoo[j + 1], zoo[j]
            j += 1
        i += 1
def sortbyage():
    i = 0
    while i < len(zoo):
        j = 0
        while j < len(zoo) - i - 1:
            if zoo[j]["age"] < zoo[j + 1]["age"]:
                    zoo[j], zoo[j + 1] = zoo[j + 1], zoo[j]
            j += 1
        i += 1
def printinfo(zoo, a):
    print("-----------------------------------")
    print( "id : ", a["id"])
    print("name : ",a["name"])
    print("espece : ", a["espece"])
    print("habitat :", a["habitat"])
    print("age :", a["age"])
    print("-----------------------------------\n")

def showanimals(zoo):
    print("[1]:show every animal:")
    print("[2]:show by age order:")
    print("[3]:show habitat order:")
    rtx = int(input("enter your choice: "))
    if rtx == 1:
        strcmp_t(zoo)
        for i in zoo:
            printinfo(zoo, i)
    elif rtx == 2:
        sortbyage()
        for j in zoo:
            printinfo(zoo, j)
    elif rtx == 3:
        hb = input("enter habitat: ")
        for n in zoo:
            if n["habitat"] == hb:
                printinfo(zoo, n)
def addfunction(zoo):
    count = 0
    while True:
        os.system("clear")
        id1 = int(input("enter id :"))
        name = input("enter name of animal:")
        espece = input("enter espece: ")
        habitat = input("enter habitat: ")
        age = input("enter age of animal: ")
        animal = { "id": id1, "name": name, "espece": espece, "habitat": habitat, "age": age }
        zoo.append(animal)
        print("saved successfully")
        count += 1
        if count == 200:
            print("you cant add more than 200 animal")
            break
        answer = input("do you want to add more animals ? Y/N")
        if answer == 'N' or answer == 'n' :
            break
def search(zoo):
    os.system("clear")
    print("------------------search---------------------")
    answer = input("do you want search by id  or name or espece : ")
    if answer == "name":
        while True:
            ans = input("enter name :")
            for a in zoo:
                if a["name"] == ans:
                    printinfo(zoo, a)
                    return
            os.system("clear")
            print("this name is not exist try again")
    if answer == "id":
        while True:
            ans2 = int(input("enter id: "))
            for i in zoo:
                if i["id"] == ans2:
                    printinfo(zoo, i)
                    return
            os.system("clear")
            print("this id is not exist try again")
    if answer == "espece":
        while True:
            ans3 = input("enter espece: ")
            for j in zoo:
                if j["espece"] == ans3:
                    printinfo(zoo, j) 
                    return
            os.system("clear")
            print("this espece is not exist try again")

def removeinfo(zoo):
    while True:
        found = False
        idx = int(input("enter id: "))
        for i in zoo:
            if idx == i["id"]:
                zoo.remove(i)
                print("animal removed successfully!")
                found = True
                os.system("clear")
                answer = input("do you want to remove more animals Y/N: ")
                if(answer == 'N' or answer == 'n'):
                    return
        if found == False:
            os.system("clear")
            print("this id is not exist try again")def updateinfo(zoo):
    os.system("clear")
    print("------------------update---------------------")
    while True:
        idofanimal = int(input("enter id of animal: "))
        name = input("enter name of animal: ")
        for i in zoo:
            if name == i["name"] and i["id"] == idofanimal:
                i["age"] = int(input("enter new age: "))
                i["espece"] = input("enter new espece: ")
                print("update done successfully")
                answer = input("do you want to update more animals Y/N ")
                if(answer == 'N' or answer == 'n'):
                    return
        os.system("clear")
        print("wrong name or id")
def removeinfo(zoo):
    while True:
        found = False
        idx = int(input("enter id: "))
        for i in zoo:
            if idx == i["id"]:
                zoo.remove(i)
                print("animal removed successfully!")
                found = True
                os.system("clear")
                answer = input("do you want to remove more animals Y/N: ")
                if(answer == 'N' or answer == 'n'):
                    return
        if found == False:
            os.system("clear")
            print("this id is not exist try again")

def statistiques(zoo):
    print("-----------------statistiques--------------------\n")
    print("number of animals is:", len(zoo))
    sum = 0
    for i in zoo:
        sum += i["age"]
    print("average of all amnimals is:", sum / len(zoo))
    sortbyage()
    j = len(zoo)
    print("the oldest animal is: ", zoo[0]["name"], "his age is: ", zoo[0]["age"], "year")
    print("the youngest animal is: ",zoo[len(zoo) - 1]["name"], "his age is: ", zoo[len(zoo) - 1]["age"], "year")
    l = 0
    mx = 0
    while l < len(zoo):
        s = 0
        count = 0
        while s < len(zoo):
            if zoo[l]["espece"] == zoo[s]["espece"]:
                count += 1
            s += 1
        if mx < count:
            mx = count
            es = zoo[l]["espece"]
        l += 1
    print("Most represented species: ", es)
def minuofzoo(zoo):
    print("----------------------------------------------------------------")
    print("                       MINU SCREEN                              ")
    print("----------------------------------------------------------------")
    print("[1]:show animals: ")
    print("[2]:add animal: ")
    print("[3]:search for animal: ")
    print("[4]:update animal: ")
    print("[5]:remove animal: ")
    print("[6]:animal statistics: ")
    rtx = int(input("enter your choice: "))
    if rtx == 1:
        os.system("clear")
        showanimals(zoo)
        input("press enter to restart: ")
        os.system("clear")
        minuofzoo(zoo)
    elif rtx == 2:
        os.system("clear")
        addfunction(zoo)
        input("press enter to restart: ")
        os.system("clear")
        minuofzoo(zoo)
    elif rtx == 3:
        os.system("clear")
        search(zoo)
        input("press enter to restart: ")
        os.system("clear")
        minuofzoo(zoo)
    elif rtx == 4:
        os.system("clear")
        updateinfo(zoo)
        input("press enter to restart: ")
        os.system("clear")
        minuofzoo(zoo)
    elif rtx == 5:
        os.system("clear")
        removeinfo(zoo)
        input("press enter to restart: ")
        os.system("clear")
        minuofzoo(zoo)
    elif rtx == 6:
        os.system("clear")
        statistiques(zoo)
        input("press enter to restart: ")
        os.system("clear")
        minuofzoo(zoo)
os.system("clear")
minuofzoo(zoo)
