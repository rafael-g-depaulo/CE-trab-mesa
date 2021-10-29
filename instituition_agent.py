from mesa import Agent
from utils import randomColor

class InstituitionAgent(Agent):
  def __init__(self, unique_id, model, territory):
    super().__init__(unique_id, model)
    self.color = randomColor()
    territory.color = self.color

  def step(self):
    # create campi logic

  def get_neighbors(self):
    neighbors_nodes = self.model.grid.get_neighbors(self.pos, include_center=False)
    print(f'im agent {self.unique_id} and my neighbors are {neighbors_nodes}')
