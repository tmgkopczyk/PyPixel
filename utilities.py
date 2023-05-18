import json
import requests
from os import environ
from mojang import API

with open("reference.json") as file:
  reference_file = json.load(file)

base_url = reference_file['servers'][0]['url']
components = reference_file['components']
paths = reference_file['paths']
info = reference_file['info']

mojang_api = API()
hypixel_key = environ['Hypixel API Key']
headers = {
  "API-Key":hypixel_key
}

def get_player_uuid(username:str):
  uuid = mojang_api.get_uuid(username)
  return uuid

def get_key():
  response = requests.get(f"{base_url}/key",headers=headers).json()
  return response['record']

def get_player(username:str):
  uuid = get_player_uuid(username)
  params = {
    "uuid":uuid
  }
  response = requests.get(f"{base_url}/player",headers=headers,params=params).json()
  return response['player']

def get_recentgames(player:str):
  uuid = get_player_uuid(player)
  params = {
    "uuid":uuid
  }
  response = requests.get(f"{base_url}/recentgames",headers=headers,params=params).json()['player']
  return response['games']

def get_status(player:str):
  uuid = get_player_uuid(player)
  params = {
    "uuid":uuid
  }
  response = requests.get(f"{base_url}/status",headers=headers,params=params).json()
  return response['session']

def get_guild(**kwargs):
  if "player" in kwargs:
    uuid = get_player_uuid(kwargs['player'])
    params = {
      "player":uuid
    }
  elif "id" in kwargs:
    params = {
      "id":kwargs['id']
    }
  elif "name" in kwargs:
    params = {
      "name":kwargs['name']
    }
  response = requests.get(f"{base_url}/guild",headers=headers,params=params).json()
  return response['guild']

def get_resources_games():
  response = requests.get(f"{base_url}/resources/games",headers=headers).json()
  return response['games']

def get_resources_achievements():
  response = requests.get(f"{base_url}/resources/achievements",headers=headers).json()
  return response['achievements']

def get_resources_challenges():
  response = requests.get(f"{base_url}/resources/challenges",headers=headers).json()
  return response['challenges']

def get_resources_quests():
  response = requests.get(f"{base_url}/resources/quests",headers=headers).json()
  return response['quests']

def get_resources_guilds_achievments():
  response = requests.get(f"{base_url}/resources/guilds/achievements",headers=headers).json()
  return response

def get_resources_skyblock_collections():
  response = requests.get(f"{base_url}/resources/skyblock/collections",headers=headers).json()
  return response['collections']

def get_resources_skyblock_skills():
  response = requests.get(f"{base_url}/resources/skyblock/skills",headers=headers).json()
  return response['skills']

def get_resources_skyblock_items():
  response = requests.get(f"{base_url}/resources/skyblock/items",headers=headers).json()
  return response['items']

def get_resources_skyblock_election():
  response = requests.get(f"{base_url}/resources/skyblock/elections",headers=headers).json()
  return response

def get_resources_skyblock_bingo():
  response = requests.get(f"{base_url}/resources/skyblock/bingo",headers=headers).json()
  return response

def get_skyblock_news():
  response = requests.get(f"{base_url}/skyblock/news",headers=headers).json()
  return response['items']

def get_skyblock_auction(**kwargs):
  if "uuid" in kwargs:
    params = {
      'uuid':kwargs['uuid']
    }
  elif "player" in kwargs:
    player_uuid = get_player_uuid(kwargs['uuid'])
    params = {
      'player':player_uuid
    }
  elif "profile" in kwargs:
    params = {
      "profile":kwargs['profile']
    }
  response = requests.get(f"{base_url}/skyblock/auction",headers=headers,params=params).json()
  return response['auctions']

def get_skyblock_auctions(page_number=0):
  params = {
    "page":page_number
  }
  response = requests.get(f"{base_url}/skyblock/auctions",params=params,headers=headers).json()
  return response

def get_skyblock_auctions_ended():
  response = requests.get(f"{base_url}/skyblock/auctions_ended",headers=headers).json()
  return response['auctions']

def get_skyblock_bazaar():
  response = requests.get(f"{base_url}/skyblock/bazaar",headers=headers).json()
  return response['products']

def get_skyblock_profile(profile_id):
  params = {
    "profile":profile_id
  }
  response = requests.get(f"{base_url}/skyblock/profile",headers=headers,params=params).json()
  return response['profile']

def get_skyblock_profiles(username):
  uuid = get_player_uuid(username)
  params = {
    "uuid":uuid
  }
  response = requests.get(f"{base_url}/skyblock/profiles",headers=headers,params=params).json()
  return response['profiles']

def get_skyblock_bingo(username):
  uuid = get_player(username)
  params = {
    "uuid":uuid
  }
  response = requests.get(f"{base_url}/skyblock/bingo",headers=headers,params=params).json()
  return response['events']

def get_skyblock_firesales():
  response = requests.get(f"{base_url}/skyblock/firesales",headers=headers).json()
  return response['sales']
  