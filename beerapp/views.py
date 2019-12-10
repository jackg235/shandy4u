from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
import pandas as pd
from beerapp.models import *
from beerapp.recommender import *


# reads in our file containing information for over 5k beers. this should only be called once in initialization
def readfile():
    data = pd.read_csv('/Users/jackgoettle/Downloads/beer-db.csv', header=0, error_bad_lines=False, encoding='latin-1')
    data = data.fillna(0)
    for idx, row in data.iterrows():
        name = data['Name'][idx]
        abv = data['Alcohol By Volume'][idx]
        bitterness = data['International Bitterness Units'][idx]
        style = data['Style'][idx]
        category = data['Category'][idx]
        brewer = data['Brewer'][idx]
        city = data['City'][idx]
        state = data['State'][idx]
        country = data['Country'][idx]
        website = data['Website'][idx]
        description = data['Description'][idx]
        json = {'name': name, 'abv': abv, 'bitterness': bitterness, 'style': style, 'category': category,
                'brewer': brewer, 'city': city, 'state': state, 'country': country, 'website': website}
        if not Drink.objects.filter(name=name).exists():
            drink = Drink.objects.create(name=name, abv=abv, description=description, bitterness=bitterness, style=style,
                                     category=category, brewer=brewer, city=city, state=state, country=country,
                                     website=website)
    return


# allows user to log in or sign up
def splash(request):
    print("rendering splash page")
    #readfile() --> ONLY TO BE CALLED ONCE WHEN LOADING DATA
    return render(request, "splash.html", {})


# authorize log in
def loginauth(request):
    if request.method == "POST":

        user = authenticate(
            username=request.POST['username'], password=request.POST['password'])
        # check to make sure user exists
        if user is not None:
            login(request, user)
            print("log in success")
            return redirect('/home')

    print("user does not exist")
    return redirect('/login_page')


# render log in page
def login_page(request):
    return render(request, "login.html", {})


# render home page
def home(request):
    # get the most popular drinks
    drinks = Drink.objects.all().order_by('-popular')
    # get recommended drinks
    recs = getRecommendations(Drink.objects.filter(users=request.user), drinks)
    for r in recs :
        print(r)
    popular = []
    for d in drinks:
        if d.popular < 1:
            break
        # only include drinks that the user has not already favorited
        if not d.users.filter(username=request.user.username).exists():
            if d.style != 'nan' and d.category != 'nan':
                popular.append(d)

    return render(request, "home.html", {'username': request.user.username, 'recs': recs, 'popular': popular})


# render registration page
def registration_page(request):
    print("rendering registration page")
    return render(request, "registration.html", {})


# register a new user
def register(request):
    if request.method == "POST":
        if User.objects.filter(username=request.POST['username']).exists():
            print("username already exists")
            return redirect('/registration_page')
        # create new user
        user = User.objects.create_user(username=request.POST['username'], email=request.POST['email'],
                                        password=request.POST['password'], first_name=request.POST['first'],
                                        last_name=request.POST['last'])
        login(request, user)
        return redirect('/home')
    return redirect('/registration_page')


# render user profile
def profile(request):
    popular = Drink.objects.filter(users=request.user)
    drinks = Drink.objects.all()
    return render(request, 'profile.html', {'popular': popular, 'drinks': drinks})


# favorite/unfavorite a beer
def favorite(request):
    drink = Drink.objects.get(name=request.GET['drink'])
    # if the user has already favorited the drink, unfavorite it
    if drink.users.filter(username=request.user.username).exists():
        drink.users.remove(request.user)
        drink.popular = drink.popular - 1
    # if the user has not already favorited the drink, favorite it
    else:
        drink.users.add(request.user)
        drink.popular = drink.popular + 1
    drink.save()
    return redirect('/profile')


# log out the current user
def logout_view(request):
    logout(request)
    return redirect("/")
