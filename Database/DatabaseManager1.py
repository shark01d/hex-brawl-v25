from Logic.Player import Players
import json
from os import read, remove
import string
import random
from typing import Dict
from Utils.Helpers import Helpers
from Files.CsvLogic.Characters import Characters

class DataBase:
    def loadAccount(self):
        with open('Database/Player/data.db', 'r') as read_data:
            for line in read_data.readlines():

                json_data = json.loads(line)
                dict = json.loads(json.dumps(json_data))  # loading and dumping json data from file
                
                if self.player.Token in dict:
                    self.TotalTrophies = 0
                    self.player.LowID = dict[str(self.player.Token)]["lowID"]
                    self.player.IsFacebookLinked = dict[str(self.player.Token)]["isFBLinked"]
                    self.player.FacebookID = dict[str(self.player.Token)]["facebookID"]
                    self.player.FacebookToken = dict[str(self.player.Token)]["facebookToken"]
                    self.player.ClubID = dict[str(self.player.Token)]["clubID"]
                    self.player.ClubRole = dict[str(self.player.Token)]["clubRole"]
                    self.player.name = dict[str(self.player.Token)]["name"]
                    self.player.gems = dict[str(self.player.Token)]["gems"]
                    self.player.gold = dict[str(self.player.Token)]["gold"]
                    self.player.starPoints = dict[str(self.player.Token)]["starpoints"]
                    self.player.tickets = dict[str(self.player.Token)]["tickets"]
                    self.player.brawlerID = dict[str(self.player.Token)]["brawlerID"]
                    self.player.skinID = dict[str(self.player.Token)]["skinID"]
                    self.player.BrawlersTrophies = dict[str(self.player.Token)]["brawlersTrophies"]
                    self.player.BrawlersTrophiesForRank = dict[str(self.player.Token)]["brawlersTrophiesForRank"]
                    self.player.BrawlersUpgradePoints = dict[str(self.player.Token)]["brawlersUpgradePoints"]
                    self.player.BrawlerPowerLevel = dict[str(self.player.Token)]["brawlerPowerLevel"]
                    
                    if self.player.UnlockType == "Off":
                        self.player.BrawlersUnlockedState = dict[str(self.player.Token)]["UnlockedBrawlers"]
                    
                    for BrawlerID in self.player.BrawlersTrophies.keys():
                        self.TotalTrophies += self.player.BrawlersTrophies[BrawlerID]

                    if self.TotalTrophies < dict[str(self.player.Token)]["highesttrophies"]:
                        self.player.maxTrophiesReached = dict[str(self.player.Token)]["highesttrophies"]
                    else:
                        self.player.maxTrophiesReached = self.TotalTrophies
                        self.player.trophies = self.TotalTrophies

                    self.player.profileIcon = dict[str(self.player.Token)]["profileIcon"]
                    self.player.namecolor = dict[str(self.player.Token)]["namecolor"]
                    self.player.brawlBoxes = dict[str(self.player.Token)]["brawlBoxes"]
                    self.player.bigBoxes = dict[str(self.player.Token)]["bigBoxes"]
                    # self.player.contentCreator = dict[str(self.player.Token)]["contentCreator"]
                    self.player.shellySkin = dict[str(self.player.Token)]["shellySkin"]
                    self.player.nitaSkin = dict[str(self.player.Token)]["nitaSkin"]
                    self.player.coltSkin = dict[str(self.player.Token)]["coltSkin"]
                    self.player.bullSkin = dict[str(self.player.Token)]["bullSkin"]
                    self.player.jessieSkin = dict[str(self.player.Token)]["jessieSkin"]
                    self.player.brockSkin = dict[str(self.player.Token)]["brockSkin"]
                    self.player.dynamikeSkin = dict[str(self.player.Token)]["dynamikeSkin"]
                    self.player.boSkin = dict[str(self.player.Token)]["boSkin"]
                    self.player.elprimoSkin = dict[str(self.player.Token)]["elprimoSkin"]
                    self.player.barleySkin = dict[str(self.player.Token)]["barleySkin"]
                    self.player.pocoSkin = dict[str(self.player.Token)]["pocoSkin"]
                    self.player.ricoSkin = dict[str(self.player.Token)]["ricoSkin"]
                    self.player.darrylSkin = dict[str(self.player.Token)]["darrylSkin"]
                    self.player.pennySkin = dict[str(self.player.Token)]["pennySkin"]
                    self.player.piperSkin = dict[str(self.player.Token)]["piperSkin"]
                    self.player.pamSkin = dict[str(self.player.Token)]["pamSkin"]
                    self.player.frankSkin = dict[str(self.player.Token)]["frankSkin"]
                    self.player.mortisSkin = dict[str(self.player.Token)]["mortisSkin"]
                    self.player.taraSkin = dict[str(self.player.Token)]["taraSkin"]
                    self.player.spikeSkin = dict[str(self.player.Token)]["spikeSkin"]
                    self.player.crowSkin = dict[str(self.player.Token)]["crowSkin"]
                    self.player.geneSkin = dict[str(self.player.Token)]["geneSkin"]
                    self.player.tickSkin = dict[str(self.player.Token)]["tickSkin"]
                    self.player.leonSkin = dict[str(self.player.Token)]["leonSkin"]
                    self.player.rosaSkin = dict[str(self.player.Token)]["rosaSkin"]
                    self.player.carlSkin = dict[str(self.player.Token)]["carlSkin"]
                    self.player.bibiSkin = dict[str(self.player.Token)]["bibiSkin"]
                    self.player.bitSkin = dict[str(self.player.Token)]["8bitSkin"]
                    self.player.sandySkin = dict[str(self.player.Token)]["sandySkin"]
                    self.player.beaSkin = dict[str(self.player.Token)]["beaSkin"]
                    self.player.emzSkin = dict[str(self.player.Token)]["emzSkin"]
                    self.player.mrpSkin = dict[str(self.player.Token)]["mrpSkin"]
                    self.player.maxSkin = dict[str(self.player.Token)]["maxSkin"]
                    self.player.jackySkin = dict[str(self.player.Token)]["jackySkin"]
                    self.player.galeSkin = dict[str(self.player.Token)]["galeSkin"]
                    self.player.naniSkin = dict[str(self.player.Token)]["naniSkin"]
                    self.player.sproutSkin = dict[str(self.player.Token)]["sproutSkin"]
                    self.player.gadget = dict[str(self.player.Token)]["gadget"]
                    self.player.starpower = dict[str(self.player.Token)]["starpower"]
                    self.player.DoNotDistrubMessage = dict[str(self.player.Token)]["DoNotDistrub"]
                    self.player.roomID = dict[str(self.player.Token)]["roomID"]
                read_data.close()

    def loadOtherAccount(self, plrLow_id):
        with open('Database/Player/data.db', 'r') as read_data:
            for line in read_data.readlines():

                json_data = json.loads(line)
                dict = json.loads(json.dumps(json_data))  # loading and dumping json data from file

                for playertoken, info in dict.items():
                    if plrLow_id == info["lowID"]:
                        self.TotalTrophies = 0
                        self.IsFacebookLinked = info["isFBLinked"]
                        self.FacebookID = info["facebookID"]
                        self.FacebookToken = info["facebookToken"]
                        self.ClubID = info["clubID"]
                        self.ClubRole = info["clubRole"]
                        self.name = info["name"]
                        self.gems = info["gems"]
                        self.gold = info["gold"]
                        self.starPoints = info["starpoints"]
                        self.tickets = info["tickets"]
                        self.BrawlersCount = info["UnlockedBrawlers"]

                        self.UnlockedBrawlersList = []
                        for brawler_id in self.BrawlersCount:
                            if self.BrawlersCount[brawler_id] == 1:
                                self.UnlockedBrawlersList.append(brawler_id)
                                
                        self.brawlerID = info["brawlerID"]
                        self.skinID = info["skinID"]
                        self.BrawlersTrophies = info["brawlersTrophies"]
                        self.BrawlersTrophiesForRank = info["brawlersTrophiesForRank"]
                        self.BrawlersUpgradePoints = info["brawlersUpgradePoints"]
                        self.BrawlerPowerLevel = info["brawlerPowerLevel"]

                        for BrawlerID in self.BrawlersTrophies.keys():
                            self.TotalTrophies += self.BrawlersTrophies[BrawlerID]

                        if self.TotalTrophies < info["highesttrophies"]:
                            self.maxTrophiesReached = info["highesttrophies"]
                        else:
                            self.maxTrophiesReached = self.TotalTrophies
                            self.trophies = self.TotalTrophies

                        self.trophies = info["trophies"]
                        self.profileIcon = info["profileIcon"]
                        self.brawlBoxes = info["brawlBoxes"]
                        self.bigBoxes = info["bigBoxes"]
                        # self.contentCreator = info["contentCreator"]
                        self.shellySkin = info["shellySkin"]
                        self.nitaSkin = info["nitaSkin"]
                        self.coltSkin = info["coltSkin"]
                        self.bullSkin = info["bullSkin"]
                        self.jessieSkin = info["jessieSkin"]
                        self.brockSkin = info["brockSkin"]
                        self.dynamikeSkin = info["dynamikeSkin"]
                        self.boSkin = info["boSkin"]
                        self.elprimoSkin = info["elprimoSkin"]
                        self.barleySkin = info["barleySkin"]
                        self.pocoSkin = info["pocoSkin"]
                        self.ricoSkin = info["ricoSkin"]
                        self.darrylSkin = info["darrylSkin"]
                        self.pennySkin = info["pennySkin"]
                        self.piperSkin = info["piperSkin"]
                        self.pamSkin = info["pamSkin"]
                        self.frankSkin = info["frankSkin"]
                        self.mortisSkin = info["mortisSkin"]
                        self.taraSkin = info["taraSkin"]
                        self.spikeSkin = info["spikeSkin"]
                        self.crowSkin = info["crowSkin"]
                        self.geneSkin = info["geneSkin"]
                        self.tickSkin = info["tickSkin"]
                        self.leonSkin = info["leonSkin"]
                        self.rosaSkin = info["rosaSkin"]
                        self.carlSkin = info["carlSkin"]
                        self.bibiSkin = info["bibiSkin"]
                        self.bitSkin = info["8bitSkin"]
                        self.sandySkin = info["sandySkin"]
                        self.beaSkin = info["beaSkin"]
                        self.emzSkin = info["emzSkin"]
                        self.mrpSkin = info["mrpSkin"]
                        self.maxSkin = info["maxSkin"]
                        self.jackySkin = info["jackySkin"]
                        self.galeSkin = info["galeSkin"]
                        self.naniSkin = info["naniSkin"]
                        self.sproutSkin = info["sproutSkin"]
                        self.namecolor = info["namecolor"]
                        self.gadget = info["gadget"]
                        self.starpower = info["starpower"]
                        self.DoNotDistrubMessage = info["DoNotDistrub"]
                        self.roomID = info["roomID"]
                        break
                read_data.close()

    def createAccount(self):
        self.player.BrawlersUnlockedState = Players.CreateNewBrawlersList()
        data = {
            self.player.token: {
                "lowID": self.player.low_id,
                "isFBLinked": 0,
                "facebookID": self.player.FacebookID,
                "facebookToken": self.player.FacebookToken,
                "clubID": 0,
                "clubRole": 0,
                "name": self.player.name,
                "gems": self.player.gems,
                "gold": self.player.gold,
                "starpoints": self.player.star_points,
                "tickets": self.player.tickets,
                "brawlerID": 0,
                "skinID": 0,
                "highesttrophies": self.player.trophies,
                "trophies": self.player.trophies,
                "profileIcon": 0,
                "namecolor": 0,
                "brawlBoxes": self.player.brawl_boxes,
                "bigBoxes": self.player.big_boxes,
                # "contentCreator": "",
                "shellySkin": 0,
                "nitaSkin": 0,
                "coltSkin": 0,
                "bullSkin": 0,
                "jessieSkin": 0,
                "brockSkin": 0,
                "dynamikeSkin": 0,
                "boSkin": 0,
                "elprimoSkin": 0,
                "barleySkin": 0,
                "pocoSkin": 0,
                "ricoSkin": 0,
                "darrylSkin": 0,
                "pennySkin": 0,
                "piperSkin": 0,
                "pamSkin": 0,
                "frankSkin": 0,
                "mortisSkin": 0,
                "taraSkin": 0,
                "spikeSkin": 0,
                "crowSkin": 0,
                "geneSkin":0,
                "tickSkin":0,
                "leonSkin":0,
                "rosaSkin":0,
                "carlSkin":0,
                "bibiSkin":0,
                "8bitSkin":0,
                "sandySkin":0,
                "beaSkin":0,
                "emzSkin":0,
                "mrpSkin":0,
                "maxSkin":0,
                "jackySkin":0,
                "galeSkin":0,
                "naniSkin":0,
                "sproutSkin":0,
                "gadget":255,
                "starpower":76,
                "DoNotDistrub":0,
                "roomID": 0,
                "brawlersTrophies": self.player.BrawlersTrophies,
                "brawlersTrophiesForRank": self.player.BrawlersTrophiesForRank,
                "brawlersUpgradePoints": self.player.BrawlersUpgradePoints,
                "brawlerPowerLevel": self.player.BrawlerPowerLevel,
                "UnlockedBrawlers": self.player.BrawlersUnlockedState
            }
        }
        
        with open('Database/Player/data.db', 'a+') as data_file:
            json.dump(data, data_file)  # writing data for new account
            data_file.write('\n')  # writing a new line

    def createGameroomDB(self):
        data = { 
            self.player.roomID: {
                "mapID": self.player.mapID,
                "useGadget": 1,
                "Player count": 1,
                self.player.LowID: {
                    "host": 1,
                    "name": self.player.name,
                    "Team": self.player.GameRoomTeam,
                    "Ready": self.player.Ready,
                    "brawlerID": self.player.brawlerID,
                    "starpower": self.player.starpower,
                    "gadget": self.player.gadget,
                    "profileIcon": self.player.profileIcon,
                    "namecolor": self.player.namecolor
                }
            }
        }
        
        with open('Database/Gameroom/gameroom.db', 'a+') as data_file:
            json.dump(data, data_file)  # writing data for new account
            data_file.write('\n')  # writing a new line

    def loadGameroom(self):
        self.playerdata = {}
        with open('Database/Gameroom/gameroom.db', 'r') as read_data:
            for line in read_data.readlines():
                json_data = json.loads(line)
                dict = json.loads(json.dumps(json_data))  # loading and dumping json data from file
                if str(self.player.roomID) in dict:
                    self.mapID = dict[str(self.player.roomID)]["mapID"]
                    self.useGadget = dict[str(self.player.roomID)]["useGadget"]
                    self.playerCount = dict[str(self.player.roomID)]["Player count"]
                    for Players,data in dict[str(self.player.roomID)].items():
                        if Players != "Player count" and Players != "mapID" and Players != "useGadget":
                            self.playerdata[Players] = {}
                            self.playerdata[Players]["IsHost"] = data["host"]
                            self.playerdata[Players]["name"] = data["name"]
                            self.playerdata[Players]["Team"] = data["Team"]
                            self.playerdata[Players]["Ready"] = data["Ready"]
                            self.playerdata[Players]["LowID"] = Players
                            self.playerdata[Players]["brawlerID"] = data["brawlerID"]
                            self.playerdata[Players]["starpower"] = data["starpower"]
                            if self.useGadget != 0:
                                self.playerdata[Players]["gadget"] = data["gadget"]
                            else:
                                self.playerdata[Players]["gadget"] = 0
                            self.playerdata[Players]["profileIcon"] = data["profileIcon"]
                            self.playerdata[Players]["namecolor"] = data["namecolor"]
                read_data.close()

    def replaceGameroomValue(self, roomID, LowId, value_name, new_value, type):
        list = []
        if type != "removePlayer" and type != "deleteGameroom":
            with open('gameroom.db', 'r+') as file:
                for line in file.readlines():
                    json_data = json.loads(line)
                    dict = json.loads(json.dumps(json_data))  # loading and dumping json data from file
                    for keys,values in dict.items():
                        if keys != str(roomID):
                            if type == "room":
                                if roomID == self.player.roomID:
                                    dict[str(self.player.roomID)][str(value_name)] = new_value
                                    list.append(line)
                            elif type == "player":
                                dict[str(self.player.roomID)][str(LowId)][str(value_name)] = new_value
                                list.append(dict)
                    file.close()
                    break

        else:
            with open('gameroom.db', 'r+') as file:
                for line in file.readlines():
                    json_data = json.loads(line)
                    dict = json.loads(json.dumps(json_data))  # loading and dumping json data from file
                    for keys,values in dict.items():
                        if type == "removePlayer" and keys == value_name:
                            values["Player count"] -= 1
                            if dict[value_name][str(new_value)]["host"] == 1:
                                dict.pop(value_name)
                                list.append(dict)
                            else:
                                dict[value_name].pop(str(new_value))
                                list.append(dict)
                        file.close()
                        break

        with open('Database/Gameroom/gameroom.db', 'w') as o:
            o.writelines('\n'.join(list))
            o.close()    


    def replaceValue(self, value_name, new_value):
        with open('Database/Player/data.db', 'r+') as file:
            list = []
            for line in file.readlines():
                json_data = json.loads(line)
                dict = json.loads(json.dumps(json_data))  # loading and dumping json data from file
                if self.player.Token in dict:
                    dict[str(self.player.Token)][str(value_name)] = new_value
                list.append(dict)
                file.close()

        with open('Database/Player/data.db', 'w') as o:
            for i in list:
                o.write(str(i).replace("'", '"') + '\n')
            o.close()

    
    def replaceOtherValue(self, LowID, value_name, new_value):
        with open('Database/Player/data.db', 'r+') as file:
            list = []
            for line in file.readlines():
                json_data = json.loads(line)
                dict = json.loads(json.dumps(json_data))  # loading and dumping json data from file
                for playertoken, info in dict.items():
                    if LowID == info["lowID"]:
                        dict[playertoken][str(value_name)] = new_value
                        break
                list.append(dict)
                file.close()

        with open('Database/Player/data.db', 'w') as o:
            for i in list:
                o.write(str(i).replace("'", '"') + '\n')
            o.close()

        # example usage: replaceValue(self, 'gems', 7777)

        # Alliance function
    
    def createClub(self, clubid):
        data = {
            clubid: {
                "name": self.clubName,                          
                "description": self.clubdescription,
                "region": "RO",
                "badgeID": self.clubbadgeID,
                "type": self.clubtype,
                "trophiesneeded": self.clubtrophiesneeded,
                "friendlyfamily": self.clubfriendlyfamily,
                "trophies": self.player.trophies,
                "members": {
                    "totalmembers": 1,
                    str(self.player.LowID): self.player.name
                }
            }
        }

        msgData = {
            clubid: {
                "Total": 1,
                "1": {
                    "Event": 2,
                    "Tick": 1,
                    "PlayerID": self.player.LowID,
                    "PlayerName": self.player.name,
                    "PlayerRole": 2,
                    "Message": "Welcome to you're new club!"
                }
            }
        }

        with open('Database/Club/club.db', 'a+') as data_file:
            json.dump(data, data_file)  # writing data for new club
            data_file.write('\n')  # writing a new line

        with open('Database/Club/chat.db', 'a+') as data_file:
            json.dump(msgData, data_file)  # writing data for new club
            data_file.write('\n')  # writing a new line

    def loadClub(self, clubid):
        self.plrids = []
        self.clubidstr = str(clubid)
        with open('Database/Club/club.db', 'r') as read_data:
            for line in read_data.readlines():
                json_data = json.loads(line)
                dict = json.loads(json.dumps(json_data))
                if self.clubidstr in dict:
                    self.clubName = dict[str(self.clubidstr)]["name"]
                    self.clubdescription = dict[str(self.clubidstr)]["description"]
                    self.clubregion = dict[str(self.clubidstr)]["region"]
                    self.clubbadgeID = dict[str(self.clubidstr)]["badgeID"]
                    self.clubtype = dict[str(self.clubidstr)]["type"]
                    self.clubtrophiesneeded = dict[str(self.clubidstr)]["trophiesneeded"]
                    self.clubfriendlyfamily = dict[str(self.clubidstr)]["friendlyfamily"]
                    self.clubtrophies = dict[str(self.clubidstr)]["trophies"]
                    self.clubmembercount = dict[str(self.clubidstr)]["members"]["totalmembers"]
                    for plridentifier, data in dict[str(self.clubidstr)]["members"].items():
                        if plridentifier != "totalmembers":
                            self.plrids.append(int(plridentifier))

                read_data.close()
    

    def replaceClubValue(self, target, inf1, inf2, inf3, inf4, inf5):
        with open('Database/Club/club.db', 'r+') as file:
            list = []
            for line in file.readlines():
                json_data = json.loads(line)
                dict = json.loads(json.dumps(json_data))  # loading and dumping json data from file
                if str(target) in dict:
                    dict[str(target)]['description'] = inf1
                    dict[str(target)]['badgeID'] = inf2
                    dict[str(target)]['type'] = inf3
                    dict[str(target)]['trophiesneeded'] = inf4
                    dict[str(target)]['friendlyfamily'] = inf5
                list.append(dict)
                file.close()

        with open('Database/Club/club.db', 'w') as o:
            for i in list:
                o.write(str(i).replace("'", '"') + '\n')
            o.close()

    def CountClub(self, minMembers, maxMembers, clubType, maxListLength):
        self.AllianceCount = 0
        with open('Database/Club/club.db', 'r') as read_data:
            for club in read_data.readlines():
                clubData = json.loads(club)
                dict = json.loads(json.dumps(clubData))
                for name, info in dict.items():
                    if info["members"]["totalmembers"] >= minMembers and info["members"]["totalmembers"] < maxMembers and info["type"] <= clubType and self.AllianceCount <= maxListLength:
                        self.AllianceCount += 1
                read_data.close()

    def AddMember(self, AllianceID, PlayerID, PlayerName, Action):
        newData = []
        if Action == 0:
            with open('Database/Club/club.db', 'r') as file:
                for club in file.readlines():
                    plrData = json.loads(club)
                    dict = json.loads(json.dumps(plrData)) # loading and dumping json data from file
                    for Identifier, data in dict.items():
                        if int(Identifier) != AllianceID:
                            newData.append(club)
                    file.close()

            with open('Database/Club/chat.db', 'r') as file:
                for messages in file.readlines():
                    plrData = json.loads(messages)
                    dict = json.loads(json.dumps(plrData)) # loading and dumping json data from file
                    for Identifier, data in dict.items():
                        if int(Identifier) != AllianceID:
                            newData.append(messages)
                    file.close()
                                                                                                    
        elif Action == 1:
            with open('Database/Club/club.db', 'r+') as file:
                for line in file.readlines():
                    json_data = json.loads(line)
                    dict = json.loads(json.dumps(json_data))
                    for Identifier, data in dict.items():
                        if int(Identifier) == AllianceID:
                            dict[Identifier]['members']['totalmembers'] += 1    
                            dict[Identifier]['members'][str(PlayerID)] = PlayerName
                            break
                    newData.append(json.dumps(dict))
                    file.close()  
            
        elif Action == 2:
            with open('Database/Club/club.db', 'r+') as file:
                for line in file.readlines():
                    json_data = json.loads(line)
                    dict = json.loads(json.dumps(json_data))
                    for Identifier, data in dict.items():
                        if int(Identifier) == AllianceID:
                            dict[Identifier]['members']['totalmembers'] -= 1
                            dict[Identifier]['members'].pop(str(PlayerID))
                            break
                    newData.append(json.dumps(dict)) 
                    file.close()        

        with open('Database/Club/club.db', 'w') as o:
            o.writelines('\n'.join(newData))
            o.close()       
            
    def GetMemberData(self, Low_id):
        with open('Database/Player/data.db', 'r') as read_data:
            for plrtoken in read_data.readlines():
                plrData = json.loads(plrtoken)
                dict = json.loads(json.dumps(plrData))
                for playertoken, data in dict.items():
                    if Low_id == data["lowID"]:
                        self.lowplrid = data["lowID"]
                        self.plrrole = data["clubRole"]
                        self.plrtrophies = data["trophies"]
                        self.plrname = data["name"]
                        self.plricon = data["profileIcon"]
                        self.plrnamecolor = data["namecolor"]
                read_data.close()
    
    def GetmsgCount(self, clubID):
        with open('Database/Club/chat.db', 'r') as read_data:
            for line in read_data.readlines():
                json_data = json.loads(line)
                dict = json.loads(json.dumps(json_data))
                if str(clubID) in dict:
                    self.MessageCount = dict[str(clubID)]['Total']
            read_data.close()

    def Addmsg(self, event, tick, Low_id, name, role, msg):
        self.updatedDict = []
        index = 0
        with open('Database/Club/chat.db', 'r+') as file:
            for line in file.readlines():
                json_data = json.loads(line)
                dict = json.loads(json.dumps(json_data))
                for clubIdentifier, data in dict.items():
                    if int(clubIdentifier) == self.player.ClubID:
                        for i in range(1, dict[str(clubIdentifier)]['Total'] + 1):
                            index += 1
                            if index == dict[str(clubIdentifier)]['Total']:
                                dict[str(clubIdentifier)][str(i + 1)] = {"Event": event, "Tick": dict[str(clubIdentifier)][str(i)]['Tick'] + 1, "PlayerID": Low_id, "PlayerName": name, "PlayerRole": role, "Message": msg}
                                dict[str(clubIdentifier)]['Total'] = i + 1
                                self.player.ClubMessageCount = dict[str(clubIdentifier)]['Total'] = i + 1
                                self.player.messageTick = dict[str(clubIdentifier)][str(i + 1)]['Tick']
                                file.close()
                                break
                self.updatedDict.append(json.dumps(dict))            
                file.close()
    
        with open('Database/Club/chat.db', 'w') as o:
            o.writelines('\n'.join(self.updatedDict))
            o.write('\n')
            o.close()