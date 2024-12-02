import sys
class Banking:
    Account_no = 1000
    def __init__(self,name,address,phoneno,initialamt):
        self.name = name.upper()
        self.address = address
        self.phoneno = phoneno
        self.initialamt = initialamt
        self.account_no = Banking.Account_no
bank=[]
transactionlist=[]


def printDetails():
    print("-----------------------------------------------------------------------------------------------------------------------------------------")
    print("NAME\t\t\tADDRESS","\t\t\t","PHONE NO.\t\t\t\tAMOUNT","\t\t\t","\t\tACCOUNTNO")
    print("-----------------------------------------------------------------------------------------------------------------------------------------")
def viewAllAccounts():
    if (len(bank) == 0):
        print("\nNO ACCOUNTS CREATED")
    else:
        print("View all added accounts")
        printDetails()
        for k in bank:
            print(k.name,"\t\t\t",k.address,"\t\t\t",k.phoneno,"\t\t\t",k.initialamt,"\t\t\t",k.account_no)
def singleAccount():
    if(len(bank)==0):
        print("\nNO ACCOUNTS CREATED")
    else:
        print("Single Account")
        accountno = int(input("Enter account number\t"))
        count=0
        #k=0
        for k in bank:
            if(accountno==k.account_no):
                printDetails()
                print(k.name, "\t\t\t", k.address, "\t\t\t", k.phoneno, "\t\t\t", k.initialamt, "\t\t\t", k.account_no)
                break
        else:
            print("Account does not exist")

class Deposit:
    def cashDeposit(self):
        if (len(bank) == 0):
            print("\nNO ACCOUNTS CREATED")
        else:
            print("Cash Deposit")
            accountno = int(input("Enter account number\t"))
            count=0
            for k in bank:
                if(accountno==k.account_no):
                    print("Your Account Balance is",k.initialamt)
                    depositamt=int(input("Enter Deposit Amount\t"))
                    if(depositamt>0):
                        k.initialamt+=depositamt
                        deposit=Transaction(k.account_no,depositamt,"credit")
                        transactionlist.append(deposit)
                        print()
                        print("Cash deposited successfully")
                        print("Your account balance is",k.initialamt)
                        count=count+1
                        break
                    if (depositamt <= 0):
                        for i in range(1, 3):
                            if (depositamt <= 0):
                                print("Enter deposit amount above zero")
                                depositamt = int(input("Enter Deposit Amount\t"))
                                if (depositamt > 0):
                                    k.initialamt += depositamt
                                    deposit=Transaction(k.account_no,depositamt,"credit")
                                    transactionlist.append(deposit)
                                    print()
                                    print("Cash Deposited Successfully")
                                    print("Your account balance is",k.initialamt)
                                    count = count + 1
                                    break
                        else:
                            print("\nPlease try again")
                            menu()
                            break
                    if(count>=1):
                        break
            else:
                print("Account does not exist")
class Withdrawal:
    def cashWithdrawal(self):
        if (len(bank) == 0):
            print("\nNO ACCOUNTS CREATED")
        else:
            print("Cash Withdrawal")
            accountno = int(input("Enter account number\t"))
            count=0
            for k in bank:
                if(accountno==k.account_no):
                    print("Your account balance is",k.initialamt)
                    withdrawamt=int(input("Enter Withdrawal Amount\t"))
                    if(withdrawamt>k.initialamt):
                        print("Insufficient Balance")
                        print("Your Account balance is",k.initialamt)
                        break
                    if(withdrawamt>0):
                        k.initialamt-=withdrawamt
                        if(k.initialamt<=1000):
                            k.initialamt+=withdrawamt
                            print("Minimum balance of Rs.1000 should be mainitained")
                            print("Your Balance is",k.initialamt)
                            break
                        withdraw=Transaction(k.account_no,withdrawamt,"debit")
                        transactionlist.append(withdraw)
                        print("Amount withdrew successfully")
                        print("Your account balance is",k.initialamt)
                        count=count+1
                        break
                    if(withdrawamt<=0):
                        for i in range(1,3):
                            if(withdrawamt<=0):
                                print("Enter withdraw amount above zero")
                                withdrawamt = int(input("Enter Withdrawal Amount\t"))
                                if(withdrawamt>0):
                                    k.initialamt-=withdrawamt
                                    if(k.initialamt<=1000):
                                        k.initialamt+=withdrawamt
                                        print("Minimum balance of rs.1000 should be maintained")
                                        print("Your account balance is",k.initialamt)
                                        break
                                    withdraw=Transaction(k.account_no,withdrawamt,"debit")
                                    transactionlist.append(withdraw)
                                    print("Amount withdrew successfully")
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
def balanceEnquiry():
    if(len(bank)==0):
        print("\nNO ACCOUNTS CREATED")
    else:
        print("Balance Enquiry")
        accountno=int(input("Enter account number\t"))
        for k in bank:
            if(accountno==k.account_no):
                print("Your account number",k.account_no)
                print("Your Balance is",k.initialamt)
                break
        else:
            print("Account does not exist")
class Transaction:
    def __init__(self,accountno, amount,status):
        self.accountno = accountno
        self.amount = amount
        self.status = status

    # def transactionHistory(self):
    #     if(len(bank)==0):
    #         print("\nNO ACCOUNTS CREATED")
    #     else:







def menu(status=None, amount=None, account=None):
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
    match (choice):
        case 1:
            print("Create Account")

            name=input("Enter a name\t")
            address=input("Enter address\t")
            phoneno=int(input("Enter phone number\t"))
            initialamt=int(input("Enter initial amount\t"))
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
            ob = Banking(name,address,phoneno,initialamt)
            bank.append(ob)
        case 2:
            viewAllAccounts()
        case 3:
            singleAccount()
        case 4:
            credit=Deposit()
            credit.cashDeposit()
        case 5:
            debit=Withdrawal()
            debit.cashWithdrawal()
        case 6:
            balanceEnquiry()
        case 7:
            if(len(transactionlist)==0):
                print("\nNO ACCOUNTS CREATED")
            else:
                print("Transaction History")
                accountno=int(input("Enter account number\t"))
                #print("\t\t\tAccount Number=",accountno)
                #print("\t\t\tAMOUNT\tSTATUS\t\t\t")
                count=0
                for list in transactionlist:
                    #print(l)
                    if(accountno==list.accountno):
                        count=count+1
                        if(count==1):
                            print("\t\t\tAccount Number=", accountno)
                            print("\t\t\tAMOUNT\tSTATUS\t\t\t")
                        print("\t\t\t",list.amount,"\t",list.status,"\t\t\t")
                if(count==0):
                    print("No Transaction Occured")

        case 8:
            print("Thank You")
            sys.exit()
        case _:
            print("Invalid Choice")
#----------------------------------------------------------------
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










