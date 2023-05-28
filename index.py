import streamlit
import pandas

streamlit.title("Tammy's New Healthy Meal")

streamlit.header('🍽️Breakfast Menu')
streamlit.text('🥣Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔🥚Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞Avacardo Toast')

streamlit.header('🍌🥭🥝🍇 Build Your Own Fruit Smoothie')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

my_fruit_list=my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include and store the selected fruits details in fruits_to_show variable
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(fruits_to_show)