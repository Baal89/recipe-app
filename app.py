import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = "recipes_app"
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

mongo = PyMongo(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_recipes")   
def get_recipes():
    return render_template("recipes.html", recipes=mongo.db.recipes.find().sort("category_name"))
    
@app.route("/add_recipe")
def add_recipe():
    return render_template("addrecipes.html", categories=mongo.db.categories.find())
    
# Add Recipe - Insert Recipe Function
@app.route("/insert_recipe", methods=["POST"])
def insert_recipe():

    ingredients = request.form.get("recipe_ingredients").splitlines()
    tools = request.form.get("recipe_tools").splitlines()
    
    # Recipe JSON object
    submission = {
        "recipe_name": request.form.get("recipe_name"),
        "category_name": request.form.get("category_name"),
        "recipe_img": request.form.get("recipe_img"),
        "recipe_difficulty": request.form.get("recipe_difficulty"),
        "recipe_ingredients": ingredients,
        "recipe_cooking_time": request.form.get("recipe_cooking_time"),
        "recipe_price": request.form.get("recipe_price"),
        "recipe_tools": tools,
        "recipe_doses": request.form.get("recipe_doses"),
        "recipe_preparation_steps": request.form.get("recipe_preparation_steps"),
    }
    
    recipes = mongo.db.recipes
    recipes.insert_one(submission)
    return redirect(url_for("get_recipes"))


if __name__=="__main__":
    app.run(host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=True)
        
        



