# Pasta Factory

Pasta Factory is a italian company who produce kitchen utensils for everyday use. with the creation of this website they want to promote their brand
of kitchen utensil.
To promote their brand of tools the Pasta Factory website include a cook book with the possibility for the user to upload, delete or modify their recipes.
This interaction could tempt more people to try new recipes and start the adventure of cooking,
and what is better if not the utensils shown. Utensils that can certainly make their kitchen experience easier.

## UX 

#### Audience

This site is for all those people of love food, from a chef to a person who is trying to cook for the first time for his/her partner. The site wants 
to help people with the passion of cooking sharing their experience and giving others idea to impress their guest or for their own pleasure.
The best way to achieving all of these is using the cooking tools promote in the site.

#### User stories

As any one of the users, I want to perform the following actions:

* As a user who loves food: I want to discover new recipes that I might enjoy, so I can check a new recipe in the recipes page.
* As a user who want to impress his/her partner: I want to discover a nice and cool recipe, so I can check in the recipes page to get new ideas.
* As a user who loves cook: I want to share with the others the recipes I have created, so I can add a recipe in the add recipe page.
* As a user who added a recipe: I want to correct an error or update a recipe I added, so I can update the recipe in the update recipe page.
* As a user who does not like the recipe added: I want to delete the recipe added before as a mistake, so I can delete the recipe with the delete recipe button.
* As a user who need to cook a recipe: I want to cook the recipe just found in the recipes page, I can check the recipe utensils needed in the shop page. 
* As a user who need to look for a specific recipe, I can use the search form and type the recipe I was looking for.
* As a user who need some ideas for his dinner, I can use the filter functionality and grab the recipes I was looking for.
* as a user who need a new tools to create a recipe, I can go to shop page and look for the tool I need.
* as a user who want to know more about Pasta Factory, I can go to about us page and read the story fo the brand.


## Features

#### existing features

The Pasta Factory website consist in the following features:

1. base.html page:
   * the navbar - allows the user who open the site to navigate through it.
   * the footer - let the user who want to contact the company with social media tel or fax to get in touch with them.
   * the search form - allow the user to search for a specific recipe or ingredient.
   
2. index.html page:
    * the carousel - help the user who just jumped in the page to understand the purpose of the site and what the site owner does.
    * the utensils cards - let the user who to understand what the company is promoting, providing a link to the catalogue as well.
    * the cookbook - provide the user with a brief explanation of the possibility to share and look for recipes.

3. about.html page:
    * the company history - provide the user who want to know more about Pasta Factory with the story and the skills of the company.

4. recipes.html page:
    * the recipes page - allow the user to check a list of recipes.
    * the update button - allow the user to modified a recipe simply clicking on the update button.
    * the delete button - allow the user to delete a recipe previously added simply clicking on the delete button.
    * the filter button - allow the user to filter the recipes stored in the page selecting the appropriate checkbox.

5. addrecipe.html page:
    * the add recipe form - allow the user to insert a new recipe in the database filling the form.

6. edit recipe.html page:
    * the edit recipe form - allow the user to modified an existing recipe filling the form.
    
7. shop.html page:
    * the youtube video - want to help the user who never used a pasta machine how simple is, with the purpose to give a positive feedback.
    * the shop page - allow the user to see a small chunk of the utensils tool promote in the page.


#### features left to implement

there are several new features to be implemented in the site, but considering they are outside the scope of the project they will be implemented in a future time:

1. it should not be possible modified or cancel recipes added from another user without a confirmation. An authentication for using the recipe page should be implemented.
2. the possibility to vote the recipes should be implemented too and meaby the possibility to leave a comment as well.
3. if comments are allowed a moderation sistem should be put in place.
4. it would be nice allow the user to upload and share the videos of their recipe too.
5. create a "school" of cooking would be interesting too, with video-lessons from chef that are using only the utensils promote in the site.
6. the shop page should redirect to a real online shop with the possibility to buy the utensils promoted.
7. an authentication system is needed to allow online payments.
8. the possibility to vote an utensils should be implemented and a sub-section  most popular utensil too.

## Technologies Used

* HTML5:
    * the project uses HTML to create the structure of the website

* CSS3:
    * the project uses CSS3 to style the site
    
* [Bootstrap 4](https://getbootstrap.com/):
    * the project uses Bootstrap 4 to make the site responsive

* [Jquery](https://jquery.com/):
    * as part of Bootstrap, the project uses Jquery to simplify DOM manipulation

* [Popper.js](https://popper.js.org/):
    * the project uses Popper.js to create a tooltip that explain what the search form does.

* [Font Awesome](https://fontawesome.com/):
    * the project uses Font Awesome to add icon to the site and make it visually more desirable.
    
* [Flask](http://flask.palletsprojects.com/) and [Python](https://www.python.org/):
    * the project use the Flask framework which allows  to get up and running building the website with minimal Python code.

* [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)
    * the project uses MOngo a document-oriented database program, to store the data of the website.

* [PyMongo](https://api.mongodb.com/)
    * the project uses PyMongo to allow the interaction between the python application and MongoDB Atlas.

* [Google Font](https://fonts.google.com/):
    * the project uses google font to make the site visually nicer.

    
## Testing

* ##### link and navigation:
    1. go to the navbar and select a link to navigate through the site.
    2. verify that all links work and dropdown menu work properly.
    3. press any button on the website and check if it redirect to the correct page.

* ##### the CRUD functionality:
    1. go in the recipes page and see if the recipes are displayed correctly.
    2. try to digit a recipe name or an ingredients in the search form and verify that it returns the right recipes.
    3. try to digit an incorrect string or a recipe not present in the database in the recipe form and verify that it returns the message *"sorry no recipe found"*.
    4. select a checkbox and verify that the site return the right recipes.
    5. verify if the combination of the checkbox selected does not return anything from the database the display the message *"sorry no recipe found"*.
    6. Try to submit the empty form in addrecipe and verify that an error message about the required fields appears.
    7. Verify if the site after submittin the add form return the message *"your recipe has been submitted"*
    8. verify that the new recipe has been added in the site.
    9. Try to submit the empty form in edit recipe and verify that an error message about the required fields appears.
    10. verify that the edited recipe has been modified correctly.
    11. verify that the site, after edit a recipe return the message *"the recipe has been edited"*
    12. press the delete button and check if the recipe has been deleted.

* ##### responsiveness:
    1. verify the site maintain the expected layout on different screen resolution.
    2. verify the font size and the image are responsive in different screen resolution.

To let the site be responsive I used bootstrap 4, though the use of several media queries to adapt the site to different resolutions it proved necessary.
To check the site responsiveness the use of the google dev tool has been incredibly useful. 
I also check the site with my mobile which is a Samsung S7.

* ##### the code:
    1. html code validator has been used for the html.
    2. css code validator has been used for css.
    3. Python code works has expected and there are not error.

if I had to do a self-assessment, the site works as expected and all features work well. 
the css code is redundant and a bit chaotic and should be reorganized, but this would require a huge work in changing classes and IDs of the elements,
with the risk of creating even more chaos. Thanks to this project, however, I became aware of how I could better organize my work in the future, 
to better prevent this type of mistake.

## Deployment

The hosting provider Heroku has been used to host the site. This because Github pages only allow us to store static websites. 

To deploy the site I have done the following steps:

1. create a new app in Heroku with a unique name and Europe as location.
2. create the requirement.txt file with *sudo pip3 freeze --local > requirements.txt* in the local workspace.
3. add the requirements.txt file to the staging area and then commit.
4. create a procfile with *echo web: python app.py > Procfile* in the local workspace.
5. add the procfile to the staging area and then commit.
6. install heroku in the local workspace with *sudo snap install --classic heroku*.
7. through the terminal log in Heroku *with heroku login --interactive*.
8. with *heroku git:remote -a recipe-guide*  link the git repository to Heroku.
9. then push to Heroku with *git push heroku master*.
10. start a web process with *heroku ps:scale web=1* in the local workspace.
11. add  the variable IP with the value 0.0.0.0 on heroku settings.
12. add the variable PORT with the value 5000 on heroku settings.
13. add the variable MONGO_URI with its value on heroku settings.
14. add the secret_key with its value on heroku settings.
14. open the app.


To run the code locally open a terminal, make sure python3 is the right interpreter and digit *python3 app.py*.

* [Github](https://github.com/Baal89/recipe-app) repository
* [Heroku](https://recipe-guide.herokuapp.com/) deployed version

## Credits

#### content

* the text in the about page has been partially copied form  [i Genietti](http://www.genietti.it/) web page.
* the recipes are copied from the site [Giallo Zafferano](https://www.giallozafferano.it/).
* the utensil description are copied form the site [Nisbets](https://www.nisbets.co.uk/).

#### media 

* all the pictures used in the website have been taken from google and they are free of copyright.
* the video in about.html has been embedded from youtube and is free to use.
* the icons used in the recipe page come from the site [flaticon](https://www.flaticon.com/).

#### Acknowledgements

 * I received inspiration for this project from:
    * the website [Cookaround](https://www.cookaround.com/)
    * the website [i Genietti](http://http://www.genietti.it/).
    * the website [Giallo Zafferano](https://www.giallozafferano.it/).

A special thanks goes to my mentor Ali Ashik and to all tutor at codeinstitute who helped me create this project.

