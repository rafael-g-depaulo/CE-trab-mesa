from mesa import Agent

class TerritoryAgent(Agent):
  def __init__(self, unique_id, model):
    super().__init__(unique_id, model)
    self.id = unique_id

  def step(self):
    # print(f'hi im agent {self.id} and im doing stuff')
    self.get_neighbors()

  def get_neighbors(self):
    neighbors_nodes = self.model.grid.get_neighbors(self.pos, include_center=False)
    print(f'im agent {self.unique_id} and my neighbors are {neighbors_nodes}')
