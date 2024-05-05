
import numpy as np
import pandas as pd
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv(r'C:\Users\Shiv\Documents\Training arc\AI&ML\MACHINE LEARNING\DATASETS\movies.csv')

selected_features = ['genres', 'keywords', 'title', 'tagline', 'cast', 'director', 'spoken_languages']


for feature in selected_features : 
    df[feature] = df[feature].fillna('')



cf = ''
for feature in selected_features: 
    cf += df[feature]


vectorizer = TfidfVectorizer()

features_vectors = vectorizer.fit_transform(cf)

similarity = cosine_similarity(features_vectors)



def suggest_movies(final_movie_input):
      
    list_of_all_titles = df['title'].tolist()
    close_matches_with_input = difflib.get_close_matches(final_movie_input, list_of_all_titles)
    closest_match = close_matches_with_input[0]
    index_of_the_closest_match = df[df.title == closest_match]['index'].values[0]
    similarity_score = list(enumerate(similarity[index_of_the_closest_match]))
    sorted_similar_movies = sorted(similarity_score, key = lambda x:x[1], reverse= True )


    i=1
    recommended_movies = []
    
    for movie in sorted_similar_movies:
        index = movie[0]
        title_from_index = df[df.index == index] ['title'].values[0]
        recommended_movies.append(title_from_index)
        i+= 1 
        if(i==20):
            break

    return recommended_movies


# movie_input = input("Enter your movie : ")
# li = []

# li = suggest_movies(movie_input)
# num = 1
# for i in li:
#     print(f'{num}. {i}')
#     num += 1