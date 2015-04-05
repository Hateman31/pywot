''' A library providing a python interface to Wargaming.net's World of Tanks API '''

import requests
import json

foo = lambda fields: ','.join(fields)
class API:
	BASE_URL = 'https://api.worldoftanks.ru/'	# no trailing slash
	_format_fields = foo
	def __init__(self, ID):
		self.app_id = ID
	def _api_call(self, endpoint, **kwargs):
		''' Initiates an API call '''
		kwargs['application_id'] = self.app_id
		r = requests.get(self.BASE_URL+endpoint, params=kwargs)
		return json.dumps(r.json(), sort_keys=True, indent=4)
				
