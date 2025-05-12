import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

st.set_page_config(layout='wide')

st.sidebar.title('Data Visualization of Bangladesh')

final_df = pd.read_csv("Merged_Data.csv")

list_of_divisions=final_df["Division"].unique().tolist()
list_of_divisions.insert(0,"Overall Bangladesh")

selected_division=st.sidebar.selectbox('Select a Division',list_of_divisions)

primary = st.sidebar.selectbox('Select Primary Parameter',sorted(final_df.columns[4:]))
secondary = st.sidebar.selectbox('Select Secondary Parameter',sorted(final_df.columns[4:]))
plot = st.sidebar.button('Plot Graph')


if plot:

    st.markdown("<h1 style='text-align: center; color: #D3D3D3;'>Bubble Size represents the primary parameter</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; color: #D3D3D3;'>Color represents the secondary parameter</h2>", unsafe_allow_html=True)

    if selected_division == 'Overall Bangladesh':
        # plot for india
        fig = px.scatter_mapbox(final_df, lat="lat", lon="long", size=primary, color=secondary, zoom=5.7,size_max=35,
                                mapbox_style="carto-positron",width=1200,height=700,hover_name='District')

        st.plotly_chart(fig,use_container_width=True)
    else:
        # plot for state
        division_df = final_df[final_df['Division'] == selected_division]

        fig = px.scatter_mapbox(division_df, lat="lat", lon="long", size=primary, color=secondary, zoom=5.6,size_max=35,
                                mapbox_style="carto-positron",width=1200,height=700,hover_name='District')

        st.plotly_chart(fig, use_container_width=True)

