"""
File: Draft.py 1.0
Author: Ryan P. Caulfield ryancaulfield89@gmail.com

Description:
    Simulation code to compare quick draft and competitive draft in MTG Arena.

To Do List:
    1. Add a second class "Roster" to make this cleaner.
    2. Sweep starting parameters and look for optimized values, i.e which mode is
        best for a given win rate, how many gems should a player start with, what
        prize structure reduces prize variance.
    3. Make number of games played in a draft into a parameter instead of hard coding
        then we can see if adjusting the number of games can also help improve
        player experience.
    4. Save data to file.
    5. Add in graphing with MatPlotLib.
    6. Make win percentage more realistic, i.e. maybe draw from a gaussian, change
        second game win rates etc. Maybe instead of a winrate have skill level and
        make winrate calculated based on it.

    Version history
        1.0 Initial version
"""
import random
import statistics

class Player:
    gems = 0 #Self-explanatory
    drafts = 0 #Keep track of the number of drafts played
    packs = 0 #Keep track of packs won along the way
    win_rate = 0.5 #Win rate for an individual game. Assume a single game is i.i.d.
    active = True #This is a flag for wether or not a player has enough gems to keep playing
    max_drafts = 1200 #Arbitrary high cutoff to keep computation time down
                      #makes sense since there is a limited amount of time to play games
    comp_prizes = [0,0,800,1500,1800,2100] #Gem prizes for competitive draft
    comp_cost = 1500 #Cost for competitive draft
    quick_prizes = [[50,0.2],[100,0.22],[200,0.24],[300,0.26],[450,0.3],[650,0.35],[850,0.4],[950,1]]
                     #Gems prizes and probability of getting a 2nd pack
    quick_cost = 750 #Cost for quick draft

    def __init__(self,starting_gems,starting_win_rate):
        #Will probably overload this later to allow for parameter sweeps
        self.gems = starting_gems
        self.win_rate = starting_win_rate
        return

    def play_game(self):
        #This determines the outcome of a single game and returns True if the player wins
        if(random.random() <= self.win_rate):
            return True
        else:
            return False

    def play_match(self):
        #Plays a best of 3 match and returns True if the player wins
        wins = 0
        loses = 0
        while(wins < 2 and loses < 2): #keep going until 2 loses or 2 wins
            if(self.play_game()):
                wins += 1
            else:
                loses += 1
        if(wins == 2):
            #player wins
            return True
        else:
            #player loses
            return False

    def play_quick_draft(self):
        #Play single games until you reach 7 wins or 3 loses
        #Then apply cost and prizes
        self.gems -= self.quick_cost
        self.drafts += 1
        wins = 0
        loses = 0
        while(loses < 3 and wins < 7): #play until 7 wins or 3 loses
            if(self.play_game()): #single games
                wins += 1
            else:
                loses += 1
        self.gems += self.quick_prizes[wins][0] #Add prize gems
        self.packs += 1 #Always get one pack
        if(random.random() < self.quick_prizes[wins][1]): #Maybe get a 2nd pack
            self.packs += 1
        if(self.gems < self.quick_cost):
            #If the player is out of gems turn off the active flag
            self.active = False

    def play_comp_draft(self):
        #Play best of 3 matches until you reach 5 wins or 2 loses
        #Then apply cost and prizes
        self.gems -= self.comp_cost
        self.drafts += 1
        wins = 0
        loses = 0
        while(loses < 2 and wins < 5): #Play until 5 wins or 2 loses
            if(self.play_match()):
                wins += 1
            else:
                loses += 1
        self.gems += self.comp_prizes[wins] #Add prize gems
        self.packs += wins + 1 #Add prize packs
        if(self.gems < self.comp_cost):
            #If the player is out of gems turn off the active flag
            self.active = False

    def try_hard_comp(self):
        #Repeatedly play drafts until the player runs out of gems or reaches max drafts
        while(self.active and self.drafts < self.max_drafts):
            self.play_comp_draft()

    def try_hard_quick(self):
        #Repeatedly play drafts until the player runs out of gems or reaches max drafts
        while(self.active and self.drafts < self.max_drafts):
            self.play_quick_draft()


#This can probably get fed into an overloaded constructor
starting_gems = 9200 #Cost 50$ on MTGA. This is a reasonable amount for players.
starting_win_rate = 0.6 #Decent player but not a pro. This could be as high as 70%-75%.

#This should probably get wrapped into another class, Roster
#Has the number of drafters and arrays of Draft objects
num_drafters = 10000 #10000 samples makes this fairly repeatable
player_roster_quick = []
player_roster_quick_drafts = []
player_roster_quick_packs = []
player_roster_comp = []
player_roster_comp_drafts = []
player_roster_comp_packs = []

#This is the part where stuff happens. Make lot's of player objects and have the draft.
#Save results in an array.
for i in range(0,num_drafters):
    player_roster_quick.append(Player(starting_gems,starting_win_rate))
    player_roster_quick[i].try_hard_quick()
    player_roster_quick_drafts.append(player_roster_quick[i].drafts)
    player_roster_quick_packs.append(player_roster_quick[i].packs)
for i in range(0,num_drafters):
    player_roster_comp.append(Player(starting_gems,starting_win_rate))
    player_roster_comp[i].try_hard_comp()
    player_roster_comp_drafts.append(player_roster_comp[i].drafts)
    player_roster_comp_packs.append(player_roster_comp[i].packs)

#This just prints the results to the screen but it would be best to make plots
#and a data file. This would be easy with MatPlotLib. Also the numbers we really
#care about here are pack:gems drafts:gems and stdev. Plyers want low stdev and
#higher pack:gems and/or drafts:gems. Players will probably tolerate lower ratios
#for less variance though. Note that some players only care about max
#drafts:gems(just want to draft) while others want to maximize
#packs:drafts(just drafting to play constructed).
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
