import requests
import pprint

from SECRET import GIT_TOKEN


session = requests.Session()
session.auth = ('DMBabich', GIT_TOKEN)

url = 'https://api.github.com/search/code?q=pickle+in:file+language:python+user:DMBabich'
pprint.pprint(requests.get(url).json())
