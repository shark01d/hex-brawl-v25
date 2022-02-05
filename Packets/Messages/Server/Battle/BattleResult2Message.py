from Utils.Writer import Writer
from Database.DatabaseManager import DataBase


class BattleResult2Message(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 23456
        self.player = player

    def encode(self):
        brawler_trophies = self.player.brawlers_trophies[str(self.player.brawler_id)]
        brawler_trophies_for_rank = self.player.brawlers_trophies_in_rank[str(self.player.brawler_id)]
        
        if 0 <= brawler_trophies <= 49:
        	win = 8
        	lose = 0
        	draw = 0
        	lose2 = 0


        else:
            if 50 <= brawler_trophies <= 99:
                win = 8
                lose = -1
                draw = 0
                lose2 = -64


            if 100 <= brawler_trophies <= 199:
                win = 8
                lose = -2
                draw = 0
                lose2 = -63


            if 200 <= brawler_trophies <= 299:
                win = 8
                lose = -3
                draw = 0
                lose2 = -62

            	
            if 300 <= brawler_trophies <= 399:
                win = 8
                lose = -4
                draw = 0
                lose2 = -61


            if 400 <= brawler_trophies <= 499:
                win = 8
                lose = -5
                draw = 0
                lose2 = -60

                
            if 500 <= brawler_trophies <= 549:
                win = 8
                lose = -5
                draw = 0
                lose2 = -60
                
            if 550 <= brawler_trophies <= 599:
                win = 8
                lose = -6
                draw = 0
                lose2 = -60

            if 600 <= brawler_trophies <= 649:
                win = 8
                lose = -6
                draw = 0
                lose2 = -59

            if 650 <= brawler_trophies <= 699:
                win = 8
                lose = -6
                draw = 0
                lose2 = -59

                
            if 700 <= brawler_trophies <= 749:
                win = 8
                lose = -7
                draw = 0
                lose2 = -58

            if 750 <= brawler_trophies <= 799:
                win = 8
                lose = -7
                draw = 0
                lose2 = -58

                
            if 800 <= brawler_trophies <= 849:
                win = 6
                lose = -8
                draw = 0
                lose2 = -57

                
            if 850 <= brawler_trophies <= 899:
                win = 6
                lose = -10
                draw = 0
                lose2 = -55

                
            if brawler_trophies >= 900:
                win = 3
                lose = -12
                draw = 0
                lose2 = -53

        
        if self.player.battle_result == 0:
            trophies = win
            restrophies = win
            tokens = 32
            anim = 16
            gold_event = 0
            xp = 8
            new_xp = self.player.player_experience + xp
            tokens_databaser = self.player.brawl_boxes + tokens
            self.player.brawlers_trophies[str(self.player.brawler_id)] = brawler_trophies + restrophies
            self.player.brawlers_trophies_in_rank[str(self.player.brawler_id)] = brawler_trophies_for_rank + restrophies
            DataBase.replaceValue(self, 'brawlersTrophies', self.player.brawlers_trophies)
            DataBase.replaceValue(self, 'brawlersTrophiesForRank', self.player.brawlers_trophies_in_rank)

        
        elif self.player.battle_result == 1:
            trophies = lose2
            restrophies = lose
            tokens = 26
            anim = 16
            gold_event = 0
            xp = 8
            new_xp = self.player.player_experience + xp
            tokens_databaser = self.player.brawl_boxes + tokens
            self.player.brawlers_trophies[str(self.player.brawler_id)] = brawler_trophies + restrophies
            self.player.brawlers_trophies_in_rank[str(self.player.brawler_id)] = brawler_trophies_for_rank + restrophies
            DataBase.replaceValue(self, 'brawlersTrophies', self.player.brawlers_trophies)
            DataBase.replaceValue(self, 'brawlersTrophiesForRank', self.player.brawlers_trophies_in_rank)


        elif self.player.battle_result == 2:
        	trophies = draw
        	tokens = 22
        	anim = 16
        	gold_event = 0
        	xp = 8
        	new_xp = self.player.player_experience + xp
        	tokens_databaser = self.player.brawl_boxes + tokens
        	self.player.brawlers_trophies[str(self.player.brawler_id)] = brawler_trophies + draw
        	self.player.brawlers_trophies_in_rank[str(self.player.brawler_id)] = brawler_trophies_for_rank + draw
        	DataBase.replaceValue(self, 'brawlersTrophies', self.player.brawlers_trophies)
        	DataBase.replaceValue(self, 'brawlersTrophiesForRank', self.player.brawlers_trophies_in_rank)


        self.writeVint(0) # Battle End Game Mode (2 = Showdown, 3 = Robo Rumble, 4 = Big Game, 5 = Duo Showdown, 6 = Boss Fight. Else is 3vs3)
        self.writeVint(self.player.rank) # Result (Victory/Defeat/Draw/Rank Score)
        self.writeVint(11) # Tokens Gained
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
        self.writeVint(6) # Battle End Screen Players
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
        
        self.writeVint(0)
        self.writeVint(16)
        self.writeVint(self.player.bot1)
        self.writeVint(0)
        self.writeVint(8)
        self.writeVint(0)
        self.writeVint(10)
        self.writeVint(0)
        self.writeString(self.player.bot1_n)
        self.writeVint(100)
        self.writeVint(28000000)
        self.writeVint(43000000)

        self.writeVint(0)
        self.writeVint(16)
        self.writeVint(self.player.bot2)
        self.writeVint(0)
        self.writeVint(8)
        self.writeVint(0)
        self.writeVint(10)
        self.writeVint(0)
        self.writeString(self.player.bot2_n)
        self.writeVint(100)
        self.writeVint(28000000)
        self.writeVint(43000000)

        self.writeVint(2)
        self.writeVint(16)
        self.writeVint(self.player.bot3)
        self.writeVint(0)
        self.writeVint(8)
        self.writeVint(0)
        self.writeVint(10)
        self.writeVint(0)
        self.writeString(self.player.bot3_n)
        self.writeVint(100)
        self.writeVint(28000000)
        self.writeVint(43000000)

        self.writeVint(2)
        self.writeVint(16)
        self.writeVint(self.player.bot4)
        self.writeVint(0)
        self.writeVint(8)
        self.writeVint(0)
        self.writeVint(10)
        self.writeVint(0)
        self.writeString(self.player.bot4_n)
        self.writeVint(100)
        self.writeVint(28000000)
        self.writeVint(43000000)

        self.writeVint(2)
        self.writeVint(16)
        self.writeVint(self.player.bot5)
        self.writeVint(0)
        self.writeVint(8)
        self.writeVint(0)
        self.writeVint(10)
        self.writeVint(0)
        self.writeString(self.player.bot5_n)
        self.writeVint(100)
        self.writeVint(28000000)
        self.writeVint(43000000)

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