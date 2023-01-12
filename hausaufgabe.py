import json

with open('tsjson/accounts.json', 'r') as accounts:
    data = json.load(accounts)
  
print(json.dumps(data, indent=4))


while True:
    eingabe = (input("Bitte gib alter oder kontostand ein:\nquit um abzubrechen.\n"))
    if eingabe == "quit":
        print("Bis zum nächsten mal...")
        break
    elif eingabe == "alter":
        for i in data:
            if i["age"] >= 25:
                printf(i["name"], i["age"])    
    elif eingabe == "kontostand":
        money = []
        for i in data: 
            money.append(i["balance"])
        highest = money[0]
        for number in money:
            if number > highest:
                highest = number
        print(i["name"], highest)
    else:
        print("falsche Eingabe, versuche es erneut!")
        
data.close()
