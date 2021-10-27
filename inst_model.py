from mesa import Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid, NetworkGrid
from mesa.datacollection import DataCollector
import networkx as nx

from territory_agent import TerritoryAgent

class InstituitionModel(Model): 
  def __init__(self, N, width, height, avgNeighbors=3):
    self.num_agents = N
    # self.grid = MultiGrid(width, height, True)
    self.schedule = RandomActivation(self)
    self.running = True

    # create grid
    prob = avgNeighbors / N
    self.G = nx.erdos_renyi_graph(n=self.num_agents, p=prob)
    self.grid = NetworkGrid(self.G)

    # Create agents
    for i, node in enumerate(self.G.nodes()):
      a = TerritoryAgent(i, self)
      self.schedule.add(a)
      # x = self.random.randrange(self.grid.width)
      # y = self.random.randrange(self.grid.height)
      self.grid.place_agent(a, node)

    # create data collector
    self.datacollector = DataCollector(
      # model_reporters={"Gini": compute_gini},
      # agent_reporters={"Wealth": "wealth"}
    )

  def step(self):
    self.datacollector.collect(self)
    self.schedule.step()
