import gym
from gym import error, spaces, utils
from gym.utils import seeding

import numpy as np

import argparse
import logging
import os
import pathlib
import shutil
import sys

from php7 import *
import php7
from fragments import *
from template import *

class FooEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        logger = logging.getLogger(__name__)

        output_dir_path = pathlib.Path('/tmp/output')
        if output_dir_path.exists():
            os.system('rm /tmp/output/*')
            os.system('rmdir /tmp/output/')
        os.mkdir(output_dir_path.as_posix())
        
        fragment_paths = [pathlib.Path(p) for p in ['fragged.pkl', 'fuzzed_fragged.pkl']]
        fragment_store = FragmentStore(fragment_paths)
        #print("{} unique sequences across {} fragments loaded from {}".format(fragment_store.num_sequences(), fragment_store.num_fragments(),[p.as_posix() for p in fragment_paths]))
        template_path = pathlib.Path('templates/cve-2013-2110-hash_init.template.php')
        self.template = Template(template_path, fragment_store)
        
        shutil.copyfile('templates/cve-2013-2110-hash_init.template.php', output_dir_path / template_path.name)

        logging.info("has {} size for choice".format(self.template.hlm_sizes_in_use()))

        candidate = self.template.instantiate()
        fpath, interactions, err = php7._run_candidate(candidate, '/home/likaiming/PHP-SHRIKE/install/bin/php')
        new_distance = php7._extract_distance(interactions)
        #print(interactions)
        logging.info("{}".format(interactions))
        logging.info("{}".format(new_distance))

        '''
        for num in range(0,2):
            logging.info("generate {} times".format(num))
            t = self.template.instantiate()
            print(t)
        '''
        '''
        self.xth = 0
        self.target_x = 0
        self.target_y = 0
        self.L = 10
        self.action_space = spaces.Discrete(5) # 0, 1, 2，3，4: 不动，上下左右
        self.observation_space = spaces.Box(np.array([-self.L, -self.L]), np.array([self.L, self.L]))
        self.state = None
        '''
    def step(self, action):
        
        
        
        '''
        x, y = self.state
        if action == 0:
            x = x
            y = y
        if action == 1:
            x = x
            y = y + 1
        if action == 2:
            x = x
            y = y - 1
        if action == 3:
            x = x - 1
            y = y
        if action == 4:
            x = x + 1
            y = y
        self.state = np.array([x, y])
            
        done = (np.abs(x)+np.abs(y) <= 1) or (np.abs(x)+np.abs(y) >= 2*self.L+1)
        done = bool(done)
        
        if not done:
            reward = -0.1
        else:
            if np.abs(x)+np.abs(y) <= 1:
                reward = 10
            else:
                reward = -50
        '''
        return self.state, reward, done, {}
    def reset(self):
        self.state = [2,2]#np.ceil(np.random.rand(2)*2*self.L)-self.L

        return self.state
    def render(self, mode='human'):
        ...
    def close(self):
        ...
