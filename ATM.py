print("WELCOME TO ABC BANK!!\n\n**Insert your card**")
password = 2177
Balance = 33000.00
choice = 1
pin = int(input("Enter your four digit pin number:\n"))
if pin==password:
    while choice != 4:
        print("\n\n*** Menu ***")
        print("1 == Balance")
        print("2 == Deposit")
        print("3 == Withdraw")
        print("4 == Cancel\n")
        choice = int(input("\nEnter your choice:\n"))
        if choice == 1:
            print("BALANCE = "f'{Balance:.2f}')
        elif choice == 2:
            deposit=float(input("Enter your deposit amount: "))
            Balance += deposit
            print("\nDeposit amount = ",deposit)
            print("BALANCE = "f'{Balance:.2f}')
        elif choice == 3:
            withdraw=float(input("Enter the amount to Withdraw: "))
            Balance -= withdraw
            print("\nWithdraw amount = ",withdraw)
            print("BALANCE = "f'{Balance:.2f}')
        elif choice == 4:
            print("\nENDED")
        else:
            print("\nINVALID ENTRY!")
else:
    print("PIN INCORRECT! TRY AGAIN")
