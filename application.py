from flask import Flask, jsonify, render_template, request
from web3 import Web3, HTTPProvider, IPCProvider, WebsocketProvider
import re
import helper



app = Flask(__name__)


@app.route("/")
def index():
    '''
    landing page 
    '''
    block = web3.eth.getBlock('latest')

    if request.form['CreateBet'] == 'create_bet':
        render_template("create_bet.html")

    return render_template('index.html', blockNR = block['number'], minerNR = block['miner'])




@app.route('/create_key', methods = ['Get', 'post'])
def create_bet():
    '''
        create a bet
    '''
    
    if request.method == 'POST': #if the user has posted account data@
        featureList = request.form.getlist('checkbox')
        print (featureList)
    
        return render_template(created_bet)




if __name__ == "__main__":
    app.run(port = 8888, debug=True)
