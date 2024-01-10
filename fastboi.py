from fastapi import FastAPI,Query
from typing import Optional
from pydantic import BaseModel
import sqlite3
from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from databases import Database
from pydantic import Json

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
                    {'id' : uuid, 'soil': round(sens.soil, 2), 'temp' : round(sens.temp, 2), 'hum' : round(sens.hum, 2), 'light' : round(sens.light, 2)})
    # finally: 
    #     pass
    conn.commit()
    # conn.disconnect()
    return sens



@app.get("/get-val/")
def get_values(uuid:str):
# def get_values(q: Json = Query()):
    # uuid = q['uuid']
    # print("Harrow")
    # try:
        # print(conn)
    conn=sqlite3.connect("SYSPI.db")
        # c = conn.cursor()
        # with conn:
    # query = f"""SELECT * FROM  esp WHERE uuid = {uuid}"""
    # print(query)
    try:
        # print("hola")
        res = conn.execute("""SELECT * FROM  esp WHERE uuid = :uuid""",{'uuid' : uuid}).fetchone()
        data = Sensors(soil=res[1],temp=res[2],hum=res[3],light=res[4])
        return data
    except:
        return {"message": "UUID does not exists"}, 404




@app.get("/")
def home():
    return {"Project's Name" : "PILS-SISPI"},200
    






# conn.commit()
# conn.close()
# conn.disconnect()
