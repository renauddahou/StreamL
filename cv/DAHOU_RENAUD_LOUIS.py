stringo="""

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Resume of DAHOU Renaud Louis</title>
    <!-- <link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet"> -->
    <!-- <link href="https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet"> -->
    <link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.14.0/css/all.min.css" rel="stylesheet">
    <style type="text/css">
    @import url(https://fonts.googleapis.com/css?family=Open+Sans:400,600,700,800);
@charset "utf-8";
@-webkit-viewport   { width: device-width; }
@-moz-viewport      { width: device-width; }
@-ms-viewport       { width: device-width; }
@-o-viewport        { width: device-width; }
@viewport           { width: device-width; }

body{
  font-family: 'Open Sans', Arial, Tahoma;
  font-weight: 400;
  color: #363636;
  background: #334960;
}
blockquote {
  font-size: 1em;
}

.container{
  margin-top: 80px;
  margin-bottom: 15px;
  background: #fff;
}

#photo-header{
  margin-top: -75px;
}
#photo{
  width: 160px;
  height: 160px;
  border-radius: 50%;
  overflow: hidden;
  padding: 5px;
  background: #334960;
  display: inline-block;
}
#photo img{
  width: 150px;
  height: 150px;
  border-radius: 50%;
}
#text-header h1{
  margin: 0;
  padding: 0;
  font-size: 1.5em;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: -1px;
}
#text-header h1::first-line{
  font-size: 1.5em;
  font-weight: 800;
  line-height: 1.5em;
}
#text-header h1 span{
  color: #334960;
  opacity: 0.7;
}
#text-header h1 sup{
  opacity: 0.5;
}
#text-header:after{
  width: 100%;
  height: 3px;
  border-bottom: 1px solid #ddd;
  margin-top: 15px;
  content: '';
  display: block;
}

.box{
  padding-bottom: 10px;
  margin-bottom: 25px;
}
.box h2{
  color: #227c74;
  font-size: 1.5em;
  font-weight: 700;
  text-transform: uppercase;
}

#awards,
#education{
  margin-top: 20px;
  margin-bottom: 0;
  position: relative;
  padding: 1em 0;
  list-style: none;
}
#awards:before,
#education:before {
  width: 5px;
  height: 100%;
  position: absolute;
  left: 35px;
  top: 0;
  content: ' ';
  display: block;
  background: #32475c;
  background: -moz-linear-gradient(top,  #ffffff 0%, #32475c 7%, #32475c 89%, #ffffff 100%);
  background: -webkit-gradient(linear, left top, left bottom, color-stop(0%,#ffffff), color-stop(7%,#32475c), color-stop(89%,#32475c), color-stop(100%,#ffffff));
  background: -webkit-linear-gradient(top,  #ffffff 0%,#32475c 7%,#32475c 89%,#ffffff 100%);
  background: -o-linear-gradient(top,  #ffffff 0%,#32475c 7%,#32475c 89%,#ffffff 100%);
  background: -ms-linear-gradient(top,  #ffffff 0%,#32475c 7%,#32475c 89%,#ffffff 100%);
  background: linear-gradient(to bottom,  #ffffff 0%,#32475c 7%,#32475c 89%,#ffffff 100%);
  filter: progid:DXImageTransform.Microsoft.gradient( startColorstr='#ffffff', endColorstr='#ffffff',GradientType=0 );
}
#awards li,
#education li{
  width: 100%;
  z-index: 2;
  position: relative;
  float: left;
}
#awards .year,
#education .year{
  width: 14%;
  background: #fff;
  padding: 10px;
  font-weight: 700;
  display: inline-block;
}
#awards .description,
#education .description{
  width: 83%;
  display: inline-block;
  background: #eee;
  margin-bottom: 10px;
  position: relative;
  padding: 10px;
  border-bottom: 1px solid #ccc;
  border-right: 1px solid #ccc;
}
#awards .description:after,
#education .description:after {
  content: '';
  position: absolute;
  top: 15px;
  right: 0;
  left: -16px;
  height: 0;
  width: 0;
  border: solid transparent;
  border-right-color: #eee;
  border-width: 8px;
  pointer-events: none;
}
#awards .description h3,
#education .description h3{
  font-size: 1.2em;
  margin: 0;
  padding: 0;
  font-weight: 700;
}
#awards .description p,
#education .description p{
  margin-top: 5px;
  padding: 0;
}

.job{
  margin-bottom: 15px;
}
.job .details {
  margin-left: 3%;
  width: 95%;
  padding: 10px;
  margin-bottom: 10px;
  background: #eee;
  border-bottom: 1px solid #ccc;
  border-right: 1px solid #ccc;
}
.job .where{
  font-size: 1.2em;
  font-weight: bold;
}
.job .year{
  opacity: 0.7;
}
.job .profession{
  font-size: 1.2em;
  font-weight: bold;
}
.job .description{
  line-height: 1.5em;
}
.job .highlights{
  padding: 5px 0;
  font-weight: bold;
}
.job .job-details {
  padding-left: 5%;
  width: 100%;
}
.publication {
  margin-bottom: 0;
}
.publication .name{
  font-size: 1em;
  font-weight: bold;
}
.publication .year{
    opacity: 0.7;
}
.publication p{
  margin: 0;
  padding-top: 10px;
}

.contact-item{
  width: 100%;
  float: left;
}
.contact-item .icon{
  padding: 10px;
  border-right: 1px solid #ccc;
  border-bottom: 1px solid #ccc;
  color: #32475c;
  background: #eee;
}
.contact-item:last-child .icon{
  border-bottom: none;
}
.contact-item .title{
  width: 80%;
  width: calc(100% - 55px);
  font-weight: 700;
  opacity: 0.9;
}
.contact-item .title.only{
  margin-top: 10px;
}
.contact-item .description{
  width: 80%;
  width: calc(100% - 55px);
  color: #334960;
}

.item-interests,
.item-skills{
  height: 30px;
  color: #334960;
  padding: 5px 10px;
  margin-bottom: 5px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  font-size: 1.1em;
  font-weight: 600;
}
.interest,
.skill{
  color: #fff;
  display: inline-block;
  margin-right: 5px;
  margin-bottom: 5px;
  padding: 5px 10px;
  background: #32475c;
  position: relative;
  font-size: .85em;
}
.skill-level {
  background-color: #227c74;
  border-radius: 4px;
  color: #fff;
  padding: 1px 8px;
  font-size: .75em;
  position: absolute;
  margin: 1px 10px;
}

#language-skills .skill{
  margin: 10px 0;
  padding-bottom: 10px;
  border-bottom: 1px solid #eee;
}

    </style>
    <style type="text/css" media="print">
    body {
  font-size: .95em;
  -webkit-print-color-adjust: exact;
}

a[href]:after {
  content: none !important;
}

#photo{
  display: none;
}

.box {
  margin-bottom: -10px;
}

blockquote,
#education,
#awards,
.contact-item,
.publication,
.skills,
.interests {
  page-break-inside: avoid;
}

.col-sm-5{
  width: 40%;
  padding: 0 15px;
}

.col-sm-7{
  width: 60%;
  padding: 0 15px;
}

.skills .col-sm-offset-1,
.interests .col-sm-offset-1{
  margin-top: -10px;
  margin-bottom: 5px;
}

#education {
  margin: 0;
  margin-bottom: -20px;
}
#awards:before,
#education:before {
  background: none;
}

#awards .description,
#education .description,
.job .details {
  border: 1px solid #eee;
}
.publication,
.publication .panel-heading,
.publication .name{
  margin: 0;
  padding: 0 5px;
  border: none;
}
.publication .panel-body {
  padding: 0 10px;
  margin: 0;
}

.badge {
  margin: 0;
}

.list-group-item{
  border: none;
  margin: 0;
  padding: 5px 15px;
}
.list-group-item:after{
  content: '';
  position: absolute;
  top: 8px;
  right: 0;
  left: -1px;
  height: 0;
  width: 0;
  border: solid transparent;
  border-right-color: #999;
  border-width: 4px;
  pointer-events: none;
 }

    </style>
  </head>
  <body>
    <div class="container">
      <div class="row">
        <div class="col-xs-12">
          <div id="photo-header" class="text-center">
            <!-- PHOTO (AVATAR) -->
            <div id="photo">
              <img src="https://avatars.githubusercontent.com/u/85571576?s=400&u=a025e326bbafef61874c405e652e3e2a77b438bb&v=4" alt="avatar">
            </div>
            <div id="text-header" >
              <h1>DAHOU Renaud Louis<br><span>??? Data scientist ??? Python Developer ??? DEVOPS</span></h1>
            </div>
          </div>
        </div>
      </div>
      <div class="row">
        <div class="col-xs-12 col-sm-7">
          <!-- ABOUT ME -->
          <div class="box">
            <h2><i class="fas fa-user ico"></i> A propos de moi</h2>
            <p>Je dispose d???une grande ouverture d???esprit et d???une grande facilit?? d???adaptation.
Je jouis d???une bonne exp??rience professionnelle suite ?? l???ex??cution de plusieurs projets et mon domaine d???intervention s?????tend aux :
??? Machine Learning et Intelligence artificielle
??? Web Scraping
??? Cloud Computing
??? Data Analysis
??? D??veloppement de API
??? Test de p??n??tration de reseau d'entreprise</p>
<br> </br>
          </div>
          <!-- WORK EXPERIENCE -->
          <div class="box">
            <h2><i class= "fas fa-suitcase ico"></i> Exp??rience professionnelle</h2>
              <div class="job clearfix">
                <div class="row">
                  <div class="details">
                    <div class="where">
                      Kikun Digital
                      <div class="pull-right">
                        France - Gabon
                      </div>
                    </div>
                    <div class="address">
                      <a href="https:&#x2F;&#x2F;www.linkedin.com&#x2F;company&#x2F;kikun-digital&#x2F;" target= "_blank"><i class="fas fa-globe ico"></i> https:&#x2F;&#x2F;www.linkedin.com&#x2F;company&#x2F;kikun-digital&#x2F;</a>
                    </div>
                    <div class="year">Janvier 2022 ??? Pr??sent</div>
                  </div>
                </div>
                <div class="row">
                  <div class="job-details col-xs-11">
                    <div class="profession">Consultant Data Science & DEVOPS</div>
                    <div class="description">
                      Description
                      <div class="highlights"> </div>
                      <ul class="list-group">
                        <li class="list-group-item">En tant que Consultant Data Science & DEVOPS , mes t??ches sont les suivantes:</li>
                        <li class="list-group-item">??? Explorer les donn??es et d??velopper des mod??les de machine learning et deep learning</li>
                        <li class="list-group-item">??? R??aliser les d??ploiements et les configurations des infrastructures technologiques.</li>
                        <li class="list-group-item">??? Provisionnement des serveurs sur le cloud AWS et AZure.</li>
                        <li class="list-group-item">??? Deploiement des applications sur le cloud.</li>
                        <li class="list-group-item">??? Developpement des APIs.</li>
                        <li class="list-group-item">??? ??laboration des documents d'installation (DIN) </li>
                        <li class="list-group-item">??? Reporter au p??le consulting</li>
                        <li class="list-group-item">??? Tester et participer ?? des ateliers de d??veloppement de logiciels</li>
                      </ul>
                    </div>
                  </div>
                </div>
              </div>
              <br> </br>
              <br> </br>
              <div class="job clearfix">
                <div class="row">
                  <div class="details">
                    <div class="where">
                      Freelance
                      <div class="pull-right">
                        
                      </div>
                    </div>
                    <div class="year">Janvier 2018 ??? D??cembre 2021</div>
                  </div>
                </div>
                <div class="row">
                  <div class="job-details col-xs-11">
                    <div class="profession"> consultant API development &amp; Cloud Deployment</div>
                    <div class="description">
                      Description
                      <div class="highlights"> </div>
                      <ul class="list-group">
                        <li class="list-group-item">En tant que Consultant API development & Cloud deployment , j'ai accompagn?? des Particuliers ; Etudiants et Entreprises dans la r??alisation de projet data driven et Machine learning:</li>
                        <li class="list-group-item">??? Application du process ETL (Extract-Transform-Load) pour l'analyse de march?? crypto-monnaie</li>
                        <li class="list-group-item">??? Developpement d'API Scoring en python  pour matcher un profile candidat par rapport ?? un job </li>
                        <li class="list-group-item">??? D??veloppement d'une application pour l'analyse de planning pour identifier les heures creuses des ??tudiants au sein d'un campus pour la programmation d'activit?? ?? forte participation</li>
                        <li class="list-group-item">??? D??veloppemnt d'une application data record et analysis dans le domains de la s??curit?? au travail</li>
                        <li class="list-group-item">??? Developpemnt d'un bot t??legram pour la commande de fastfood</li>
                        <li class="list-group-item">??? Developpement d'une API de traduction multilangue</li>
                        <li class="list-group-item">??? Deploiement d'application en CI/CD sur le cloud AWS et Azure</li>
                        <li class="list-group-item">??? Dockerisation et deploiement d'application sur le cloud AWS et Azure</li>
                      </ul>
                    </div>
                  </div>
                </div>
              </div>
          </div>
          <!-- PROJECTS -->
          <div class="box">
            <h2><i class= "fas fa-code-branch ico"></i> Projets</h2>
              <div class="address">
              </div>
            <ul class="list-group">
              <a href="https://renaud17.github.io/mesprojets/EDA_funnel_marketing_B2B.html" target= "_blank"><i class="fas fa-globe ico"> Analyse exploratoire des donn??es d'
un funnel marketing B2B en utilisant Python</i></a>
              <li class="list-group-item">Ce projet se concentre sur la r??alisation D'une analyse exploratoire des donn??es (EDA) pour le Marketing B2B en utilisant Python. 
              Nous utiliserons les donn??es D'Olist, une plate-forme de commerce ??lectronique qui relie les petites et moyennes entreprises aux principaux march??s du Br??sil, 
              par exemple. En plus de fournir la m??thode et le code, je veux ??galement discuter des principes fondamentaux du Marketing B2B et de la fa??on dont ces id??es EDA 
              peuvent aider Olist ?? prendre une meilleure d??cision marketing.
              </li>
              <a href="https://renaud17.github.io/mesprojets/EDA%20_segmentation_LTV_NPD_TS.html" target= "_blank"><i class="fas fa-globe ico">  Segmentation de client e-commerce,
pr??diction du CLV</i></a>
              <li class="list-group-item">Ce projet se concentre sur la r??alisation D'une segementation et la prediction de la valeur ?? vie du client ;des jours d'achats future et la prevision des vente pour le Marketing B2C en utilisant Python. Nous utiliserons les donn??es d'un d??taillant en ligne bas??e au Royaume-Uni pendant une p??riode de huit mois. En plus de fournir la m??thode et le code, je veux ??galement discuter des principes fondamentaux du Marketing B2C et de la fa??on dont ces id??es EDA peuvent aider ?? prendre une meilleure d??cision marketing.
              </li>
              <a href="https://renauddahou-streaml-hsekpimainapp3-2vpzvp.streamlitapp.com" target= "_blank"><i class="fas fa-globe ico"> Application streamlit pour le suivi des indicateurs HSE</i></a>
              <li class="list-group-item">Ce projet se concentre sur la r??alisation d'une application avec base de donn??es SQL ayant les fonctionnalit??s suivantes : 
 
 ??? Ajouter, afficher, modifier, supprimer et t??l??charger des donn??es 
  
 ??? Interface de travail personnel ?? chaque utilisateur(login) 
  
 ??? Gestion KPI-HSE de plusieurs chantiers et suivi graphique..
              </li>
              <a href="https://renauddahou-streaml-p2app-y7zbjh.streamlitapp.com" target= "_blank"><i class="fas fa-globe ico"> Application pour l'exploration automatique des donn??es</i></a>
              <li class="list-group-item">Ce projet se concentre sur la r??alisation D'une analyse exploratoire des donn??es (EDA) de fa??on automatique.
              </li>
            </ul>
          </div>
        </div>
        <div class="col-xs-12 col-sm-5">
          <!-- CONTACT -->
          <div class="box clearfix">
            <h2><i class="fas fa-bullseye ico"></i> Contact</h2>
            <div class="contact-item">
              <div class="icon pull-left text-center"><span class="fas fa-map-marker fa-fw"></span></div>
              <div class="title pull-right">C&#x2F;40 COTONOU</div>
              <div class="title  pull-right"> BJ</div>
            </div>
            <div class="contact-item">
              <div class="icon pull-left text-center"><span class="fas fa-phone fa-fw"></span></div>
              <div class="title only pull-right">+22967927952</div>
            </div>
            <div class="contact-item">
              <div class="icon pull-left text-center"><span class="fas fa-envelope fa-fw"></span></div>
              <div class="title only pull-right"><a href="mailto:dahou.r@yahoo.com" target="_blank">dahou.r@yahoo.com</a></div>
            </div>
            <div class="contact-item">
              <div class="icon pull-left text-center"><span class="fab fa-linkedin fa-fw"></span></div>
              <div class="title pull-right">LinkedIn</div>
              <div class="description pull-right"><a href="https:&#x2F;&#x2F;www.linkedin.com&#x2F;in&#x2F;dahou-renaud-louis-8958599a&#x2F;" target="_blank">dahou-renaud-louis-8958599a</a></div>
            </div>
          </div>
          <!-- EDUCATION -->
          <div class="box">
            <h2><i class="fas fa-university ico"></i> Education</h2>
            <ul id="education" class="clearfix">
              <li>
                <div class="year pull-left">2022 - Pr??sent</div>
                <div class="description pull-right">
                  <h3>MIT Sloan School of Management</h3>
                  <div class="where"></div>
                  <p><i class= "fas fa-graduation-cap ico"></i> Machine Learning in Business</p>
                  <p>Incorporer l'apprentissage automatique dans votre strat??gie d'entreprise, en explorant la valeur et l'impact de cette technologie</p>
                </div>
              </li>
              <li>
                <div class="year pull-left">2022 </div>
                <div class="description pull-right">
                  <h3>MEL-ACADEMIE</h3>
                  <div class="where"></div>
                  <p><i class= "fas fa-graduation-cap ico"></i> Certification</p>
                  <p>Pentesting</p>
                    <div>Cours ?? distance</div>
                    <ul class="list-group">
                      <li class="list-group-item">Hacking Base professionnel</li>
                      <li class="list-group-item">Hacking Distant</li>
                      <li class="list-group-item">Administration et S??curit?? des serveurs d'entreprise</li>
                    </ul>
                </div>
              </li>
              <li>
                <div class="year pull-left">2019 2022</div>
                <div class="description pull-right">
                  <h3>CentraleSup??lec</h3>
                  <div class="where"></div>
                  <p><i class= "fas fa-graduation-cap ico"></i> Certification</p>
                  <p>Data Science</p>
                    <div>Cours ?? distance</div>
                    <ul class="list-group">
                      <li class="list-group-item">Scientific Computing avec Python</li>
                      <li class="list-group-item">Analyse de donn??es textuelles</li>
                      <li class="list-group-item">Conception des architectures Big Data</li>
                      <li class="list-group-item">R??alisation des calculs distribu??s sur des donn??es massives</li>
                      <li class="list-group-item">??valuation et am??lioration des performances d'un mod??le de machine learning</li>
                      <li class="list-group-item">Entra??nement d'un mod??le pr??dictif lin??aire</li>
                      <li class="list-group-item">Exploration de donn??es avec des algorithmes non supervis??s</li>
                      <li class="list-group-item">Utilisation des mod??les supervis??s non lin??aires</li>
                    </ul>
                </div>
              </li>
              <li>
                <div class="year pull-left">2017 2018</div>
                <div class="description pull-right">
                  <h3>Haute Ecole de Commerce et de Management</h3>
                  <div class="where"></div>
                  <p><i class= "fas fa-graduation-cap ico"></i> Master en Management des Projets</p>
                  <p>Management des projets</p>
                </div>
              </li>
            </ul>
          </div>
          <!-- SKILLS -->
          <div class="box">
            <h2><i class="fas fa-tasks ico"></i> Comp??tences</h2>
            <div class="skills clearfix">
              <div class="item-skills">
                  Languages-Packages-Services
                  <span class="skill-level">Exp??riment??</span>
              </div>
              <div class="col-sm-offset-1 col-sm-12 clearfix">
                <span class= "skill badge">Python</span>
                <span class= "skill badge">SQL</span>
                <span class= "skill badge">NoSQL</span>
                <span class= "skill badge">GitHub</span>
                <span class= "skill badge">Bitbucket</span>
                <span class= "skill badge">Docker</span>
                <span class= "skill badge">Ansible</span>
                <span class= "skill badge">Terraform</span>
                <span class= "skill badge">Kubernetes</span>
                <span class= "skill badge">Sklearn</span>
                <span class= "skill badge">Keras</span>
                <span class= "skill badge">Tensorflow</span>
                <span class= "skill badge">Streamlit</span>
                <span class= "skill badge">Flask</span>
                <span class= "skill badge">API REST</span>
                <span class= "skill badge">AWS</span>
                <span class= "skill badge">Azure</span>
                <span class= "skill badge">Machine learning</span>
                <span class= "skill badge">Deep learning</span>
              </div>
            </div>
            <br> </br>
            <div class="skills clearfix">
              <div class="item-skills">
                Syst??mes d'exploitation
                  <span class="skill-level">Exp??riment??</span>
              </div>
              <div class="col-sm-offset-1 col-sm-12 clearfix">
                <span class= "skill badge">Linux</span>
                <span class= "skill badge">Windows</span>
              </div>
            </div>
          </div>
          <!-- HOBBIES -->
          <div class="box">
            <h2><i class="fas fa-heart ico"></i> Int??r??ts</h2>
            <div class="interests clearfix">
              <div class="item-interests">
                Technologie
              </div>
              <div class="col-sm-offset-1 col-sm-12 clearfix">
                <span class= "interest badge">Automatisation</span>
                <span class= "interest badge">Cloud</span>
                <span class= "interest badge">Serverless</span>
                <span class= "interest badge">IoT</span>
                <span class= "interest badge">Intelligence artificielle</span>
                <span class= "interest badge">Cyber S??curit??</span>
              </div>
            </div>
            <div class="box">
            <h2><i class= "fas fa-check-square ico"></i> References</h2>
            
              <div>Josu?? AFOUDA</div>
              <div class="contact-item">
              <div class="icon pull-left text-center"><span class="fab fa-linkedin fa-fw"></span></div>
              <div class="title pull-right">Consultant Data Science</div>
              <div class="description pull-right"><a href="https://www.linkedin.com/in/josu%C3%A9-a-741693217/" target="_blank">josu??-a-741693217</a></div>
              <br> </br>
              <br> </br>
              <div>Olivier Moulengue </div>
              <div class="contact-item">
              <div class="icon pull-left text-center"><span class="fab fa-linkedin fa-fw"></span></div>
              <div class="title pull-right">Responsable p??le Architecture IT HEC Paris</div>
              <br> </br>
              <div class="description pull-right"><a href="https://www.linkedin.com/in/olivier-moulengue-10b7b39/" target="_blank">olivier-moulengue-10b7b39</a></div>
              <br> </br>
              <div>Yanick Mezui </div>
              <div class="contact-item">
              <div class="icon pull-left text-center"><span class="fab fa-linkedin fa-fw"></span></div>
              <div class="title pull-right">Business Intelligence / SQL Senior Premier Field Engineer</div>
              <div class="description pull-right"><a href="https://www.linkedin.com/in/yanick-mezui-23a7271/" target="_blank">yanick-mezui-23a7271</a></div>
            </div>

            <br> </br>
            <br> </br>
            <div class="box">
            <h2><i class= "fas fa-code-branch ico"></i> Portfolio</h2>
            
            <ul class="list-group">
              <a href="https://renauddahou-streaml-cvapp-asrxsl.streamlitapp.com/" target= "_blank"><i class="fas fa-globe ico"> D??couvrer mes autres projets via cette URL </i></a>
            </ul>
            
          </div>
          </div>
        </div>
      </div>
    </div>

  </body>
</html>
"""
