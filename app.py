from app_base import *


DB = DashBoard()

st.set_page_config(layout="wide")

st.title("MURPH Dashboard")

with st.expander('About this app'):
    st.markdown("This is an interactive dashboard built to post-process the simulation data generated from the MURPH Solver.")

# sidebar arguments
st.sidebar.title('Menu')

unstructured = st.sidebar.header("Unstructured")

mesh_2d = st.sidebar.checkbox("2D")
mesh_3d = st.sidebar.checkbox("3D")
grid_ind = st.sidebar.checkbox("Grid Independence")

if mesh_2d:
    # Upload results
    DB.load_simulation_data()

    # View Dataset
    df = DB.view_dataset

    # Mesh Geometry
    DB.Grid_2D()

    contours = st.checkbox("Contour Plot")
    if contours:
        st.info("Not implemented yet!!!")

elif mesh_3d:
    st.info("3-D is not implemented yet!!!")

elif grid_ind:
    st.info("Grid Independence is not implemented yet!!!")

