#!/usr/bin/env python
import rumps
import os
import time
import urllib2, json

class lil_ip_toolbar(rumps.App):

    @rumps.timer(10)
    def showIP(self, _):
        external_ip = os.popen("curl -s http://whatismyip.akamai.com/").read()
        local_ip = os.popen("ifconfig | grep -Eo 'inet (addr:)?([0-9]*\.){3}[0-9]*' | grep -Eo '([0-9]*\.){3}[0-9]*' | grep -v '127.0.0.1'").read()
        local_ip = local_ip.split('\n')
        response = urllib2.urlopen("http://ip-api.com/json")
        data = json.loads(response.read())
        city = data['city']
        country = data['country']
        self.title =  external_ip + ", " + country + " * " + local_ip[0]

if __name__ == "__main__":
    lil_ip_toolbar("Awesome App").run()
