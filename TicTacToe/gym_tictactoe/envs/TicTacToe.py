import gym
from gym import error, spaces, utils
from gym.utils import seeding

class TicTacToe(gym.Env):
    metadata = {'render.modes': ['human']}
    
    def __init__(self):
        self.state = []
        for i in range(3):
            self.state += [[]]
            for j in range(3):
                self.state[i] += ["-"]
            #end
        #end
        self.counter = 0
        self.done = 0
        self.add = [0, 0]
        self.reward = 0
    #end
    
    def check(self):
        if self.counter < 5:
            return 0
        #end
        
        for i in range(3):
            if(self.state[i][0] != "-" and self.state[i][1] == self.state[i][0] and self.state[i][1] and self.state[i][1] == self.state[i][2]):
                if self.state[i][0] == "o":
                    return 1
                else:
                    return 2
                #end
            #end
            
            if(self.state[0][i] != "-" and self.state[1][i] == self.state[0][i] and self.state[1][i] == self.state[2][i]):
                if self.state[0][i] == "o":
                    return 1
                else:
                    return 2
                #end
            #end
        #end
        
        if self.state[0][0] != "-" and self.state[1][1] == self.state[0][0] and self.state[1][1] == self.state[2][2]:
            if self.state[0][0] == "o":
                return 1
            else:
                return 2
            #end
        #end
        
        if self.state[0][2] != "-" and self.state[0][2] == self.state[1][1] and self.state[1][1] == self.state[2][0]:
            if self.state[1][1] == "o":
                return 1
            else:
                return 2
            #end
        #end
    #end
    
    def step(self, target):
        if self.done == 1:
            print("Game Over")
            return [self.state, self.reward, self.done, self.add]
        elif self.state[int(target/3)][target%3] != "-":
            print("Invalid step")
            return [self.state, self.reward, self.done, self.add]
        else:
            if self.counter % 2 == 0:
                self.state[int(target/3)][target%3] = "o"
            else:
                self.state[int(target/3)][target%3] = "x"
            #end
            self.counter += 1
            if (self.counter == 9):
                self.done = True
            #end
        #end
        
        win = self.check()
        if win:
            self.done = True
            print("Player ", win, " wins.", sep="", end="\n")
            self.add[win-1] = 1
            if win == 1:
                self.reward = 100
            else:
                self.reward = -100
            #end
        #end
        
        return [self.state, self.reward, self.done, self.add]
    #end
    
    def reset(self):
        for i in range(3):
            for j in range(3):
                self.state[i][j] = "-"
            #end
        #end
        self.counter = 0
        self.done = 0
        self.add = [0,0]
        self.reward = 0
        return self.state
    #end
    
    def render(self):
        for i in range(3):
            for j in range(3):
                print(self.state[i][j], end=" ")
            #end
            print("")
        #end
    #end
    
#end