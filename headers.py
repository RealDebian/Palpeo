import random


class HEADERS():
	
	def header_selector(self):
		header = {
			"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
			"Accept-Encoding": "gzip, deflate, br",
			"Accept-Language": "en-US,en;q=0.9,es;q=0.8",
			"Sec-Ch-Ua": "\"Google Chrome\";v=\"107\", \"Chromium\";v=\"107\", \"Not=A?Brand\";v=\"24\"",
			"Sec-Ch-Ua-Platform": "\"Windows\"",
			"User-Agent": "{}",
			}
		
		user_agents = (
			{
				"Chrome": {
					"Chrome 74 on Windows 10": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
					"Chrome 72 on Windows 10": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
					"Chrome 44 on Linux": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
				},
				
				"Chromium": {
					"Chromium 74 on Linux": "Mozilla/5.0 (X11; Linux armv7l) AppleWebKit/537.36 (KHTML, like Gecko) Raspbian Chromium/74.0.3729.157 Chrome/74.0.3729.157 Safari/537.36"
				},
				
				"Firefox": {
					"Firefox 33 on Mac OS X (Yosemite)": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10; rv:33.0) Gecko/20100101 Firefox/33.0",
					"Firefox 24 on Ubuntu Linux": "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:24.0) Gecko/20100101 Firefox/24.0",
					"Firefox 54 on Windows 7": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",
					"Firefox 7 on Windows XP": "Mozilla/5.0 (Windows NT 5.1; rv:7.0.1) Gecko/20100101 Firefox/7.0.1"
				},
				
				"Opera": {
					"Opera 12 on Windows 7": "Opera/9.80 (Windows NT 6.1; WOW64) Presto/2.12.388 Version/12.18",
					"Opera 84 on Windows 10": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36 OPR/84.0.4316.14",
					"Opera 12 on Linux": "Opera/9.80 (Linux armv7l) Presto/2.12.407 Version/12.51 , D50u-D1-UHD/V1.5.16-UHD (Vizio, D50u-D1, Wireless)"
				},
				
				"Safari": {
					"Safari 11.1 on Mac OS X (El Capitan)": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1.2 Safari/605.1.15",
					"Safari 10.1 on Mac OS X (Yosemite)": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.1.2 Safari/603.3.8"
				},
				
				"Apple iPhone/iPad": {
					"Apple iPad iOS 12.2": "Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
					"Apple iPhone iOS 12.2": "Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148"
				},
				
				"Internet Explorer": {
					"Internet Explorer 6 on Windows XP SP2": "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)",
					"Internet Explorer 11 on Windows 7": "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko"
				},
				
				"Outlook 3": {
					"Outlook 3 on iOS Apple iPhone": "Outlook-iOS/709.2226530.prod.iphone (3.24.1)"
				},
				
				"Thunderbird": {
					"Thunderbird 45.8 on Linux": "Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Thunderbird/45.8.0"
				}
				}
			)
		
		user_agent_software = {
			"1": "Chrome",
			"2": "Chromium",
			"3": "Firefox",
			"4": "Opera",
			"5": "Safari",
			"6": "Apple iPhone/iPad",
			"7": "Internet Explorer",
			"8": "Outlook 3",
			"9": "Thunderbird"
			}


def show_user_agent_software():
	for software in user_agent_software:
		print(software, user_agent_software[software])

def user_agent_selector(software="Thunderbird", values=False):
	for user_agent in user_agents[software]:
		if values:
			print(user_agent, "--->", user_agents[software][user_agent])
		else:
			print(user_agent)

def random_user_agent():
	software = random.choice(list(user_agent_software.values()))
	user_agent = random.choice(list(user_agents[software].values()))
	print(user_agent)
