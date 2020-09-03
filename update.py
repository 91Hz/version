import webbrowser
import requests
import win32api

__version__ = 1.4	


def check_updates():
	print("Checking for updates...")
	try:
		response = requests.get('https://raw.githubusercontent.com/91Hz/version/master/ver.txt')
		data = response.text
		
		if float(data) > float(__version__):
			print("Update is available! New version: "+ str(data))
		else:
			print("{}".format(__version__))
	except Exception as e:
		print("Blad")

check_updates()