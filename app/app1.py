import streamlit as st
import snscrape.modules.twitter as sntwitter
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import time
import re
from subprocess import call
import os

import nltk
from wordcloud import WordCloud
from nltk.corpus import stopwords
st.title("Application pour l'analyse en temps réel des tweets")
st.markdown("*Cette application a été réalisée par Josué AFOUDA*")

#call("python collector.py"+" "+"-t"+" "+str(tag), shell=True)
#cmd = "python collector.py"+" "+"-t"+" "+str(tag)
#os.system(cmd)


def scrapetweet(tag):
    # On peut récupérer plusieurs attributs du tweet
    tag=tag
    tweets = []
    limit = 120

    #for tweet in sntwitter.TwitterSearchScraper(str(tag+" "+'near:'+'"'+country+'"')).get_items():
    for tweet in sntwitter.TwitterSearchScraper(tag).get_items():

        # print(vars(tweet))
        # break
        if len(tweets) == limit:
            break
        else:
            tweets.append([tweet.date, tweet.user.username, tweet.renderedContent, 
						   tweet.user.description, tweet.content, tweet.user.followersCount, 
						   tweet.likeCount, tweet.retweetCount, tweet.replyCount, 
						   tweet.user.friendsCount, tweet.user.location])

    df = pd.DataFrame.from_records(tweets, columns=['Date', 'User', 'Rendered Content', 'Description', 
													'Tweet', 'Number of followers', 'Count of likes', 
													'Count of retweets', 'Count of replies', 
													'Number of friends', 'Location'])
    return df


import subprocess
with st.sidebar.beta_expander("Analyse"):
    #country = st.text_input('Pays')
    keyword = st.text_input('Mot clé à analyser')
    keyword2 = st.text_input('Mot clé à compter')
    keyword2 = str(keyword2.lower())
    tag = str(keyword.lower())
    st.text("Demarrer ou rappeler une analyse\nen cours")
    if st.button('submit/start'):
        #subprocess.Popen("python collector.py"+" "+"-t"+" "+str(tag)+" "+"-c"+" "+str(country), shell=True)
        #subprocess.Popen("python collector.py"+" "+"-t"+" "+str(tag), shell=True)
        #time.sleep(10)
        globals()[df]=scrapetweet(tag)
        
# Création d'une fonction pour compter le nombre de fois qu'un mot apparaît dans un tweet
def count_word(word, text):
    word = word.lower()
    text = text.lower()
    match = re.search(word, text)

    if match:
        return True
    return False

# Création d'une fonction de nettoyage des tweets
def clean_text(text):
    text = re.sub(r'@[A-Za-z0-9]+', '', text) #Suppression des @
    text = re.sub(r'#', '', text) #Suppression des #
    text = re.sub(r'&', '', text) #Suppression des &
    #text = re.sub(r'RT[\s]+', '', text) #Suppression des retweets
    text = re.sub(r'https?:\/\/\S+', '', text) #Suppression des liens hypertextes
    return text


#while True:
    #if time.sleep(55):
st.sidebar.text("Afficher ou actualiser\nles stats")
if st.sidebar.checkbox('Show/Actualise'):
    # Initialisation
    #[python, rstats, statistic, machinelearning, deeplearning] = [0, 0, 0, 0, 0]
    # Importation des tweets
    try:
        tweets_data = df
        tweets_data=load_data().drop_duplicates(subset=['Tweet'], keep='last')
        tweets_data['Tweet clean'] = tweets_data['Tweet'].apply(clean_text)
    except:
        st.error("Patientez quelques secondes et cliquez sur le boutton Show/Actualise")
    # Nettoyage des tweets
    tweets_data.drop_duplicates(subset=['Tweet'], keep='last')
    tweets_data['Tweet clean'] = tweets_data['Tweet'].apply(clean_text)
    lst=keyword2.split(',')
    #initialisation de chaque liste de mot en tant que variable
    for i in lst:
        globals() [i]= 0

    #comptage de chaque elements dans les tweets
    for index, row in tweets_data.iterrows():
        for i in lst:
            globals() [i] = globals() [i] +  count_word(i, row['Tweet clean'])
    # Recuperation des compte dans une liste
    countls=[]
    for i in range(0,len(lst)):
        countls.append(int(globals()[lst[i]]))
    
    # Affichage
    fig, ax = plt.subplots()
    ax = sns.barplot(lst, countls)
    ax.set(ylabel="count")
    plt.setp(ax.get_xticklabels(), rotation=45)
    plt.figure(figsize=(15,10))
    st.pyplot(fig)

if st.sidebar.checkbox("Nuage de mots avec stopwords"):
    # Nettoyage des tweets
    tweets_data=load_data().drop_duplicates(subset=['Tweet'], keep='last')
    tweets_data['Tweet clean'] = tweets_data['Tweet'].apply(clean_text)
    allwords = ' '.join(t for t in tweets_data['Tweet clean'])
    my_cloud1 = WordCloud(random_state = 21, background_color='white').generate(allwords)
    fig=plt.figure(figsize=(15,10))
    plt.imshow(my_cloud1, interpolation='bilinear') 
    plt.axis("off")
    plt.show()
    st.pyplot(fig)

if st.sidebar.checkbox("Nuage de mots sans stopwords"):
    # Nettoyage des tweets
    tweets_data=load_data().drop_duplicates(subset=['Tweet'], keep='last')
    tweets_data['Tweet clean'] = tweets_data['Tweet'].apply(clean_text)
    allwords = ' '.join(t for t in tweets_data['Tweet clean'])
    my_stop_words= stopwords.words('english') + stopwords.words('french')
    my_cloud2 = WordCloud(stopwords = my_stop_words, random_state = 21, background_color='black').generate(allwords)
    fig=plt.figure(figsize=(15,10))
    plt.imshow(my_cloud2, interpolation='bilinear') 
    plt.axis("off")
    plt.show()
    st.pyplot(fig)
