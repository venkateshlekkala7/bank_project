import mysql.connector

mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='123456',
    database='bankdb',
    auth_plugin='mysql_native_password'
)
mycursor=mydb.cursor()

display='''
** WELCOME TO INDIAN BANK **
1.CREATE BANK ACCOUNT
2.SHOW ACCOUNT DETAILS
3.DEPOSIT MONEY
4.WITHDRAW MONEY
5.CHECK BALANCE 
6.EXIT
**---------------------**
'''
print(display)


def create():
    firstname=input('ENTER FIRST NAME:')
    lastname=input('ENTER LAST NAME:')
    account_no=input('ENTER YOUR ACCOUNT NUMBER:')
    address=input('ENTER YOUR ADDRESS:')
    mobile_no=input('ENTER YOUR MOBILE NUMBER:')
    balance=input('ENTER OPENING ACCOUNT BALANCE:')
    #inserting values inside columnns 
    col='insert into user_details values (%s,%s,%s,%s,%s,%s)'
    val=(firstname,lastname,account_no,address,mobile_no,balance)
    mycursor.execute(col,val)
    mydb.commit()
    print(' WELCOME',firstname,lastname,'YOUR ACCOUNT CREATED SUCCESSFULLY ')
    print('YOUR FIRST NAME:',firstname)
    print('YOUR LAST NAME:',lastname)
    print('YOUR ACCOUNT NUMBER:',account_no)
    print('YOUR ADDRESS:',address)
    print('YOUR MOBILE NUMBER:',mobile_no)
    print('YOUR BALANCE:',balance)
# create()

def show():
    print('-----ENTER YOUR ACCOUNT NUMBER TO SHOW DETAILS------')
    account_no=input('ENTER ACCOUNT NUMBER:')
    print('first name,last name,account number,address,mobile no,balance')
    col='select * from user_details where account_number=%s'
    val=(account_no,)
    mycursor.execute(col,val)
    myresult=mycursor.fetchall()
    for i in myresult:
        print(i)
# show()



def deposit():
    print('----DEPOSIT YOUR MONEY-----')
    account_no=input('ENTER ACCCOUNT NUMBER:')
    amount=float(input('ENTER YOUR MONEY FOR DEPOSIT:'))
    a='select balance from user_details where account_number=%s'
    b=(account_no,)
    mycursor.execute(a,b)
    myresult=mycursor.fetchone()
    totalamount=myresult[0]+amount
    col=('update user_details set balance=%s where account_number=%s')
    val=(totalamount,account_no)
    mycursor.execute(col,val)
    mydb.commit()
    print('SUCCESSFULLY DEPOSITED YOUR MONEY')
# deposit()

def withdraw():
    print('---WITHDRAW YOUR MONEY HERE---')
    account_no=input('ENTER YOUR ACCOUNT NUMBER:')
    amount=float(input('ENTER MONEY TO WITHDRAW:'))
    a='select balance from user_details where account_number=%s'
    b=(account_no,)
    mycursor.execute(a,b)
    myresult=mycursor.fetchone()
    totalamount=myresult[0]-amount
    col='update user_details set balance=%s where account_number=%s'
    val=(totalamount,account_no)
    mycursor.execute(col,val)
    mydb.commit()
    print('---AMOUNT WITHDRAWED SUCCESSFYLLY---')
# withdraw()

def checkbalance():
    print('---CHECK YOUR BALANCE HERE---')
    account_no=input('ENTER YOUR ACCOUNT NUMBER:')
    a='select balance from  user_details where account_number=%s'
    b=(account_no,)
    mycursor.execute(a,b)
    myresult=mycursor.fetchone()
    print('YOUR BALANCE IS:',myresult)
# checkbalance()


while True:
    option=int(input('SELECT YOUR OPTION:'))
    if option==1:
        create()
        print('press 1 for main menu')
        print('press 2 for exit')
        option=int(input('enter option:'))
        if option==1:
            print(display)
        elif option==2:
            print('thanks for visiting indian bank')
            break
    elif option==2:
        show()
        print('press 1 for main menu')
        print('press 2 for exit')
        option=int(input('enter option:'))
        if option==1:
            print(display)
        elif option==2:
            print('thanks for visiting indian bank')
            break
    elif option==3:
        deposit()
        print('press 1 for main menu')
        print('press 2 for exit')
        option=int(input('enter option:'))
        if option==1:
            print(display)
        elif option==2:
            print('thanks for visiting indian bank')
            break
    elif option==4:
        withdraw()
        print('press 1 for main menu')
        print('press 2 for exit')
        option=int(input('enter option:'))
        if option==1:
            print(display)
        elif option==2:
            print('thanks for visiting indian bank')
            break
    elif option==5:
        checkbalance()
        print('press 1 for main menu')
        print('press 2 for exit')
        option=int(input('enter option:'))
        if option==1:
            print(display)
        elif option==2:
            print('thanks for visiting indian bank')
            break
    elif option==6:
        print('THANKS FOR VISITING INDIAN BANK')
    else:
        print('please choose above options')
