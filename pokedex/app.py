import os
import psycopg2
from decouple import config
from flask import Flask, render_template, jsonify, request, abort, redirect, url_for

app = Flask(__name__)

# CONNECT TO DATABASE
def get_db_connection():
    conn = psycopg2.connect(host=config('DB_HOST'),
                            user=config('DB_USERNAME'),
                            password=config('DB_PASSWORD'))
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/items/')
def items():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM items;')
    items = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('items.html', items=items)

@app.route('/items/add/', methods=["POST", "GET"])
def add_item():
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        cur.execute('INSERT INTO items (name,description,type,number) VALUES (%s,%s,%s,%s)', (request.json['name'], request.json['description'], request.json['type'], request.json['number']))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify(True)
    except:
        return jsonify(False)

@app.route('/pokedex/')
def pokedex():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM pokedex_mon ORDER BY dex_id;')
    pokemon = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('pokedex.html', pokemon=pokemon)

@app.route('/pokedex/<poke>/', methods=["GET"])
def get_pokemon(poke):
    conn = get_db_connection()
    cur = conn.cursor()
    q = "SELECT * FROM pokedex_mon WHERE name= '" + poke + "'"
    cur.execute(q)
    conn.commit()
    rowcount = cur.rowcount
    cur.close()
    conn.close()
    if rowcount > 0:
        return "True"
    else:
        return "False"
@app.route('/pokedex/add/', methods=["GET","POST", "PATCH"])
def add_pokemon():
    conn = get_db_connection()
    cur = conn.cursor()
    if request.method =='PATCH':
        try:
            q = "UPDATE pokedex_mon SET caught = 'True' WHERE name = '" + request.json['name'] +"'"
            cur.execute(q)
            conn.commit()
            cur.close()
            conn.close()
            return jsonify("patch worked")
        except:
            return jsonify("patch failed")
    else:
        if (request.json['caught'] == True):
            caught = True
        else:
            caught = False
        try:
            cur.execute('INSERT INTO pokedex_mon (name,description,image,seen,caught,dex_id) VALUES (%s,%s,%s,%s,%s,%s)', (request.json['name'], request.json['description'], request.json['image'], True, caught, request.json['dex_id']))
            conn.commit()
            cur.close()
            conn.close()
            return jsonify(True)
        except:
            return jsonify(False)