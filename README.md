**Create a virtual environment**

python -m venv venv  

 **Activate the virtual environment (Linux/Mac)**
 
source venv/bin/activate 
 
**Activate the virtual environment (Windows)**

venv\Scripts\activate

**Install the required libraries**

pip install -r requirements.txt

**Database  sqlalchemy**

step 1. terminal run "python"

step 2. insert balance 

from app import app
from models import Wallet
from database import db

with app.app_context():
    db.session.add(Wallet(current_balance=100.00))
    db.session.commit()

step 3. show data 
with app.app_context():
    Wallet.query.all()

current data
**[id: 1 - wallet_balance : 100.00 ]**

**run python file**
app.py



**Api endpoints**


balance 

url: {local}/balance/<id>

cash in 

url: {local}/cash-in/<id>

payload (json-raw):
{
    "amount":100
}

debit

url: {local}/debit/<id>

payload (json-raw):
{
    "amount":100
}


