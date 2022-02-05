from Utils.Writer import Writer
from Database.DatabaseManager import DataBase


class BattleResultMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 23456
        self.player = player
        
    def encode(self):
        brawler_trophies = self.player.brawlers_trophies[str(self.player.brawler_id)]
        brawler_trophies_for_rank = self.player.brawlers_trophies_in_rank[str(self.player.brawler_id)]
        
        if 0 <= brawler_trophies <= 49:
            rank_0 = 10
            rank_1 = 10
            rank_2 = 8
            rank_3 = 6
            rank_4 = 5
            rank_5 = 4
            rank_6 = 4
            rank_7 = 3
            rank_8 = 2
            rank_9 = 1
            rank_10 = 0

        else:
            if 50 <= brawler_trophies <= 99:
                rank_0 = 10
                rank_1 = 10
                rank_2 = 8
                rank_3 = 6
                rank_4 = 5
                rank_5 = 3
                rank_6 = 1
                rank_7 = 0
                rank_8 = -1
                rank_9 = -1
                rank_10 = -2

            if 100 <= brawler_trophies <= 199:
                rank_0 = 10
                rank_1 = 10
                rank_2 = 8
                rank_3 = 6
                rank_4 = 4
                rank_5 = 2
                rank_6 = 1
                rank_7 = -1
                rank_8 = -2
                rank_9 = -2
                rank_10 = -3

            if 200 <= brawler_trophies <= 299:
                rank_0 = 10
                rank_1 = 10
                rank_2 = 8
                rank_3 = 6
                rank_4 = 4
                rank_5 = 3
                rank_6 = 1
                rank_7 = -1
                rank_8 = -2
                rank_9 = -2
                rank_10 = -3

            if 300 <= brawler_trophies <= 399:
                rank_0 = 10
                rank_1 = 10
                rank_2 = 8
                rank_3 = 6
                rank_4 = 4
                rank_5 = 1
                rank_6 = 0
                rank_7 = 0
                rank_8 = 0
                rank_9 = 0
                rank_10 = 0

            if 400 <= brawler_trophies <= 499:
                rank_0 = 10
                rank_1 = 10
                rank_2 = 8
                rank_3 = 6
                rank_4 = 3
                rank_5 = 2
                rank_6 = -2
                rank_7 = -3
                rank_8 = -4
                rank_9 = -5
                rank_10 = -5

            if 500 <= brawler_trophies <= 549:
                rank_0 = 10
                rank_1 = 10
                rank_2 = 8
                rank_3 = 6
                rank_4 = 3
                rank_5 = 0
                rank_6 = -2
                rank_7 = -3
                rank_8 = -4
                rank_9 = -5
                rank_10 = -5
                
            if 550 <= brawler_trophies <= 599:
                rank_0 = 10
                rank_1 = 10
                rank_2 = 8
                rank_3 = 6
                rank_4 = 3
                rank_5 = 0
                rank_6 = -3
                rank_7 = -4
                rank_8 = -5
                rank_9 = -5
                rank_10 = -6
                
            if 600 <= brawler_trophies <= 649:
                rank_0 = 8
                rank_1 = 8
                rank_2 = 6
                rank_3 = 5
                rank_4 = 2
                rank_5 = -2
                rank_6 = -2
                rank_7 = -3
                rank_8 = -5
                rank_9 = -6
                rank_10 = -6
                
            if 650 <= brawler_trophies <= 699:
                rank_0 = 7
                rank_1 = 7
                rank_2 = 6
                rank_3 = 5
                rank_4 = 2
                rank_5 = -2
                rank_6 = -3
                rank_7 = -4
                rank_8 = -6
                rank_9 = -6
                rank_10 = -7
                
            if 700 <= brawler_trophies <= 749:
                rank_0 = 7
                rank_1 = 7
                rank_2 = 6
                rank_3 = 5
                rank_4 = 2
                rank_5 = -3
                rank_6 = -3
                rank_7 = -5
                rank_8 = -6
                rank_9 = -6
                rank_10 = -7
                
            if 750 <= brawler_trophies <= 799:
                rank_0 = 7
                rank_1 = 7
                rank_2 = 6
                rank_3 = 5
                rank_4 = 2
                rank_5 = -4
                rank_6 = -5
                rank_7 = -6
                rank_8 = -6
                rank_9 = -6
                rank_10 = -7
                
            if 800 <= brawler_trophies <= 849:
                rank_0 = 7
                rank_1 = 7
                rank_2 = 6
                rank_3 = 5
                rank_4 = 2
                rank_5 = -4
                rank_6 = -8
                rank_7 = -10
                rank_8 = -12
                rank_9 = -14
                rank_10 = -18

            if 850 <= brawler_trophies <= 899:
                rank_0 = 6
                rank_1 = 6
                rank_2 = 5
                rank_3 = 4
                rank_4 = 1
                rank_5 = -4
                rank_6 = -5
                rank_7 = -6
                rank_8 = -6
                rank_9 = -7
                rank_10 = -8
                
            if 900 <= brawler_trophies <= 949:
                rank_0 = 6
                rank_1 = 6
                rank_2 = 3
                rank_3 = 2
                rank_4 = 1
                rank_5 = 0
                rank_6 = -4
                rank_7 = -6
                rank_8 = -8
                rank_9 = -10
                rank_10 = -13
                
            if 950 <= brawler_trophies <= 999:
                rank_0 = 6
                rank_1 = 6
                rank_2 = 3
                rank_3 = 2
                rank_4 = 1
                rank_5 = -3
                rank_6 = -6
                rank_7 = -7
                rank_8 = -8
                rank_9 = -12
                rank_10 = -16

            if 1000 <= brawler_trophies <= 1199:
                rank_0 = 6
                rank_1 = 6
                rank_2 = 3
                rank_3 = 2
                rank_4 = 1
                rank_5 = -3
                rank_6 = -6
                rank_7 = -7
                rank_8 = -8
                rank_9 = -12
                rank_10 = -16
                
            if 1200 <= brawler_trophies <= 1249:
                rank_0 = 6
                rank_1 = 6
                rank_2 = 3
                rank_3 = 1
                rank_4 = -4
                rank_5 = -7
                rank_6 = -8
                rank_7 = -9
                rank_8 = -12
                rank_9 = -14
                rank_10 = -20
                
                
            if brawler_trophies >= 1250:
                rank_0 = 4
                rank_1 = 4
                rank_2 = 2
                rank_3 = 1
                rank_4 = -4
                rank_5 = -8
                rank_6 = -10
                rank_7 = -11
                rank_8 = -15
                rank_9 = -18
                rank_10 = -22
                       
                
                 
        if self.player.rank == 1:
        	trophies = rank_1
        	tokens = 32
        	anim = 16
        	gold_event = 0
        	xp = 8
        	new_xp = self.player.player_experience + xp
        	tokens_databaser = self.player.brawl_boxes + tokens
        	self.player.brawlers_trophies[str(self.player.brawler_id)] = brawler_trophies + rank_1
        	self.player.brawlers_trophies_in_rank[str(self.player.brawler_id)] = brawler_trophies_for_rank + rank_1
        	DataBase.replaceValue(self, 'brawlersTrophies', self.player.brawlers_trophies)
        	DataBase.replaceValue(self, 'brawlersTrophiesForRank', self.player.brawlers_trophies_in_rank)


        	
        elif self.player.rank == 2:
        	trophies = rank_2
        	tokens = 26
        	anim = 16
        	gold_event = 0
        	xp = 8
        	new_xp = self.player.player_experience + xp
        	tokens_databaser = self.player.brawl_boxes + tokens
        	self.player.brawlers_trophies[str(self.player.brawler_id)] = brawler_trophies + rank_2
        	self.player.brawlers_trophies_in_rank[str(self.player.brawler_id)] = brawler_trophies_for_rank + rank_2
        	DataBase.replaceValue(self, 'brawlersTrophies', self.player.brawlers_trophies)
        	DataBase.replaceValue(self, 'brawlersTrophiesForRank', self.player.brawlers_trophies_in_rank)



        elif self.player.rank == 3:
        	trophies = rank_3
        	tokens = 22
        	anim = 16
        	gold_event = 0
        	xp = 8
        	new_xp = self.player.player_experience + xp
        	tokens_databaser = self.player.brawl_boxes + tokens
        	self.player.brawlers_trophies[str(self.player.brawler_id)] = brawler_trophies + rank_3
        	self.player.brawlers_trophies_in_rank[str(self.player.brawler_id)] = brawler_trophies_for_rank + rank_3
        	DataBase.replaceValue(self, 'brawlersTrophies', self.player.brawlers_trophies)
        	DataBase.replaceValue(self, 'brawlersTrophiesForRank', self.player.brawlers_trophies_in_rank)


        	
        elif self.player.rank == 4:
        	trophies = rank_4
        	tokens = 20
        	anim = 16
        	gold_event = 0
        	xp = 6
        	new_xp = self.player.player_experience + xp
        	tokens_databaser = self.player.brawl_boxes + tokens
        	self.player.brawlers_trophies[str(self.player.brawler_id)] = brawler_trophies + rank_4
        	self.player.brawlers_trophies_in_rank[str(self.player.brawler_id)] = brawler_trophies_for_rank + rank_4
        	DataBase.replaceValue(self, 'brawlersTrophies', self.player.brawlers_trophies)
        	DataBase.replaceValue(self, 'brawlersTrophiesForRank', self.player.brawlers_trophies_in_rank)


        	
        elif self.player.rank == 5:
        	trophies = rank_5
        	tokens = 16
        	anim = 16
        	gold_event = 0
        	xp = 4
        	new_xp = self.player.player_experience + xp
        	tokens_databaser = self.player.brawl_boxes + tokens
        	self.player.brawlers_trophies[str(self.player.brawler_id)] = brawler_trophies + rank_5
        	self.player.brawlers_trophies_in_rank[str(self.player.brawler_id)] = brawler_trophies_for_rank + rank_5
        	DataBase.replaceValue(self, 'brawlersTrophies', self.player.brawlers_trophies)
        	DataBase.replaceValue(self, 'brawlersTrophiesForRank', self.player.brawlers_trophies_in_rank)


        	
        elif self.player.rank == 6:
        	trophies = rank_6
        	tokens = 14
        	anim = 16
        	gold_event = 0
        	xp = 4
        	new_xp = self.player.player_experience + xp
        	tokens_databaser = self.player.brawl_boxes + tokens
        	self.player.brawlers_trophies[str(self.player.brawler_id)] = brawler_trophies + rank_6
        	self.player.brawlers_trophies_in_rank[str(self.player.brawler_id)] = brawler_trophies_for_rank + rank_6
        	DataBase.replaceValue(self, 'brawlersTrophies', self.player.brawlers_trophies)
        	DataBase.replaceValue(self, 'brawlersTrophiesForRank', self.player.brawlers_trophies_in_rank)


        	
        elif self.player.rank == 7:
        	trophies = rank_7
        	tokens = 10
        	anim = 16
        	gold_event = 0
        	xp = 2
        	new_xp = self.player.player_experience + xp
        	tokens_databaser = self.player.brawl_boxes + tokens
        	self.player.brawlers_trophies[str(self.player.brawler_id)] = brawler_trophies + rank_7
        	self.player.brawlers_trophies_in_rank[str(self.player.brawler_id)] = brawler_trophies_for_rank + rank_7
        	DataBase.replaceValue(self, 'brawlersTrophies', self.player.brawlers_trophies)
        	DataBase.replaceValue(self, 'brawlersTrophiesForRank', self.player.brawlers_trophies_in_rank)


        	
        elif self.player.rank == 8:
        	trophies = rank_8
        	tokens = 5
        	anim = 16
        	gold_event = 0
        	xp = 2
        	new_xp = self.player.player_experience + xp
        	tokens_databaser = self.player.brawl_boxes + tokens
        	self.player.brawlers_trophies[str(self.player.brawler_id)] = brawler_trophies + rank_8
        	self.player.brawlers_trophies_in_rank[str(self.player.brawler_id)] = brawler_trophies_for_rank + rank_8
        	DataBase.replaceValue(self, 'brawlersTrophies', self.player.brawlers_trophies)
        	DataBase.replaceValue(self, 'brawlersTrophiesForRank', self.player.brawlers_trophies_in_rank)

        	
        elif self.player.rank == 9:
        	trophies = rank_9
        	tokens = 0
        	anim = 16
        	gold_event = 0
        	xp = 1
        	new_xp = self.player.player_experience + xp
        	tokens_databaser = self.player.brawl_boxes + tokens
        	self.player.brawlers_trophies[str(self.player.brawler_id)] = brawler_trophies + rank_9
        	self.player.brawlers_trophies_in_rank[str(self.player.brawler_id)] = brawler_trophies_for_rank + rank_9
        	DataBase.replaceValue(self, 'brawlersTrophies', self.player.brawlers_trophies)
        	DataBase.replaceValue(self, 'brawlersTrophiesForRank', self.player.brawlers_trophies_in_rank)

        elif self.player.rank == 10:
        	trophies = rank_10
        	tokens = 0
        	anim = 16
        	gold_event = 0
        	xp = 0
        	new_xp = self.player.player_experience + xp
        	tokens_databaser = self.player.brawl_boxes + tokens
        	self.player.brawlers_trophies[str(self.player.brawler_id)] = brawler_trophies + rank_10
        	self.player.brawlers_trophies_in_rank[str(self.player.brawler_id)] = brawler_trophies_for_rank + rank_10
        	DataBase.replaceValue(self, 'brawlersTrophies', self.player.brawlers_trophies)
        	DataBase.replaceValue(self, 'brawlersTrophiesForRank', self.player.brawlers_trophies_in_rank)


        self.writeVint(2) # Battle End Game Mode (2 = Showdown, 3 = Robo Rumble, 4 = Big Game, 5 = Duo Showdown, 6 = Boss Fight. Else is 3vs3)
        self.writeVint(self.player.rank) # Result (Victory/Defeat/Draw/Rank Score)
        self.writeVint(0) # Tokens Gained
        self.writeVint(trophies) # Trophies Result
        self.writeVint(0) # Power Play Points Gained
        self.writeVint(0) # Doubled Tokens
        self.writeVint(0) # Double Token Event
        self.writeVint(0) # Token Doubler Remaining
        self.writeVint(0) # Big Game/Robo Rumble Time and Boss Fight Level Cleared
        self.writeVint(0) # Epic Win Power Play Points Gained
        self.writeVint(0) # Championship Level Passed
        self.writeVint(0) # Challenge Reward Type (0 = Star Points, 1 = Star Tokens)
        self.writeVint(0) # Challenge Reward Ammount
        self.writeVint(0) # Championship Losses Left
        self.writeVint(0) # Championship Maximun Losses
        self.writeVint(0) # Coin Shower Event
        self.writeVint(16) # Battle Result Type ((-16)-(-1) = Power Play Battle End, 0-15 = Practice Battle End, 16-31 = Matchmaking Battle End, 32-47 = Friendly Game Battle End, 48-63  = Spectate and Replay Battle End, 64-79 = Championship Battle End)
        self.writeVint(0) # Championship Cleared and Beta Quests
        
        # Players Array
        self.writeVint(1) # Battle End Screen Players
        self.writeVint(1)
        self.writeScId(16, self.player.brawler_id) # Player Brawler
        self.writeScId(29, self.player.skin_id) # Player Skin
        self.writeVint(brawler_trophies) # Brawler Trophies
        self.writeVint(0) # Player Power Play Points
        self.writeVint(0) # Brawler Power Level
        self.writeBoolean(True) # Player HighID and LowID Array
        self.writeInt(0) # HighID
        self.writeInt(1) # LowID
        self.writeString(self.player.name) # Player Name
        self.writeVint(9) # Player Experience Level
        self.writeVint(28000000) # Player Profile Icon
        self.writeVint(43000000) # Player Name Color

        # Experience Array
        self.writeVint(2) # Count
        self.writeVint(0) # Normal Experience ID
        self.writeVint(0) # Normal Experience Gained
        self.writeVint(8) # Star Player Experience ID
        self.writeVint(0) # Star Player Experience Gained

        # Rank Up and Level Up Bonus Array
        self.writeVint(0) # Count

        # Trophies and Experience Bars Array
        self.writeVint(2) # Count
        self.writeVint(1) # Trophies Bar Milestone ID
        self.writeVint(brawler_trophies) # Brawler Trophies
        self.writeVint(brawler_trophies_for_rank) # Brawler Trophies for Rank
        self.writeVint(5) # Experience Bar Milestone ID
        self.writeVint(1) # Player Experience
        self.writeVint(1) # Player Experience for Level
        
        self.writeScId(28, 0)  # Player Profile Icon
        self.writeBoolean(True)  # Play Again