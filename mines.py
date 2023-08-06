# Network Layer Proxy Mines Game / Mine Creator
# Lubut Mines V.0.1
# Created: 2023.05.06
# Creator: LBT CRYPT
#############
import random
import json

class Request:
    def __init__(self, mine_count, bet):
        self.mine_count = mine_count
        self.bet = bet

def get_current_user_id():
    return netWork_get_auth_user('id')

request = Request(mine_count=request.query_params.get('mine_count'), bet=request.query_params.get('user_bet'))

boxES = list(range(1, 26)) 
random.shuffle(boxES)
mines = boxES[:request.mine_count]

class MinesGame:
    def __init__(self):
        self.user_id = None
        self.game_key = None
        self.hash_key = None
        self.mine_count = None
        self.bet = None
        self.mines = None

    def save(self):
        save_all_game_details() # Extra Layer For Backup

create = MinesGame()
create.user_id = get_current_user_id()
create.game_key = get_network_game_key()
create.hash_key = get_network_game_hash_key()
create.mine_count = request.mine_count
create.bet = request.bet
create.mines = json.dumps(mines)
create.save()

xMultplier = MinesGame.xCalc(request.mine_count, 1)  # Get Win Rater for Mines
