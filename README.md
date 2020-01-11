##Shandy4u
Shandy4u is a both a cellar and a bartender - it allows you to search for
and save all your favorite beers and it recommends you new
beers based off what you like and what is popular.

### Implementation Requirments

Class + magic methods:
__str__ (to string method)
__eq__ (equals method) within the Drink model

First party packages:
math (formatting abv when displaying on screen),
random (add a random drink to the recommendations)

Third party packages:
Django (web + app design),
SKLearn (recommendation model),
pandas (recommendation model)

### Installation Instructions
To run shandy4u, cd to the outer "shandy4u" directory 
and type "python manage.py runserver" into the terminal

### Code Structure
recommender.py contains the code for the recommendation algorithm which
uses k-means clustering to find out which drinks the user is most likely
to enjoy. 

models.py contains the beer model

views.py contains all of the routes necessary to have a 
functioning frontend, including log in, log out, registration,
favoriting a beer, unfavoriting a beer, and the rendering for
our django apps pages. 
