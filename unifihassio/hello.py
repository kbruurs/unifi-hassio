from pyunifi.controller import Controller
from flask import Flask
from flask import jsonify
import json 
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
app = Flask(__name__)
app.secret_key = 'ewfsdfwefs4d56f4sa1bre5g4gw'

def connect_controller():
    with open("/data/options.json", "r") as read_file:
        data = json.load(read_file)

    return Controller(data["ControllerURL"], data["Login"]["Username"], data["Login"]["Password"],data["Port"],data["Version"],data["SiteID"],data["ValidSSL"])

@app.route('/')
def hello_world():
    c = connect_controller()
    vouchers =  c.list_vouchers()
    return render_template('tickets/index.html', vouchers=vouchers)

@app.route('/aps')
def aps():
    c = connect_controller()
    x ='Test'
    for ap in c.get_aps():
        x = x + 'AP named %s with MAC %s' % (ap.get('name'), ap['mac'])

    return x

@app.route('%%ingress_entry%%')
def keys():
    c = connect_controller()
    x ='Test'
    vouchers =  c.list_vouchers()
    for voucher in vouchers:
        x = x+json.dumps(voucher)+'</br>'+voucher.get("_id")+'</br>'
    return x

@app.route('/tickets')
def tickets():
    c = connect_controller()
    vouchers =  c.list_vouchers()
    return render_template('tickets/index.html', vouchers=vouchers)

@app.route('/create_tickets', methods=('GET', 'POST'))
def create_tickets():
    if request.method == 'POST':
            quantity = request.form['quantity']
            duration = request.form['duration']
            error= None

            if quantity is None:
                error = 'Incorrect quantity.'
            elif duration is None:
                error = 'Incorrect duration.'
            if error is None:
                c = connect_controller()
                c.create_voucher(int(quantity), 0, int(duration)*60*60*24)
                flash('Ticket(s) created')
                return redirect(url_for('tickets'))


            flash(error)

    return render_template('tickets/create.html')



