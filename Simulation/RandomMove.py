import time as t
from Agent.AgentRandomMove import AgentRandomMove


class RandomMove():
    def __init__(self, agent: AgentRandomMove):
        self.agent = agent

    def run(self):
        self.agent.move()
        self.agent.env.root.after(150, self.run)