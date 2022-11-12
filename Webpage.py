import streamlit as st
from streamlit_option_menu import option_menu
st.set_page_config(layout="wide")
st.title('Villum Center for Hybrid Quantum Materials and Devices')


selected=option_menu('',['Group members','Facilities','Publications','Gallery','Openings'],orientation='horizontal')
if selected=='Group members':
    
    st.header('Principal Investigators')
    st.subheader('Prof. Yong P. Chen')
    col1,col2=st.columns([4,30])

    with col1:
        st.image('chen.png',width=120)
    with col2:
        st.markdown('My lab exploits quantum physics to manipulate electrons, \
        atoms, spins and photons in various materials and artificial systems, with the aim to uncover \
        novel quantum phenomena and new states of matter, and to explore applications in quantum devices\
        (such as quantum information and quantum computation devices), nanotechnology (such as nanoelectronics \
        and nanosensors) and energy.')
        st.markdown('[Google Scholar](https://scholar.google.com/citations?user=9EBAemEAAAAJ&hl=en)')

        st.markdown('**Email**: <yongchen@phys.au.dk>')
    



    st.subheader('Dr. Richard Balog')
    col1,col2=st.columns([4,30])

    with col1:
        st.image('richard.png',width=120)
    with col2:
        st.markdown('My expertise in surface science and in particular my research activities\
        related to understanding and controlling reactions in molecular ices induced by electrons, as well as reactions\
        at surfaces and interfaces induced by atomic species will help shed light on how complex molecules are formed in\
        ultra-cold interstellar space. The experiments will be performed using a Createc type LT-STM setup situated at the\
        Interdisciplinary Nanoscience Center (iNANO). ')
        st.markdown('[Google Scholar](https://scholar.google.com/citations?user=xSJAvTkAAAAJ&hl=en)')
        st.markdown('**Email**: <balog@phys.au.dk>')
    
    st.markdown('---')
