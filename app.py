from flask import Flask
import psycopg2

app = Flask(__name__)

def conectar():
    return psycopg2.connect(
        host="postgres-db",
        dbname="bd_aplicacao",
        user="postgres",
        password="admin"
    )

@app.route("/")
def home():
    try:
        conn = conectar()
        cur = conn.cursor()
        cur.execute("SELECT * FROM usuarios;")
        usuarios = cur.fetchall()
        cur.close()
        conn.close()
        return {"usuarios": usuarios}
    except Exception as e:
        return {"erro": str(e)}, 500