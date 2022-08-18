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
from collector import *
import nltk
from wordcloud import WordCloud
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
st.title("Application pour l'analyse en temps réel des tweets")
st.markdown("*Cette application a été réalisée par Renaud Louis DAHOU*")

#call("python collector.py"+" "+"-t"+" "+str(tag), shell=True)
#cmd = "python collector.py"+" "+"-t"+" "+str(tag)
#os.system(cmd)
#@st.cache


text_file = open("sample.txt", "w",encoding="utf-8")
n = text_file.write(stringo)
text_file.close()

contents = open("sample.txt","r")
with open("collector2.py", "w") as e:
	e.write(contents.read())
	e.close()

def load_data():
    df = pd.read_csv(tag+'.csv',index_col='Date',parse_dates=True)
    return df


command = "pip install snscrape; pip install pandas; python -m nltk.downloader stopwords"

# before Python 3.7:
# ret = subprocess.run(command, stdout=subprocess.PIPE, shell=True)


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
        subprocess.Popen(command+"; "+"python collector2.py"+" "+"-t"+" "+str(tag), shell=True)
        time.sleep(10)


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
        #tweets_data = load_data()
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
