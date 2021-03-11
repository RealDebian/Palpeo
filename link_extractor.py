from utils.alerts import good, bad
from utils.headers import HEADERS
from time import sleep
import requests
import database
import re
import json
from bs4 import BeautifulSoup
import colorama

def run_enumeration(target_host):

    try:
        print(good, 'Requesting domain {}'.format(target_host))
        sleep(.5)

        requests_call = requests.get(target_host, headers=HEADERS)
        html_object = requests_call.content.__str__()

        print(good, 'Domains extraction start...')
        sleep(.5)
        data = re.findall(r'(http|ftp|https):\/\/([\w\-_]+(?:(?:\.[\w\-_]+)+))([\w\-\.,@?^=%&:/~\+#]*[\w\-\@?^=%&/~\+#])?', html_object)

        malicious_string = ['xxx', 'porn', 'sex', 'xnxx', 'xvideo', '.firebaseio.com']

        print(good, 'Domain filtering...')
        sleep(.5)

        positive_domains = []
        non_positive_domains = []

        for url_data in data:
            trigger = None
            protocol = url_data[0]
            domain = url_data[1]
            route = url_data[2]

            for string in malicious_string:
                if string in domain + route:
                    positive_domains.append(domain + route)
                    trigger = True
                    if domain[:4] == 'www.':
                        print(bad, domain[4:] + route)
                        sleep(.3)
                    else:
                        print(bad, domain + route)
                        sleep(.3)
                else:
                    pass
            if trigger == None:
                non_positive_domains.append(domain + route)
                if domain[:4] == 'www.':
                    print(good, domain[4:] + route)
                    sleep(.3)
                else:
                    print(good, domain + route)
                    sleep(.3)

        json_data = {
            target_host : {
                'positive_domains': positive_domains,
                'non_positive_domains': non_positive_domains
                }
            }

        #   Data Base Function
        database.write_database(json_data)
        print('Data Base saved!')

        sleep(1)
        if len(positive_domains) > 0:
            print("""
            Palpe0 found {} positive domains
            Palpe0 found {} non positive domains
            """.format(len(positive_domains), len(non_positive_domains)))
        else:
            print('All domains checked, {} domains non positive'.format(len(non_positive_domains)))

        print(good, 'done!')
    except (requests.exceptions.ConnectionError, requests.exceptions.MissingSchema) as err:
        e = err.__str__()
        if e[:18] == 'HTTPConnectionPool' or e[:19] == 'HTTPSConnectionPool':
            print(bad, 'Failed to establish a new connection, domain not available!')
        elif e[2:20] == 'Connection aborted':
            print(bad, 'An existing connection has been forced to break by the remote host')
        else:
            print(bad, e)
    except KeyboardInterrupt:
        print()
        print('Palpe0 Stopped...')
