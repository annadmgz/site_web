from flask import Flask, render_template, jsonify 
import requests

site = Flask(__name__)     #regarde dans son dossier pour trouver les autres nécéssaire 

#aller à l'HTML 
@site.route("/")   #va à la base de l'ordinateur
def index(): 
    return render_template("exercice27_API.html")     #se deplace jusqu'à mon fichier html 


#aller à l'API 
@site.route("/get-data")
def get_data():       #sert à envoyer des données 
      resultat = requests.get("https://catfact.ninja/fact")    #va chercher la reponse
      data = resultat.json()    #convertir la reponse JSON en dictionnaire python
      print(f"Le contenu de data est : {data}")
      return jsonify(data)    #JSP



#POKEMON
@site.route("/pokemon")
def pokemon ():
     return render_template("exercice_poke.html")


@site.route("bbbbbbbbb")
def get_pekemon():
     resultat = requests.get("https://pokeapi.co/")
     data = resultat.json()





site.run(debug=True)



