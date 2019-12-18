import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = "recipe_guide"
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

mongo = PyMongo(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_recipes")  
def get_recipes():
    return render_template("recipes.html", recipes = mongo.db.recipes.find().sort("category_name", -1), 
                                categories = mongo.db.categories.find(),
                                types = mongo.db.types.find(),
                                difficulties = mongo.db.difficulties.find(),
                                prices = mongo.db.prices.find())

@app.route("/filter")
def filter():
    return render_template("filter.html", recipes = mongo.db.recipes.find().sort("category_name", -1), 
                                categories = mongo.db.categories.find(),
                                types = mongo.db.types.find(),
                                difficulties = mongo.db.difficulties.find(),
                                prices = mongo.db.prices.find())
    
# filter category function        
@app.route("/filter_recipes", methods=['POST'])
def filter_recipes(category_name):
    recipes = mongo.db.recipes.find({'category_name': category_name})
    return render_template("filter.html", recipes = recipes)
 
# filter difficult function  
@app.route("/filter_difficulty/<difficulty>")
def filter_difficulty(difficulty):
    difficulties = mongo.db.recipes.find({'recipe_difficulty': difficulty})
    return render_template("filter.html", recipes = difficulties)
    
# filter dietary function  
@app.route("/filter_dietary/<types>")
def filter_dietary(types):
    types = mongo.db.recipes.find({'recipe_dietary': types})
    return render_template("filter.html", recipes = types)
    
# filter price function  
@app.route("/filter_prices/<prices>")
def filter_prices(prices):
    prices = mongo.db.recipes.find({'recipe_price': prices})
    return render_template("filter.html", recipes = prices)
    
   
# search index function      
@app.route("/search", methods=['POST'])  
def search():
    query = request.form.get('query')
    recipes = mongo.db.recipes.find({'$text' : {'$search' : query} })
    return render_template("recipes.html", recipes = recipes, type = 'searched')
        
@app.route("/add_recipe")
def add_recipe():
    return render_template("addrecipes.html", categories=mongo.db.categories.find())
    
# Add Recipe - Insert Recipe Function
@app.route("/insert_recipe", methods=["POST"])
def insert_recipe():

    ingredients = request.form.get("recipe_ingredients").splitlines()
    allergens = request.form.get("recipe_allergens").splitlines()
    
    
    # Recipe JSON object
    submission = {
        "recipe_name": request.form.get("recipe_name"),
        "category_name": request.form.get("category_name"),
        "recipe_img": request.form.get("recipe_img"),
        "recipe_difficulty": request.form.get("recipe_difficulty"),
        "recipe_ingredients": ingredients,
        "recipe_allergens": allergens,
        "recipe_cooking_time": request.form.get("recipe_cooking_time"),
        "recipe_price": request.form.get("recipe_price"),
        "recipe_dietary": request.form.get("recipe_dietary"),
        "recipe_doses": request.form.get("recipe_doses"),
        "recipe_preparation_steps": request.form.get("recipe_preparation_steps"),
    }
    
    recipes = mongo.db.recipes
    recipes.insert_one(submission)
    return redirect(url_for("get_recipes"))


# edit recipe - edit recipe function
@app.route("/edit_recipe/<recipe_id>")
def edit_recipe(recipe_id):
    the_recipe = mongo.db.recipes.find_one({"_id" : ObjectId(recipe_id) })
    all_recipes = mongo.db.categories.find()
    
    return render_template("editrecipes.html", recipes = the_recipe, categories = all_recipes)
 
#update recipe - update recipe function
@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    recipes = mongo.db.recipes
    
    ingredients = request.form.get("recipe_ingredients").splitlines()
    allergens = request.form.get("recipe_allergens").splitlines()
   
    
    recipes.update( {'_id': ObjectId(recipe_id)},
    
    
    {
        "recipe_name": request.form.get("recipe_name"),
        "category_name": request.form.get("category_name"),
        "recipe_img": request.form.get("recipe_img"),
        "recipe_difficulty": request.form.get("recipe_difficulty"),
        "recipe_ingredients": ingredients,
        "recipe_allergens": allergens,
        "recipe_cooking_time": request.form.get("recipe_cooking_time"),
        "recipe_price": request.form.get("recipe_price"),
        "recipe_dietary": request.form.get("recipe_dietary"),
        "recipe_doses": request.form.get("recipe_doses"),
        "recipe_preparation_steps": request.form.get("recipe_preparation_steps"),
    })
    return redirect("/get_recipes")

@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('get_recipes'))

@app.route('/about')
def about():
    return render_template('about-us.html')
    
@app.route('/shop')
def shop():
    return render_template('shop.html', utensils = mongo.db.utensils.find())
    
if __name__=="__main__":
    app.run(host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=True)
        
    