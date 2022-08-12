import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

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
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Banana'])

def get_fruitvice_data(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
  fruityvice_normalized=pandas.json_normalize(fruityvice_response.json())
  streamlit.dataframe(fruityvice_normalized)
streamlit.header("Fruityvice Fruit Advice!")
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
  if not fruit_choice:
    streamlit.error("please select a fruit to get information")
  else:
    back_from_funtion= get_fruitvice_data(fruit_choice)
    streamlit.dataframe(back_from_funtion)
except URLError as e:
  streamlit.error()
  
streamlit.write('The user entered ', fruit_choice)

fruits_to_show = my_fruit_list.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)
streamlit.stop()
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_row = my_cur.fetchone()
my_data_rows =my_cur.fetchall()
streamlit.header("the fruit load list contains:")
streamlit.dataframe(my_data_rows)

add_my_fruit = streamlit.text_input('What fruit would you like to add?','jackfruit')
my_cur.execute("insert into fruit_load_list_values ('from streamlit')")
