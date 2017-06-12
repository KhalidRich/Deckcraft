from app import db
from app.models import User, Game
from app.helpers import database_manager

class DeckBuilderHelper():
    def __init__(self):
        self.deck_contents_table = 'deck_contents'
        pass

    def get_all_games(self):
        """ Returns an object with game names and information. """
        games = Game.query.all()
        return games

    def create_new_deck(self, uid, gid):
        deck = Deck(game_id=gid, user_id=uid)
        database_manager.create(deck) #TODO: Create database manager
        return deck

    def load_deck(self, deid):
        deck = Deck.query.filter_by(deid=deid).first()
        if deck:
            return deck
        else:
            return None #TODO: Figure out some better error handling

    def delete_deck(self, deid):
        res = database_manager.delete(deid)
        if res:
            return res
        else:
            pass #TODO: Figure out some better error handling.

    def add_card_to_deck(self, cid, deid, qty=1):
        res = database_manager.update(self.deck_contents_table, values=(deid, cid, qty))
        if res:
            return res
        else:
            pass #TODO: Figure out some better error handling.

    def revise_qty_of_card(self, cid, deid, qty):
        if qty >= 0:
            self.add_card_to_deck(cid, deid, qty)

    def delete_card_from_deck(self, cid, deid, qty=1):
        pass
