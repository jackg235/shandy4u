from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
import requests
import pandas as pd
from beerapp.models import *


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
    response = requests.get('http://freegeoip.net/json/')
    geodata = response.json()
    print(geodata)
    return render(request, "home.html", {})


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
        user = User.objects.create_user(username=request.POST['username'], email=request.POST['email'],
                                        password=request.POST['password'], first_name=request.POST['first'],
                                        last_name=request.POST['last'])
        return redirect('/home')
    return redirect('/registration_page')


# favorite a beer
def favorite(request):
    if request.method == "POST":
        if not User.objects.filter(username=request.POST['username']).exists():
            print("Beer added to favorites!")
            #add beer object to drinks database for user, not sure how


# un-favorite a beer
def unFavorite(request):
    if request.method == "POST":
        if User.objects.filter(username=request.POST['username']).exists():
            print("Beer removed favorites!")
            #remove beer object to drinks database for user, not sure how


# log out the current user
def logout_view(request):
    logout(request)
    return redirect("/")
