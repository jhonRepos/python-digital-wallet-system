**Create a virtual environment**

python -m venv venv  

 **Activate the virtual environment (Linux/Mac)**
 
source venv/bin/activate 
 
**Activate the virtual environment (Windows)**

venv\Scripts\activate

**Install the required libraries**

pip install -r requirements.txt

**Insert balance in sqlalchemy**

from app import app
from models import Wallet
from database import db

with app.app_context():
    db.session.add(Wallet(current_balance=100.00))
    db.session.commit()


**run python file**
app.py


