from mesa import Agent
from random import uniform

class TerritoryAgent(Agent):
  def __init__(self, unique_id, model, pop_density, pib_per_capita, pib_instituition_weight, pop_instituition_weight, pib_variation, pop_variation):
    super().__init__(unique_id, model)
    self.pop_density = pop_density
    self.pib_per_capita = pib_per_capita
    self.pib_instituition_weight = pib_instituition_weight
    self.pop_instituition_weight = pop_instituition_weight
    self.pib_variation = pib_variation
    self.pop_variation = pop_variation
    self.campi = None
    self.color = None

  def step(self):
    self.get_neighbors()
    self.pop_density += self.pop_density * self.pop_variation * uniform(-1, 1)
    self.pib_per_capita += self.pop_density * self.pib_per_capita * uniform(-1, 1)

  def should_create_instituition(self):
    instituition_creation_threshold = 200000
    should_create_instituition = (pop_density * pop_instituition_weight + pib_per_capita * pib_instituition_weight) > instituition_creation_threshold
    if (should_create_instituition and self.campi == None):
      self.model.createInstituition(self)

  def get_neighbors(self):
    neighbors_nodes = self.model.grid.get_neighbors(self.pos, include_center=False)
    print(f'im agent {self.unique_id} and my neighbors are {neighbors_nodes}')
