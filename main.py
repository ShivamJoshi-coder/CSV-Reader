# HI GUYS HOPE YOU ENJOY!
import csv 
import os
product_list = []
with open("products-10000.csv", "r", encoding="utf-8") as products:
    reader = csv.DictReader(products)
    for row in reader:
        product_list.append(row)
def write_to_file():
    headers = product_list[0].keys()
    with open("products-10000.csv", "w", newline="", encoding= "utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(product_list)
while True:
    print("MENU! Input a number to select")
    print("--------------------------------")
    print("1. Looking for something, here is 10,000 options")
    print("2. Search for product")
    print("3. Update data")
    print("4. End Program")
    userInput = input("Please enter a number from above: ")
    os.system('cls' if os.name == 'nt' else 'clear') 
    if userInput == "4":
        break
    elif userInput == "2":
        product = input("What product do you want? ")
        Found = False
        for item in product_list:
            if item["Name"] == product:
                for key in item.keys():
                    print(key + ": " + item[key])
                Found = True
                input("Press enter to continue")
                break
        if Found == False:
            print("We couldn't find anything of your use")
    elif userInput == "1":
        for item in product_list:
            print (item["Name"])
    elif userInput == "3":
        product = input("What product do you want to change? ")
        for item in product_list:
            if item["Name"] == product:
                print("Name,Description,Brand,Category,Price,Currency,Stock,EAN,Color,Size,Availability,Internal ID")
                category = input("What category would you like to change? ")
                if category in item.keys():
                    item[category] = input("What is the new value ")
                    write_to_file()
                    break
                else: 
                    print("Invalid category")
