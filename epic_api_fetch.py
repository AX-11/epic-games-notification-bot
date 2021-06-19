from epicstore_api import EpicGamesStoreAPI, OfferData
import pandas as pd

API=EpicGamesStoreAPI()

def get_games():
	games=API.get_free_games()['data']['Catalog']['searchStore']['elements']#games is a python list of games, each item in that list is a dict
	nice_data=pd.DataFrame.from_dict(games)
	#nice_data.to_csv('out.csv')
	print(nice_data)
	for game in games:
		print(game)
		print('-'*50)
