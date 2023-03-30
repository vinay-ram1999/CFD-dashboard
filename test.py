import h5py
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


path = "./double_ramp.h5"
nodes = pd.DataFrame(np.array(h5py.File(path)["point"]))
nodes.columns = ["x","y"]
# nodes = nodes.sort_values(by="x")

mesh = go.Mesh3d(x=nodes.iloc[:,0], y=nodes.iloc[:,1], z=np.zeros(nodes.shape[0]), color='lightblue')
mesh = go.Scatter(x=nodes.iloc[:,0], y=nodes.iloc[:,1], mode="markers", marker_size=4)

fig = go.Figure(data=[mesh])
fig.show()

cells = pd.DataFrame(np.array(h5py.File(path)["cell_node_map"]))
cells.columns = ["l","b","r","t"]

