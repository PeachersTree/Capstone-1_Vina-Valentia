# CAPSTONE PROJECT
from tabulate import tabulate

Etalase = [["1", "Foods"], ["2", "Drinks"], ["3", "Snacks"], ["4", "Meds"], ["5", "Exit Section"]]

Foods = [["Fried Rice", 10, "Spicy", "Big", 2.99], 
         ["Fried Chicken", 10, "Spicy", "Medium", 2.50], 
         ["Butter Rice", 10, "Mild", "Big", 2.00], 
         ["Pot Pie", 10, "Spicy", "Small", 3.00], 
         ["Carbonara", 10, "Mild", "Medium", 3.75]]
# print(tabulate(Foods, headers = ["Index", "Foods", "Stock", "Spice Level", "Portion", "Price"]))

Drinks = [["Tea", 10, "Non-alcohol", "Medium", 1.99], 
         ["Coffee", 10, "Non-alcohol", "Small", 2.20], 
         ["Water", 10, "Non-alcohol", "Big", 1.00], 
         ["Soda", 10, "Alcohol", "Medium", 2.55], 
         ["Beer", 10, "Alcohol", "Small", 3.60]]
# print(tabulate(Drinks, headers = ["Index", "Drinks", "Stock", "Category", "Portion", "Price"]))

Snacks = [["Pillows", 10, "Medium", 2.10], 
         ["Candy", 10, "Small", 0.66], 
         ["Ice Cream", 10, "Small", 1.99], 
         ["Cake", 10, "Big", 3.99], 
         ["Jelly", 10, "Medium", 1.60]]
# print(tabulate(Snacks, headers = ["Index", "Snacks", "Stock", "Portion", "Price"]))

Meds = [["Paracetamol", 10, "Fever", 2.50], 
         ["Inhaler", 10, "Cold", 2.99], 
         ["Eye drop", 10, "Pink eye", 2.80], 
         ["Cough Syrup", 10, "Cough", 3.60], 
         ["Band Aid", 10, "Wound", 1.35]]
# print(tabulate(Meds, headers = ["Index", "Meds", "Stock", "Indication", "Price"]))

menu = [["1", "Go to Section"], ["2", "Add to Cart"], ["3", "Discard Cart"], ["4", "Payment"], ["5", "Exit"]]


def display():
    while True:
        print("\n")
        print(tabulate(Etalase, headers=["Index", "Section"]))
        user_eta = input("\nWhich section you want to go: ")
        if user_eta == "1":
            print(tabulate(Foods, headers=["Foods", "Stock", "Spice Level", "Portion", "Price"]))
        elif user_eta == "2":
            print(tabulate(Drinks, headers=["Drinks", "Stock", "Category", "Portion", "Price"]))
        elif user_eta == "3":
            print(tabulate(Snacks, headers=["Snacks", "Stock", "Portion", "Price"]))
        elif user_eta == "4":
            print(tabulate(Meds, headers=["Meds", "Stock", "Indication", "Price"]))
        elif user_eta == "5":
            break
        else:
            print("Invalid input.")

def add(cart, total, cart_index):
    while True:
        user_eta = input("\nWhich section you want to go :")
        if user_eta == "1":
            section = Foods
            section_name = "Foods"
            headers = ["Index", "Foods", "Stock", "Spice Level", "Portion", "Price($)"]
            # print("\n")
            # print(tabulate(Foods, headers = headers))
        elif user_eta == "2":
            section = Drinks
            section_name = "Drinks"
            headers = ["Index", "Drinks", "Stock", "Category", "Portion", "Price($)"]
            # print("\n")
            # print(tabulate(Drinks, headers = headers))
        elif user_eta == "3":
            section = Snacks
            section_name = "Snacks"
            headers = ["Index", "Snacks", "Stock", "Portion", "Price"]
            # print("\n")
            # print(tabulate(Snacks, headers = headers))
        elif user_eta == "4":
            section = Meds
            section_name = "Meds"
            headers=["Index", "Meds", "Stock", "Indication", "Price"]
            # print("\n")
            # print(tabulate(Meds, headers = headers))
        elif user_eta == "5":
            break
        else:
            print("\nInvalid input.")
            continue

        while True:
            try:
                print("\n")
                section_with_index = [[i + 1] + item for i, item in enumerate(section)]  # Reindex dynamically
                print(tabulate(section_with_index, headers=headers))
                user_add = input("\nInput the item index that you want to buy: ")
                user_add = int(user_add) - 1 
                if 0 <= user_add < len(section):
                    stock = section[user_add][1]  
                    quant = int(input(f"\nEnter quantity for {section[user_add][0]} :"))
                    if quant <= stock:
                        price = quant * section[user_add][-1]
                        cart.append([cart_index , section[user_add][0], quant, section_name, price])
                        cart_index += 1
                        section[user_add][1] -= quant
                        print("\nCart")
                        print(tabulate(cart, headers=["Item", "Quantity", "Section", "Price"]))
                        total += price
                        print("Total Price :", total)
                    else:
                        print("\nSorry, only", stock, "units available for", section[user_add][1])
                else:
                    print("\nInvalid item index")
            except ValueError:
                print("\nPlease enter a valid number.")

            resume = input("\nDo you still want to buy from this section (yes/no): ").lower()
            if resume == "yes":
                continue
            else:
                print("\n")
                print(tabulate(Etalase, headers=["Index", "Section"]))
                break
    return cart, total, cart_index 

def discard(cart, sections):
    while True:
        dc = input("\nInput the item index you want to discard: ")
        dc = int(dc) - 1 
        if 0 <= dc < len(cart):
            item_name = cart[dc][1]
            dc_quant = int(input(f"How many {item_name} you want to discard :"))
            if dc_quant > 0 and dc_quant <= cart[dc][2]:
                cart[dc][-1] -= ((cart[dc][-1]/cart[dc][2])* dc_quant)
                cart[dc][2] -= dc_quant
                total = sum(item[-1] for item in cart)
                for section in sections:
                    for item in section:
                        if item[1] == item_name:
                            item[2] += dc_quant
                            break
                if cart[dc][2] == 0:
                    cart.pop(dc)
                print("\n")
                print(tabulate(cart, headers=["Index", "Item", "Quantity", "Section", "Price"]))
                print("Total Price :", total)
                other_dc = input("\nAre there any other item to discard (yes/no) :")
                if other_dc == "yes":
                    continue
                else:
                    break
            else:
                print("\nInvalid input.")
        else:
            print("\nInvalid input")

def payment(cart):
    total = sum(item[-1] for item in cart)
    print ("\nPlease double check your order!")
    print("\n")
    print (tabulate(cart, headers=["Index", "Item", "Quantity", "Section", "Price"]))
    print ("Total Price :", total)
    proceed = input("\nDo you want to proceed (yes/no) ?")
    if proceed == "yes":
        cuan = float(input("\nInput your total money :"))
        while True:
            if cuan < total:
                print ("\nYou don't have enough money")
                cuan = float(input("\nInput your total money :"))
            elif cuan == total:
                print ("\nThank You for your purchases")
                cart.clear()
                break
            elif cuan > total:
                change = cuan - total
                cart.clear()
                print("\nYour change :", change)
                print ("Thank You for your purchases")
                break

cart = []

def main(cart):
    cart_index = 1
    total = 0
    sections = [Foods, Drinks, Snacks, Meds]
    
    while True:
        print("\n")
        print(tabulate(menu, headers=["Index", "Menu"]))
        user_menu = input("\nInput number: ")

        if user_menu == "1":
            display()
        
        elif user_menu == "2":
            print("\n")
            print(tabulate(Etalase, headers = ["Index", "Section"]))
            add(cart, total, cart_index)
        
        elif user_menu == "3":
            if len(cart) > 0:
                update = [item[1:] for item in cart]
                cart_dex = [[i + 1] + item for i, item in enumerate(update)]  # Reindex dynamically
                print("\nCart")
                print(tabulate(cart_dex, headers = ["Index", "Item", "Quantity", "Section", "Price"]))
                discard(cart, sections)
            else:
                print("\nYour cart is now empty")

        elif user_menu == "4":
            payment(cart)
        
        elif user_menu == "5":
            print("\nTerima Kasih.\nSilahkan Datang Kembali!")
            break
        
        else:
            print("\nInvalid input")

menu_seller = [["1.", "Display item"], ["2.", "Add item"], ["3.", "Erase Item"], ["4.", "Exit"]]


def seller_add():
    while True:
        print("\n")
        print(tabulate(Etalase, headers=["Index", "Section"]))
        s_section = input("\nWhich section index do you want to go: ")
        if s_section == "1":
            while True:
                print("\n")
                print(tabulate(Foods, headers=["Foods", "Stock", "Spice Level", "Portion", "Price($)"]))
                s_add = input("\nInput food name you want to add: ").title()
                item_names = [item[0] for item in Foods]  
                if s_add in item_names:
                    print(f"{s_add} is already in draft.")
                    index = item_names.index(s_add) 
                    stock = int(input(f"Input stock addition for {s_add}: "))
                    Foods[index][1] += stock  
                else:
                    price = float(input(f"Input price for {s_add}: "))
                    stock = int(input(f"Input quantity for {s_add}: "))
                    spice_lv = input(f"Input spice level for {s_add}: ")
                    portion = input(f"Input portion for {s_add}: ")
                    Foods.append([s_add, stock, spice_lv, portion, price])
                print("\n")
                print(tabulate(Foods, headers=["Foods", "Stock", "Spice Level", "Portion", "Price($)"]))
                more = input("\nDo you still want to add in this section (yes/no): ").lower()
                if more == "yes":
                    continue
                else:
                    break
        elif s_section == "2":
            while True:
                print("\n")
                print(tabulate(Drinks, headers = ["Drinks", "Stock", "Category", "Portion", "Price($)"]))
                s_add = input("\nInput drink name you want to add :").title()
                item_names = [item[0] for item in Drinks]
                if s_add in item_names:
                    print(f"{s_add} is already in draft.")
                    index = item_names.index(s_add) 
                    stock = int(input(f"Input stock addition for {s_add}: "))
                    Drinks[index][1] += stock  
                else:
                    price = float(input(f"Input price for {s_add} :"))
                    stock = int(input(f"Input quantity for {s_add} :"))
                    category = input(f"Input category for {s_add} :")
                    portion = input(f"Input portion for {s_add} :")
                    Drinks.append([s_add, stock, category, portion, price])
                print("\n")
                print(tabulate(Drinks, headers=["Drinks", "Stock", "Category", "Portion", "Price($)"]))
                more = input("\nDo you still want to add in this section (yes/no): ").lower()
                if more == "yes":
                    continue
                else:
                    break
        elif s_section == "3":
            while True:
                print("\n")
                print(tabulate(Snacks, headers = ["Index", "Snacks", "Stock", "Portion", "Price($)"]))
                s_add = input("\nInput snack name you want to add :").title()
                item_names = [item[0] for item in Snacks]
                if s_add in item_names :
                    print(f"{s_add} is already in draft.")
                    index = item_names.index(s_add) 
                    stock = int(input(f"Input stock addition for {s_add}: "))
                    Snacks[index][1] += stock  
                else:
                    price = float(input(f"Input price for {s_add} :"))
                    stock = int(input(f"Input quantity for {s_add} :"))
                    portion = input(f"Input portion for {s_add} :")
                    Snacks.append([s_add, stock, portion, price])
                print("\n")
                print(tabulate(Snacks, headers=["Snacks", "Stock", "Portion", "Price($)"]))
                more = input("\nDo you still want to add in this section (yes/no): ").lower()
                if more == "yes":
                    continue
                else:
                    break
        elif s_section == "4":
            while True:
                print("\n")
                print(tabulate(Meds, headers = ["Meds", "Stock", "Indication", "Price($)"]))
                s_add = input("\nInput meds name you want to add :").title()
                item_names = [item[0] for item in Meds]
                if s_add in item_names :
                    print(f"{s_add} is already in draft.")
                    index = item_names.index(s_add) 
                    stock = int(input(f"Input stock addition for {s_add}: "))
                    Meds[index][1] += stock  
                else:
                    price = float(input(f"Input price for {s_add} :"))
                    stock = int(input(f"Input quantity for {s_add} :"))
                    indication = input(f"Input indication for {s_add} :")
                    Meds.append([s_add, stock, indication, price])
                print("\n")
                print(tabulate(Meds, headers=["Meds", "Stock", "Indication", "Price($)"]))
                more = input("\nDo you still want to add in this section (yes/no): ").lower()
                if more == "yes":
                    continue
                else:
                    break
        elif s_section == "5":
            break
        else:
            print("\nInvalid input")

def seller_er():
    while True :
        print("\n")
        print(tabulate(Etalase, headers=["Index", "Section"]))
        section = input("\nWhich section index you want to go :")
        if section == "1":
            while True :
                foods_dex = [[i + 1] + item for i, item in enumerate(Foods)]
                print("\n")
                print(tabulate(foods_dex, headers = ["Index", "Foods", "Stock", "Spice Level", "Portion", "Price($)"]))
                item = int(input("\nInput item index you want to erase :"))
                if item - 1 < len(Foods):
                    if Foods[item - 1] in Foods:
                        del Foods[item - 1]
                        print("\n")
                        print(tabulate(Foods, headers = ["Index", "Foods", "Stock", "Spice Level", "Portion", "Price($)"]))
                        more = input("\nDo you still want to erase item in this section (yes/no) :").lower()
                        if more == "yes":
                            continue
                        else:
                            break
                else:
                    print("\nItem is not in draft.")
                    continue
        elif section == "2":
            while True :
                drinks_dex = [[i + 1] + item for i, item in enumerate(Drinks)]
                print("\n")     
                print(tabulate(drinks_dex, headers = ["Index", "Drinks", "Stock", "Category", "Portion", "Price($)"]))
                item = int(input("\nInput item index you want to erase :"))
                if item - 1 < len(Drinks):
                    if Drinks[item - 1] in Drinks:
                        del Drinks[item - 1]
                        print("\n")
                        print(tabulate(Drinks, headers = ["Index", "Drinks", "Stock", "Category", "Portion", "Price($)"]))
                        more = input("\nDo you still want to erase item in this section (yes/no) :").lower()
                        if more == "yes":
                            continue
                        else:
                            break
                else:
                    print("\nItem is not in draft.")
                    continue
        elif section == "3":
            while True:
                snacks_dex = [[i + 1] + item for i, item in enumerate(Snacks)]
                print("\n") 
                print(tabulate(snacks_dex, headers = ["Index", "Snacks", "Stock", "Portion", "Price($)"]))
                item = int(input("Input item index you want to erase :").capitalize())
                if item - 1 < len(Snacks):
                    if Snacks[item - 1] in Snacks:
                        del Snacks[item - 1]
                        print(tabulate(Snacks, headers = ["Index", "Snacks", "Stock", "Portion", "Price($)"]))
                        more = input("Do you still want to erase item in this section (yes/no) :").lower()
                        if more == "yes":
                            continue
                        elif more == "no":
                            break
                else:
                    print("Item is not in draft.")
                    continue
        elif section == "4":
            while True :
                meds_dex = [[i + 1] + item for i, item in enumerate(Meds)]
                print("\n")
                print(tabulate(meds_dex, headers = ["Index", "Meds", "Stock", "Indication", "Price($)"]))
                item = int(input("\nInput item index you want to erase :"))
                if item - 1 < len(Meds):
                    if Meds[item - 1] in Meds:
                        del Meds[item - 1]
                        print("\n")
                        print(tabulate(Meds, headers = ["Index", "Meds", "Stock", "Indication", "Price($)"]))
                        more = input("\nDo you still want to erase item in this section (yes/no) :").lower()
                        if more == "yes":
                            continue
                        else:
                            break
                else:
                    print("\nItem is not in draft.")
                    continue            
        elif section == "5":
            break
        else:
            print("\nInvalid input")
            
def seller_main():
    while True:
        print("\n")
        print(tabulate(menu_seller, headers = ["Index", "Menu"]))
        seller = input("\nWhich menu index do you want to go :")
        if seller == "1":
            display()
        elif seller == "2":
            seller_add()
        elif seller == "3":
            seller_er()
        elif seller == "4":
            break
        else:
            print("Invalid input")
            continue

def buyer_seller():
    print("\nWELCOME TO INDOVINA!")
    while True:
        user = input("\nBuyer or Seller :").lower()
        if user == "buyer":
            main(cart)
        elif user == "seller":
            code = input("Password :")
            if code == "016Vina":
                seller_main()
            else:
                print("Wrong Password")
                continue

buyer_seller()