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
        self._mesh = st.file_uploader("Upload the simulation data in h5/hdf5 file format.", type=["h5", "hdf5"])

        if self._mesh:
            pass
        else:
            st.info("Please upload the simulation data!")

        return

    def view_dataset(self):
        """ """
        view = st.header("View Dataset")

        if self._mesh:
            dataset = st.multiselect("Select datasets to view", np.array(h5py.File(self._mesh, 'r')), ["point"])
            columns_obj = list(st.columns(len(dataset)))

            for i, col in enumerate(columns_obj):
                with col:
                    col_name = st.caption(dataset[i])
                    df = pd.DataFrame(np.array(h5py.File(self._mesh, 'r')[dataset[i]]))
                    df = st.dataframe(df)
            return
        else:
            st.warning("Please upload the simulation data!")
            pass

    def grid_2D(self):
        """ """
        mesh_geo = st.header("Mesh Geometry")

        if self._mesh:
            node_dataset = st.multiselect("Select the Node dataset.", np.array(h5py.File(self._mesh, 'r')), ["point"])

            nodes = pd.DataFrame(np.array(h5py.File(self._mesh, 'r')[node_dataset[0]]))
            nodes.columns = ["x","y"]

            mesh_trace = go.Mesh3d(x = nodes.x, y = nodes.y, z = np.zeros(nodes.shape[0]), color='lightblue')
            scatter_trace = go.Scatter(x = nodes.x, y = nodes.y, mode="markers", marker_size=4)

            plot_opt = {"Scatter Plot": scatter_trace, "Surface Plot": mesh_trace}

            plot_selection = st.selectbox("Plot Type", list(plot_opt.keys()))
            fig = go.Figure(data=[plot_opt[plot_selection]])

            st.plotly_chart(fig)
            return
        else:
            st.warning("Please upload the simulation data!")
            pass

    def surface_contours(self):
        """ """
        contours_2d = st.header("2D Contour Plot")

        if self._mesh:
            primitive = pd.DataFrame(np.array(h5py.File(self._mesh, 'r')["node_primitive"]))
            nodes = pd.DataFrame(np.array(h5py.File(self._mesh, 'r')["point"]))
            nodes.columns = ["x","y"]

            st.markdown("Enter the index number of Primitive variables in Node Primitive Dataset.")

            col1, col2 = st.columns(2)

            d_idx = col1.number_input("**Density**:", min_value=0, max_value=(primitive.shape[1] - 1), value = 0)
            p_idx = col1.number_input("**Pressure**:", min_value=0, max_value=(primitive.shape[1] - 1), value = 1)
            t_idx = col1.number_input("**Temperature**:", min_value=0, max_value=(primitive.shape[1] - 1), value = 2)

            u_idx = col2.number_input("**U Velocity**:", min_value=0, max_value=(primitive.shape[1] - 1), value = 3)
            v_idx = col2.number_input("**V Velocity**:", min_value=0, max_value=(primitive.shape[1] - 1), value = 4)

            dset_idx_map = {"Density":d_idx, "Pressure":p_idx, "Temperature":t_idx, "U Velocity":u_idx, "V Velocity":v_idx}

            species = st.checkbox("Species")
            if species:
                mf_idx = col2.slider("**Range of Species Mass Fractions** (Not required for IdealGas):", min_value=0, max_value=(primitive.shape[1] - 1), value = (1,2))
                dset_idx_map["Species Mass Fractions"] = mf_idx

            plot_selection = st.multiselect("Plot Variable", list(dset_idx_map.keys()), ["Temperature"])
            col1, col2 = st.columns(2)

            plot = st.button("**Plot**")

            if plot:
                for i, selection in enumerate(plot_selection):
                    if i%2 == 0:
                        col = col1
                    else:
                        col = col2

                    with col:
                        col_name = st.caption(selection + " Contour")

                        contours_trace = go.Contour(z = primitive.iloc[:,dset_idx_map[selection]], x = nodes.x, y = nodes.y, colorscale="Viridis")
                        fig = go.Figure(data=[contours_trace])

                        st.plotly_chart(fig, use_container_width=True)
                return
        else:
            st.warning("Please upload the simulation data!")
            pass

        return


