from app import db

class Card(db.Model):
    cid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    card_type = db.Column(db.String(11), nullable=False)
    card_info = db.Column(db.String(512), nullable=False)
