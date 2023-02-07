from Environnement.Bloc.Case import Case
from Environnement.Bloc.Wall import Wall
from Norms.Norm import Norm


class AgentCannotMoveOnWall(Norm):

    desc = 'Agent cannot move on wall'
    def __init__(self, env):
        super().__init__(env)
        self.env.addNorm(self)

    def __is_wall(self, x, y):
        return isinstance(self.env.mapObject[x][y], Wall)

    def check(self, **kwargs):
        next_x, next_y = kwargs['next_x'], kwargs['next_y']
        return not self.__is_wall(next_x, next_y)
