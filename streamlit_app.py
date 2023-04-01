from app_base import *


DB = DashBoard()

st.set_page_config(page_title="MURPH Analytics",
                   page_icon="📊",
                   layout="wide",
                   menu_items = {"About": "Source: https://github.com/vinay-ram1999/CFD-dashboard \n MURPH Solver: https://github.com/UnstructuredFVM/",
                                 "Report a Bug": "mailto:vinayramgazula@gmail.com"})

st.title("MURPH Analytics")

with st.expander("About", expanded=False):
    st.markdown("This is an interactive dashboard built to post-process and perform different analytical studies on the simulation data generated from the MURPH Solver.")

# sidebar arguments
st.sidebar.title('Menu')

st.sidebar.header("Unstructured")
section = st.sidebar.radio("", ["2D", "3D", "Grid Independence"], label_visibility="collapsed")

if section == "2D":
    # Upload results
    DB.load_simulation_data()

    view, grid, contour = st.tabs(["View Dataset", "Mesh Geometry", "Contour Plot"])

    # View Dataset
    with view:
        df_list = DB.view_dataset()

    # Mesh Geometry
    with grid:
        grid2D = DB.grid_2D()

    # Contour Plot
    with contour:
        contour2D = DB.surface_contours()


if section == "3D":
    st.info("3-D is not implemented yet!!!")


if section == "Grid Independence":
    st.info("Grid Independence is not implemented yet!!!")

