import pandas as pd
import pickle
from surprise import Dataset
from surprise import Reader
from surprise import KNNWithMeans
from surprise.model_selection import train_test_split
from surprise import accuracy
from collections import defaultdict
from surprise.model_selection import GridSearchCV

# load anime titles into an array for access
with open("../animeList.csv", "r", encoding="utf-8") as f:
    animes = f.readlines()[0].split(",")

"""
ratings_dict = {
    "anime": [1, 2, 1, 2, 1, 2, 1, 2, 1],
    "user": ['A', 'A', 'B', 'B', 'C', 'C', 'D', 'D', 'E'],
    "rating": [1, 2, 2, 4, 2.5, 4, 4.5, 5, 3],
}
"""

ratingsDict = defaultdict(list)

# import score data into a dictionary
with open("../animeScores.csv", "r", encoding="utf-8") as scores:
    rows = scores.readlines()
    count = 0

    for user, userRatings in enumerate(rows):
        count += 1
        userRatings = userRatings.split(",")
        #print(count)

        for animeIndex, rating in enumerate(userRatings):
            rating = int(rating)

            if animeIndex < len(animes) and rating != 0:
                title = animes[animeIndex]

                ratingsDict["anime"] += [title]
                ratingsDict["user"] += [user]
                ratingsDict["rating"] += [rating]

    print("done")

df = pd.DataFrame(ratingsDict)
reader = Reader(rating_scale=(1, 10))

# Loads Pandas dataframe
data = Dataset.load_from_df(df[["user", "anime", "rating"]], reader)

# Perform the train-test split
trainset, testset = train_test_split(data, test_size=0.2, random_state=42)

sim_options = {
    "name": "msd",
    "min_support": 3,
    "user_based": False  # Compute  similarities between items
}

algo = KNNWithMeans(sim_options=sim_options)

#trainingSet = data.build_full_trainset()

algo.fit(trainset)

predictions = algo.test(testset)

# Calculate RMSE (Root Mean Squared Error)
rmse = accuracy.rmse(predictions)
print(f'RMSE: {rmse}')

# Calculate MAE (Mean Absolute Error)
mae = accuracy.mae(predictions)
print(f'MAE: {mae}')


"""
# To use item-based cosine similarity
sim_options = {
    "name": ["msd", "cosine"],
    "min_support": [3, 4, 5],
    "user_based": [False, True],
}

param_grid = {"sim_options": sim_options}

gs = GridSearchCV(KNNWithMeans, param_grid, measures=["rmse", "mae"], cv=3)
gs.fit(data)

print(gs.best_score["rmse"])
print(gs.best_params["rmse"])
"""


with open('recommender.pkl', 'wb') as f:  # open a text file
   pickle.dump(algo, f) # serialize the list
