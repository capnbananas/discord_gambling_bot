import json

class commands:

	def streamer_read():
		with open('bank/user_account/streamers.json', 'r') as openfile:
			json_data = json.load(openfile)
			openfile.close()
			return json_data

	def streamer_write(dic):
		with open('bank/user_account/streamers.json', 'w') as openfile:
			json.dump(dic, openfile)
			openfile.close()

	def troll_farm_read():
		with open('bank/user_account/troll.json', 'r') as openfile:
			json_data = json.load(openfile)
			openfile.close()
			return json_data

	def troll_farm_write(dic):
		with open('bank/user_account/troll.json', 'w') as openfile:
			json.dump(dic, openfile)
			openfile.close()

	def userbal_read():
		with open('bank/user_account/users.json', 'r') as openfile:
			json_data = json.load(openfile)
			openfile.close()
			return json_data

	def userbal_write(dic):
		with open('bank/user_account/users.json', 'w') as openfile:
			json.dump(dic, openfile)
			openfile.close()

	def league_read():
		with open('bank/user_account/league_users.json', 'r') as openfile:
			json_data = json.load(openfile)
			openfile.close()
			return json_data

	def league_write(dic):
		with open('bank/user_account/league_users.json', 'w') as openfile:
			json.dump(dic, openfile)
			openfile.close()


	def active_bets_read():
		with open('bank/wagers/activewagers.json', 'r') as openfile:
			json_data = json.load(openfile)
			openfile.close()
			return json_data

	def active_bets_write(dic):
		with open('bank/wagers/activewagers.json', 'w') as openfile:
			json.dump(dic, openfile)
			openfile.close()

'''

class league_payouts:

	def single_win_condition_met(win_condition, ammount):
		if win_condition == 'win':
			payout = ammount * 2
			return payout
		if win_condition == 'loss':
			print(win_condition)
		if win_condition == 'firstBloodKill':
			print(win_condition)

	def group_win_condition_met(win_condition):
		if win_condition == 'totalDamageDealt':
			print(win_condition)
		if win_condition == 'totalDamageDealtToChampions':
			print(win_condition)

'''
