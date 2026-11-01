import requests
def inventory(type_seed, quantity, unit):
    if(type_seed == "tomato"):
        print("tomato seeds :", quantity, " ", unit, "available")
    elif(type_seed == "carrot"):
        print("carrot seeds :", quantity, " ", unit, "total")
    elif(type_seed == "lettuce"):
        print("lettuce seeds : covers ", quantity, "square meters")
inventory("tomato", 15, "packets")

