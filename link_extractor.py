from utils.alerts import good, bad
from time import sleep
import requests
import database
import re
import json
from bs4 import BeautifulSoup
import colorama

SITE = "https://lacatedralmusical.com"




# def run_enumeration(target_host):
def links_extractor(target_host):
				try:
								print(good, 'Requesting domain {}'.format(target_host))
								sleep(.5)
								requests_call = requests.get(target_host, headers=HEADERS)
								html_object = requests_call.content.__str__()
								print(good, 'Domains extraction start...')
								sleep(.5)
								data = re.findall(r'(http|ftp|https):\/\/([\w\-_]+(?:(?:\.[\w\-_]+)+))([\w\-\.,@?^=%&:/~\+#]*[\w\-\@?^=%&/~\+#])?', html_object)
								print(data)

				except (requests.exceptions.ConnectionError, requests.exceptions.MissingSchema) as err:
								e = err.__str__()
								if e[:18] == 'HTTPConnectionPool' or e[:19] == 'HTTPSConnectionPool':
												print(bad, 'Failed to establish a new connection, domain not available!')
								elif e[2:20] == 'Connection aborted':
												print(bad, 'An existing connection has been forced to break by the remote host')
								else:
												print(bad, e)




