import requests
def plan():
    time = int(input("Enter plant age in days :"))
    if(time <= 60):
        print("Plant needs more time to grow.")
    else:
        print("Plant is ready to harvest!")
plan()

