from flask import Flask, render_template, request
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

movies = pd.read_csv("movies.csv")

cv = CountVectorizer()

vectors = cv.fit_transform(movies["genre"])

similarity = cosine_similarity(vectors)


def recommend(movie_name):

    if movie_name not in movies["title"].values:
        return []

    index = movies[movies["title"] == movie_name].index[0]

    distances = list(enumerate(similarity[index]))

    movies_list = sorted(distances, key=lambda x: x[1], reverse=True)[1:6]

    recommendations = []

    for i in movies_list:
        recommendations.append(movies.iloc[i[0]].title)

    return recommendations


@app.route("/", methods=["GET", "POST"])
def home():

    recs = []

    if request.method == "POST":

        movie = request.form["movie"]

        recs = recommend(movie)

    return render_template(
        "index.html",
        movies=movies["title"].tolist(),
        recommendations=recs
    )


if __name__ == "__main__":
    app.run(debug=True)