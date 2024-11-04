from database import db


class Wallet(db.Model):
    __tablename__ = 'wallets'

    id = db.Column(db.Integer, primary_key=True)
    current_balance = db.Column(db.Numeric(10, 2), nullable=False, default=0.00)

    def __repr__(self):
        return f"wallet balance: {self.current_balance}"

class Wallet_logs(db.Model):
    __tablename__ = 'wallet_logs'  # Optional: Define your table name explicitly

    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, nullable=False, default=db.func.now())  # Timestamp column
    action = db.Column(db.String(120))

    def __init__(self, action):
        self.action = action