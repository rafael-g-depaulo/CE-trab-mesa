from inst_model import InstituitionModel
from visualization import visualization

from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.UserParam import UserSettableParameter

model = InstituitionModel

model_params = {
  "territory_num": 15,
  "avgNeighbors": 2
}

model_name = "InstituitionModel"

server = ModularServer(model, visualization, model_name, model_params)
server.port = 8521
