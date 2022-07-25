import requests
import json
from turtle import*
import turtle
   # login

def A():
    response = requests.post(url = 'http://176.9.164.222:2211/api/Login',data = {'username': input('please enter your username to login'), 'password':input('please enter your password')})
    if response == 200 or 201:
        tok=response.json()
        toke=tok['token']
        return toke
    else:
        print('error\ninput/s is/are wrong')
token=A()
    #Bank_Account_List_Create_post
def B():
    bank_account={'accountOwner':{'firstName':input('please enter your first name'),'lastName':input('please enter your last name'),'phoneNumber':input('please enter your phonNumber'),'nationalCode':input('please enter your nationalCode')}}
    bank_account=json.dumps(bank_account)
    bank__account = requests.post(url ='http://176.9.164.222:2211/api/accounts/BankAccountListCreate', data = bank_account,headers={'Authorization': 'JWT ' + token,'content-type':'application/json'})
    bank__account=json.loads(bank__account.text)
    return bank__account
    # Bank_Account_List_Create_get
def C():
    bank_account_list=requests.get(url='http://176.9.164.222:2211/api/accounts/BankAccountListCreate',headers={'Authorization': 'JWT ' + token})
    if 200 or 201==bank_account_list:
        bank_account_list=bank_account_list.json()
        return bank_account_list
    else:
        print('error\nurl or username or password is wrong')
    # Sign_Up
def D():
    perssonalInfo={'username': input('please enter password'),'password':input('please enter username')}
    perssonalInfo=json.dumps(perssonalInfo)
    signUp_response=requests.post(url='http://176.9.164.222:2211/api/accounts/User/SignUp',data=perssonalInfo,headers={'Authorization': 'JWT ' + token,'content-type':'application/json'})
    if 200 or 201==signUp_response:
        signUp_response=json.loads(signUp_response.text)
        return signUp_response
    else:
        print('error\ninput/s is/are wrong')
    # GetBankAccountLogs
def E():
    accountNumber=input('please enter your account Num')
    accountNumber=json.dumps({'accountNumber':accountNumber})
    bank_account_logs=requests.post(url='http://176.9.164.222:2211/api/accounts/GetBankAccountLogs',data=accountNumber,headers={'Authorization': 'JWT ' + token,'content-type':'application/json'})
    if 200 or 201==bank_account_logs:
        bank_account_logs=json.loads(bank_account_logs.text)
        return bank_account_logs
    else:
        print('error\ninput/s is/are wrong')
    # Add_Account_To_Account_Owner
def F():
    nationalCode={'nationalCode':input('please enter your nationalCode')}
    nationalCode=json.dumps(nationalCode)
    adding_account_to_account_owner=requests.post(url='http://176.9.164.222:2211/api/accounts/AddAccountToAccountOwner',data=nationalCode,headers={'Authorization': 'JWT ' + token,'content-type':'application/json'})
    if 200 or 201==bank_account_logs:
        adding_account_to_account_owner=json.loads(adding_account_to_account_owner.text)
        return adding_account_to_account_owner
    else:
        print('error\ninput/s is/are wrong')
    # close_block
def G():
    if input('do you want to close or block an account?')=='yes':
        account_num=input('please enter the account that you want to block or close')
        account_num={'accountNumber':account_num}
        if 200 or 201==account_num:
            account_num=json.dumps(account_num)
        else:
            print('error\ninput/s is/are wrong')
        if input('do you want to close this account')=='yes':
            CloseAccount=requests.post(url='http://176.9.164.222:2211/api/accounts/CloseAccount',data=account_num,headers={'Authorization': 'JWT ' + token,'content-type':'application/json'})
            if 200 or 201==CloseAccount:
                CloseAccount_respons=json.loads(CloseAccount.text)
                return CloseAccount_respons
            else:
                print('error you cant close this account')
        elif input('do you want to block this account')=='yes':
            BlockAccount=requests.post(url='http://176.9.164.222:2211/api/accounts/BlockAccount',data=account_num,headers={'Authorization': 'JWT ' + token,'content-type':'application/json'})
            if 200 or 201==BlockAccount:
                BlockAccount_respons=json.loads(BlockAccount.text)
                return BlockAccount_respons
            else:
                print('error you cant block this account')
    # BankAccountRetrieve
def H():
    accountNumber=input('please enter an account number')
    url=['http://176.9.164.222:2211/api/accounts/BankAccountRetrieve/']+[accountNumber]
    url="".join(url)
    bank_account_retrueve=requests.get(url,headers={'Authorization': 'JWT ' + token,'content-type':'application/json'})
    if 200 or 201==bank_account_retrueve:
        bank_account_retrueve=json.loads(bank_account_retrueve.text)
        return bank_account_retrueve
    else:
        print('error your username or password or url is wrong')
    # Bank_Account_Owner_Retrieve
def I():
    nationalNumber=input('please enter a national number')
    url='http://176.9.164.222:2211/api/accounts/BankAccountOwnerRetrieve/'+ nationalNumber
    bank_account_owner_retrieve_respons = requests.get(url,headers={'Authorization': 'JWT ' + token,'content-type':'application/json'})
    if bank_account_owner_retrieve_respons == 200 or 201:
        bank_account_owner_retrieve_respons = bank_account_owner_retrieve_respons.json()
    else :
        print('error : the account is not found')
    # Transaction_List_Create_post
def J():
    Transaction_List_Create_post={'fromAccount':input('please enter your account num'),'toAccount':input('please enter the account num which you want to send money'),'amount':int(input('please enter the amount of money')),'definition':'','cash':input('do you have money in cash?')}
    Transaction_List_Create_post=json.dumps(Transaction_List_Create_post)
    Transaction_List_Create_post_respons=requests.post(url='http://176.9.164.222:2211/api/transaction/TransactionListCreate',data=Transaction_List_Create_post,headers={'Authorization': 'JWT ' + token,'content-type':'application/json'})
    if Transaction_List_Create_post_respons:
        Transaction_List_Create_post_respons=json.loads(Transaction_List_Create_post_respons.text)
        return Transaction_List_Create_post_respons
    else:
        print('error\ninput/s is/are wrong')
    # Transaction_List_Create_get
def K():
    Transaction_List_Create_get_respons=requests.get(url='http://176.9.164.222:2211/api/transaction/TransactionListCreate',headers={'Authorization': 'JWT ' + token,'content-type':'application/json'})
    if Transaction_List_Create_get_respons==200 or 201:
        Transaction_List_Create_get_respons=json.loads(Transaction_List_Create_get_respons.text)
        return Transaction_List_Create_get_respons
    else:
        print('error your username or password or url is wrong')
def L():
    m=E()
    s=turtle.Screen()
    a=turtle.Turtle()
    a.color('red')
    a.speed(10)
    a.up()
    a.goto(-700,-100)
    turtle.ht()
    a.down()
    a.shape('classic')
    a.speed(10)
    b=turtle.Turtle()
    d=turtle.Turtle()
    b.speed(10)
    b.up()
    b.pensize(12)
    d.pensize(12)
    b.left(90)

    b.goto(-700,-100)
    b.down()
    b.color('blue')
    b.shape('arrow')
    d.speed(10)
    d.up()
    d.goto(-700,-100)
    d.down()
    d.color('blue')
    d.shape('arrow')
    d.forward(1000)
    s.bgcolor('black')
    b.goto(-700,450)
    c=0
    am=0
    z=turtle.Turtle()
    y=turtle.Turtle()
    v=900/(len(m['logs']))
    k=[]
    a.pensize(10)
    for j in range(len(m['logs'])):
        if m['logs'][j]['logType'] =='-':
            m['logs'][j]['amount']= -1 * m['logs'][j]['amount']
            k.append(m['logs'][j]['amount'])
    maxi=max(k)
    mini=min(k)
    maxi=maxi-mini
    ta=500//maxi
    z=turtle.Turtle()
    y=turtle.Turtle()
    z.pensize(9)
    y.pensize(9)
    z.color('green')
    y.color('green')
    az=turtle.Turtle()
    az.up()
    az.goto(-900,-300)
    az.down()
    az.color('white')
    for i in range(len(m['logs'])):
        c+=m['logs'][i]['amount']
        a.goto(-700+(v*(i+1)),((c*ta)-100))
        y.up()
        z.up()
        az.up()
        y.goto(-740,-100+(ta*c))
        z.goto(-700+(v*(i+1)),-140)
        az.goto(-900+1.5*(v*(i+1)),-300)
        z.down()
        y.down()
        az.down()
        am += m['logs'][i]['amount']
        y.write(str(am),font='bold')
        z.write(str(i+1),font='bold')
        y.ht()
        a.ht()
        z.ht()
        w=m['logs'][i]['date']   
        e=w[:3]+'/'+w[5:7]+'/'+w[9:10]+'\n'+w[12:19]
        az.write(str(i+1)+'='+e,font='bold')
        az.ht()
    az.up()
    az.goto(700,300)
    az.down()
    az.color('yellow')
    az.pensize(9)
    az.write('BANK DIAGRAM\n98 PRIJECT',font='bold')
    az.ht()
    
    az.up()
    az.goto(500,-100)
    az.down()
    az.color('orange')
    az.write('date',font='bold')
    az.ht()
    
    az.up()
    az.goto(-770,400)
    az.down()
    az.color('orange')
    az.write('money',font='bold')
    az.ht()
    turtle.done()
while True:
    if input('wanna login?(yse/no)')=='yes':
        answer=input('please choose a worde:\nB=Bank_Account_List_Create_post\nC=Bank_Account_List_Create_get\nD=Sign_Up\nE=GetBankAccountLogs\nF=Add_Account_To_Account_Owner\nG=close_block\nH=BankAccountRetrieve\nI=Bank_Account_Owner_Retrieve\nJ=Transaction_List_Create_post\n K=Transaction_List_Create_get\n L=bank diagram\nEXIT\n')
        if answer=='B':
            XX=B()
            print(XX)
        elif'C'==answer:
            XX=C()
            print(XX)
        elif'D'==answer:
            XX=D()
            print(XX)
        elif answer=='E':
            XX=E()
            print(XX)
        elif answer=='F':
            XX=F()
            print(XX)
        elif answer=='G':
            XX=G()
            print(XX)
        elif answer=='H':
            XX=H()
            print(XX)
        elif answer=='J':
            XX=J()
            print(XX)
        elif answer=='K':
            XX=K()
            print(XX)
        elif answer=='L':
            XX=L()
            print(XX)
        elif answer=='EXIT':
            break
    else:
        break
