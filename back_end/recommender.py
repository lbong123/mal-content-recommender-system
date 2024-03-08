import pandas as pd
import pickle
from surprise import Dataset
from surprise import Reader
from surprise import KNNWithMeans

# This is the same data that was plotted for similarity earlier
# with one new user "E" who has rated only movie 1
ratings_dict = {
    "anime": [1, 2, 1, 2, 1, 2, 1, 2, 1],
    "user": ['A', 'A', 'B', 'B', 'C', 'C', 'D', 'D', 'E'],
    "rating": [1, 2, 2, 4, 2.5, 4, 4.5, 5, 3],
}

df = pd.DataFrame(ratings_dict)
reader = Reader(rating_scale=(1, 5))

# Loads Pandas dataframe
data = Dataset.load_from_df(df[["user", "anime", "rating"]], reader)

# To use item-based cosine similarity
sim_options = {
    "name": "cosine",
    "user_based": False,  # Compute  similarities between items
}

algo = KNNWithMeans(sim_options=sim_options)

trainingSet = data.build_full_trainset()

algo.fit(trainingSet)

with open('recommender.pkl', 'wb') as f:  # open a text file
    pickle.dump(algo, f) # serialize the list