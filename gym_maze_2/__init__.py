from gym.envs.registration import register

register(
    id='maze-v2',
    entry_point='gym_maze_2.envs:MazeEnv2',
)
