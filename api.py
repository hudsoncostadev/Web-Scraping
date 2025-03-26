from fastapi import FastAPI
import mysql.connector

app = FastAPI()

db = mysql.connector.connect(
    host="localhost",
    user="MySQL80",
    password="hudson3254",
    database="ans_database"
)

@app.get("/operadoras")
def get_operadoras():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM operadoras LIMIT 10;")
    operadoras = cursor.fetchall()
    return {"data": operadoras}