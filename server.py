from inst_model import InstituitionModel, compute_gini

from mesa.batchrunner import BatchRunner
from mesa.visualization.ModularVisualization import ModularServer

import matplotlib.pyplot as plt
import numpy as np



from matplotlib.colors import ListedColormap, LinearSegmentedColormap




fixed_params = {
  "width": 10,
  "height": 10
}

variable_params = {
  "N": range(10, 500, 10)
}

model = InstituitionModel

model_params = {
  "N": 100,
  "width": 10,
  "height": 10
}

model_name = "InstituitionModel"



# 
# 
# 
# 
# 
# 
# 

cmap = ListedColormap(["lightblue", "orange", "green",])

def plot_grid(model,fig,layout='spring',title=''):
  graph = model.G
  if layout == 'kamada-kawai':      
    pos = nx.kamada_kawai_layout(graph)  
  elif layout == 'circular':
    pos = nx.circular_layout(graph)
  else:
    pos = nx.spring_layout(graph, iterations=5, seed=8)  
  plt.clf()
  ax=fig.add_subplot()
  states = [int(i.state) for i in model.grid.get_all_cell_contents()]
  colors = [cmap(i) for i in states]

  nx.draw(graph, pos, node_size=100, edge_color='gray', node_color=colors, #with_labels=True,
          alpha=0.9,font_size=14,ax=ax)
  ax.set_title(title)
  return


fig,ax=plt.subplots(1,1,figsize=(16,10))
f=plot_grid(model,fig,layout='kamada-kawai')

# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 

mesa_server = ModularServer(model, [f], model_name, model_params)
mesa_server.port = 8521
# mesa_server.launch()


# batch_run = BatchRunner(
#   model,
#   variable_params,
#   fixed_params,
#   iterations=5,
#   max_steps=100,
#   # model_reporters={"Gini": compute_gini}
# )

# batch_run.run_all()

# run_data = batch_run.get_model_vars_dataframe()
# run_data.head()
# plt.scatter(run_data.N, run_data.Gini)

# plt.show()
