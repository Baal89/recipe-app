import os
from flask import Flask, render_template, redirect, request, url_for,flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = "recipe_guide"
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)

#route for index.html
@app.route("/")
def index():
    return render_template("index.html")

#route for recipes.html
@app.route("/get_recipes")  
def get_recipes():
    return render_template("recipes.html", recipes = mongo.db.recipes.find().sort("category_name", -1), 
                                categories = mongo.db.categories.find(),
                                types = mongo.db.types.find(),
                                difficulties = mongo.db.difficulties.find(),
                                prices = mongo.db.prices.find())


# filter category function        
@app.route("/filter_recipes", methods=['POST'])
def filter_recipes():
    print(request.form)
    
    # binding the data from the form
    category = request.form.get("category_name")
    price = request.form.get("price_amount")
    types = request.form.get("type_name")
    difficult = request.form.get("difficult_level")
    
    # creating a list comprehension for each filters fields 
    all_categories = [category["category_name"] for category in mongo.db.categories.find()]
    all_prices = [price["amount"] for price in mongo.db.prices.find()]
    all_types = [type["name"] for type in mongo.db.types.find()]
    all_difficulties = [difficult["level"] for difficult in mongo.db.difficulties.find()]
    
    # if nothing is checked return all the list else return the selected option
    recipes = mongo.db.recipes.find({"category_name": category if category else{"$in": all_categories},
                                    "recipe_price": price if price else {"$in": all_prices},
                                    "recipe_dietary": types if types else {"$in": all_types},
                                    "recipe_difficulty": difficult if difficult else {"$in": all_difficulties}
    })
    
    #return a message if no recipe are found
    if recipes.count() == 0:
        flash("sorry no recipe found")
        return render_template("filter.html", recipes = recipes)
    
    return render_template("filter.html", recipes = recipes)
    
   
# search index function      
@app.route("/search", methods=['POST'])  
def search():
    query = request.form.get('query')
    recipes = mongo.db.recipes.find({'$text' : {'$search' : query} })
    
    #return a message if no recipe are found
    if recipes.count() == 0:
        flash("sorry no recipe found")
        return render_template("search.html", recipes = recipes, type = 'searched')
        
    return render_template("search.html", recipes = recipes, type = 'searched')
        
@app.route("/add_recipe")
def add_recipe():
    return render_template("addrecipes.html", categories=mongo.db.categories.find())
    
# Add Recipe - Insert Recipe Function
@app.route("/insert_recipe", methods=["POST"])
def insert_recipe():
    
    #splitlines is used to return an array in mongo
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
    flash("your recipe has been submitted")
    return redirect(url_for("get_recipes"))


# route for editrecipe.html
@app.route("/edit_recipe/<recipe_id>")
def edit_recipe(recipe_id):
    the_recipe = mongo.db.recipes.find_one({"_id" : ObjectId(recipe_id) })
    all_recipes = mongo.db.categories.find()
    
    return render_template("editrecipes.html", recipes = the_recipe, categories = all_recipes)
 
#update recipe - update recipe function
@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    recipes = mongo.db.recipes
    
    #splitlines is used to return an array in mongo
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
    
    flash("the recipe has been updated")
    return redirect("/get_recipes")

#delete recipe function
@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('get_recipes'))

#route for about.html
@app.route('/about')
def about():
    return render_template('about-us.html')

#route for shop.html    
@app.route('/shop')
def shop():
    return render_template('shop.html', utensils = mongo.db.utensils.find())
    
if __name__=="__main__":
    app.run(host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=True)
        
    