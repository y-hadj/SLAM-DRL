import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
from GDAM_env import ImplementEnv
from GDAM_args import d_args

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

class ActorNetwork(nn.Module):
    def __init__(self):
        super(ActorNetwork, self).__init__()
        self.layer1 = nn.Linear(24, 800)
        self.layer2 = nn.Linear(800, 600)
        self.layer3 = nn.Linear(600, 2)

    def forward(self, x):
        x = torch.relu(self.layer1(x))
        x = torch.relu(self.layer2(x))
        out = torch.tanh(self.layer3(x))
        return out

def test(env, actor):
  while True:
        action = torch.zeros(2)
        s2, toGoal = env.step(action.numpy())
        s = np.append(s2, toGoal)
        s = np.append(s, action.numpy())

        while True:
            s_tensor = torch.from_numpy(np.array([s], dtype=np.float32))
            a = actor(s_tensor).detach().numpy()
            a_in = a
            a_in[0,0] = (a_in[0,0] + 1) / 4
            s2, toGoal = env.step(a_in[0])
         
            s = np.append(s2, a[0])
            s = np.append(s, toGoal)
            # print(s)

def main(env):
    print(1)

    actor = ActorNetwork()

   
    # a_net_params = list(actor.parameters())


    # for idx, param in enumerate(a_net_params):
    #     print("  var {:3}: {:15}   {}".format(idx, str(param.size()), param))

    checkpoint = torch.load("./pytorch_models/TD3_velodyne_actor.pth", map_location=device)
    actor.load_state_dict(checkpoint, strict=False)

    test(env, actor)

env = ImplementEnv(d_args)
main(env)