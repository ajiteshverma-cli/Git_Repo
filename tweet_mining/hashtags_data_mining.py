import os
import click
import tweepy as tw
import pandas as pd
import plotly.figure_factory as ff


consumer_key = "iY3da0W9XGRKBNi8uzxV9WNqJ"
consumer_secret = "mPqe47qGOJHvjs4HJMAW7JFgX291t2ByPZc611bzgzSlszwg4Y"

access_token = "1510345927273369604-9SxrlFB45Fl0TG6BosKCRIYRuZzi7S"
access_token_secret = "UVQqwD4f3NLMyVPLLxBmGcLg5CUOs2pEebLqd8LCQ8B3u"


bearer_token = "AAAAAAAAAAAAAAAAAAAAADZtbAEAAAAATTKit4X2GL0rfOE5I75xgd7D0Ho%3DRxoD2uBIdRJjWNlBTXwLQ8P4waLuuqnCI4izvtpsT7I2gdPlqj"


@click.command()
@click.option('--env', '-e',default="tweet_stats", type=click.Choice(["tweet_stats"],case_sensitive=False),
              prompt='which script to run', help='script to run')
def stats_creator(env):
    """
    ask user for hashtags and then create stats on the basis of that
    """

    if env == "tweet_stats":

        # You can authenticate as your app with just your bearer token
        client = tw.Client(bearer_token=bearer_token)

        # You can provide the consumer key and secret with the access token and access
        # token secret to authenticate as a user
        client = tw.Client(
            consumer_key=consumer_key, consumer_secret=consumer_secret,
            access_token=access_token, access_token_secret=access_token_secret
        )


        auth = tw.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
        api = tw.API(auth)

        try:
            api.verify_credentials()
            print("Authentication OK")
        except BaseException as err:
            print(f"Unexpected// {err=}, {type(err)=}")
            raise

        search_words = click.prompt("add search words like: #globalwarming ")
        fromDate = click.prompt("add the date from which you want to search, for example: 2022-02-22  ")
        remove_retweets = click.prompt("do you want to remove retweets or not, type y for yes, or n for no: ")

        if "y" in remove_retweets:
            actual_search_words = search_words + " -filter:retweets"
        else:
            actual_search_words = search_words

        # using the data provided by user, lets dig in the filthy world of twitter (database of humanity, wow so edgy!)
        tweets = tw.Cursor(api.search_tweets,
                           q=actual_search_words,
                           lang="en", fromDate=fromDate).items(2)

        users_locs = [[tweet.user.screen_name, tweet.user.location] for tweet in tweets]
        tweet_dataframe = pd.DataFrame(data=users_locs,
                                  columns=['user', "location"])

        create_dataframe_table(tweet_dataframe)

        print(tweet_dataframe)


def create_dataframe_table(data_dictionary):
    """
    using provided dictionary it creates html tables
    :return: figure
    """

    # dataframe and plot for run arguments
    df_info = pd.DataFrame(data_dictionary, index=[0])
    fig = ff.create_table(df_info)

    return fig


if __name__ == '__main__':

    #_main function starts
    try:
        stats_creator()
    except Exception as ex:
        print(ex)
        click.pause()
    #_main function ends