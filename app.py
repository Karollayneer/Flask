from flask import Flask, request, render_template, json, jsonify
#from sqlite_creator import *
import sqlite3

app = Flask(__name__)


@app.route('/')
def home():
    #return("Hi, fela")
    return(render_template('index.html', title='home'))

def connection():
    global conn
    conn = None
    try:
        conn = sqlite3.connect('sqlite3db.db', check_same_thread=False)
    except sqlite3.error as err:
        print(err)
    return conn
connection()

@app.route('/showdata', methods=["GET"])
def showdata():
    if request.method == "GET":
        cursor = conn.execute("SELECT * FROM dados")
        data = cursor.fetchall()
        data_size = len(data)
        #print('data size : ', data_size)
        dt_full = data[0]
        dt_name = data[0][0]
        dt_age = data[0][1]
        dt_mount = {'Nome ': dt_name, 'age ': dt_age}
        #return(json.dumps(dt_mount))
        return(jsonify(data))

'{add data}'
# @app.route('/writedata', methods=["POST"])
# def writedata():
#     if request.method == "POST":
#         cursor = conn.execute("INSERT INTO dados VALUES (?, ?)", 'Carlos', 21)


if __name__ == '__main__':
    app.run(debug=True, port=9999, host="0.0.0.0")
