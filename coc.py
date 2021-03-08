#api endpoints
import requests as request
import json 

#per day info of a clan-war-league
class WarDay(): 
    def __init__(self,day,warTag,res): 
        self.day = day
        self.warTag = warTag
        self.responce = res
    

class ClanInfo:
    def __init__(self,clantag): 
        self.base = "https://api.clashofclans.com/v1/"
        self.token = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImM5MzRmMjllLTA0Y2UtNGQ2ZS1iZDM1LWVmZmNlNDI4MWEzYiIsImlhdCI6MTYxNDY4NjcxNywic3ViIjoiZGV2ZWxvcGVyLzhlOTIyMmY4LWNjZDUtN2MyZi1mMDE5LWRhNjI0MjlhMjdhNCIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjc3LjE2MS4xMjUuMTM1IiwiNS4xOTkuMTQ4LjIwMSJdLCJ0eXBlIjoiY2xpZW50In1dfQ.aU5Oe-l_Way2quK62V1f25FuVuo_efwUfdnQXmZbkV6o-Sf8Ph5mAdGNd6EJ3WizgBklDnRHx0p4JN_80Nqlug"
        self.headers = {'Content-Type': 'application/json', 'Authorization': self.token}
        self.ownClanWars = []
        self.clanTag = "%23"+clantag[1:]


    # get /clanwarleagues/wars/{warTag} 
    #https://api.clashofclans.com/v1/clanwarleagues/wars/%232RL9C2CUG
    def clanwarleagues_wars(self,warTags):
        urlSaveWarTag = "%23"+warTags[1:]
        endpoint = self.base + f"clanwarleagues/wars/{urlSaveWarTag}"
        res = request.get(endpoint,headers=self.headers)
        if res.status_code == 200: 
            return res.json()
        else: 
            return res.status_code

    #https://api.clashofclans.com/v1/clans/%2329G2CU2JY/currentwar/leaguegroup
    def currentwar_leaguegroup(self): 
        endpoint = self.base+"clans/"+self.clanTag+"/currentwar/leaguegroup"
        r = request.get(endpoint, headers = self.headers)
        if r.status_code == 200: 
            return r.json()

    #goes through currentwar_leaguegroup("war tag")
    def get_tags(self,day): 
        tags = []
        r = self.currentwar_leaguegroup()
        if r:   
            for warTag in r['rounds'][day]['warTags']: 
                tags.append(warTag)
        return tags

    def clan_war_league_event(self,days):
        
        tags = []
        for day in range(days):
            #print(day) 
            tags = self.get_tags(day)
            for warTag in tags: 
                res = self.clanwarleagues_wars(warTag)
                if res['clan']['tag'] == '#29G2CU2JY' or  res['opponent']['tag'] == '#29G2CU2JY':
                   # print( "own clan", res['clan']['tag'])
                    _war = WarDay(day,warTag,res)
                   # print(_war.warTag)
                    self.ownClanWars.append( _war ) 
  

 






claninfo = ClanInfo("#29G2CU2JY")
claninfo.clan_war_league_event(2)



class Fight(): 
    def __init__(self,tag):
        self.tag = tag 
        self.townhallLevel = None
        self.stars = None
        self.mapPosition = None
        self.opponentTag = None
        self.opponentMapPosition = None
        self.opponentTownhallLevel = None


def attack_results():
    fights = {}
    for fight in claninfo.ownClanWars: 
        for member in fight.responce["clan"]["members"]:
            if 'attacks' in member: 
                F = Fight(member['tag'])
                F.townhallLevel = member["townhallLevel"]
                F.mapPosition = member['mapPosition']
                F.opponentTag =  member['attacks'][0]['defenderTag']
                F.stars =   member['attacks'][0]['stars']

            for opponent in fight.responce['opponent']['members']: 
                if opponent['tag'] == F.opponentTag: 
                    F.opponentTownhallLevel = opponent['townhallLevel']
                    F.opponentMapPosition = opponent["mapPosition"]
            fights[ member['tag'] ]= F

    return fights
results = attack_results()

for key in results: 
    fight = results[key]
    print("stars: ", fight.stars)
    print("tags: ", fight.tag, fight.opponentTag)
    print("townhall levels:" , fight.townhallLevel, fight.opponentTownhallLevel)
    print("--------------------------------------------------------------------")



# print("number of clan war entries:", len(claninfo.ownClanWars))
# for war in claninfo.ownClanWars:
#     if war.responce["clan"]["tag"] == '#29G2CU2JY':
#         for member in war.responce["clan"]["members"]: 

#             # FOR DISPLAY PURPOSES
#             if len(member['name']) <= 6: #character limit that will place tab on right spot
#                 member['name'] += "\t" #if name would be too short, add a tab to the name 
#             # FOR DISPLAY PURPOSES

#             print(member['name'],"\t",member['townhallLevel'],"\t",member['mapPosition'])
#     print("\n")
    
#     if war.responce["opponent"]["tag"] == '#29G2CU2JY':
#         for member in war.responce["opponent"]["members"]: 
            
#             # FOR DISPLAY PURPOSES
#             if len(member['name']) <= 6: #character limit that will place tab on right spot
#                 member['name'] += "\t" #if name would be too short, add a tab to the name 
#             # FOR DISPLAY PURPOSES

#             print(member['name'],"\t",member['townhallLevel'],"\t",member['mapPosition'])
#     print("\n")


#clan tag = #29G2CU2JY
#war tag = #2RL9C2CUG
#https://api.clashofclans.com/v1/clans/clanwarleagues/wars/%232RLL9UYPG
#https://api.clashofclans.com/v1/clanwarleagues/wars/%232RL9C2CUG