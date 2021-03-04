#api endpoints
import requests as request
import json 


class WarDay(): 
    def __init__(self,day,warTag,res): 
        self.day = day
        self.warTag = warTag
        self.responce = res
    

class ClanInfo:
    def __init__(self): 
        self.base = "https://api.clashofclans.com/v1/"
        self.token = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImM5MzRmMjllLTA0Y2UtNGQ2ZS1iZDM1LWVmZmNlNDI4MWEzYiIsImlhdCI6MTYxNDY4NjcxNywic3ViIjoiZGV2ZWxvcGVyLzhlOTIyMmY4LWNjZDUtN2MyZi1mMDE5LWRhNjI0MjlhMjdhNCIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjc3LjE2MS4xMjUuMTM1IiwiNS4xOTkuMTQ4LjIwMSJdLCJ0eXBlIjoiY2xpZW50In1dfQ.aU5Oe-l_Way2quK62V1f25FuVuo_efwUfdnQXmZbkV6o-Sf8Ph5mAdGNd6EJ3WizgBklDnRHx0p4JN_80Nqlug"
        self.headers = {'Content-Type': 'application/json', 'Authorization': self.token}
        self.ownClanWars = []


    # get /clanwarleagues/wars/{warTag} 
    def clanwarleagues_wars(self,warTags):
        urlSaveWarTag = "%23"+warTags[1:]
        endpoint = self.base + f"clanwarleagues/wars/{urlSaveWarTag}"
        res = request.get(endpoint,headers=self.headers)
        if res.status_code == 200: 
            return res.json()
        else: 
            return res.status_code

    def currentwar_leaguegroup(self, clantag): 
        endpoint = self.base+"clans/"+clantag+"/currentwar/leaguegroup"

        r = request.get(endpoint, headers = self.headers)
        if r.status_code == 200: 
            return r.json()

    def get_tags(self,clantag,day): 
        tags = []
        r = self.currentwar_leaguegroup("%2329G2CU2JY")
        if r:   
            for warTag in r['rounds'][day]['warTags']: 
                tags.append(warTag)
        return tags

    def clan_war_league_event(self,clantag,days):
        tags = []
        for day in range(days):
            #print(day) 
            tags = self.get_tags(clantag,day)
            for warTag in tags: 
                res = self.clanwarleagues_wars(warTag)
                if res['clan']['tag'] == '#29G2CU2JY' or  res['opponent']['tag'] == '#29G2CU2JY':
                   # print( "own clan", res['clan']['tag'])
                    _war = WarDay(day,warTag,res)
                   # print(_war.warTag)
                    self.ownClanWars.append( _war ) 








claninfo = ClanInfo()
claninfo.clan_war_league_event("%2329G2CU2JY",2)

print(len(claninfo.ownClanWars))
for war in claninfo.ownClanWars: 
    for member in war.responce["clan"]["members"]: 
        print(member['name'])


#zin

#clan tag = #29G2CU2JY
#war tag = #2RL9C2CUG
#https://api.clashofclans.com/v1/clans/clanwarleagues/wars/%232RLL9UYPG
#https://api.clashofclans.com/v1/clanwarleagues/wars/%232RL9C2CUG