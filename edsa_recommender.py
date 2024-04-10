"""

    Streamlit webserver-based Recommender Engine.

    Author: Explore Data Science Academy.

    Note:
    ---------------------------------------------------------------------
    Please follow the instructions provided within the README.md file
    located within the root of this repository for guidance on how to use
    this script correctly.

    NB: !! Do not remove/modify the code delimited by dashes !!

    This application is intended to be partly marked in an automated manner.
    Altering delimited code may result in a mark of 0.
    ---------------------------------------------------------------------

    Description: This file is used to launch a minimal streamlit web
	application. You are expected to extend certain aspects of this script
    and its dependencies as part of your predict project.

	For further help with the Streamlit framework, see:

	https://docs.streamlit.io/en/latest/

"""
# Streamlit dependencies
import streamlit as st

# Data handling dependencies
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
import warnings
import wordcloud
from wordcloud import WordCloud

# Ignore FutureWarning
warnings.simplefilter(action='ignore', category=FutureWarning)

# Custom Libraries
from utils.data_loader import load_movie_titles
from recommenders.collaborative_based import collab_model
from recommenders.content_based import content_model

# Data Loading
# Load necessary datasets
title_list = load_movie_titles('resources/data/movies.csv')  # Load movie titles
gen = pd.read_csv("resources/data/aggregated_rating_streamlit.csv")  # Load aggregated ratings
mov = pd.read_csv("resources/data/movie_details_average.csv")  # Load movie details
pie = pd.read_csv("resources/data/gen_only.csv")  # Load genre data
movie_df = pd.read_csv('resources/data/movie_insights_3.csv')  # Load movie insights
tag_df = pd.read_csv('resources/data/tag_insights.csv')  # Load tag insights
rating_count = pd.read_csv('resources/data/rating_count.csv')  # Load rating counts

# Displaying the logo image
log = "resources/imgs/logo2.jpeg"
#st.image(image, width=200)

cola, mid, colb = st.columns([25, 1, 40])
with mid:
    st.image(log, width=100)

# App declaration
def main():
    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.
    page_options = ["Recommender System", "Instruction & Overview", 'Insights', 'Contact Us']
    with st.sidebar:
        st.image(log, width=250)

    # -------------------------------------------------------------------
    # ----------- !! THIS CODE MUST NOT BE ALTERED !! -------------------
    # -------------------------------------------------------------------
    # Selecting page option from the sidebar
    page_selection = st.sidebar.selectbox("Choose Option", page_options)
    if page_selection == "Recommender System":
        # Header contents
        st.write('# Movie Recommender Engine')
        st.write('### EXPLORE Data Science Academy Unsupervised Predict')
        st.image('resources/imgs/Image_header.png', use_column_width=True)
        # Recommender System algorithm selection
        sys = st.radio("Select an algorithm",
                       ('Content Based Filtering',
                        'Collaborative Based Filtering'))

        # User-based preferences
        st.write('### Enter Your Three Favorite Movies')
        movie_1 = st.selectbox('First Option', title_list[14930:15200])
        movie_2 = st.selectbox('Second Option', title_list[2325:2525])
        movie_3 = st.selectbox('Third Option', title_list[2020:2120])
        fav_movies = [movie_1, movie_2, movie_3]

        # Perform top-10 movie recommendation generation
        if sys == 'Content Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = content_model(movie_list=fav_movies,
                                                            top_n=10)
                    st.title("We think you'll like:")
                    for i, j in enumerate(top_recommendations):
                        st.subheader(str(i + 1) + '. ' + j)
                except:
                    st.error("Oops! Looks like this algorithm doesn't work. "
                             "We'll need to fix it!")

        if sys == 'Collaborative Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = collab_model(movie_list=fav_movies,
                                                           top_n=10)
                    st.title("We think you'll like:")
                    for i, j in enumerate(top_recommendations):
                        st.subheader(str(i + 1) + '. ' + j)
                except:
                    st.error("Oops! Looks like this algorithm doesn't work. "
                             "We'll need to fix it!")

    # -------------------------------------------------------------------

    # ------------- SAFE FOR ALTERING/EXTENSION -------------------
    # Information and instruction page
    if page_selection == "Instruction & Overview":
        # Title and image
        st.title("Welcome to ***Sortify*** Movie Recommender App 🎥🍿")
        st.image("resources/imgs/Movie-Recommendation-System-with-Streamlit-and-Python-ML-1.jpg")
        # Introduction
        st.write("Hi there🙋‍♂️, looking for that nice thing to watch without having to go over the hustle of scrolling for movies? Relax, we've got you.🤗")
        st.write("")
        st.subheader("About the App")
        st.write("This app helps you discover personalized movie recommendations based on your preferences.")
        st.write("On the left of this page you will find a side-bar with a dropdown menu for the pages available, these pages include:")
        st.write("1. **Recommender System** - This is where you will get your recommended movies.")
        st.write("2. **Instruction and Overview** - The current page with the information about how to use this App.")
        st.write("3. **Insights** - This is were you get the insigts about the movies and genres. ")
        st.write("4. **Contact Us** - This page has the App developer team information.")

        # Displaying images in columns
        image_urls = [
            "resources/imgs/free.jpg",
            "resources/imgs/images.jpg",
            "resources/imgs/download.jpg"
        ]
        col1, col2, col3 = st.columns(3)
        image_width = 200
        index = 0
        count_pic = 0 
        while count_pic < 1:
            count_pic += 1
            col1.image(image_urls[index], width=image_width)
            time.sleep(2)  # Change image every 5 seconds
            index = (index + 1) 
            col2.image(image_urls[index], width=image_width)
            time.sleep(2)  # Change image every 5 seconds
            index = (index + 1) 
            col3.image(image_urls[index], width=image_width)
            time.sleep(2)  # Change image every 5 seconds
        st.markdown("<h2 style='text-align: center;'>Yummy Flavors😋...!</h2>", unsafe_allow_html=True)
        # How to use the app section
        st.subheader("How to Use the App")
        st.write("1. Navigate to the 'Recommender System' page.")
        st.write("2. Select the type of filtering (Content-based or Collaborative) for you movie choices.")
        st.write("3. Select you three favourite movies.")
        st.write("4. Press 'Recommend'.")
        st.write("5. Receive personalized movie recommendations based on your favourite movies.")
        st.write("**Content-based filtering** - means your recommended movies will be based on the properties of your three favourite movies.")
        st.write("**Collaborative filtering** - means your recommended movies will be based on other users who have liked your favourite movies.")

    # Insights page
    if page_selection == "Insights":
        # Tabs for different insights
        tab1, tab2, tab3 = st.tabs(["Genres Insights", "Movie Insights", "Other Visuals"])
        with tab1:
            # Checkboxes for genres selection
            col1, col2, col3, col4, col5 = st.columns([10, 10, 15, 10, 10])
            with col1:
                act = st.checkbox("Action")
                war = st.checkbox("War")
                rom = st.checkbox("Romantic")
                com = st.checkbox("Comedy")
            with col2:
                drm = st.checkbox("Drama")
                adv = st.checkbox("Adventure")
                sf = st.checkbox("Sci-fi")
                thr = st.checkbox("Thriller")
            with col3:
                ani = st.checkbox("Animation")
                doc = st.checkbox("Documentary")
                chi = st.checkbox("Children")
                fan = st.checkbox("Fantasy")
            with col4:
                cri = st.checkbox("Crime")
                hor = st.checkbox("Horror")
                mys = st.checkbox("Mystery")
                im = st.checkbox("IMAX")
            with col5:
                mus = st.checkbox("Musical")
                wes = st.checkbox("Western")
                fil = st.checkbox("Film-Noir")

            # Button for exploration
            ls = "True"
            btn = st.button("Explore")

            if btn:
                # Displaying top-ranked movies and genre proportions
                col6, col7 = st.columns([10, 10])
                g_count = pie['genres'].value_counts()
                # Genre selection and corresponding dataframe filtering
                if act:
                    ls = ls + "& gen['Genres'].str.contains(\"Action\")"
                    df_selected_genre = mov[mov['genres'].str.contains("Action")]
                    df_genre_count = df_selected_genre.groupby(df_selected_genre['year'])['genres'].count()
                    highlight_genre = 'Action'
                # Similar blocks for other genres
                ...
                # Displaying selected genre's top ranked movies and genre proportion
                with col6:
                    st.write("<p style='text-align: center;'>Top Ranked Movies</p>", unsafe_allow_html=True)
                    exec("st.write(gen[" + ls + "].sort_values(by=['rating'], ascending=False,ignore_index=True)[['Title']])")
                with col7:
                    st.write("<p style='text-align: center;'>Proportion of the Genre</p>", unsafe_allow_html=True)
                    fig, ax = plt.subplots()
                    ax.pie(g_count.values, labels=g_count.index)
                    highlight_index = g_count.index.tolist().index(highlight_genre)
                    highlighted_wedge = ax.patches[highlight_index]
                    highlighted_wedge.set_edgecolor('white')
                    highlighted_wedge.set_linewidth(3)
                    highlighted_wedge.set_alpha(1)
                    ax.axis('equal')
                    st.pyplot(fig)
                
                # Displaying movies releases per year
                col8, col9 = st.columns([10, 1])
                with col8:
                    st.write("<p style='text-align: center;'>Movies Releases Per Year</p>", unsafe_allow_html=True)
                    st.line_chart(df_genre_count)

        with tab2:
            # Displaying top movies for selected year and detailed information on a searched movie
            ...

        with tab3:
            # Displaying top rated movies for selected year and movies with highest rating count for selected year
            ...

    if page_selection == "Contact Us":
        # Company details and inquiry form
        company_name = "SORTIFY"
        company_address = "123 Street, Johannesburg, South Africa"
        company_phone = "+27 11 555 6666"
        company_email = "sortify@data.com"

        st.subheader("Company Details")
        st.info(f"Name: {company_name}")
        st.info(f"Address: {company_address}")
        st.info(f"Phone: {company_phone}")
        st.info(f"Email: {company_email}")

        st.subheader("Inquiry Form")
        name = st.text_input("Your Email")
        inquiry = st.text_area("Your Inquiry")
        submit_button = st.button("Submit")

        if submit_button:
            # Here you would typically handle the submission of the inquiry
            st.success("Inquiry submitted successfully!")

    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.

# Run the main function
if __name__ == "__main__":
    main()



if __name__ == '__main__':
    main()
