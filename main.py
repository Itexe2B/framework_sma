from Agent.AgentRandomMove import AgentRandomMove
from Environnement.Bloc.AgentGraphic import AgentGraphic
from Environnement.PathFinding.MapSimple import MapSimple
import time as t

from Norms.AgentCannotMoveOnWall import AgentCannotMoveOnWall
from Simulation.RandomMove import RandomMove

map = MapSimple()
agent = AgentRandomMove(map)
AgentCannotMoveOnWall(map)

#map.root.after_idle(RandomMove(agent).run)
map.root.mainloop()
