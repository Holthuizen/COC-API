#api endpoints
import requests as request
import json 

class ClanInfo:
    def __init__(self): 
        self.base = "https://api.clashofclans.com/v1/clans/"
        self.token = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImM5MzRmMjllLTA0Y2UtNGQ2ZS1iZDM1LWVmZmNlNDI4MWEzYiIsImlhdCI6MTYxNDY4NjcxNywic3ViIjoiZGV2ZWxvcGVyLzhlOTIyMmY4LWNjZDUtN2MyZi1mMDE5LWRhNjI0MjlhMjdhNCIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjc3LjE2MS4xMjUuMTM1IiwiNS4xOTkuMTQ4LjIwMSJdLCJ0eXBlIjoiY2xpZW50In1dfQ.aU5Oe-l_Way2quK62V1f25FuVuo_efwUfdnQXmZbkV6o-Sf8Ph5mAdGNd6EJ3WizgBklDnRHx0p4JN_80Nqlug"
        self.headers = {'Content-Type': 'application/json', 'Authorization': self.token}


    def currentwar_leaguegroup(self, clantag): 
        endpoint = self.base+clantag+"/currentwar/leaguegroup"
        print(endpoint)
        r = request.get(endpoint, headers = self.headers)
        if r.status_code == 200: 
            return r.json()
    def get_tags(self,clantag): 
        r = self.currentwar_leaguegroup("%2329G2CU2JY")
        if r:   
            for tag in r['rounds'][0]['warTags']: 
                print(tag)

claninfo = ClanInfo()
tags = claninfo.get_tags("%2329G2CU2JY")



