from time import sleep
import requests
import re

def links_extractor(target_host):
    try:
        print("Requesting domain {}".format(target_host))
        sleep(0.5)
        response = requests.get(target_host)
        html_object = str(response.content)
        print("Domains extraction start...")
        sleep(0.5)
        data = re.findall(r'(http|ftp|https):\/\/([\w\-_]+(?:(?:\.[\w\-_]+)+))([\w\-\.,@?^=%&:/~\+#]*[\w\-\@?^=%&/~\+#])?', html_object)
        print(data)
    except Exception as e:
        print(e)



