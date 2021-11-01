from mesa import Agent
from random import uniform, random

class TerritoryAgent(Agent):
  def __init__(self, unique_id, model, pop_density, pib_per_capita, pib_instituition_weight, pop_instituition_weight, pib_variation, pop_variation):
    super().__init__(unique_id, model)
    self.pop_density = pop_density
    self.pib_per_capita = pib_per_capita
    self.pib_instituition_weight = pib_instituition_weight
    self.pop_instituition_weight = pop_instituition_weight
    self.pib_variation = pib_variation
    self.pop_variation = pop_variation
    self.campi = []
    self.color = None

  def step(self):
    self.get_neighbors()
    self.pop_density += self.pop_density * self.pop_variation * uniform(-1, 1)
    self.pib_per_capita += self.pib_per_capita * self.pib_variation * uniform(-1, 1)
    self.should_create_campus()

  def should_create_campus(self):
    campus_creation_threshold = 1.0
    should_create_capus = (2 ** (((len(self.campi)**3)+1) / (self.pop_density * self.pib_per_capita))) - uniform(-0.00015, 0.0000015)
    # print("A: ")
    # print(should_create_capus)
    if (should_create_capus < campus_creation_threshold):
      # print('NEW CAMPUS CREATED')
      self.model.createCampus(self)


  def get_neighbors(self):
    neighbors_nodes = self.model.grid.get_neighbors(self.pos, include_center=False)
    # print(f'im agent {self.unique_id} and my neighbors are {neighbors_nodes}')
