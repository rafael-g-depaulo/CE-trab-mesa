from mesa import Agent

class TerritoryAgent(Agent):
  def __init__(self, unique_id, model, pop_density, pib_per_capita, pib_instituition_weight, pop_instituition_weight):
    super().__init__(unique_id, model)
    self.pop_density = pop_density
    self.pib_per_capita = pib_per_capita
    self.pib_instituition_weight = pib_instituition_weight
    self.pop_instituition_weight = pop_instituition_weight

  def step(self):
    self.get_neighbors()

  def get_neighbors(self):
    neighbors_nodes = self.model.grid.get_neighbors(self.pos, include_center=False)
    print(f'im agent {self.unique_id} and my neighbors are {neighbors_nodes}')
