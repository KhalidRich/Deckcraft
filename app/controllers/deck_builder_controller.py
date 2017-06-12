from flask import render_template, flash, redirect, session, url_for, request, g
from app import app, db
from app.forms import *
from app.models import User
from app.helpers import account_manager, DeckBuilderHelper

deck_builder_helper = DeckBuilderHelper()

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/deck-builder/select-game', methods=['GET', 'POST'])
def select_game():
    if request.method == 'GET':
        games = deck_builder_helper.get_all_games()
        games_simple = dict()
        game_select_form = GameSelectForm()
        for game in games:
            games_simple[game.name] = game.gid
        return render_template("select_game.html", form=game_select_form, games=games_simple)
    elif request.method == 'POST' and game_select_form.validate():
        uid, gid = form.user_id, form.game_id
        deck = deck_builder_helper.create_new_deck(uid, gid)
        if deck:
            redirect('/deck-builder/build/{}'.format(deck.deid), deck=deck, msg="Deck successfully created!")
        else:
            pass
    else:
        pass #404?
