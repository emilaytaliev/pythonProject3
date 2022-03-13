import json
from flask import Flask

with open('candidates.json', 'r', encoding='utf-8') as f:

     result = json.load(f)
     app = Flask(__name__)


     @app.route("/")
     def main():
        w = ''
        for i in result:
             w += f"<br>{i['name']} <br> {i['position']}<br> {i['skills']}<br>"
        return w


     @app.route("/candidate/<int:id>")
     def candidate(id):
         t = ''
         for i in result:
             if str(id) in str(i['id']):
                 t += f"<img src={i['picture']}></img> <br> {i['name']} <br> {i['position']} <br> {i['skills']}<br>"
         return t


     @app.route("/skills/<skill>")
     def skills(skill):
         s = ''
         for i in result:
             if skill in i['skills']:
                 s += f"<br>{i['name']} <br> {i['position']}<br> {i['skills']}<br>"
         return s

#fgdfvbf





     app.run()


