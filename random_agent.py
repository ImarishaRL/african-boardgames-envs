import numpy as np
import Ajua_env

env = Ajua_env.AJUA()
done = False
steps = 0
agent_1 = 0
agent_2 = 0
while not done:
    steps += 1
    action = np.random.randint(0, 18)
    state, reward, done, _ = env.step(action)
    if env.current_player == 9:
        agent_2 += reward
    else:
        agent_1 += reward
    print("\nAction: ",action, "Player: ", env.current_player, "Reward: ", reward)
    env.render()
print(agent_2, agent_1)