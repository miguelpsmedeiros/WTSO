# -*- coding: utf-8 -*-
"""Beta_WHOs_THE_SPECIAL_ONE_.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oBFWzp4tALWdCPoAjpVD14YHnyJGPtKX
"""

import pandas as pd
import numpy as np

from itertools import chain
import time


WTSO = pd.read_csv('data_beta_version.csv')

gk = WTSO[WTSO['Cluster']=='GK']

gk = gk.sample(n=2)

gk['short_name'].values

gk['player_positions'] = gk['player_positions'].apply(lambda x: x.split(', '))

gk['player_positions']

cb = WTSO[WTSO['Cluster']=='Defense_center']

cb = cb.sample(n=3)

cb['short_name'].values

cb['player_positions'] = cb['player_positions'].apply(lambda x: x.split(', '))

cb['player_positions']

lrb = WTSO[WTSO['Cluster']=='Defense_wing']

lrb = lrb.sample(n=3)

lrb['short_name'].values

lrb['player_positions'] = lrb['player_positions'].apply(lambda x: x.split(', '))

lrb['player_positions']

mc = WTSO[WTSO['Cluster']=='Midfield_center']

mc = mc.sample(n=4)

mc['short_name'].values

mc['player_positions'] = mc['player_positions'].apply(lambda x: x.split(', '))

mc['player_positions']

mw = WTSO[WTSO['Cluster']=='Midfield_wing']

mw = mw.sample(n=3)

mw['short_name'].values

mw['player_positions'] = mw['player_positions'].apply(lambda x: x.split(', '))

mw['player_positions']

aw = WTSO[WTSO['Cluster']=='Attack_wing']

aw = aw.sample(n=3)

aw['short_name'].values

aw['player_positions'] = aw['player_positions'].apply(lambda x: x.split(', '))

aw['player_positions']

ac = WTSO[WTSO['Cluster']=='Attack_center']

ac = ac.sample(n=3)

ac['short_name'].values

ac['player_positions'] = ac['player_positions'].apply(lambda x: x.split(', '))

ac['player_positions']

merge_data = [gk, ac, mc, cb, mw, aw, lrb]

players_21 = pd.concat(merge_data, 0)


list_21 = list(chain(gk['short_name'], ac['short_name'], mc['short_name'], cb['short_name'], mw['short_name'], aw['short_name'], 
                     lrb['short_name']))


def run_game():

  tatics = {433: ['GK', 'LB', 'CB', 'CB', 'RB', 'CM', 'CM', 'CAM','LW', 'ST', 'RW'],
            343: ['GK', 'CB', 'CB', 'CB', 'CM', 'CM', 'RWB','LWB', 'LW', 'ST', 'RW'],
            442: ['GK', 'LB', 'CB', 'CB', 'RB', 'CM', 'CM', 'RM','LM', 'ST', 'ST'],
            352: ['GK', 'CB', 'CB', 'CB', 'CM', 'CM', 'RM','LM', 'CAM', 'ST', 'ST'],
            41212: ['GK', 'LB', 'CB', 'CB', 'RB', 'CDM', 'RM', 'LM','CAM', 'ST', 'ST'],
            4123: ['GK', 'LB', 'CB', 'CB', 'RB', 'CDM', 'CM', 'CM','LW', 'ST', 'RW'],
            4231: ['GK', 'LB', 'CB', 'CB', 'RB', 'CDM', 'CDM', 'CAM','LM', 'RM', 'ST']}

  points = 0

  players = list_21

  tatics_list = [k for k in tatics.keys()]

  coach_name = input("Hey Coach! Introduce yourself to the team, what's your name: " )

  start_time = time.time()

  print("\n")

  print(f'{coach_name} these are your 21 players available for tonight: ')

  print("\n")

  print(np.array(players).reshape(21,-1))

  print("\n")

  print('Now that you know your players, choose the formation that best suits your desired starting 11: ', tatics_list)

  print("\n")

  nationalities_11 = []

  leagues_11 = []

  teams_11 = []

  t = tatics.copy()

  formation = int(input('tatic:'))

  print("\n")

  print(t[formation])

  print("\n")

  temp = t[formation].copy()

  players_1 = players.copy()

  for player in players:

    print(f"{coach_name} it's time to select the starting 11 : ")

    print("\n")

    print(players_1)

    print("\n")

    starters = input(f'do you want {player} to play:')

    print("\n")

    if starters == 'YES':

      nationalities_11.append(players_21[players_21['short_name'] == player]['nationality'].values[0])

      leagues_11.append(players_21[players_21['short_name'] == player]['league_name'].values[0])

      teams_11.append(players_21[players_21['short_name'] == player]['club_name'].values[0])

      print('where do you want him to play', player)

      print("\n")

      choose = input('choose position: ')

      print("\n")

      positions = players_21[players_21['short_name'] == player]['player_positions'].values[0]

      temp.remove(choose)

      print(temp)

      print("\n")

      players_1.remove(player)

      if (choose in positions) & (choose in t[formation]):

        points = points + 8

      if choose in ['CB'] and bool(set(positions).intersection(set(['CDM', 'RB', 'LB']))):

        points = points + 3

      if choose in ['RB'] and bool(set(positions).intersection(set(['LB', 'CB', 'RM']))):

        points = points + 3

      if choose in ['LB'] and bool(set(positions).intersection(set(['RB', 'CB', 'LM']))):

        points = points + 3

      if choose in ['CDM'] and bool(set(positions).intersection(set(['CM']))):

        points = points + 6

      if choose in ['CDM'] and bool(set(positions).intersection(set(['CB', 'CAM']))):

        points = points + 3

      if choose in ['RM'] and bool(set(positions).intersection(set(['RW']))):

        points = points + 6

      if choose in ['RM'] and bool(set(positions).intersection(set(['LM']))):

        points = points + 5

      if choose in ['RM'] and bool(set(positions).intersection(set(['LW']))):

        points = points + 3

      if choose in ['LM'] and bool(set(positions).intersection(set(['LW']))):

        points = points + 6

      if choose in ['LM'] and bool(set(positions).intersection(set(['RM']))):

        points = points + 5

      if choose in ['LM'] and bool(set(positions).intersection(set(['RW']))):

        points = points + 3

      if choose in ['LM', 'RM'] and bool(set(positions).intersection(set(['CM', 'CAM']))):

        points = points + 3

      if choose in ['CAM'] and bool(set(positions).intersection(set(['CM', 'CF']))):

        points = points + 6

      if choose in ['CAM'] and bool(set(positions).intersection(set(['CDM', 'RM', 'LM', 'ST']))):

        points = points + 3

      if choose in ['LW'] and bool(set(positions).intersection(set(['LM']))):

        points = points + 6

      if choose in ['LW'] and bool(set(positions).intersection(set(['RW']))):

        points = points + 5

      if choose in ['LW'] and bool(set(positions).intersection(set(['RM', 'ST']))):

        points = points + 3

      if choose in ['RW'] and bool(set(positions).intersection(set(['RM']))):

        points = points + 6

      if choose in ['RW'] and bool(set(positions).intersection(set(['LW']))):

        points = points + 5

      if choose in ['RW'] and bool(set(positions).intersection(set(['LM', 'ST']))):

        points = points + 3

      if choose in ['ST'] and bool(set(positions).intersection(set(['LM', 'RM', 'LW', 'RW', 'CAM', 'CF']))):

        points = points + 4

      else:

        points = points + 0

    else:

      players_1.remove(player)

      continue

  nationalities_11_count = {i:nationalities_11.count(i) for i in nationalities_11}

  nationality_points = sum([i for i in nationalities_11_count.values() if i > 1])

  leagues_11_count = {i:leagues_11.count(i) for i in leagues_11}

  league_points = sum([i for i in leagues_11_count.values() if i > 1])

  teams_11_count = {i:teams_11.count(i) for i in teams_11}

  team_points = sum([i for i in teams_11_count.values() if i > 1])*2

  final_score = points + nationality_points + league_points + team_points

  print("\n")

  print(final_score)

  print("--- %s seconds ---" % (time.time() - start_time))

