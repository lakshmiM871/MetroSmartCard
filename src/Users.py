import uuid
import sqlite3
from Database_ops import connect_to_database,close_connection,add_data,bal_update,retrieve_bal,update_boarding_sta,retrieve_boarding_sta
stations = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12,
            'M': 13, 'N': 14, 'O': 15}
#Getting Username and ID proof from Passanger
def generate_user(func):
    def wrapper():
        #Decorator function func will generate a unique metrocard num for the passanger
        card_num=func()
        name= input("   enter name of the passenger -  ")
        aadhar_id= int(input("   enter aadhar no - "))
        #Inserting Passanger details to database without any duplicates
        try:
            add_data(name,aadhar_id,card_num,50)
            raise
        except Exception as e:
            print("User already have a metrocard")
        return card_num
    return wrapper

@generate_user
def generate_card():
    unique_id = str(uuid.uuid4().int)[:10]
    return unique_id
#generate_card()

def recharge(amt,metro_card_num):
    #Retrieving balance from the database and updating into database
    bal= retrieve_bal(metro_card_num)
    bal = bal + amt
    bal_update(bal,metro_card_num)
    return  bal

#Retrieving balance form database
def check_balance(metro_card_num):
    return retrieve_bal(metro_card_num)

#Checking Passanger has enough Balance to travel and Connecting to database and updating the boarding station name for the particular passanger if he swipe in successfully
def start_journey(source_name,metro_card_num):
    global stations
    bal=retrieve_bal(metro_card_num)
    if(bal<15):
        return "Insufficient Balance to enter into Metro ! Please Recharge"

    if(source_name in stations.keys()):
        update_boarding_sta(source_name,metro_card_num)
        return "Successfull Swipe In"


'''Retrieving Boarding station Details and checking the no of stations passanger has travelled and deciding the price based on below constraints and updating the total balance after deduction into Database
Calculate the fare and deduct it from card. Fare for 1st three stations is fixed at Rs.15 then Rs.5 per station

                - User shouldn’t be enter if the balance is less than Rs15 and user shouldn’t be able to exit if the balance is less than 0.

                - Add discount of 5% after every 5 stations
'''
def end_journey(dst_name,metro_card_num):
    bal=retrieve_bal(metro_card_num)
    boarding_station=retrieve_boarding_sta(metro_card_num)
    #print("balance ",bal)
    no_of_stas=abs(stations[dst_name]-stations[boarding_station])
    if(no_of_stas<4):
        bal -= 15
    elif(no_of_stas<6):
        bal-=(no_of_stas*5)
    else:
        bal=bal-(5*5+(no_of_stas-5)*(5-0.25))
    bal_update(bal,metro_card_num)
    try:
        if(bal>0):
            print("SwipeOut successfully")
        else:
            raise

    except Exception as e:
        print(" Insufficent Balance to Swipe Out! Please Recharge ")
