from app import db

class Deck(db.Model):
    deid = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user._id'), nullable=False)

# Many-to-many relationship between deck and cards.
deck_contents = db.Table('deck_contents',
        db.Column('deck_id', db.Integer, db.ForeignKey('deck.deid'), primary_key=True),
        db.Column('card_id', db.integer, db.ForeignKey('card.cid'), primary_key=True)
)
