"""Assess a betting strategy.  		   	  			  	 		  		  		    	 		 		   		 		  

Copyright 2018, Georgia Institute of Technology (Georgia Tech)  		   	  			  	 		  		  		    	 		 		   		 		  
Atlanta, Georgia 30332  		   	  			  	 		  		  		    	 		 		   		 		  
All Rights Reserved  		   	  			  	 		  		  		    	 		 		   		 		  

Template code for CS 4646/7646  		   	  			  	 		  		  		    	 		 		   		 		  

Georgia Tech asserts copyright ownership of this template and all derivative  		   	  			  	 		  		  		    	 		 		   		 		  
works, including solutions to the projects assigned in this course. Students  		   	  			  	 		  		  		    	 		 		   		 		  
and other users of this template code are advised not to share it with others  		   	  			  	 		  		  		    	 		 		   		 		  
or to make it available on publicly viewable websites including repositories  		   	  			  	 		  		  		    	 		 		   		 		  
such as github and gitlab.  This copyright statement should not be removed  		   	  			  	 		  		  		    	 		 		   		 		  
or edited.  		   	  			  	 		  		  		    	 		 		   		 		  

We do grant permission to share solutions privately with non-students such  		   	  			  	 		  		  		    	 		 		   		 		  
as potential employers. However, sharing with other current or future  		   	  			  	 		  		  		    	 		 		   		 		  
students of CS 7646 is prohibited and subject to being investigated as a  		   	  			  	 		  		  		    	 		 		   		 		  
GT honor code violation.  		   	  			  	 		  		  		    	 		 		   		 		  

-----do not edit anything above this line---  		   	  			  	 		  		  		    	 		 		   		 		  

Student Name: Tofique Sikder (replace with your name)
GT User ID: tsikder3 (replace with your User ID)
GT ID: 902859202 (replace with your GT ID)
"""

import numpy as np


def author():
    return 'tsikder3'


def gtid():
    return 902859202


def get_spin_result(win_prob):
    result = False
    if np.random.random() <= win_prob:
        result = True
    return result


# add your code here to implement the experiments
def betting_strategy(win_prob, max_spins=1000, goal=80):
    n = 0
    episode_winnings = 0
    winnings = np.zeros(max_spins + 1, dtype=np.int)

    while episode_winnings < goal:
        won = False
        bet_amount = 1

        while not won:
            n += 1
            won = get_spin_result(win_prob)
            if won:
                episode_winnings = episode_winnings + bet_amount
            else:
                episode_winnings = episode_winnings - bet_amount
                bet_amount = bet_amount * 2

            winnings[n] = episode_winnings

            if n == max_spins:
                return winnings

    winnings[n + 1:] = goal

    return winnings
def betting_strategy_bankroll(win_prob, max_spins=1000, goal=80):
    n = 0
    episode_winnings = 0
    winnings = np.zeros(max_spins + 1, dtype=np.int)

    while episode_winnings < goal:
        won = False
        bet_amount = 1

        while not won:
            n += 1
            won = get_spin_result(win_prob)
            if won:
                episode_winnings = episode_winnings + bet_amount
            else:
                episode_winnings = episode_winnings - bet_amount
                bet_amount = bet_amount * 2

            winnings[n] = episode_winnings

            if n == max_spins:
                return winnings

    winnings[n + 1:] = goal

    return winnings


def roulette_simulation(winProb, runs, bankRoll=None, max_spins=1000):
    simulations = np.zeros((runs, max_spins + 1), dtype=np.int)
    for t in range(runs):
        if bankRoll:
            print('')
        else:
            print('not bankroll')
            simulations[t, :] = betting_strategy(winProb, max_spins=max_spins)

    return simulations


def experiment_1(win_prob):
    figure_1 = roulette_simulation(win_prob, 10)


def test_code():
    win_prob = (18 / 38)  # set appropriately to the probability of a win
    np.random.seed(gtid())  # do this only once
    experiment_1(win_prob)


if __name__ == "__main__":
    test_code()
