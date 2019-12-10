#Shandy4u
Shandy4u is a both a cellar and a bartender - it allows you to search for
and save all your favorite beers and it recommends you new
beers based off what you like and what is popular. 

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