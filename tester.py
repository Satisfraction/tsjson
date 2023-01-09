import json

with open('tsjson/accounts.json', 'r') as f:
    data = json.load(f)
  
print(data)

while True:
    eingabe = (input("Bitte gib alter oder kontostand ein:\nq um abzubrechen.\n"))
    if eingabe == "q":
        print("Bis zum nächsten mal...")
        break
    elif eingabe == "alter":
        for i in data:
            if i["age"] > 25:
                print(i["name"],i["age"])    
    elif eingabe == "kontostand":
        money = []
        for i in data: 
            money.append(i["balance"])
        highest = money[0]
        for number in money:
            if number > highest:
                highest = number
        print(highest)
    else:
        print("falsche Eingabe, versuche es erneut!")

data.close()
