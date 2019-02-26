import gym
from gym import error, spaces, utils
from gym.utils import seeding

class FooEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        self.action_space = spaces.Discrete(5)
        self.result = []
    def step(self, action):
        self.result.append(action)
        reward = action
        done = False
        if len(self.result)>50:
            done = True
        return 1,reward,done,{}
    def reset(self):
        self.result = []
    def render(self, mode='human'):
        ...
    def close(self):
        ...
