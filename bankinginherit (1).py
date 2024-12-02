import sys
class Banking:
    account_no = 1000
    transactionlist=[]
    def __init__(self,name,address,phoneno,initialamt):
        self.name = name.upper()
        self.address = address.capitalize()
        self.phoneno = phoneno
        self.initialamt = initialamt
        self.account_no = Banking.account_no
    @staticmethod
    def printDetails():
        print("-----------------------------------------------------------------------------------------------------------------------------------------")
        print("NAME\t\t\tADDRESS", "\t\t\t", "PHONE NO.\t\t\t\tAMOUNT", "\t\t\t", "\t\tACCOUNTNO")
        print("-----------------------------------------------------------------------------------------------------------------------------------------")

    def singleAccount(self):
        print(self.name, "\t\t\t", self.address, "\t\t\t", self.phoneno, "\t\t\t", self.initialamt, "\t\t\t", self.account_no)
    def balanceEnquiry(self):
        print("Your account number", self.account_no)
        print("Your Balance is", self.initialamt)
bank=[]
class Deposit(Banking):
    def cashDeposit(self,depositamt):
        self.initialamt += depositamt
        deposit = {"Account_Number":self.account_no,"Amount":depositamt,"Status":"credit","Balance":self.initialamt}
        Banking.transactionlist.append(deposit)
class Withdrawal(Banking):
    def cashWithdrawal(self,withdrawamt):
        self.initialamt -= withdrawamt
        withdraw = {"Account_Number":self.account_no,"Amount":withdrawamt,"Status":"debit","Balance":self.initialamt}
        Banking.transactionlist.append(withdraw)

class Transaction(Deposit,Withdrawal):
    @staticmethod
    def transactionHistory():
        if (len(Banking.transactionlist) == 0):
            print("\nNO ACCOUNTS CREATED")
        else:
            print("Transaction History")
            accountno = int(input("Enter account number\t"))
            count = 0
            for list in Banking.transactionlist:
                if (accountno == list["Account_Number"]):
                    count = count + 1
                    if (count == 1):
                        print("\t\t\tAccount Number=", accountno)
                        print("\t\t\tAMOUNT\tSTATUS\t\t\t")
                    print("\t\t\t", list["Amount"], "\t", list["Status"], "\t\t\t")
            for k in bank:
                if(accountno==k.account_no):
                    print("Your Closing Balance is",k.initialamt)

            if(count==0):
                print("NO TRANSACTION OCCURED")





def menu():
    print("\t\t\t*******************")
    print("\t\t\tStar Bank of India")
    print("\t\t\t*******************")
    print("\t\t\t1.Create Account")
    print("\t\t\t2.View all added accounts")
    print("\t\t\t3.Single Account")
    print("\t\t\t4.Cash Deposit")
    print("\t\t\t5.Cash Withdrawal")
    print("\t\t\t6.Balance Enquiry")
    print("\t\t\t7.Transaction History")
    print("\t\t\t8.Exit")
    choice = int(input("\nEnter choice:\t"))
    match(choice):
        case 1:
            print("Create Account")
            name = input("Enter a name\t")
            address = input("Enter address\t")
            phoneno = int(input("Enter phone number\t"))
            initialamt = int(input("Enter initial amount\t"))
            if (initialamt >= 1000):
                Banking.Account_no = Banking.Account_no + 1
                print()
                print("Account created successfully")
                print()
                print("Your Account number is", Banking.Account_no)
            else:
                for i in range(1, 3):
                    if (initialamt <= 1000):
                        print("Enter initial amount above 1000")
                        initialamt = int(input("Enter initial amount:\t"))
                        if (initialamt >= 1000):
                            Banking.Account_no = Banking.Account_no + 1
                            print()
                            print("Account created successfully")
                            print()
                            print("Your Account number is", Banking.Account_no)
                            break
                else:
                    print("\nPlease try again")
                    menu()
            ob=Transaction(name,address,phoneno,initialamt)
            bank.append(ob)


        case 2:
            if(len(bank)==0):
                print("\nNO ACCOUNTS CREATED")
            else:
                print("View all added accounts")
                Banking.printDetails()
                for k in bank:
                    k.singleAccount()


        case 3:
            if(len(bank)==0):
                print("\nNO ACCOUNTS CREATED")
            else:
                print("Single Account")
                accountno=int(input("Enter account number\t"))
                for k in bank:
                    if (accountno == k.account_no):
                        Banking.printDetails()
                        k.singleAccount()
                        break
                else:
                    print("Account does not exist")




        case 4:
            #print("Cash Deposit")
            if(len(bank)==0):
                print("\nNO ACCOUNTS CREATED")
            else:
                print("Cash Deposit")
                accountno = int(input("Enter account number\t"))
                count = 0
                for k in bank:
                    if(accountno == k.account_no):
                        print("Your Account Balance is", k.initialamt)
                        depositamt = int(input("Enter Deposit Amount\t"))
                        if (depositamt > 0):
                           k.cashDeposit(depositamt)
                           print()
                           print("Cash Deposited Successfully")
                           print("Your account balance is", k.initialamt)
                           count=count+1
                           break
                        if(depositamt<=0):
                            for i in range(1,3):
                                if(depositamt<=0):
                                    print("Enter deposit amount above zero")
                                    depositamt = int(input("Enter Deposit Amount\t"))
                                    if (depositamt > 0):
                                        k.cashDeposit(depositamt)
                                        print()
                                        print("Cash Deposited Successfully")
                                        print("Your account balance is", k.initialamt)
                                        count=count+1
                                        break
                            else:
                                print("\nPlease try again")
                                menu()
                                break
                        if(count>=1):
                            break
                else:
                    print("Account does not exist")


        case 5:
            #print("Cash Withdrawal")
            if(len(bank)==0):
                print("\nNO ACCOUNTS CREATED")
            else:
                print("Cash Withdrawal")
                accountno = int(input("Enter account number\t"))
                count=0
                for k in bank:
                    if(accountno==k.account_no):
                        print("Your account balance is", k.initialamt)
                        withdrawamt = int(input("Enter Withdrawal Amount\t"))
                        if (withdrawamt > k.initialamt):
                            print("Insufficient Balance")
                            print("Your Account balance is", k.initialamt)
                            break
                        if (withdrawamt > 0):
                            if (k.initialamt-withdrawamt < 1000):
                                print("Minimum balance of Rs.1000 should be maintained")
                                print("Your Balance is", k.initialamt)
                                break
                            k.cashWithdrawal(withdrawamt)
                            print()
                            print("Amount withdrew successfully")
                            print("Your account balance is", k.initialamt)
                            count = count + 1
                            break
                        if (withdrawamt <= 0):
                            for i in range(1, 3):
                                if (withdrawamt <= 0):
                                    print("Enter withdraw amount above zero")
                                    withdrawamt = int(input("Enter Withdrawal Amount\t"))
                                    if (withdrawamt > 0):
                                        if(k.initialamt-withdrawamt<1000):
                                            print("Minimum balance of rs.1000 should be maintained")
                                            print("Your account balance is", k.initialamt)
                                            break
                                        k.cashWithdrawal(withdrawamt)
                                        print()
                                        print("Your account balance is",k.initialamt)
                                        count=count+1
                                        break
                            else:
                                print("\nPlease try again")
                                menu()
                        if(count>=1):
                            break
                else:
                    print("Account does not exist")
        case 6:
            #print("Balance Enquiry")
            if (len(bank) == 0):
                print("\nNO ACCOUNTS CREATED")
            else:
                print("Balance Enquiry")
                accountno = int(input("Enter account number\t"))
                for k in bank:
                    if (accountno == k.account_no):
                        k.balanceEnquiry()
                        break
                else:
                    print("Account does not exist")
        case 7:
            Transaction.transactionHistory()

        case 8:
            print("Thank You")
            sys.exit()
        case _:
            print("Invalid Choice")
#--------------------------------------------------------------------
while True:
    menu()
    while True:
        comment=input("\nDo you want to continue?Enter y or n:\t")
        if(comment=='y' or comment=='Y'):
            menu()
            pass
        elif(comment=='n' or comment=='N'):
            print("Thank You Visit Again")
            break
        else:
            print("Invalid comment")
            pass
    if(comment=='n' or comment=='N'):
        break