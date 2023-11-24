import mysql.connector

#set your mysql password
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="passsymql@$12",
    database="art_gallery_2"
)

c = mydb.cursor()

def add_art_db(id, art_desc, art_price):
    c.execute('INSERT INTO gallery (`art_dsc`, `art_price`, `artist_id`) VALUES (%s, %s, %s);', (art_desc, art_price, id))
    mydb.commit()

def view_sold_art_db(id):
    c.execute('SELECT art_id, art_dsc, art_price, is_avail from gallery where artist_id=%s', (id,))
    data = c.fetchall()
    return data