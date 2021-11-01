from mesa import Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid, NetworkGrid
from mesa.datacollection import DataCollector

import networkx as nx
from random import random, randint

from territory_agent import TerritoryAgent
from instituition_agent import InstituitionAgent
from campus_agent import CampusAgent

large_number = 2 ** 15

class InstituitionModel(Model): 
  def __init__(self, territory_num, avgNeighbors, pib_instituition_weight, pop_instituition_weight, pib_variation, pop_variation):
    self.num_agents = territory_num
    self.schedule = RandomActivation(self)
    self.running = True

    self.pib_instituition_weight = pib_instituition_weight
    self.pop_instituition_weight = pop_instituition_weight
    self.pib_variation = pib_variation
    self.pop_variation = pop_variation
    print(f'self.pib_instituition_weight: {self.pib_instituition_weight} self.pop_instituition_weight: {self.pop_instituition_weight} self.pib_variation: {self.pib_variation} self.pop_variation: {self.pop_variation} self.num_agents {self.num_agents}')

    # create grid
    prob = avgNeighbors / territory_num
    self.G = nx.erdos_renyi_graph(n=self.num_agents, p=prob)
    self.grid = NetworkGrid(self.G)

    # Create agents
    for i, node in enumerate(self.G.nodes()):
      # a = TerritoryAgent(i, self, 2, 20000, self.pib_instituition_weight, self.pop_instituition_weight)
      territory = self.createTerritory(i, node)

    # create data collector
    self.datacollector = DataCollector(
      # model_reporters={"Gini": compute_gini},
      # agent_reporters={"Wealth": "wealth"}
    )

  def createTerritory(self, id, node):
    pib_per_capita = randint(500, 35000) if random() < 0.95 else randint(35000, 65000)
    pop_density = randint(10, 24) if random() < 0.70 else randint(24, 7300)
    territory = TerritoryAgent(id, self, pop_density, pib_per_capita, self.pib_instituition_weight, self.pop_instituition_weight, self.pib_variation, self.pop_variation)
    self.schedule.add(territory)
    self.grid.place_agent(territory, node)

  # NOT FINISHED
  # def createInstituition(self, territory):
  #   instituition = InstituitionAgent(large_number + territory.unique_id, self, territory)
  #   self.schedule.add(instituition)
  #   # create first campus of that instituition in that territory
  #   self.createCampus(instituition, territory)
    # print(f'self.num_agents {self.num_agents}.  territory.unique_id {territory.unique_id}, {self.num_agents * 1 + territory.unique_id}')
    # print(f'created instituition {instituition.unique_id} in territory {territory.unique_id}')

  # NOT FINISHED
  def createCampus(self, territory):
    campus = CampusAgent(large_number*2 + self.num_agents * len(territory.campi) + territory.unique_id, self, territory)
    territory.color = "#00FF00"
    self.schedule.add(campus)
    territory.campi.append(campus)


  def step(self):
    self.datacollector.collect(self)
    self.schedule.step()
