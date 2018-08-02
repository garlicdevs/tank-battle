import collections as cl
import numpy as np
from tankbattle.env.engine import TankBattle
from tankbattle.env.utils import Utils


def machine_control(two_players=False):
    exp_replay = cl.deque(maxlen=1000)
    game = TankBattle(render=True, player1_human_control=False, player2_human_control=False, two_players=two_players,
                      speed=60, debug=True, frame_skip=5)
    num_of_actions = game.get_num_of_actions()
    game.reset()

    # Convert state into grayscale (84, 84)
    state = Utils.process_state(game.get_state())
    
    while True:
        if two_players:
            random_action_p1 = np.random.randint(0, num_of_actions)
            random_action_p2 = np.random.randint(0, num_of_actions)
            reward = game.step(random_action_p1, random_action_p2)
        else:
            random_action = np.random.randint(0, num_of_actions)
            reward = game.step(random_action)

        next_state = Utils.process_state(game.get_state())
        is_terminal = game.is_terminal()

        ####################################################################
        # Put [state, reward, next_state, is_terminal] to experience replay
        exp_replay.append([state, reward, next_state, is_terminal])
        # ...
        ####################################################################

        if is_terminal:
            print("P1 Score:", game.total_score_p1)
            if two_players:
                print("P2 Score:", game.total_score_p2)
            print("Total Score", game.total_score)
            game.reset()
            break


def human_control(two_players=False):

    game = TankBattle(render=True, player1_human_control=True, player2_human_control=True, two_players=two_players,
                      speed=60, debug=True, frame_skip=5)

    print("Press 'Space' to fire and arrow keys to control the tank !")

    game.reset()
    scores = []

    for step in range(100000):
        game.render()

        terminal = game.is_terminal()
        if terminal:
            print("P1 Score:", game.total_score_p1)
            if two_players:
                print("P2 Score:", game.total_score_p2)
            print("Total Score", game.total_score)
            print("Current steps:", step)
            scores.append(game.total_score)
            game.reset()

    print(scores)


if __name__ == '__main__':

    # machine_control()

    human_control()