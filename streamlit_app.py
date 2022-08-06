import streamlit
import pandas

streamlit.title("my parents healthy food")
streamlit.header(" breakfast menu")
streamlit.text('doss sambar vadai')
streamlit.text('rice dal sambar')
streamlit.text('idl samba chutney')

streamlit.header("favorite Food")
streamlit.text('🥣 soup') 
streamlit.text ('🥗 spinach')
streamlit.text("🐔 chicken")
streamlit.text('🥑 avacado')
streamlit.text('🍞 bread')

streamlit.header("🍌🥭Special menu item 🥝🍇")
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index)['Avacado'])
streamlit.dataframe(my_fruit_list)

