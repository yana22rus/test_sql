from flask_sqlalchemy import SQLAlchemy
from flask import Flask,request,render_template,url_for

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/qwe/card.db'
db = SQLAlchemy(app)

class Card(db.Model):
    id_card = db.Column(db.Integer, primary_key=True)
    name_card = db.Column(db.String,nullable=False)
    description_card = db.Column(db.String,nullable=True)
    class_card = db.Column(db.String,nullable=False)
    type_card = db.Column(db.String,nullable=False)
    rare_card = db.Column(db.String,nullable=False)
    mana_card = db.Column(db.Integer,nullable=False)
    attack_card = db.Column(db.Integer,nullable=True)
    life_card = db.Column(db.Integer,nullable=True)
    keyword_card = db.Column(db.String,nullable=True)

    def __repr__(self):
        return '<User %r>' % self.username

@app.route("/filter",methods=('GET', 'POST'))
@app.route("/",methods=['GET', 'POST'])
def filter():

    if request.method == "POST":

        if request.form['btn'] == 'Класс карты':

            return request.form['class_card']

        if request.form['btn'] == 'Тип карты':

            return request.form['type_card']

        if request.form['btn'] == 'Редкость карты':

            return request.form['rare']

        if request.form['btn'] == 'Стоимость карты':

            return request.form['cost']


    return render_template("filter.html")


@app.route('/add_card',methods=("GET","POST"))
def add_card():

    type_card= ["creature","action","item","support"]
    class_card= ["strength","agility","intellect","willpower","endurance","netural"]
    rare_card = ["common","rare","epic","legendary","uniq_legendary"]
    mana_card = [str(x) for x in range(0,13)]
    attack_card = [str(x) for x in range(0,13)]
    life_card = [str(x) for x in range(0,13)]
    keyword_card = ["guard","charge","breakthrough","ward","drain"]

    if request.method == "POST":


        card = Card(
                    name_card=request.form["name_card"],
                    description_card=request.form["description_card"],
                    class_card=request.form["class_card"],
                    type_card=request.form["type_card"],
                    rare_card=request.form["rare_card"],
                    mana_card=request.form["mana_card"],
                    attack_card=request.form["attack_card"],
                    life_card=request.form["life_card"],
                    keyword_card=",".join(request.form.getlist("keyword_card"))
        )

        db.session.add(card)
        db.session.flush()
        db.session.commit()

    return render_template("add_card.html",
                           class_card=class_card,
                           type_card=type_card,
                           rare_card=rare_card,
                           mana_card=mana_card,
                           attack_card=attack_card,
                           life_card=life_card,
                           keyword_card=keyword_card

                           )



if __name__ == "__main__":
    app.run(debug=True)