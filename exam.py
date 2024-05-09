# Doston Togayev
import threading
import time

# 1 masala

import psycopg2

db_product = psycopg2.connect(dbname="n35",
                      user="postgres",
                      password="102030",
                      host="localhost",
                      port="5432")
cur = db_product.cursor()


create_product = '''
            CREATE TABLE IF NOT EXISTS products (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            price INTEGER,
            color VARCHAR(255) NOT NULL,
            image VARCHAR(255) NOT NULL)'''

cur.execute(create_product)




#2 masala
def insert_product(name, price, color, image):
    insert_product = "INSERT INTO products (name, price, color, image) VALUES (%s, %s, %s, %s)"
    insertproduct_parms = (name, price, color, image)
    cur.execute(insert_product, insertproduct_parms)
    db_product.commit()

def select_product(id):
    select_product = "SELECT * FROM products WHERE id = %s"
    select_product_parms = (id,)
    cur.execute(select_product, select_product_parms)
    row = cur.fetchall()
    return row

def update_product(id, name, price, color, image):
    update_product = "UPDATE products SET name = %s, price = %s, color = %s, image = %s WHERE id = %s"
    update_product_parms = (name, price, color, image, id)
    cur.execute(update_product, update_product_parms)
    db_product.commit()

def delete_product(id):
    delete_product = "DELETE FROM products WHERE id = %s"
    delete_product_parms = (id,)
    cur.execute(delete_product, delete_product_parms)
    db_product.commit()



#3 masala
class Alphabet:
    list1 = ['A','B','C','D','E','F','G','H','J','K','I','L','M','N','O','R','P','S','T','U','V','W','X','Y','Z']
    def __init__(self, list1):
        self.list1 = list1
    alfabet = iter(list1)
    for i in alfabet:
        print(i)




#4 masala

def print_numbers():
    for i in range(1, 6):
        print(i)
        time.sleep(1)

def print_leters():
    for i in 'ABCDE':
        print(i)
        time.sleep(1)

t1=threading.Thread(target=print_numbers)
t2=threading.Thread(target=print_leters)
t1.start()
t2.start()
t1.join()
t2.join()

#5 masala
class product:
    def __init__(self, name, price, color, image):
        self.name = name
        self.price = price
        self.color = color
        self.image = image

    def save_products(self):
        insert_product(name=self.name, price=self.price, color=self.color, image=self.image)
        insert_product_params = (self.name, self.price, self.color, self.image)
        cur.execute(create_product)
        db_product.commit()

#6 masala
#contaxtmangers
class ContextManagers:
    def __init__(self, file, mode ='r'):
        self.file = file
        self.mode = mode

    def __enter__(self):
        self.file = open(self.file, self.mode)
        return self.file

    def __exit__(self, type, value, traceback):
        cur = db_product.cursor()
        db_product.commit()
        if self.file and not self.file.close():
            self.file.close


s = "asdfgh"
S = iter(s)
for i in S:
    print(i)