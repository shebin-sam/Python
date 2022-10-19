import mysql.connector as mycon
import datetime
con=mycon.connect(host='shebinsam.mysql.pythonanywhere-services.com',user='shebinsam',passwd='Qwertyuiop1234!',database='shebinsam$emmanuelwork')

cur=con.cursor()

def create_table():
    
    query1='create table if not exists workers(worker_id int primary key auto_increment,worker_name varchar(40),type char(1));'
    cur.execute(query1)
    query2='create table if not exists work(work_id int primary key auto_increment,worker_id int,dateofwork date,site_id int);'
    cur.execute(query2)
    query3='create table if not exists sites(site_id int primary key auto_increment,site_name varchar(20),place varchar(30));'
    cur.execute(query3)
    query4='create table if not exists wages(wage_id int primary key auto_increment,worker_id int,wage int);'
    cur.execute(query4)
    query5='create table if not exists advance(advance_id int primary key auto_increment ,worker_id int,amount int);'
    cur.execute(query5)
    con.commit()

create_table()




def add_sites():
    a=input('Enter site name :')
    b=input('Enter place:')
    query="insert into sites(site_name,place) values('{}','{}')"
    cur.execute(query.format(a,b))
    con.commit()

def search_worker():
    a=input('enter worker name :')
    query="select * from workers where worker_name ='{}'"
    cur.execute(query.format(a))
    a=cur.fetchone()
    return a[0]

def search_worker1(a):
    query="select * from workers where worker_name ='{}'"
    cur.execute(query.format(a))
    a=cur.fetchone()
    try:
        return a[0]
    except TypeError:
        return 'name does not exists'

def add_worker():
    a=input('Enter worker name :')
    if search_worker1(a) !="name does not exists":
        print('name already exists !!')
    else:
        b=input('Enter type(M/H):')
        query="insert into workers(worker_name,type) values('{}','{}')"
        cur.execute(query.format(a,b))
        con.commit()
def add_wage():
    a=search_worker()
    b=int(input('Enter wage :'))
    query="insert into wages(worker_id,wage) values({},{})"
    cur.execute(query.format(a,b))
    con.commit()

def site_search():
    a=input('enter site name :')
    query="select * from sites where site_name ='{}'"
    cur.execute(query.format(a))
    a=cur.fetchone()
    return a[0]


def add_work():
    ch='y'
    while ch=='y':
        a= search_worker()
        b=datetime.date.today()
        c=site_search()
        query="insert into work(worker_id,dateofwork,site_id) values({},'{}',{})"
        cur.execute(query.format(a,b,c))
        con.commit()
        ch=input('continue to add worker(y/n):')

def view_workchart():
    query='select worker_name,count(work_id) from workers w,work v where w.worker_id=v.worker_id group by worker_name'
    cur.execute(query)
    a=cur.fetchall()
    for i in a:
        print('=======================')
        print('Name :',i[0])
        print('work :',i[1])
        print('=======================')

def add_advance():
    ch='y'
    while ch=='y':
        query='insert into advance(worker_id,amount) values({},{})'
        a=search_worker()
        b=int(input("enter amount given:"))
        cur.execute(query.format(a,b))
        con.commit()
        ch=input('continue to add advance(y/n):')

def total_advance(c):
    a=search_worker1(c)
    query='select sum(amount) from advance where worker_id={}'
    cur.execute(query.format(a))
    b=cur.fetchone()
    return b[0]
def calculate():
    query1="select count(work_id) from workers w,work v where w.worker_id=v.worker_id and worker_name='{}'"
    a=input('Enter worker name :')
    cur.execute(query1.format(a))
    b=cur.fetchone()
    b=b[0]
    query2='select wage from wages where worker_id={}'
    c=search_worker1(a)
    cur.execute(query2.format(c))
    d=cur.fetchone()
    d=d[0]
    
    e=total_advance(a)
    if e!=None:
        total=(b*d)-e
        print('Amount Due :',total)
    else:
        total=b*d
        print('Amount Due :',total)

# mainmenu
print('=================================================================================================================')
ch='y'
while ch =='y':
    try:
        x=int(input('1.Add Worker \n2.Add Sites\n3.Add Wages\n4.Add Work\n5.Add Advance\n6.View Work Chart\n7.Calculate Amount Due\n=================================================================================================================\nChoose(1,2,3,4,5,6,7):'))
        print('=================================================================================================================')
        if x==1:
            add_worker()
        elif x==2:
            add_sites()
        elif x==3:
            add_wage()
        elif x==4:
            add_work()
        elif x==5:
            add_advance()
        elif x==6:
            view_workchart()
        elif x==7:
            calculate()
        else:
            print('Invalid Option!')

    except ValueError:
        print("Invalid Option !")
    print('=================================================================================================================')
    ch = input("continue(y/n):")
