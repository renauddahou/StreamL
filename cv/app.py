# Core Pkgs
import streamlit as st 
import codecs
# Components Pkgs
import streamlit.components.v1 as components
#st.set_page_config(layout="wide")
st.set_page_config( 
layout="wide",  
initial_sidebar_state="auto",
page_title= "CV",   
)

#masquer le menu streamlit
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

def st_display_sweetviz(report_html,width=1000,height=3100):
	report_file = codecs.open(report_html,'r',"utf-8")
	page = report_file.read()
	components.html(page,width=width,height=height,scrolling=True)


image_ren ="""
<img src="https://technology.amis.nl/wp-content/uploads/2020/11/image-27.png" alt="Avatar" style="vertical-align: middle;width: 100px;height: 100px;border-radius: 50%;" >
"""

image_ren2 ="""
<img src="https://awslabs.github.io/aws-orbit-workbench/img/service/streamlit_logo.png" alt="Avatar" style="vertical-align: middle;width: 100px;height: 100px;border-radius: 50%;" >
"""

contents = open("DAHOU_RENAUD_LOUIS.txt","r")
with open("DAHOU_RENAUD_LOUIS.html", "w") as e:
	e.write(contents.read())


p = open("DAHOU_RENAUD_LOUIS.html")


def main():
	st.sidebar.markdown('# **PROJETS EDA ET APP**')
	st.sidebar.markdown("* **Il s'agit de projets personnels que j'ai réalisés pendant mes heures libres en ce qui concerne mes projets professionnels ils sont notamment réalisés sur le cloud aws et azure et tenu par le secret professionnel.**")
	st.sidebar.markdown(image_ren2, unsafe_allow_html = True)
	st.sidebar.markdown("[** Application streamlit pour le suivi des indicateurs HSE ** ](https://renauddahou-streaml-hsekpimainapp3-2vpzvp.streamlitapp.com/)")
	st.sidebar.markdown("[** Application streamlit pour l'exploration automatique des données ** ](https://renauddahou-streaml-p2app-y7zbjh.streamlitapp.com/)")
	st.sidebar.markdown(image_ren, unsafe_allow_html = True)
	st.sidebar.markdown("[**Analyse exploratoire des données d' un funnel marketing B2B en utilisant Python** ](https://renaud17.github.io/mesprojets/EDA_funnel_marketing_B2B.html)")
	st.sidebar.markdown("[** Segmentation de client e-commerce, prédiction du CLV** ](https://renaud17.github.io/mesprojets/EDA%20_segmentation_LTV_NPD_TS.html)")
	st.sidebar.markdown("[**Analyse de sentiment client ** ](https://renaud17.github.io/mesprojets/analyse_texte_Amazon.html)")
	st.sidebar.markdown("[**Scraping Web MTN BENIN** ](https://renaud17.github.io/mesprojets/scraping_Web_MTN.html)")
	st.sidebar.markdown("[**Segmentation de la clientèle MTN BENIN** ](https://renaud17.github.io/mesprojets/Segmentation.html)")
	st.sidebar.markdown("[**Classification des patients porteurs du diabète ou non ** ](https://renaud17.github.io/mesprojets/diabete_prediction.html)")
	st.sidebar.markdown("[**Identification du sujet d’ont traite un document avec LDA ** ](https://renaud17.github.io/mesprojets/NLTK.html)")
	st.sidebar.markdown("[**Problème de régression hypbands VS Temperature VS Soil moisture ** ](https://renaud17.github.io/mesprojets/soilmoisture.html)")
	st.sidebar.markdown("[**Prédiction des maladies cardiaques** ](https://renaud17.github.io/mesprojets/maladie_cardiaque.html)")
	st.sidebar.markdown("[**Prévision de la quantité de Co2 qui sera éjecté dans la nature au Bénin en 2020 ** ](https://renaud17.github.io/mesprojets/Co2_2020_prediction.html)")
	st_display_sweetviz("DAHOU_RENAUD_LOUIS.html")
	#components.html(p.read())
if __name__ == '__main__':
	main()