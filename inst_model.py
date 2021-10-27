# tutorial code from https://mesa.readthedocs.io/en/master/tutorials/intro_tutorial.html

from mesa import Agent, Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid, NetworkGrid
from mesa.datacollection import DataCollector
import networkx as nx

def compute_gini(model):
  agent_wealths = [agent.wealth for agent in model.schedule.agents]
  x = sorted(agent_wealths)
  N = model.num_agents
  B = sum( xi * (N-i) for i,xi in enumerate(x) ) / (N*sum(x))
  return (1 + (1/N) - 2*B)

class MoneyAgent(Agent):
  """ An agent with fixed initial wealth."""
  def __init__(self, unique_id, model):
    super().__init__(unique_id, model)
    self.wealth = 1
    self.id = unique_id

  def step(self):
    print(f'hi im agent {self.id} and im doing stuff')

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
      a = MoneyAgent(i, self)
      self.schedule.add(a)
      # x = self.random.randrange(self.grid.width)
      # y = self.random.randrange(self.grid.height)
      self.grid.place_agent(a, node)

    # create data collector
    self.datacollector = DataCollector(
        model_reporters={"Gini": compute_gini},
        agent_reporters={"Wealth": "wealth"})

  def step(self):
    self.datacollector.collect(self)
    self.schedule.step()
