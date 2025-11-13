import streamlit as st
import pandas as pd
import math
from pathlib import Path
import requests

# Set the title and favicon that appear in the Browser's tab bar.
st.set_page_config(
    page_title='EVE',
    page_icon='https://wiki.eveuniversity.org/File:Icon_ISIS_Exploration.png', # This is an emoji shortcode. Could be a URL too.
)


@st.cache_data
def get_plex_price():
    url = "https://evetycoon.com/api/v1/market/orders/44992"
    r = requests.get(url)
    data = r.json()
    df = pd.DataFrame(data['orders'])
    plex_price =df[~df.isBuyOrder].price.min()
    return plex_price


plex_price = get_plex_price()
st.metric(label="PLEX", value=plex_price)

 t.markdown("[![Click me](app/static/plex.png)](https://streamlit.io)")