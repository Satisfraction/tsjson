import json

user_file = open('tsjson/accounts.json')

  
print(user_file)


data = json.load(user_file)


while True:
    eingabe = (input("Bitte gib alter oder Kontostand ein:\nq um abzubrechen.\n"))
    if eingabe == "q":
        print("Bis zum nächsten mal...")
        break
    elif eingabe == "alter":
        for i in data:
            if i["age"] > 25:
                print(i["name"],i["age"])    
    elif eingabe == "Kontostand":
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


user_file.close()