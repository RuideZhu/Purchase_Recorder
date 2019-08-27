from datetime import date
import os


def cmdList():
    print("\"dis\"  for displaying all items in file")
    print("\"add\"  for adding items in file")
    print("\"cmd\"  for seeing this list again")
    print("\"del\"  for deleteing items in file")
    print("\"date\" for searching purchase according to date")
    print("\"cate\" for searching purchase according to category")
    print("\"remove\" for deleteing ALL data")
    print("\"repo\" for generating report for purchase on the specific month")
    print("\"quit\" for quiting the program")

def main():
    print("\nWelcome!\n")
    cmdList()

    try:
        file = open("output.txt",'r+')
    except:
        print("\n\nOops! You are the first time here!")
        f = open("output.txt","w+")
        f.close()
        print("A file named \"output.txt\" created under the same dictionary")
        print("It used to stored all the data generated by program")
        file = open("output.txt",'r+')

    keepgoing = True
    while keepgoing:
        cmd = input("\nCommand: ").strip().lower()
        file.seek(0)
        print()

        if cmd == "cmd":
            cmdList()

        elif cmd == "remove":
            comfirm = input("Are you sure you want to remove output.txt (y/n)?").lower()
            if(comfirm == 'y'):
                os.remove("output.txt")
                keepgoing = False
                print("Safely exited")


        elif cmd == "add":
            old_data = file.read()
            cate = input("Under which category? ").strip()
            file.write(cate)
            money = float(input("Money cost: "))
            file.write(", %.2f, " %money)
            today = date.today()
            file.write(today.strftime("%m/%d/%Y"))
            note = input("Any additional notes? enter \"no\" if there is not any: \n").strip()
            if(note!="no"):
                file.write(", %s" %note)
            file.write("\n")
            file.close()
            file = open("output.txt",'r+')

        elif cmd == "dis":
            print("CATEGORY          PRICE        DATE  NOTES\n")
            data = file.readlines()
            for i in range(len(data)):
                data2=data[i].split(",")
                for p in range(len(data2)):
                    if(p==3):
                        print(data2[p],end = "  ")
                    else:
                        print("%10s"%data2[p],end = "  ")
                print()
            print()

        elif cmd == "del":
            cate = input("category of the item you want to remove: ")
            num = input("cost of the item you want to remove (X.XX): ")
            lines = file.read().strip().split("\n")
            file.close()
            file = open("output.txt",'w')
            did = False
            for i in range(len(lines)):
                temp = lines[i].split(",")
                if (temp[0].strip() != cate or temp[1].strip() != num):
                    file.write(lines[i])
                    file.write("\n")
                else:
                    did = True
            if did:
                print("\nDeleted!")
            else:
                print("\nFailed!")
            file.close()
            file = open("output.txt",'r+')

        elif cmd == "date":
            data = input("\nEnter the date to find purchase (MM/DD/YYYY): ")
            print("\nPurchase on that day:")
            print("  CATEGORY        PRICE        DATE   NOTES\n")
            file_data = file.readlines()
            for i in range(len(file_data)):
                data2=file_data[i].split(",")
                if (data2[2].strip() == data):
                    for p in range(len(data2)):
                        if(p==3):
                            print(data2[p],end = "  ")
                        else:
                            print("%10s"%data2[p],end = "  ")
                    print()
            print()

        elif cmd == "cate":
            data = input("\nEnter the category to find purchase: ")
            print("\nPurchase on that category:")
            print("CATEGORY          PRICE        DATE   NOTES\n")
            file_data = file.readlines()
            for i in range(len(file_data)):
                data2=file_data[i].split(",")
                if (data2[0].strip() == data):
                    for p in range(len(data2)):
                        if(p==3):
                            print(data2[p],end = "  ")
                        else:
                            print("%10s"%data2[p],end = "  ")
                    print()
            print()

        elif cmd == "repo":
            mon = input("\nWhich month do you want to generate report (MM/YYYY): ")
            file_data = file.readlines()
            print("\nPurchase on that month:")
            print("CATEGORY          PRICE        DATE   NOTES")
            dic = {}
            sum = 0;
            for i in range(len(file_data)):
                data2=file_data[i].strip().split(",")
                if (data2[2].strip()[0:2]==mon[0:2] and data2[2].strip()[6:10]==mon[3:7]):
                    if data2[0] in dic:
                        dic[data2[0]] += float(data2[1])
                    else:
                        dic[data2[0]] = float(data2[1])
                    sum += float(data2[1]);
                    for p in range(len(data2)):
                        if(p==3):
                            print(data2[p],end = "  ")
                        else:
                            print("%10s"%data2[p],end = "  ")
                    print()
            print()

            print("Spending Analysis: ")
            for key in dic:
                print("%10s"%key,end = "   ")
                print("%10.2f"%(float(dic[key])/sum*100),end = "")
                print("%")

        elif cmd == "quit":
            keepgoing = False
            file.close()
            print("Safely exited")
        else:
            print("Invaild Command")

if __name__ == '__main__':
    main()
