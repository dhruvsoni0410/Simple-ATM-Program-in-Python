import time

def PinCheck(pinn):
    with open("pin.txt") as f:
        pin = f.read()
    if pin == pinn:
        return True
    else:
        return False

def WithrawMoney(bal):
    with open("bal.txt") as f:
            abal = f.read()
    if(abal < bal):
        time.sleep(3)
        print("Insufficint Balance!!!")
    else:
        newbal = int(abal) - int(bal)
        with open("bal.txt", "w") as f:
                f.write(str(newbal))
        time.sleep(3)
        print("Collect Your Cash.....")

def BalanceEnquiry():
    with open("bal.txt") as f:
        bal = f.read()
    return bal

def ChangePin():
    cpin = input("Enter Current PIN: ")
    npin = input("Enter New PIN: ")
    if PinCheck(cpin) == False:
        print("Wrong PIN!!!")
    else:
        with open("pin.txt", "w") as f:
            f.write(npin)
        time.sleep(3)
        print("PIN Updated!!!")

print("\n******************************************** Welcome To The DJS Bank ATM *******************************************************\n")

pinn = input("Enter a PIN: ")
if PinCheck(pinn) == False:
    print("Worng PIN!!!")
    exit()
else: 
    print('''\n 1. Withraw Cash
 2. Balance Enquiry
 3. Change PIN
''')
choice = int(input("Please Enter Your Choise: "))

if choice == 1:
    bal = input("Enter The Number: ")
    WithrawMoney(bal)

elif choice == 2:
    time.sleep(3)
    print(f"Your Account Balance is {BalanceEnquiry()}")

elif choice == 3:
    ChangePin()
