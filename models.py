from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import JSON

db = SQLAlchemy()

class Customer(db.Model):
    __tablename__ = 'customers'

    customer_id = db.Column(db.String, primary_key=True)
    customer_configuration = db.Column(JSON, nullable=False)
    customer_name = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'<Customer {self.customer_name}>'