stock = [5, 7, 8]
fruit = ['apple', 'grape', 'orange']
price = [10000, 15000, 20000]
qtt = [0,0,0]

#for exit function
import sys  

#for pause menu
import time

#hide typing while input]
import getpass

print('\nLOGON PAGE\n')
#this print is useless

def main(): #fucntion not really usefull
    login()

def login():
    username = 'admin'
    password = 'admin'
    print('Please write your username:')
    answer_u = input()
    answer_p = getpass.getpass('Please write your passwod: \n')
    if answer_u == username and answer_p == password:
        print('\nWelcome to Fruit Store')
        time.sleep(1) # 1 sec pause
        menu() #return to menu
def availability():
    print('\nCurrent stock is')
    print(f'{stock[0]} of {fruit[0]}')
    print(f'{stock[1]} of {fruit[1]}')
    print(f'{stock[2]} of {fruit[2]}')

def menu():
    print("\n\n\n**********MAIN MENU**********")
    time.sleep(1)
    menu_choice = int(input("""
    1. See Cart
    2. See Available Fruit
    3. Add Fruit
    4. Shop/Pay
    5. Exit
    Your choice : """))
    if menu_choice == 1:
        print(
            f'Your cart is\n{qtt[0]} of {fruit[0]} for {price[0]} each,\n{qtt[1]} of {fruit[1]} for {price[1]} each,\n{qtt[2]} of {fruit[2]} for {price[2]} each')
        menu()
    elif menu_choice == 2:
        availability()
        print(input('Press enter to go back to menu : '))
        menu()
    elif menu_choice == 3:
        # stock = [5,7,8]
        # fruit = ['apple','grape','orange']
        print('\nCurrent stock is')
        print(f'{stock[0]} of {fruit[0]}')
        print(f'{stock[1]} of {fruit[1]}')
        print(f'{stock[2]} of {fruit[2]}')
        for i in range(len(stock)):
            aggn = True
            while aggn:
                qtt[i] = int(input(f"\nHow many {fruit[i]} do you want? "))
                if qtt[i] > stock[i]:
                    print(f'Your request is exeeding our stock {stock[i]}')
                else:
                    aggn = False
            i += 1

        menu()
    elif menu_choice == 4:
        print('Your total bill is:')
        print(f"{qtt[0]} of apple x 10000 = {qtt[0] * int(price[0])}\n")
        print(f"{qtt[1]} of grape x 15000 = {qtt[1] * int(price[1])}\n")
        print(f"{qtt[2]} of orange x 20000 = {qtt[2] * int(price[2])}\n")
        total_bill = (((qtt[0]) * int(price[0])) + ((qtt[1]) * int(price[1])) + ((qtt[2]) * int(price[2])))
        print(f"Your total cart is {total_bill}\n")
        print('Please insert amount you want to pay')
        pay1 = int(input())
        if pay1 < total_bill:
            print('Please insert more money..')
            pay2 = int(input())
            pay3 = pay2 + pay1
            if pay3 < total_bill:
                print('Please pay the amount left!!')
                last_pay4 = int(input())
                final_pay = last_pay4 + pay3
                if final_pay < total_bill:
                    newqtt = list(map(lambda x: x * 0, qtt))
                    print(newqtt)
                    empty_cart_total = (((newqtt[0]) * int(price[0])) + ((newqtt[1]) * int(price[1])) + ((newqtt[2]) * int(price[2])))
                    print(f"Your total cart is {empty_cart_total}\n")
                if final_pay > total_bill:
                    tot = final_pay - total_bill
                    print('Your total bill is:')
                    print(f"{qtt[0]} of apple x 10000 = {qtt[0] * int(price[0])}\n")
                    print(f"{qtt[1]} of grape x 15000 = {qtt[1] * int(price[1])}\n")
                    print(f"{qtt[2]} of orange x 20000 = {qtt[2] * int(price[2])}\n")
                    print(f"Your total bill is {total_bill}\n")
                    print(f'And your change is {tot}')
                if final_pay==total_bill:
                    print('Your total bill is:')
                    print(f"{qtt[0]} of apple x 10000 = {qtt[0] * int(price[0])}\n")
                    print(f"{qtt[1]} of grape x 15000 = {qtt[1] * int(price[1])}\n")
                    print(f"{qtt[2]} of orange x 20000 = {qtt[2] * int(price[2])}\n")
                    print(f"Your total bill is {total_bill}\n")

            if pay3 > total_bill:
                tot1 = pay3 - total_bill
                print('Your total bill is:')
                print(f"{qtt[0]} of apple x 10000 = {qtt[0] * int(price[0])}\n")
                print(f"{qtt[1]} of grape x 15000 = {qtt[1] * int(price[1])}\n")
                print(f"{qtt[2]} of orange x 20000 = {qtt[2] * int(price[2])}\n")
                print(f"Your total bill is {total_bill}\n")
                print(f'And your change is {tot1}')
            if pay3 == total_bill:
                print('Your total bill is:')
                print(f"{qtt[0]} of apple x 10000 = {qtt[0] * int(price[0])}\n")
                print(f"{qtt[1]} of grape x 15000 = {qtt[1] * int(price[1])}\n")
                print(f"{qtt[2]} of orange x 20000 = {qtt[2] * int(price[2])}\n")
                print(f"Your total cart is {total_bill}\n")
        elif pay1 > total_bill:
            tot2 = pay1 - total_bill
            print(f"{qtt[0]} of apple x 10000 = {qtt[0] * int(price[0])}\n")
            print(f"{qtt[1]} of grape x 15000 = {qtt[1] * int(price[1])}\n")
            print(f"{qtt[2]} of orange x 20000 = {qtt[2] * int(price[2])}\n")
            print(f"Your total cart is {total_bill}\n")
            print(f'Your change is {tot2}')

        for i in range(len(stock)):
            new_sum = int(stock[i]) - int(qtt[i])
        #   stock = [(int(stock[i]))-(int(qtt[i]) for i in (len(stock)))]   ///error
            stock.pop(i)
            stock.insert(i, new_sum)

        
        menu()
    elif menu_choice == 5:
        sys.exit
    else: #looping wrong input
        print('You only need to select either 1,2,3, or 4')
        print('Please try again')
        menu()


main()