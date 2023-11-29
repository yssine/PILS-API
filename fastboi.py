from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import sqlite3
from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from databases import Database

# conn = Database("sqlite:///SYSPI.db")
# conn.connect()


app=FastAPI()

# conn=sqlite3.connect("sqlite:///SYSPI.db")
# c = conn.cursor()


class Sensors(BaseModel):
    soil    : float
    temp    : float
    hum     : float
    light   : float




@app.post("/esp/{uuid}")
def post_values(uuid:str, sens:Sensors):
    # print("Harrow")
    # try:
        # print(conn)
    conn=sqlite3.connect("SYSPI.db")
        # c = conn.cursor()
        # with conn:
    conn.execute("""UPDATE esp SET soil = :soil,
                    temp = :temp,
                    hum = :hum,
                    light = :light WHERE uuid = :id""",
                    {'id' : uuid, 'soil': sens.soil, 'temp' : sens.temp, 'hum' : sens.hum, 'light' : sens.light})
    # finally: 
    #     pass
    conn.commit()
    # conn.disconnect()
    return sens



@app.get("/get-val/")
def get_values(uuid:str):
    # print("Harrow")
    # try:
        # print(conn)
    conn=sqlite3.connect("SYSPI.db")
        # c = conn.cursor()
        # with conn:
    # query = f"""SELECT * FROM  esp WHERE uuid = {uuid}"""
    # print(query)
    try:
        print("hola")
        res = conn.execute("""SELECT * FROM  esp WHERE uuid = :uuid""",{'uuid' : uuid}).fetchone()
        data = Sensors(soil=res[1],temp=res[2],hum=res[3],light=res[4])
        return data
    except:
        return {"message": "UUID does not exists"}, 404
    # res = conn.execute(query)
    # res = conn.fetch_all(query=query)
    # print(res)
    # data=Sensors()
    # conn.
    # finally: 
    #     pass
    # conn.commit()
    return {'message': "ok"}







# conn.commit()
# conn.close()
# conn.disconnect()
