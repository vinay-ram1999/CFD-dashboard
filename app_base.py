import h5py
import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt
import plotly.graph_objects as go


class DashBoard(object):

    def __init__(self):
        return

    def load_simulation_data(self):
        self._mesh = st.file_uploader("Upload the simulation data in .h5 file format!", type=["h5", "hdf5"])

        if self._mesh:
            pass
        else:
            st.info("Please upload the simulation data.")

        return

    @property
    def view_dataset(self):
        view = st.checkbox("View Dataset")

        if view:
            dataset = st.selectbox("Select a dataset", np.array(h5py.File(self._mesh, 'r')))
            df = pd.DataFrame(np.array(h5py.File(self._mesh, 'r')[dataset]))
            return st.dataframe(df)

    @property
    def plotGrid_2D(self):
        return

    def Grid_2D(self):
        """ """
        mesh_geo = st.checkbox("Mesh Geometry")

        if mesh_geo:
            st.header("Mesh Geometry")

            node_dataset = st.multiselect("Select the Node dataset.", np.array(h5py.File(self._mesh, 'r')), ["point"])

            nodes = pd.DataFrame(np.array(h5py.File(self._mesh, 'r')[node_dataset[0]]))
            nodes.columns = ["x","y"]

            mesh_trace = go.Mesh3d(x=nodes.iloc[:,0], y=nodes.iloc[:,1], z=np.zeros(nodes.shape[0]), color='lightblue')
            scatter_trace = go.Scatter(x=nodes.iloc[:,0], y=nodes.iloc[:,1], mode="markers", marker_size=4)

            plot_opt = {"scatter plot": scatter_trace, "surface plot": mesh_trace}

            plot_selection = st.selectbox("Plot Type", list(plot_opt.keys()))

            fig = go.Figure(data=[plot_opt[plot_selection]])
            st.plotly_chart(fig)

        return
