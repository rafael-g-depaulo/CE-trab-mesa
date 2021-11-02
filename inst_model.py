import csv

from mesa import Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid, NetworkGrid
from mesa.datacollection import DataCollector

import networkx as nx
from random import random, randint

from territory_agent import TerritoryAgent
from campus_agent import CampusAgent

large_number = 2 ** 15

def campi_count(model):
  c = sum([len(territory.campi) for territory in model.territories])
  return c

def production_count(model):
  c = sum([sum(map(lambda x: x.scientific_production, territory.campi)) for territory in model.territories])
  return c


class InstituitionModel(Model): 
  def __init__(self, territory_num, avgNeighbors, pib_instituition_weight, pop_instituition_weight, pib_variation, pop_variation):
    self.num_agents = territory_num
    self.schedule = RandomActivation(self)
    self.running = True

    self.pib_instituition_weight = pib_instituition_weight
    self.pop_instituition_weight = pop_instituition_weight
    self.pib_variation = pib_variation
    self.pop_variation = pop_variation
    self.territories = []

    # create grid
    prob = avgNeighbors / territory_num
    self.G = nx.erdos_renyi_graph(n=self.num_agents, p=prob)
    self.grid = NetworkGrid(self.G)

    # Create agents
    for i, node in enumerate(self.G.nodes()):
      self.createTerritory(i, node)

    # create data collector
    self.datacollector = DataCollector(
      {
        "Campi":  campi_count,
        "Production": production_count,
        # "Um Campus":  number_susceptible,
        # "Dois Campi": number_resistant,
        # "Mais que 2 Campi": number_resistant,
      }
    )

  # create a territory
  def createTerritory(self, id, node):
    pib_per_capita = randint(500, 35000) if random() < 0.95 else randint(35000, 65000)
    pop_density = randint(10, 24) if random() < 0.70 else randint(24, 7300)
    territory = TerritoryAgent(id, self, pop_density, pib_per_capita, self.pib_instituition_weight, self.pop_instituition_weight, self.pib_variation, self.pop_variation)
    self.schedule.add(territory)
    self.grid.place_agent(territory, node)
    self.territories.append(territory)
    return territory

  # export ppc, pop density and scientific production of all territories to a csv file
  def exportToCsv(self, filename):
    with open(filename, 'w', newline='') as myfile:
      wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
      wr.writerow(["id", "pib per capita", "densidade populacional", "producao cientifica"])
      for territorio in self.territories:
        prod_scient = sum(map(lambda campus: campus.scientific_production, territorio.campi))
        wr.writerow([territorio.unique_id, territorio.pib_per_capita, territorio.pop_density, prod_scient])

  # create a campus in a territory
  def createCampus(self, territory):
    campus = CampusAgent(large_number*2 + self.num_agents * len(territory.campi) + territory.unique_id, self, territory)
    territory.color = "#00FF00"
    self.schedule.add(campus)
    territory.campi.append(campus)

  def step(self):
    self.datacollector.collect(self)
    self.schedule.step()
    self.exportToCsv("./test.csv")
