from flask import Flask, jsonify, render_template, request
from web3 import Web3, HTTPProvider, IPCProvider, WebsocketProvider
import re



app = Flask(__name__)


@app.route("/")
def index():
    '''
    landing page 
    '''

    if request.method == 'POST':
        print ('test')
        if request.form['CreateBet'] == 'create_bet':
            return render_template("create_bet.html")
    else:
        return render_template('index.html', blockNR = '666', minerNR = '666')




@app.route('/create_bet.html', methods = ['Get', 'post'])
def create_bet():
    '''
        create a bet
    '''
    
    
    if request.method == 'POST': #if the user has posted account data@
        featureList = request.form.to_dict()
        print (featureList)
    
        return render_template('create_bet.html', betInfo = featureList)
    

    
    return render_template('create_bet.html')




if __name__ == "__main__":
    app.run()
