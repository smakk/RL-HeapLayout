import gym
import gym_foo

from baselines import deepq

'''
env = gym.make("CartPole-v0")

env.reset()
env.step(env.action_space.sample())
print(env.result)
'''

env = gym.make('foo-v0')

act = deepq.learn(
    env,
    network='mlp',
    lr=1e-3,
    total_timesteps=100000,
    buffer_size=50000,
    exploration_fraction=0.1,
    exploration_final_eps=0.02,
    print_freq=10,
)
