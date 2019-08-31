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
import matplotlib.pyplot as plt
import pandas as pd


def author():
    return 'tsikder3'


def gtid():
    return 902859202


def get_spin_result(win_prob):
    result = False
    if np.random.random() <= win_prob:
        result = True
    return result


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


def betting_strategy_bankroll(win_prob, bank_roll, max_spins=1000, goal=80):
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
                bet_amount = min(bet_amount * 2, bank_roll + episode_winnings)

            winnings[n] = episode_winnings
            if bank_roll + episode_winnings == 0:
                winnings[n + 1] = episode_winnings
                return winnings

            if n == max_spins:
                return winnings

    winnings[n + 1:] = goal

    return winnings


def roulette_simulation(winProb, runs, bankRoll=None, max_spins=1000):
    simulations = np.zeros((runs, max_spins + 1), dtype=np.int)
    for t in range(runs):
        if bankRoll:
            simulations[t, :] = betting_strategy_bankroll(winProb, 256, max_spins=max_spins)
        else:

            simulations[t, :] = betting_strategy(winProb, max_spins=max_spins)

    return simulations


def experiment_1(win_prob):
    figure_1 = roulette_simulation(win_prob, 10)
    # figure 1
    fig, ax = plt.subplots()
    pd.DataFrame(figure_1.T).plot(
        title="Winnings of 10 simulations",
        ax=ax
    )
    ax.set_xlim(0, 300)
    ax.set_ylim(-256, 100)
    ax.set_ylabel("Exp winnings")
    ax.set_xlabel("Spin number")
    plt.savefig("experiment1-figure1.png")

    # Figure 2
    figure_2 = roulette_simulation(win_prob, 1000)
    figure_2_mean = np.mean(figure_2, axis=0)
    figure_2_std = np.std(figure_2, axis=0)
    fig, ax = plt.subplots(figsize=(8, 4))
    df = pd.DataFrame(np.array([
        figure_2_mean,
        figure_2_mean + figure_2_std,
        figure_2_mean - figure_2_std
    ]))

    df.ix[0].plot(
        title="Winnings of 1000 simulations",
        style="-",
        color="red",
        ax=ax
    )
    df.ix[1].plot(style="-", color="green", linewidth=0.5, ax=ax)
    df.ix[2].plot(style="-", color="green", linewidth=0.5, ax=ax)
    ax.set_xlim(0, 300)
    ax.set_ylim(-256, 100)
    ax.set_ylabel("Exp winnings")
    ax.set_xlabel("Spin number")
    plt.legend(["Mean", "Mean +/- Std"])
    plt.tight_layout()
    plt.savefig("experiment1-figure2.png")

    # Figure 3
    figure_3_median = np.median(figure_2, axis=0)
    df = pd.DataFrame(np.array([
        figure_3_median,
        figure_3_median + figure_2_std,
        figure_3_median - figure_2_std
    ]))
    df.ix[0].plot(
        title="Winnings of 1000 simulations",
        style="-",
        color="red",
        ax=ax
    )
    df.ix[1].plot(style="-", color="green", linewidth=0.5, ax=ax)
    df.ix[2].plot(style="-", color="green", linewidth=0.5, ax=ax)
    ax.set_xlim(0, 300)
    ax.set_ylim(-256, 100)
    ax.set_ylabel("Exp winnings")
    ax.set_xlabel("Spin number")
    plt.legend(["Median", "Mean +/- Std"])
    plt.tight_layout()
    plt.savefig("experiment1-figure3.png")


def experiment_2(win_prob):
    # Figure 4
    figure_4 = roulette_simulation(win_prob, 1000, 256)
    figure_4_mean = np.mean(figure_4, axis=0)
    figure_4_std = np.std(figure_4, axis=0)
    fig, ax = plt.subplots()
    df = pd.DataFrame(np.array([
        figure_4_mean,
        figure_4_mean + figure_4_std,
        figure_4_mean - figure_4_std
    ]))

    df.ix[0].plot(
        title="Winnings of 1000 simulations",
        style="-",
        color="red",
        ax=ax
    )
    df.ix[1].plot(style="-", color="green", linewidth=0.5, ax=ax)
    df.ix[2].plot(style="-", color="green", linewidth=0.5, ax=ax)
    ax.set_xlim(0, 300)
    ax.set_ylim(-256, 100)
    ax.set_ylabel("Exp winnings")
    ax.set_xlabel("Spin number")
    plt.legend(["Mean", "Mean +/- Std"])
    plt.tight_layout()
    plt.savefig("experiment2-figure4.png")

    # Figure 5
    figure_5_median = np.median(figure_4, axis=0)
    fig, ax = plt.subplots(figsize=(8, 4))
    df = pd.DataFrame(np.array([
        figure_5_median,
        figure_5_median + figure_4_std,
        figure_5_median - figure_4_std
    ]))
    df.ix[0].plot(
        title="Winnings of 1000 simulations",
        style="-",
        color="red",
        ax=ax
    )
    df.ix[1].plot(style="-", color="green", linewidth=0.5, ax=ax)
    df.ix[2].plot(style="-", color="green", linewidth=0.5, ax=ax)
    ax.set_xlim(0, 300)
    ax.set_ylim(-256, 100)
    ax.set_ylabel("Exp winnings")
    ax.set_xlabel("Spin number")
    plt.legend(["Median", "Mean +/- Std"])
    plt.tight_layout()
    plt.savefig("experiment2-figure5.png")


def helper_methods(win_prob):
    q2 = roulette_simulation(win_prob, 1000)
    q2_mean = np.mean(q2, axis=0)
    fig, ax = plt.subplots(figsize=(8, 4))
    pd.DataFrame(q2_mean).plot(
        title="Winnings of 10 simulations",
        ax=ax
    )
    ax.set_xlim(0, 1000)
    ax.set_ylim(-256, 100)
    ax.set_ylabel("Exp winnings mean")
    ax.set_xlabel("Spin number")
    plt.savefig("question2.png")




def test_code():
    win_prob = (18 / 38)  # set appropriately to the probability of a win
    np.random.seed(gtid())  # do this only once
    experiment_1(win_prob)
    experiment_2(win_prob)
    # Q4
    q4 = roulette_simulation(win_prob, 1000, max_spins=1000, bankRoll=256)
    has_reach_goal = np.apply_along_axis(
        lambda s: np.any(s == 80), 1, q4)
    q4_probabilty = np.mean(has_reach_goal)
    helper_methods(win_prob)


if __name__ == "__main__":
    test_code()
