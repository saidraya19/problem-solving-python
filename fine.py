import requests
def plan():
    time = int(input("Enter plant age in days :"))
    if(time > 2):
        print("Water the plants!")
    else:
        print("Plants are fine")
plan()
