from bank.teller import commands
from games.slotmachine import slot_machine
from games.images.gif_maker import img_ready
from games.league_of_legends import league
# from games.images.erickson import update_troll
import json
#----------------------------------------------------------------------------------------------------
def user_request(user_id, command_list):
	user_json = commands.userbal_read()
	user_wallet = user_json[user_id]
	try:

		if command_list[0] == 'add_stream':
			streamer_dic = commands.streamer_read()
			print(streamer_dic)
			streamer_dic[user_id] = command_list[1]
			commands.streamer_write(streamer_dic)
			return 'added ' + command_list[1]

		if command_list[0] == 'live':
			streamer_dic = commands.streamer_read()
			if bool(streamer_dic[str(user_id)]) is True:
				return streamer_dic[user_id]
			else:
				return 'please add link to stream with add_stream + url'

		if command_list[0] == 'troll':
		        troll_dic = commands.troll_farm_read()
		        troll_dic["Jordan"] = troll_dic["Jordan"] + 1
		        how_many = troll_dic["Jordan"]
		        commands.troll_farm_write(troll_dic)
		        return "Jordan bet against Tyson = " + str(how_many)

		if command_list[0] == 'league':
			league_dic = commands.league_read()
			league_data = league_dic['league_data']
			league_ud = league_data[user_id]
			# {'league_data': {'379360147002228737': {'accountid': 'XlK2FeBqUn-ib1kM14f9f3VwMnzYf-PSc0uZbhXGsf-AYQ', 'id': 'rcwefNoY2P5n1MnRsX-Rq4p9lGeQbkB3jpQZK3xCxxeadnM', 'username': 'capnbananas'}}}
			if user_bet_placed(user_id, int(command_list[2]), user_json) == 'not enough minerals':
				print('not enough minerals')
				return 'not enough minerals'
			else:
				active_bets = commands.active_bets_read()
				league_pool = active_bets["league of legends"]
				last_game = league.get_last_game(league_ud['accountid'])
				lg_gid = last_game['matches'][0]['gameId']
				league_pool[user_id].append({'wager': int(command_list[2]), 'win condition': command_list[1], 'last game': lg_gid,})
				commands.active_bets_write(active_bets)
				return 'Bet placed!'

		if command_list[0] == 'wallet':
			return 'user ' + user_wallet['name'] + " has a balance of $" + str(user_wallet['wallet'])

		if command_list[0] == 'slots':

			ammount = command_list[1]

			if (user_bet_placed(user_id, ammount, user_json)) == 'not enough minerals':
				return 'not enough minerals'

			else:
				payout = slot_machine(ammount)

				if payout == 'loser':
					return 'you suck try again'

				else:
					img_ready()
					user_wallet['wallet'] = sum(payout) + user_wallet['wallet']
					commands.userbal_write(user_json)
					return sum(payout)
	except:
		pass
#----------------------------------------------------------------------------------------------------
def user_bet_placed(user_id, ammount, user_json):
	user_wallet = user_json[user_id]
	balance = user_wallet['wallet']
	req_bet = balance - ammount
	if bool(req_bet < 0) is True:
		return 'not enough minerals'
	else:
		user_wallet['wallet'] = req_bet
		commands.userbal_write(user_json)
#----------------------------------------------------------------------------------------------------

# user_request('379360147002228737', ['slots', 1000])