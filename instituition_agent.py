from mesa import Agent
from utils import randomColor
import random

# NOT FINISHED
class InstituitionAgent(Agent):
  def __init__(self, unique_id, model, territory):
    super().__init__(unique_id, model)
    self.color = randomColor()
    self.territory = territory
    territory.color = self.color

  def step(self):
    # create campi logic
    # print(f'o porra')
    self.should_create_campus()

  def should_create_campus(self):
    campus_creation_threshold = 1.0
    should_create_capus = (2 ** (1 / (self.territory.pop_density * self.territory.pib_per_capita))) - random.uniform(-0.000005, 0.0000015)
    print("A: ")
    print(should_create_capus)
    if (should_create_capus < campus_creation_threshold):
      print('NEW CAMPUS CREATED')
      self.model.createCampus(self, self.territory)

  # def createCampus(self):
    # 
