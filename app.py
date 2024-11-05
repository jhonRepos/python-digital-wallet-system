from flask import Flask, request, jsonify
from models import Wallet, Wallet_logs
from database import db, init_db
from decimal import Decimal, InvalidOperation

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///wallet.db'  
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


init_db(app)


def log_action(action):
    logs = Wallet_logs(action=action)
    db.session.add(logs)
    db.session.commit()

def update_balance(wallet, amount):
    wallet.current_balance += amount
    db.session.commit()

@app.route('/balance/<id>', methods=['GET'])
def get_balance(id):
    wallet = Wallet.query.get(id)
    
    if wallet is None:
        return jsonify({'message': 'Wallet not found'}), 404

    log_action(f'View balance of Id: {wallet.id}')
    return jsonify({'balance': float(wallet.current_balance)})

@app.route('/cash-in/<id>', methods=['POST'])
def cash_in(id):
    data = request.get_json()
    wallet = Wallet.query.get(id)
    if wallet is None:
        return jsonify({'message': 'Wallet not found'}), 404
    try:
        amount = Decimal(data['amount'])
        if amount < 0:
            message = "That's not a valid amount"
        else:
            if wallet:
                update_balance(wallet, amount)  # Use update_balance to increase the balance
                message = f"Success Cash-In Id: {id}"
            else:
                message = f"No wallet found with id: {id}"
    except (ValueError, InvalidOperation):
        message = "That's not a valid amount"

    log_action(f'Cashin Id: {id} - {message}')
    return jsonify({'message': message,'balance': float(wallet.current_balance)})

@app.route('/debit/<id>', methods=['POST'])
def debit(id):
    data = request.get_json()
    wallet = Wallet.query.get(id)
    if wallet is None:
        return jsonify({'message': 'Wallet not found'}), 404
    try:
        amount = Decimal(data['amount'])
        if amount < 0:
            message = "That's not a valid amount"
        else:
            if wallet:
                update_balance(wallet, -amount)  # Use update_balance to decrease the balance
                message = f"Success Debit Id: {id}"
            else:
                message = f"No wallet found with id: {id}"
    except (ValueError, InvalidOperation):
        message = "That's not a valid amount"

    log_action(f'Debit Id: {id} - {message}')
    return jsonify({'message': message,'balance': float(wallet.current_balance)})


if __name__ == '__main__':
    app.run(port=777, debug=True)