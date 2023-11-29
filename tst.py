import uuid, sqlite3
import os
import qrcode





conn=sqlite3.connect("SYSPI.db")
c = conn.cursor()


# img = qrcode.make('https://f08b-2a06-e040-6912-1313-fd4d-1-2a2f-ac4e.ngrok-free.app')
# img = qrcode.make(uuid.uuid4())

# img.save("qr.png", "PNG")






# c.execute("""CREATE TABLE esp (
#           uuid  text unique primary key,
#           soil  real,
#           temp  real,
#           hum   real,
#           light real
# )""")




# c.execute("""CREATE TABLE user  (
#           email  text unique primary key,
#           password text not null,
#           uuid0  text,
#           uuid1  text,
#           uuid2  text,
#           uuid3  text,
#           uuid4  text
# )""")
















# for i in range(1000):
#     id = str(uuid.uuid4())
#     # id = "".join(str(uuid.uuid4()).split("-"))
#     # id = "".join(uuid.uuid4().split("-"))
#     # print(id)
#     os.system(f"mkdir QR/qr_{i}")
#     os.system(f"echo {id} > QR/qr_{i}/id.txt")
#     img = qrcode.make(id)
#     img.save(f"QR/qr_{i}/qr_{i}.png", "PNG")
#     c.execute("""INSERT OR IGNORE INTO esp ("uuid", "soil", "temp", "hum", "light") VALUES (?, ?, ?, ?, ?)""",(id, 0.0, 0.0, 0.0, 0.0))
# os.system("display qr.png")

# print(uuid.uuid4())
# print(uuid.uuid4())

with conn:
    c.execute("""select * from esp where uuid = ?""",('d5251247-50bc-4881-90a3-2c737308be17',))
    print(c.fetchall())



conn.commit()
conn.close()






