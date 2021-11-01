from mesa import Agent
from utils import randomColor

from numpy.random import exponential
from math import floor
import random

class CampusAgent(Agent):
  def __init__(self, unique_id, model, territory):
    super().__init__(unique_id, model)
    self.territory = territory
    self.scientific_production = self.get_initial_prod()

  def get_initial_prod(self):
    median_scientific_prod = 100
    pib_scale = (self.territory.pib_per_capita / 650000)
    scientific_prod = exponential() * median_scientific_prod * (1+pib_scale)
    return floor(scientific_prod)

  def fluctuate_production(self):
    if (random.random() < 0.2): self.scientific_production += 1
    if (random.random() < 0.2): self.scientific_production -= 1
    if (self.scientific_production < 0): self.scientific_production = 0

  def step(self):
    self.fluctuate_production()
