import pandas as pd
from sklearn.cluster import KMeans
from beerapp.models import *
from sklearn.metrics import pairwise_distances_argmin_min


def getRecommendations(favorites, beers):
    # process beers
    brew = preprocessing_df(beers)
    # drop name (rename so that we can retrieve later)
    beer_df = brew.drop(['name'], axis=1)
    # process favorites
    favorites_df = preprocessing_df(favorites)
    favorites_df = favorites_df.drop(['name'], axis=1)
    # get centroids
    centroids = favorites_df.values
    # initialize kmeans model
    kmeans = KMeans(n_clusters=len(centroids), n_init=1, init=centroids)
    kmeans.fit(beer_df)
    # get the drinks most closely related to our favorites
    closest, _ = pairwise_distances_argmin_min(kmeans.cluster_centers_, beer_df)
    recs = []
    # get details for most similar drinks and pass as drink objects back to home page
    for c in closest :
        name = brew.iloc[c, 0]
        drink = Drink.objects.get(name=name)
        recs.append(drink)
        print(drink)
    return recs


def preprocessing_df(beers):
    brews = []
    # create 2d array of values
    for b in beers:
        row = [b.name, b.style, b.category, b.brewer, b.abv, b.bitterness, b.city, b.state, b.country, b.popular]
        brews.append(row)
    df = pd.DataFrame(brews, columns=['name', 'style','category','brewer','abv','bitterness','city','state', 'country', 'popular'])
    # drop na for all columns and convert string columns to categorical to categorical codes
    df['abv'] = df['abv'].fillna(0)
    df['bitterness'] = df['bitterness'].fillna(0)
    df['popular'] = df['popular'].fillna(0)
    df["style"] = df["style"].astype('category').cat.codes
    df["category"] = df["category"].astype('category').cat.codes
    df["brewer"] = df["brewer"].astype('category').cat.codes
    df["city"] = df["city"].astype('category').cat.codes
    df["state"] = df["state"].astype('category').cat.codes
    df["country"] = df["country"].astype('category').cat.codes
    return df

