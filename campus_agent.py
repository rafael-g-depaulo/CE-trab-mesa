from mesa import Agent
from utils import randomColor

from numpy.random import exponential
from math import floor
import random

class CampusAgent(Agent):
  def __init__(self, unique_id, model, territory):
    super().__init__(unique_id, model)
    self.territory = territory
    self.random_factor = exponential()
    self.scientific_production = self.get_production()

  def get_production(self):
    median_scientific_prod = 100
    neighboring_campi = sum([len(territory.campi) for territory in self.territory.get_neighbors()]) + len(self.territory.campi) - 1
    neighboring_scale = 0.02 * neighboring_campi
    self.random_factor += self.random_factor * 0.05 * random.uniform(-1, 1)
    pib_scale = (self.territory.pib_per_capita / 650000)
    scientific_prod = self.random_factor * median_scientific_prod * (1+pib_scale) * (1+neighboring_scale)
    return floor(scientific_prod)

  def step(self):
    self.scientific_production = self.get_production()
