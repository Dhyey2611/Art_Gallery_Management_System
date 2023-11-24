import mysql.connector


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="passsymql@$12",
    database="art_gallery_2"
)

c = mydb.cursor()
#delete function
def resell_art(id, art_id):
    c.execute('DELETE from purchase WHERE customer_id=%s AND art_id=%s', (id, art_id))
    mydb.commit()
    c.execute('UPDATE gallery SET is_avail=1 WHERE art_id=%s', (id,))
    mydb.commit()
    return


def show_costliest():
    c.execute('SELECT g.art_id, g.art_dsc, g.art_price, a.artist_name from gallery as g, artist as a WHERE art_price=(SELECT MAX(art_price) from gallery) AND a.artist_id=g.artist_id AND is_avail=1;')
    data = c.fetchall()
    return data

def avail_art_ids():
    c.execute('SELECT art_id FROM gallery WHERE is_avail=1')
    data = c.fetchall()
    return data

def view_available_art_db():
    c.execute('SELECT g.art_id, g.art_dsc, g.art_price, a.artist_name FROM gallery as g, artist as a WHERE a.artist_id=g.artist_id AND is_avail=0x01')
    data = c.fetchall()
    return data

#nested query
def view_purchased_art_db(id):
    c.execute('SELECT g.art_id, g.art_dsc, g.art_price, a.artist_name FROM gallery as g, artist as a WHERE art_id IN (SELECT art_id FROM purchase where customer_id=%s) AND a.artist_id=g.artist_id;', (id,))
    data=c.fetchall()
    return data

def buy_art_db(id, art_id):
    c.execute('INSERT INTO purchase (customer_id, art_id) VALUES (%s, %s);', (id, art_id))
    mydb.commit()
    c.execute('UPDATE gallery SET is_avail=0 WHERE art_id = %s;', (art_id,))
    mydb.commit()