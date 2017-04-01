from app import db

class Expansion(db.Model):
    eid = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey('game.gid'), nullable=False)
    name = db.Column(db.String(80), nullable=False)
    set_code = db.Column(db.String(11))

