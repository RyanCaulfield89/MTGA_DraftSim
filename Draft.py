import random
import statistics

class Draft:
    gems = 0
    drafts = 0
    packs = 0
    win_rate = 0.5
    active = True

    def Draft(starting_gems,starting_win_rate):
        gems = starting_gems
        win_rate = starting_win_rate
        return

    def play_game():
        if(random.random() <= self.win_rate):
            return True
        else:
            return False

    def play_match():
        wins = 0
        loses = 0
        while(wins < 2 and loses < 2):
            if(self.play_game()):
                wins += 1
            else:
                loses += 1
        if(wins == 2):
            return True
        else:
            return False

    def play_quick_draft():
        self.gems -= 750
        self.drafts += 1
        wins = 0
        loses = 0
        while(loses < 3 and wins < 7):
            if(self.play_game()):
                wins += 1
            else:
                loses += 1
        if(wins == 7):
            self.gems += 950
            self.packs += 2
        elif(wins == 6):
            self.gems += 850
            self.packs += 1
            if(random.random() > 0.4):
                self.packs += 1
        elif(wins == 5):
            self.gems += 650
            self.packs += 1
            if(random.random() > 0.35):
                self.packs += 1
        elif(wins == 4):
            self.gems += 450
            self.packs += 1
            if(random.random() > 0.3):
                self.packs += 1
        elif(wins == 3):
            self.gems += 300
            self.packs += 1
            if(random.random() > 0.26):
                self.packs += 1
        elif(wins == 2):
            self.gems += 200
            self.packs += 1
            if(random.random() > 0.24):
                self.packs += 1
        elif(wins == 1):
            self.gems += 100
            self.packs += 1
            if(random.random() > 0.22):
                self.packs += 1
        else:
            self.gems += 50
            self.packs += 1
            if(random.random() > 0.2):
                self.packs += 1
        if(self.gems < 750):
            self.active = False

    def play_comp_draft():
        self.gems -= 1500
        self.drafts += 1
        wins = 0
        loses = 0
        while(loses < 2 and wins < 5):
            if(self.play_match()):
                wins += 1
            else:
                loses += 1
        if(wins == 5):
            self.gems += 2100
            self.packs += 6
        elif(wins == 4):
            self.gems += 1800
            self.packs += 5
        elif(wins == 3):
            self.gems += 1500
            self.packs += 4
        elif(wins == 2):
            self.gems += 800
            self.packs += 3
        elif(wins == 1):
            self.packs += 2
        else:
            self.packs += 1
        if(self.gems < 1500):
            self.active = False

    def try_hard_comp():
        while(self.active and drafts < 1200):
            self.play_comp_draft()

    def try_hard_quick():
        while(self.active and drafts < 1200):
            self.play_quick_draft()

num_drafters = 100
starting_gems = 9200
starting_win_rate = 0.6
player_roster_quick = []
player_roster_quick_drafts = []
player_roster_quick_packs = []
for i in range(0,num_drafters):
    player_roster.append(Draft(starting_gems,starting_win_rate))
    player_roster[i].try_hard_quick
    player_roster_quick_drafts.append(player_roster[i].drafts)
    player_roster_quick_packs.append(player_roster[i].packs)
player_roster_comp = []
player_roster_comp_drafts = []
player_roster_comp_packs = []
for i in range(0,num_drafters):
    player_roster.append(Draft(starting_gems,starting_win_rate))
    player_roster[i].try_hard_comp
    player_roster_comp_drafts.append(player_roster[i].drafts)
    player_roster_comp_packs.append(player_roster[i].packs)

print("Quick drafters starting with"+starting_gems+"gems and a winrate of "+starting_win_rate+":")
print("Number of drafts:")
print("Average:"+statistics.mean(player_roster_quick_drafts))
print("Median:"+statistics.median(player_roster_quick_drafts))
print("Standard Deviation:"+statistics.stdev(player_roster_quick_drafts))
print("Number of packs:")
print("Average:"+statistics.mean(player_roster_quick_packs))
print("Median:"+statistics.median(player_roster_quick_packs))
print("Standard Deviation:"+statistics.stdev(player_roster_quick_packs))

print("Competitive drafters starting with"+starting_gems+"gems and a winrate of "+starting_win_rate+":")
print("Number of drafts:")
print("Average:"+statistics.mean(player_roster_comp_drafts))
print("Median:"+statistics.median(player_roster_comp_drafts))
print("Standard Deviation:"+statistics.stdev(player_roster_comp_drafts))
print("Number of packs:")
print("Average:"+statistics.mean(player_roster_comp_packs))
print("Median:"+statistics.median(player_roster_comp_packs))
print("Standard Deviation:"+statistics.stdev(player_roster_comp_packs))
