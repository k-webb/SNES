from datetime import datetime
import requests, webbrowser, time

snes = 'http://www.gamestop.com/snes/consoles/super-nes-classic-edition/152771'
g = 'http://www.gamestop.com/nintendo-switch/consoles/nintendo-switch-console-with-gray-joy-con-mario-kart-bundle/152938'

class Monitor():
    def __init__(self):
        self.sleep = raw_input('Enter Sleep Time Seconds ')

    def get_site(self,site):
        print 'GETTING SITE %s\nTime %s'%(site,utctoest())
        r = requests.get(site)
        if r.status_code != 404:
            webbrowser.open(site)
        else:
            print 'Out of Stock\n'
            time.sleep(int(self.sleep))
            self.get_site(site)

def utctoest():
    current = datetime.now()
    return str(current) + " CST"

Monitor_instance = Monitor()

Monitor_instance.get_site(snes)
##TEST
#Monitor_instance.get_site(g)
