import sqlite3
conn = sqlite3.connect("stocks.db")
cursor = conn.cursor()
try:
    cursor.execute("""CREATE TABLE stock(id INTEGER,item TEXT, amount INTEGER)""")
    print("Created table")
    conn.commit()
except:
    print("table already created")
    conn.commit()
    print("Welcome to the stock checker")
while True:
    choice = int(input("""\nWhat do you want to do?
    Enter the number:
    1. Check Stock
    2. Add Stock
    3. Update Stock
    4. Delete Stock
    5. Exit\n"""))

    if choice == 1:
        rows = cursor.execute("""SELECT id,item,amount FROM stock""").fetchall()
        if rows == []:
            print("\nNo stock recorded")
        else:
            for item in rows:
                print(f'Item ID: {item[0]} Item: {item[1]} Amount: {item[2]}')
        conn.commit()

    elif choice == 2:
        id = 0
        rows = cursor.execute("""SELECT id,item,amount FROM stock""").fetchall()
        if rows == []:
            print(id)
        else:
            for item in rows:
                id = item[0]
            while True:
                print(f'\nLast item ID = {id}')
                print(f'New Item ID = {id+1}')
                item = input("Enter the item: ")
                amount = int(input("Enter the amount: "))
                check = input(f'\nItem ID: {id+1}, Item: {item}, Amount: {amount} is this right? (yes/no): ')
                if check.lower() == "no":
                    exiting = int(input("""Do you want to go:
                     1. Restart
                     2. Go Back
                     3. Quit
                     """))
                    if exiting == 1:
                        pass
                    elif exiting == 2:
                        break
                    elif exiting == 3:
                        quit()
                    else:
                        print("Enter a number from the list")
                elif check.lower() == "yes":
                    cursor.execute("INSERT INTO stock VALUES(?,?,?)",(id+1, item, amount))
                    conn.commit()
                    print("Added new stock item!")
                    break
                else:
                    print("Yes or No?")

    elif choice == 3:
        rows = cursor.execute("""SELECT id,item,amount FROM stock""").fetchall()
        if rows == []:
            print("\nNo stock recorded")
        else:
            for item in rows:
                print(f'Item ID: {item[0]} Item: {item[1]} Amount: {item[2]}')
            itemID = int(input("Enter the ID of the item you want to update: "))
            while True:
                choice = input("Name/Amount Change?: ")

                if choice.lower() == 'amount':
                    newAmount = int(input("Enter the quantity: "))
                    cursor.execute("""UPDATE stock SET amount=? WHERE id=?""",(newAmount,itemID))
                    conn.commit()
                    print("Updated!")
                    break
                elif choice.lower() == 'name':
                    newItem = input("Enter the name of the item: ")
                    cursor.execute("""UPDATE stock SET item=? WHERE id=?""",(newItem, itemID))
                    conn.commit()
                    print("Updated!")
                    break
                else:
                    print("Chose name or amount")

    elif choice == 4:
        rows = cursor.execute("""SELECT id,item,amount FROM stock""").fetchall()
        if rows == []:
            print("\nNo stock recorded")
        else:
            for item in rows:
                print(f'Item ID: {item[0]} Item: {item[1]} Amount: {item[2]}')
        itemID = int(input("Enter the ID of the item you want to delete: "))
        choice = input(f"Do you want to delete this item with id of {itemID}? (yes/no)")
        if choice.lower() == 'yes':
            cursor.execute("DELETE FROM stock WHERE id=?",(itemID,))
            print("Deleted item!")
        elif choice.lower() == 'no':
            print("Going back to main menu...")

        else:
            print("Yes or no")


    elif choice == 5:
        conn.commit()
        conn.close()
        exit()

    else:
        print("Pick a number from the option")