from flask import Flask, redirect, render_template, request, url_for

import helpers
import os
import sys
from analyzer import Analyzer

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search")
def search():

    # validate screen_name
    screen_name = request.args.get("screen_name", "").lstrip("@")
    if not screen_name:
        return redirect(url_for("index"))

    # get screen_name's tweets
    tweets = helpers.get_user_timeline(screen_name)
    if type(tweets) is not list:
        return redirect(url_for("index"))

    # absolute paths to lists
    positives = os.path.join(sys.path[0], "positive-words.txt")
    negatives = os.path.join(sys.path[0], "negative-words.txt")

    # instantiate analyzer
    analyzer = Analyzer(positives, negatives)


    # TODO

    positive, negative, neutral = 0.0, 0.0, 0.0



    for tweet in tweets[:100]:
        scorePerTweet = analyzer.analyze(tweet)
        if scorePerTweet > 0.0:
            positive += 1
        elif scorePerTweet < 0.0:
            negative += 1
        else:
            neutral += 1

    # if less than 100 tweets in account, work out new percentage
    if len(tweets) < 100:
        totalTweets = positive + negative + neutral
        positive = (positive/totalTweets)*100
        negative = (negative/totalTweets)*100
        neutral = (neutral/totalTweets)*100

    # generate chart
    chart = helpers.chart(positive, negative, neutral)

    # render results
    return render_template("search.html", chart=chart, screen_name=screen_name)
