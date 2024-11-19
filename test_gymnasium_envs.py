
"""
Updated Nov 18, 2024
@author: Kananart K.
"""

import argparse
import gymnasium as gym


### Gymnasium Environments from https://gymnasium.farama.org/ (Nov 18, 2024)
CLASSICAL_CONTROL_ENVS = ['Acrobot-v1', 'CartPole-v1', 'MountainCarContinuous-v0', 'MountainCar-v0', 'Pendulum-v1']
BOX2D_ENVS = ['BipedalWalker-v3', 'CarRacing-v3', 'LunarLander-v3']
TOY_TEXT_ENVS = ['Blackjack-v1', 'Taxi-v3', 'CliffWalking-v0', 'FrozenLake-v1']
MUJOCO_ENVS = ['Ant', 'HalfCheetah', 'Hopper', 'Humanoid', 'HumanoidStandup', 'InvertedDoublePendulum', 
               'InvertedPendulum', 'Pusher', 'Reacher', 'Swimmer', 'Walker2d']
MUJOCO_ENVS = [env + '-v5' for env in MUJOCO_ENVS]
ATARI_ENVS = ['Adventure', 'AirRaid', 'Alien', 'Amidar', 'Assault', 'Asterix', 'Asteroids', 'Atlantis', 'Atlantis2', 'Backgammon', 
              'BankHeist', 'BasicMath', 'BattleZone', 'BeamRider', 'Berzerk', 'Blackjack', 'Bowling', 'Boxing', 'Breakout', 'Carnival', 
              'Casino', 'Centipede', 'ChopperCommand', 'CrazyClimber', 'Crossbow', 'Darkchambers', 'Defender', 'DemonAttack', 'DonkeyKong', 'DoubleDunk',
              'Earthworld', 'ElevatorAction', 'Enduro', 'Entombed', 'Et', 'FishingDerby', 'FlagCapture', 'Freeway', 'Frogger', 'Frostbite', 
              'Galaxian', 'Gopher', 'Gravitar', 'Hangman', 'HauntedHouse', 'Hero', 'HumanCannonball', 'IceHockey',  'Jamesbond', 'JourneyEscape', 
              'Kaboom', 'Kangaroo', 'KeystoneKapers', 'KingKong', 'Klax', 'Koolaid', 'Krull', 'KungFuMaster', 'LaserGates', 'LostLuggage',
              'MarioBros', 'MiniatureGolf', 'MontezumaRevenge', 'MrDo', 'MsPacman', 'NameThisGame', 'Othello', 'Pacman', 'Phoenix', 'Pitfall', 
              'Pitfall2', 'Pong', 'Pooyan', 'PrivateEye', 'Qbert', 'Riverraid', 'RoadRunner', 'Robotank', 'Seaquest', 'SirLancelot', 
              'Skiing', 'Solaris', 'SpaceInvaders', 'SpaceWar', 'StarGunner', 'Superman', 'Surround', 'Tennis', 'Tetris', 'TicTacToe3D', 
              'TimePilot', 'Trondead', 'Turmoil', 'Tutankham', 'UpNDown', 'Venture', 'VideoCheckers', 'VideoChess', 'VideoCube', 'VideoPinball', 
              'WizardOfWor', 'WordZapper', 'YarsRevenge', 'Zaxxon']
ATARI_ENVS = ['ALE/' + env + '-v5' for env in ATARI_ENVS]

# Gymnasium Environments
GYMNASIUM_ENVS = {'Classical Control': CLASSICAL_CONTROL_ENVS, 'Box2D': BOX2D_ENVS, 'Toy Text': TOY_TEXT_ENVS, 'MuJoCo': MUJOCO_ENVS, 'Atari': ATARI_ENVS}


### Gymnasium-Robotics Environments from https://robotics.farama.org/index.html (Feb 16, 2024)
FETCH_ENVS = ['FetchPickAndPlace', 'FetchPush', 'FetchReach', 'FetchSlide']
FETCH_ENVS = [env + '-v3' for env in FETCH_ENVS]
SHADOW_DEXTEROUS_HAND_ENVS = ['HandManipulateBlock', 'HandManipulateBlock_ContinuousTouchSensors', 
                              'HandManipulateEgg', 'HandManipulateEgg_ContinuousTouchSensors', 
                              'HandManipulatePen', 'HandManipulatePen_ContinuousTouchSensors', ]
SHADOW_DEXTEROUS_HAND_ENVS = [env + '-v1' for env in SHADOW_DEXTEROUS_HAND_ENVS] + ['HandReach-v2']
MAZE_ENVS = ['AntMaze_UMaze-v5' , 'AntMaze_BigMaze_DG-v5', 'AntMaze_HardestMaze_DGR-v5',
             'PointMaze_UMaze-v3', 'PointMaze_Medium_Diverse_G-v3', 'PointMaze_Large_Diverse_GR-v3']
ADROIT_HAND_ENVS = ['AdroitHandDoor-v1', 'AdroitHandHammer-v1', 'AdroitHandPen-v1', 'AdroitHandRelocate-v1']
FRANKAKITCHEN_ENVS = ['FrankaKitchen-v1']

# Gymnasium-Robotics Environments
GYMNASIUM_ROBOTICS_ENVS = {'Fetch': FETCH_ENVS, 'Shadow Dexterous Hand': SHADOW_DEXTEROUS_HAND_ENVS, 'Maze': MAZE_ENVS, 
                           'Adroit Hand': ADROIT_HAND_ENVS, 'Franka Kitchen': FRANKAKITCHEN_ENVS}
GYMNASIUM_ROBOTICS_ENVS_LIST = [env for envs in GYMNASIUM_ROBOTICS_ENVS.values() for env in envs]


### Domains containing Gymnasium and Gymnasium-Robotics Environments
DOMAINS = {'Gymnasium': GYMNASIUM_ENVS, 'Gymnasium-Robotics': GYMNASIUM_ROBOTICS_ENVS}



def test_environment(env_name, steps, print_flag=False):
    """Test environment by initializing, sampling observation / action, and running a simple experiment"""

    # ALE environments require ale_py
    if env_name in ATARI_ENVS:
        import ale_py
        gym.register_envs(ale_py)

    # Gymnasium-Robotics environments require gymnasium_robotics
    if env_name in GYMNASIUM_ROBOTICS_ENVS_LIST:
        import gymnasium_robotics
        gym.register_envs(gymnasium_robotics)

    # Test: initialize environment
    env = gym.make(env_name)
    if print_flag: 
        print(f"initialize environment {env_name} successfully")

    # Test: sample observation / action
    try: 
        obs_sample = env.observation_space['observation'].sample()
    except TypeError:
        obs_sample = env.observation_space.sample()
    action_sample = env.action_space.sample()

    if print_flag: 
        print("observation:", obs_sample.shape)
        print("action:", action_sample.shape)

    # Test: run simple experiment
    env.reset()
    for _ in range(steps):
        action = env.action_space.sample() 
        observation, reward, terminated, truncated, info = env.step(action)
        if terminated or truncated:
            observation, info = env.reset()
    env.close()


def test_all_environments(domains, steps, print_flag=False):
    """Test all environments in the domains"""

    for domain, subdomains in domains.items():
        for subdomain, envs in subdomains.items():
            print(f"========== {domain}: {subdomain} ==========")

            for env in envs:
                try: 
                    test_environment(env, steps, print_flag)
                    print(f"SUCCESS: {env}")
                except:
                    print(f"FAIL: {env}")
            print()


def test(env_name, domains):
    """Test specific environment or all environments"""

    # default parameters
    steps = 10
    print_flag = False

    # test specific environment or all environments
    if env_name == 'all':
        test_all_environments(domains, steps, print_flag)
    else:
        test_environment(env_name, steps, print_flag)
        print(f"SUCCESS: {env_name}")


def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Test Gymnasium environments.")
    parser.add_argument(
        '--env-id', 
        type=str, 
        default='all', 
        help="Specify the environment ID to test. Default is 'all' to test all environments."
    )
    
    # Parse arguments
    args = parser.parse_args()
    env_name = args.env_id
    test(env_name, DOMAINS)


if __name__ == "__main__":
    main()