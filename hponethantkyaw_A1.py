"""
Name: Hpone Thant Kyaw
Date: 28/4/2017
Detail: This program is about Shopping List. In this program, we receive information from the user and store the received information in a file called items.csv, and can be rechecked what items are stored in this program.
Link: https://github.com/hponethat1/hponethantkyaw_A1_Programming-I.git

"""

MENU_TEXT = ["R", "List required items", "C", "List completed items", "A", "Add new item",
             "M", "Mark an item as completed", "Q", "Quit"]

itemFile = open("items.csv", "r+")
itemList = []
for row in itemFile:
    itemList.append(row)
itemFile.close()

"""
Function main
open items.csv as itemFile
turn itemFile into a list named itemList
close itemFile
display "Shopping List 1.0 - by Hpone Thant Kyaw"
display number of lines in itemList + "items loaded from items.csv"
while menuInput not equal to "Q"
    display menu
    get menuInput from user
    while menuInput does not equal menu options
        display "Invalid menu choice"
        get menuInput from user
    if menuInput equals "R"
        display "Required items:"
        run function itemMenu("r")
    else if menuInput equals "C":
        display "Completed items:"
        run function itemMenu("c")
    else if menuInput equals "A":
    Display “Item name: “
        get newItemName
        while newItemName is blank
            display "Input can not be blank"
        Display “Item name: “
            get newItemName
    display "Price: $"
    get newItemPrice
        while newItemPrice < 0
            display "Price must be >= $0"
            display "Price: $"
            get newItemPrice
    display “Priority: "
    get newItemPriority
    while newItemPriority < 0 or > 3
        display "Priority must be 1, 2 or 3"
        display “Priority: "
        get newItemPriority
    newItemInfo = "r "
    newItem = newItemName + newItemPrice + newItemPriority + newItemInfo
    add newItem to itemList
    display newItem + “ added to the shopping list
    else if menuInput equals "M":
        get itemOrder from function itemMenu("r")
        display "Enter the number of an item to mark as completed"
        display ">>>"
        get itemMarkInput
            while itemMarkInput not in itemOrder
                display"Invalid item number")
                display ">>>"
                get itemMarkInput
        itemSelected = itemOrder[itemMarkInput]
        i = 0
        for row in itemList:
            if row equals itemSelected:
                itemInfo = row.split(",")
                itemInfo[3] = "c"
                itemList[i] = itemInfo[0] + "," + itemInfo[1] + "," + itemInfo[2] + "," + itemInfo[3]
            i += 1
        display itemSelected[name] + “ marked as completed
    else if menuInput equals "Q":
        open items.csv as itemFile
        for item in itemList:
            print item itemFile
        display number of lines in itemList + " items saved to items.csv"
        display "Have a nice day 🙂"
        close itemFile
Function itemMenu
itemCount = 0
    for row in itemList
        item = row.split()
        if item[3] equals "r" or "c"
            itemCount += 1
    i = 0
    itemTotal = 0.0
    for priority in range(3)
        for row in itemList
            item = row.split()
            if item[3] equals "r" or "c" and item[2] equals priority
                display i + item[0] + item[1] + item[2]
                itemTotal += item[1]
                itemOrder[i] = row
                i += 1
    display itemTotal
    return itemOrder

"""

def main():
    print("Shopping List 1.0 - by Hpone Thant Kyaw")
    print("{} items loaded from items.csv".format(len(itemList)))

    menuInput = ""
    while menuInput != "Q":
        menuInput = ""
        while menuInput not in MENU_TEXT[::2]:
            print("Menu:")
            for item in range(5):
                item *= 2
                print("{} - {}".format(MENU_TEXT[item], MENU_TEXT[item+1]))
            menuInput = str(input(">>>")).upper()
            if menuInput not in MENU_TEXT[::2]:
                print("Invalid menu choice")
        if menuInput == "R":
            print("Required items:")
            itemMenu("r")

        elif menuInput == "C":
            print("Completed items:")
            itemMenu("c")

        elif menuInput == "A":
            newItemInfo = ["",0.0,0,""]
            newItemInfo[0] = str(input("Item name: "))
            while newItemInfo[0] == " ":
                print("Input can not be blank")
                newItemInfo[0] = str(input("Item name: "))
            while True:
                try:
                    newItemInfo[1] = float(input("Price: $"))
                    while newItemInfo[1] < 0:
                        print("Price must be >= $0")
                        newItemInfo[1] = float(input("Price: $"))
                    break
                except ValueError:
                    print("Invalid input; enter a valid number")
            while True:
                try:
                    newItemInfo[2] = int(input("Priority: "))
                    while newItemInfo[2] <= 0 or newItemInfo[2] > 3:
                        print("Priority must be 1, 2 or 3")
                        newItemInfo[2] = int(input("Priority: "))
                    break
                except ValueError:
                    print("Invalid input; enter a valid number")
            newItemInfo[3] = "r\n"
            newItem = str(newItemInfo[0]) + "," + str(newItemInfo[1]) + "," + str(newItemInfo[2]) + "," + str(newItemInfo[3])
            itemList.append(newItem)
            print("{}, ${:.2f} (priority {}) added to the shopping list".format(newItemInfo[0], newItemInfo[1], newItemInfo[2]))

        elif menuInput == "M":
            itemOrder = itemMenu("r")
            print("Enter the number of an item to mark as completed")
            while True:
                try:
                    itemMarkInput = int(input(">>>"))
                    while itemMarkInput not in range(len(itemOrder)):
                        print("Invalid item number")
                        itemMarkInput = int(input(">>>"))
                    break
                except ValueError:
                    print("Invalid input; enter a number")
            itemSelected = itemOrder[itemMarkInput]
            i = 0
            for row in itemList:
                if row == itemSelected:
                    itemInfo = row.split(",")
                    itemInfo[3] = "c\n"
                    itemList[i] = itemInfo[0] + "," + itemInfo[1] + "," + itemInfo[2] + "," + itemInfo[3]
                i += 1
            print("{} marked as completed".format(itemSelected.split(",")[0]))

        elif menuInput == "Q":
            itemFile = open("items.csv", "w")
            for item in itemList:
                itemFile.write(item)
            print("{} items saved to items.csv".format(len(itemList)))
            print("Have a nice day 🙂")
            itemFile.close()


def itemMenu(itemState):
    itemCount = 0
    for row in itemList:
        item = row.split(",")
        if item[3] == "{}\n".format(itemState):
            itemCount += 1
    i = 0
    itemTotal = 0.0
    itemOrder = [0] * itemCount
    for priority in range(3):
        for row in itemList:
            item = row.split(",")
            if item[3] == "{}\n".format(itemState) and item[2] == str(priority + 1):
                print("{}. {:18}  $ {:.2f} ({})".format(i, item[0], float(item[1]),item[2]))
                itemTotal += float(item[1])
                itemOrder[i] = row
                i += 1
    print("Total expected price for {} items: ${:.2f}".format(i, itemTotal))
    return itemOrder

main()



