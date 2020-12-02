import requests
import json

api_key = '?api_key='

class league:
  def get_last_game(account_id):
    ag1 = 'https://na1.api.riotgames.com/lol/match/v4/matchlists/by-account/'
    gr = ag1 + account_id + '?endIndex=1&api_key=' + api_key
    with requests.Session() as s:
      api_rq = s.get(gr)
      game_data = api_rq.json()
      return game_data

  def sumid(sumid):
    url1 = 'https://na1.api.riotgames.com/lol/league/v4/entries/by-summoner/'
    mr_url = url1 + sumid + api_key
    with requests.Session() as s:
      api_rq = s.get(mr_url)
      game_data = api_rq.json()
      return game_data

  def get_user_id(username):
    u1 = 'https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/'
    username_req = u1 + username + api_key
    with requests.Session() as s:
      username_id = s.get(username_req)
      player_json = username_id.json()
      return player_json

  def get_active_game(user_id):
    ag1 = 'https://na1.api.riotgames.com/lol/spectator/v4/active-games/by-summoner/'
    gr = ag1 + user_id + api_key
    with requests.Session() as s:
      api_rq = s.get(gr)
      game_data = api_rq.json()
      return game_data

  def game_results(match_id):
    url1 = 'https://na1.api.riotgames.com/lol/match/v4/matches/'
    mr_url = url1 + match_id + api_key
    with requests.Session() as s:
      api_rq = s.get(mr_url)
      game_data = api_rq.json()
      return game_data


