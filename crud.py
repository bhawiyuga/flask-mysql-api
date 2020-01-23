from flask import Flask, render_template, request
import pymysql.cursors
import json

app = Flask(__name__)

# Connect to the database
connection = pymysql.connect(host='127.0.0.1',
                             user='user',
                             password='123456',
                             db='sensordata',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

cur = connection.cursor()

@app.route('/', methods=['GET'])
def index():
    cur.execute("SELECT * from sensordata")
    result = cur.fetchall()
    return json.dumps(result)

if __name__ == '__main__':
    app.run()