import gym
from gym import error, spaces, utils
from gym.utils import seeding

class FooEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        self.action_space = spaces.Discrete(5)
        self.observation_space = spaces.Discrete(50)
        self.state = 0
    def step(self, action):
        self.state += action
        reward = action
        done = False
        if self.state>50:
            done = True
        return state,reward,done,{}
    def reset(self):
        self.state = 0
    def render(self, mode='human'):
        ...
    def close(self):
        ...
