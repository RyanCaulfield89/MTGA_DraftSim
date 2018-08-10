"""
File: Draft.py
Author: Ryan P. Caulfield ryancaulfield89@gmail.com

Description:
    Simulation code to compare quick draft and competitive draft in MTG Arena.

To Do List:
    1. Add a second class "Player" to make this cleaner
    2. Sweep starting parameters and look for optimized values
    3. Save data to file
    4. Add in graphing with MatPlotLib

"""
import random
import statistics

class Draft:
    gems = 0
    drafts = 0
    packs = 0
    win_rate = 0.5
    active = True
    max_drafts = 1200
    comp_prizes = [0,0,800,1500,1800,2100]
    comp_cost = 1500
    quick_prizes = [[50,0.2],[100,0.22],[200,0.24],[300,0.26],[450,0.3],[650,0.35],[850,0.4],[950,1]]
    quick_cost = 750

    def __init__(self,starting_gems,starting_win_rate):
        self.gems = starting_gems
        self.win_rate = starting_win_rate
        return

    def play_game(self):
        if(random.random() <= self.win_rate):
            return True
        else:
            return False

    def play_match(self):
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

    def play_quick_draft(self):
        self.gems -= self.quick_cost
        self.drafts += 1
        wins = 0
        loses = 0
        while(loses < 3 and wins < 7):
            if(self.play_game()):
                wins += 1
            else:
                loses += 1
        self.gems += self.quick_prizes[wins][0]
        self.packs += 1
        if(random.random() > self.quick_prizes[wins][1]):
            self.packs += 1
        if(self.gems < self.quick_cost):
            self.active = False

    def play_comp_draft(self):
        self.gems -= self.comp_cost
        self.drafts += 1
        wins = 0
        loses = 0
        while(loses < 2 and wins < 5):
            if(self.play_match()):
                wins += 1
            else:
                loses += 1
        self.gems += self.comp_prizes[wins]
        self.packs += wins + 1
        if(self.gems < self.comp_cost):
            self.active = False

    def try_hard_comp(self):
        while(self.active and self.drafts < self.max_drafts):
            self.play_comp_draft()

    def try_hard_quick(self):
        while(self.active and self.drafts < self.max_drafts):
            self.play_quick_draft()

num_drafters = 10000 #10000 samples makes this fairly repeatable
starting_gems = 9200 #Cost 50$ on MTGA. This is a reasonable amount for players.
starting_win_rate = 0.6 #Decent player but not a pro. This could be as high as 70%-75%.
player_roster_quick = []
player_roster_quick_drafts = []
player_roster_quick_packs = []
for i in range(0,num_drafters):
    player_roster_quick.append(Draft(starting_gems,starting_win_rate))
    player_roster_quick[i].try_hard_quick()
    player_roster_quick_drafts.append(player_roster_quick[i].drafts)
    player_roster_quick_packs.append(player_roster_quick[i].packs)
player_roster_comp = []
player_roster_comp_drafts = []
player_roster_comp_packs = []
for i in range(0,num_drafters):
    player_roster_comp.append(Draft(starting_gems,starting_win_rate))
    player_roster_comp[i].try_hard_comp()
    player_roster_comp_drafts.append(player_roster_comp[i].drafts)
    player_roster_comp_packs.append(player_roster_comp[i].packs)

print("Quick drafters starting with "+str(starting_gems)+" gems and a winrate of "+str(starting_win_rate)+":")
print("Number of drafts:")
print("Average:"+str(statistics.mean(player_roster_quick_drafts)))
print("Median:"+str(statistics.median(player_roster_quick_drafts)))
print("Standard Deviation:"+str(statistics.stdev(player_roster_quick_drafts)))
print("Number of packs:")
print("Average:"+str(statistics.mean(player_roster_quick_packs)))
print("Median:"+str(statistics.median(player_roster_quick_packs)))
print("Standard Deviation:"+str(statistics.stdev(player_roster_quick_packs)))

print("Competitive drafters starting with "+str(starting_gems)+" gems and a winrate of "+str(starting_win_rate)+":")
print("Number of drafts:")
print("Average:"+str(statistics.mean(player_roster_comp_drafts)))
print("Median:"+str(statistics.median(player_roster_comp_drafts)))
print("Standard Deviation:"+str(statistics.stdev(player_roster_comp_drafts)))
print("Number of packs:")
print("Average:"+str(statistics.mean(player_roster_comp_packs)))
print("Median:"+str(statistics.median(player_roster_comp_packs)))
print("Standard Deviation:"+str(statistics.stdev(player_roster_comp_packs)))
