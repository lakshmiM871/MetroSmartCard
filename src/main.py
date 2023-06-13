from Users import *
from Database_ops import create_table,delete_table
#from SmartCard import *

if __name__ == '__main__':
    print("******************* Hello! Welcome to Metro Smart Card System************************")
    conn = connect_to_database()
#    delete_table(conn)
    #Create a table if not exist, if exists it display the table info
    create_table(conn)
    while(True):
        print()
        print("Please select operation from below options:")
        print("1. Generate new smart card")
        print("2. Recharge existing smart card")
        print("3. Check balance in smart card")
        print("4. Start journey")
        print("5. End journey")
        op=int(input("enter the option - "))
        match op:
            case 1:
                print(f"Your card num is {generate_card()} with balance amount Rs:50 created")
            case 2:
                print(f"After Recharging amount in the card is {recharge(int(input('Please Enter Amount to Recharge - ')),int(input('Please Enter Metro Card Num - ')))} ")
            case 3:
                print(f"Balance in the card is {check_balance(int(input('Please Enter Metro Card Num - ')))}")
            case 4:
                start_journey(input("Enter Boarding Station name  [A-O] - "),int(input('Please Enter Metro Card Num - ')))
            case 5:
                end_journey(input("Enter Destination Station name [A-O] - "),int(input('Please Enter Metro Card Num - ')))
            case _:
                print(" In-Valid Option")

        ch=input("Want to perform More Opearations Y/N ")
        if(ch =='y' or ch== 'Y'):
            continue
        else:
            print("\nHave a Good Day :) ")
            break



