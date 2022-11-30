import tweepy
import json

consumer_key = "LBAKpozEPGi5wugMAN9oknkML"
consumer_secret = "NEeoGxCYxS3WDeddAmrbil1MX1PB0WWSvUCobEgj9yeOT6OJgz"
access_token = "105985980-4Y268lHivmTEOwM36a4TiPRLWF3KdBntBtXNafga"
access_token_secret = "TpAXU7vNEw9AHWhCzZhCbCvwvQPxNiopELvDE62I1vtlD"

auth=tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

lista_tweets=api.search_tweets(q="TheBatman", result_type='recent', lang="es", count=100)
lista_tweets_json=[]
print("inicio de generar archivo")
with open('archivotweetsjson.json','w') as file:
    for tweet in lista_tweets:
        lista_tweets_json.append(tweet._json)
        json.dump(lista_tweets_json, file, indent=3)

print("fin de generar archivo")