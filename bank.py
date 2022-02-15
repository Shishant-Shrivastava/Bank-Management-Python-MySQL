import mysql.connector
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '@Naruto123',
    database = 'bankmanagement'
)

cur = mydb.cursor()

while True:
    print("*"*200)
    print(" "*85,end='')
    print("Bank Managemet System")
    print("*"*200)
    choice = int(input("Please Choose one:\n1->Open Account\n2->Cash Deposit\n3->Cash Withdraw\n4->Account Details\n5->Update Account\n6->Exit\n\nEnter Your Choice : "))
    if choice==1:
        query = "SELECT accno FROM accounttable ORDER BY accno DESC LIMIT 0,1"
        cur.execute(query)
        a=list(cur.fetchone())
        a[0]+=1
        print("="*200) 
        name = input("\nEnter the name of Account Holder: ")
        balance = int(input("\nEnter the Opening Balance: "))
        mob = input("\nEnter your mobile no. : ")
        query = "INSERT INTO accounttable values({},'{}',{},'{}')".format(a[0],name,balance,mob)
        cur.execute(query)
        mydb.commit()
        print("="*200) 
        print("Congrats! Your Account is Succefully Created.\n\nYour Account Number is {}".format(a[0]))
        print("="*200)
    if choice==2:
        print("="*200)
        accno = int(input("Please Enter You Acconut Number : "))
        query = "SELECT * FROM accounttable WHERE accno = {}".format(accno)
        cur.execute(query)
        b = list(cur.fetchone())
        print("="*200)
        print("Your Current Balance : {}".format(b[2]))
        print("="*200)
        balance = int(input("Please Enter How much Cash you want to deposit: "))
        b[2]=b[2]+balance
        query = "UPDATE accounttable SET balance = {} WHERE accno = {}".format(b[2],accno)
        cur.execute(query)
        mydb.commit()
        query = "SELECT * FROM accounttable WHERE accno = {}".format(accno)
        cur.execute(query)
        b = list(cur.fetchone())
        print("="*200)
        print("\nCash Successfully Deposited!\nYour Current Balance : {}".format(b[2]))
        print("="*200)

    if choice==3:
        print("="*200)
        accno = int(input("Please Enter You Acconut Number : "))
        query = "SELECT * FROM accounttable WHERE accno = {}".format(accno)
        cur.execute(query)
        b = list(cur.fetchone())
        print("="*200)
        print("Your Current Balance : {}".format(b[2]))
        print("="*200)
        balance = int(input("Please Enter How much Cash you want to Withdraw: "))

        if b[2]>=balance:
            b[2]=b[2]-balance
            query = "UPDATE accounttable SET balance = {} WHERE accno = {}".format(b[2],accno)
            cur.execute(query)
            mydb.commit()
            query = "SELECT * FROM accounttable WHERE accno = {}".format(accno)
            cur.execute(query)
            b = list(cur.fetchone())
            print("="*200)
            print("\nCash Successfully Deposited!\nYour Current Balance : {}".format(b[2]))
            print("="*200)
        else:
            print("="*200)
            print("Withdraw ammount is greater than your Current Balance")
            print("="*200)

    if choice==4:
        print("="*200)
        accno = int(input("Please Enter You Acconut Number : "))
        query = "SELECT * FROM accounttable WHERE accno = {}".format(accno)
        cur.execute(query)
        b = list(cur.fetchone())
        print("="*200)
        print("Account Holder Name = {}\nYour Current Balance : {}\nRegistered Mobile Number: {}".format(b[1],b[2],b[3]))
        print("="*200)
    
    if choice==5:
        print("="*200)
        accno = int(input("Please Enter You Acconut Number : "))
        print("="*200)
        name = input("Enter the New Account Holder Name: ")
        balance = int(input("Enter the New Opening balance: "))
        mob = int(input("Enter the New Mobile Number: "))
        query = "UPDATE accounttable SET name = '{}', balance = {}, mob = '{}' WHERE accno = {}".format(name,balance,mob,accno)
        cur.execute(query)
        mydb.commit()
        query = "SELECT * FROM accounttable WHERE accno = {}".format(accno)
        cur.execute(query)
        b = list(cur.fetchone())
        print("="*200)
        print("New Account Holder Name = {}\nYour New Current Balance : {}\nNew Registered Mobile Number: {}".format(b[1],b[2],b[3]))
        print("="*200)


    if choice==6:
        break



