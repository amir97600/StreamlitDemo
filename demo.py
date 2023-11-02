#Importations
import streamlit as st
from st_speckmol import spec_plot
import glob

st.set_page_config(layout='wide')
st.markdown(
 '''# st-speckmol :package:
_A Streamlit **Component** for creating Speck molecular structures within Streamlit Web app._'''
    
    )

x_files =  glob.glob("*.xyz")
with st.sidebar:
    ex_xyz = st.selectbox('Select a molecule',x_files)
    f = open(ex_xyz,"r")
    ex_xyz = f.read()
    #st.write(ex_xyz)




#Features
with st.sidebar.expander("Parameters",expanded=True):
    outl = st.checkbox('Outline',value=True)
    bond = st.checkbox('Bond',value=True)
    bond_scale = st.slider('BondScale',min_value=0.0,max_value=1.0,value=0.8)
    brightness = st.slider('Brightness',min_value=0.0,max_value=1.0,value=0.4)
    relativeAtomScale = st.slider('RelativeAtomScale',min_value=0.0,max_value=1.0,value=0.64)
    bondShade = st.slider('bondShade',min_value=0.0,max_value=1.0,value=0.5)

_PARAMETERS = { 'outline': outl, 'bondScale': bond_scale,
                'bonds': bond, 'bondShade': bondShade,
                'brightness': brightness, 'relativeAtomScale': relativeAtomScale,}

res = spec_plot(ex_xyz,wbox_height="800px",wbox_width="800px",scroll=True,_PARAMETERS = _PARAMETERS)
