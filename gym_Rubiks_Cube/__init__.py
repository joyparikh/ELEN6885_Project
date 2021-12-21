from gym.envs.registration import register

register(
    id='RubiksCube-v0',
    entry_point='gym_Rubiks_Cube.envs:RubiksCubeEnv',
)

register(
    id='ERubiksCube-v0',
    entry_point='gym_Rubiks_Cube.envs:RubiksCubeEnv',
    kwargs={'explore' : True}
)

register(
    id='RubiksCube-v1',
    entry_point='gym_Rubiks_Cube.envs:RubiksCubeEnv',
    kwargs={'optimize' : True}
)

register(
    id='ERubiksCube-v1',
    entry_point='gym_Rubiks_Cube.envs:RubiksCubeEnv',
    kwargs={'optimize' : True, 'explore' : True}
)

register(
    id='RubiksCube-v2',
    entry_point='gym_Rubiks_Cube.envs:RubiksCubeEnv',
    kwargs={'optimize' : True, 'ultragoal' : True}
)

register(
    id='ERubiksCube-v2',
    entry_point='gym_Rubiks_Cube.envs:RubiksCubeEnv',
    kwargs={'optimize' : True, 'ultragoal' : True, 'explore' : True}
)

register(
    id='RubiksCube2x2-v0',
    entry_point='gym_Rubiks_Cube.envs:RubiksCubeEnv',
    kwargs={'orderNum' : 2},
)

register(
    id='RubiksCube4x4-v0',
    entry_point='gym_Rubiks_Cube.envs:RubiksCubeEnv',
    kwargs={'orderNum' : 4},
)
