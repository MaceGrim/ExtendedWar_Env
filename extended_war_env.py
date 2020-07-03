from abc import ABC

import gym
from gym import spaces
import numpy as np
import random as rd


class ExtendedWar(gym.Env):

    def render(self, mode='human'):
        pass

    def __init__(self):
        self.deck = [i for i in range(1, 14)] * 4
        self.deck = rd.sample(13*4)

        self.hand1 = [self.deck.pop() for i in range(26)]
        self.hand2 = [self.deck.pop() for i in range(26)]

        self.score1 = 0
        self.score2 = 0

        self.card1 = None
        self.card2 = None

        self.observation_space = spaces.Discrete(52)
        self.action_space = spaces.Discrete(26)

    def reset(self):
        self.deck = [i for i in range(1, 14)] * 4
        self.deck = rd.sample(13 * 4)

        self.hand1 = [self.deck.pop() for i in range(26)]
        self.hand2 = [self.deck.pop() for i in range(26)]

        self.played1 = []
        self.played2 = []

        self.score1 = 0
        self.score2 = 0

        self.card1 = None
        self.card2 = None

    def step(self, player, index_of_card_to_play):


        return observation, reward, done, {}

    def get_observation(self, player):
        hand = self.hand1 if player == 1 else self.hand2
        hand_vector = self._convert_hand_to_vector(hand)

        player_score = self.score1 if player == 1 else self.score2
        opp_score = self.score1 if player == 2 else self.score2

        player_score_vector = self._convert_score_to_vector(player_score)
        opp_score_vector = self._convert_score_to_vector(opp_score)

        return np.concatenate([hand_vector, player_score_vector, opp_score_vector])

    def _convert_score_to_vector(self, score):
        bin_score = str(bin(score))[2:]
        while len(bin_score) < 6:
            bin_score = "0" + bin_score
        return np.array(list(bin_score))

    def _convert_hand_to_vector(self, hand):
        bin_vector = []
        count_dict = {i: hand.count(i) for i in range(1, 14)}
        for i in range(1, 14):
            count = count_dict[i]
            bin_count = bin(count)
            bin_string = str(bin_count)[2:]
            for bit in bin_string:
                bin_vector.append(int(bit))
        return np.array(bin_vector)
