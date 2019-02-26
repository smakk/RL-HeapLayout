import gym
import gym_foo

env = gym.make('foo-v0')
env.reset()
env.step(env.action_space.sample())
print(env.result)
