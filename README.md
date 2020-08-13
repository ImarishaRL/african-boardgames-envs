**Status:** In development

Imarisha Learning Suite
========================

**Imarisha is a reinforcement learning library for african board games.** The ``Imarisha learning`` suite provides a set of diverse, two-player board game environments that vary widely in complexity.
From Ajua to Fanarona, the learning suite offers environments of increasing complexity for reinforcement learning research. Researchers can use the environments provided as stepping stones when testing the scalability and efficiency of their algorithms on increasingly harder problems.

For more information check out [ImarishaRL](imarisharl.github.io/plartfoms/index/) our site.



Basics
======

The Imarisha learning suite has a gym like interface for interaction.

The following are the ``Env`` methods you
should know:

- `reset(self)`: Reset the environment's state. Returns `observation`.
- `step(self, action)`: Step the environment by one timestep. Returns `observation`, `reward`, `done`, `info`.
- `render(self)`: Render one frame of the environment.

Supported systems
-----------------

We currently support Linux and OS X running Python 3.5 -- 3.8

Installation
============

You can perform a minimal install of ``imarisha`` with:

.. code:: shell

    git clone https://github.com/ImarishaRL/african-boardgames-envs.git
    cd african-boardgames-envs


Environments
============

**Ajua**
See `Ajua_rules.txt` for detailed description of Ajua environment.

**Coming Soon:**

-  `Gulugufe`
-  `Tsoro Yematatu`
-  `Doki`
-  `Senet`
-  `Fanorona`


Example
========

**This example runs a random policy in the ajua environment**

.. code:: python

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

Resources
=========

-  `mail-imarisharl@gmail.com`
-  `imarisharl.github.io/plartfoms/index`

