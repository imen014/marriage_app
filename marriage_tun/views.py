from django.shortcuts import render, redirect
from .forms import Register, Login, Caraceters_auth, WantedCaraceters_auth, MessageForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Caracteres, WantedCaracteres, UserRegister, Message
from django.db.models import Q

def register(request):
    form = Register()
    message = ""
    if request.method=="POST":
        form = Register(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            message = "Welcome ! Ure registered successfully!"
            return redirect('home')
        form = Register(request.POST)
        message = "Invalid data"
    return render(request, "marriage_tun/regiter.html", {"message":message,"form":form})

def login_user(request):
    form = Login()
    message = ""
    if request.method == "POST":
        form = Login(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
        form = Login(request.POST)
        message = "Invalid data"
    return render(request, "marriage_tun/login.html", {"message":message, "form":form})
        

def home(request):
    return render(request, "marriage_tun/home.html")


def logout_user(request):
    logout(request)
    return redirect('login')


def delete_my_profil(request):
    user = request.user
    if request.method == "POST":
        logout(request)
        user.delete()
        messages.success(request, "u're account has deleted successufully !")
        return redirect('register')
    return render(request, "marriage_tun/confirm_delete.html")


@login_required
def get_my_profil(request):
    user = request.user
    return render(request, "marriage_tun/get_auth_profil.html",{"user":user})


@login_required
def create_auth_profil(request):
    form = Caraceters_auth()
    if request.method == "POST":
        form = Caraceters_auth(request.POST)
        if form.is_valid():
            caracters = form.save(commit=False)
            caracters.user = request.user
            existed_auth_caracters = Caracteres.objects.filter(user=request.user)
            if not existed_auth_caracters:
                caracters.save()
                return redirect('home')
            else:
                messages.error(request, "u have already create u're caracter profil")
        else:
            form = Caraceters_auth(request.POST)
            messages.error(request, "Invalid data !")
    return render(request, "marriage_tun/create_auth_caracetres.html", {'form':form})


@login_required
def get_auth_caracters(request):
    caraceters_auth = Caracteres.objects.filter(user=request.user)
    return render(request, "marriage_tun/get_my_caracters.html", {"caraceters_auth":caraceters_auth})


def delete_my_caracters(request):
    caracters_auth = Caracteres.objects.filter(user=request.user)
    caracters_auth.delete()
    messages.success(request, "u're caracters deleted successfully !")
    return redirect('home')


def update_auth_caracters(request):
    caractere_instance = Caracteres.objects.filter(user=request.user).first()
    caracters = Caraceters_auth(instance=caractere_instance)
    if request.method == "POST":
        caracters = Caraceters_auth(request.POST,instance=caractere_instance)
        if caracters.is_valid():
            caracters.save()
            return redirect('get_auth_caracters')
        else:
            caracters = Caraceters_auth(request.POST,instance=caractere_instance)
            messages.error(request, "Invalid data !")
    return render(request, "marriage_tun/update_auth_caracters.html",{"caracters":caracters})
    

@login_required
def create_wanted_profil(request):
    form = WantedCaraceters_auth()
    if request.method == "POST":
        form = WantedCaraceters_auth(request.POST)
        if form.is_valid():
            caracters = form.save(commit=False)
            caracters.user = request.user
            existed_auth_caracters = WantedCaracteres.objects.filter(user=request.user)
            if not existed_auth_caracters:
                caracters.save()
                return redirect('home')
            else:
                messages.error(request, "u have already a wanted profil created!")
        else:
            form = Caraceters_auth(request.POST)
            messages.error(request, "Invalid data !")
    return render(request, "marriage_tun/create_wanted_caracetres.html", {'form':form})


@login_required
def get_wanted_caracters(request):
    caraceters_auth = WantedCaracteres.objects.filter(user=request.user)
    return render(request, "marriage_tun/get_wanted_caracters.html", {"caraceters_auth":caraceters_auth})

def delete_wanted_caracters(request):
    caracters_auth = WantedCaracteres.objects.filter(user=request.user)
    caracters_auth.delete()
    messages.success(request, "u're caracters deleted successfully !")
    return redirect('home')

def update_wanted_caracters(request):
    caractere_instance = WantedCaracteres.objects.filter(user=request.user).first()
    caracters = Caraceters_auth(instance=caractere_instance)
    if request.method == "POST":
        caracters = Caraceters_auth(request.POST,instance=caractere_instance)
        if caracters.is_valid():
            caracters.save()
            return redirect('get_wanted_caracters')
        else:
            caracters = Caraceters_auth(request.POST,instance=caractere_instance)
            messages.error(request, "Invalid data !")
    return render(request, "marriage_tun/update_wanted_caracters.html",{"caracters":caracters})
    


@login_required
def matching_partenaires(request):
    partenaire = None
    partenaire_profil = None
    message = ""
    wanted_profil = WantedCaracteres.objects.filter(user=request.user).first()
    if wanted_profil:
        partenaire = Caracteres.objects.filter(
        nerveux=wanted_profil.nerveux,
        nice=wanted_profil.nice,
        generous=wanted_profil.generous,
        likes_outings=wanted_profil.likes_outings,
        frugal=wanted_profil.frugal,
        misspent=wanted_profil.misspent,
        smoker=wanted_profil.smoker,
        drinks_wine=wanted_profil.drinks_wine,
        chapel=wanted_profil.chapel,
        available=wanted_profil.available,
        regular_prayer=wanted_profil.regular_prayer,
        has_car=wanted_profil.has_car,
        has_house=wanted_profil.has_house,
        has_bank_account=wanted_profil.has_bank_account,
        riche=wanted_profil.riche,
        polygamous_relationships=wanted_profil.polygamous_relationships,
    ).exclude(user__genre=request.user.genre).first()
        if partenaire:
                message = "partenaire found successfully!"
        else:
                message =  "partenaire with this criteria was not found!"
    return render(request, "marriage_tun/matching_partenaires_all_wanted_caraceters.html",{"partenaire":partenaire,"partenaire_profil":partenaire_profil,"message":message})

@login_required
def get_user_profil(request,id):
    user = UserRegister.objects.get(id=id)
    return render(request, "marriage_tun/get_other_user_profil.html",{"user":user})



@login_required
def get_auth_score(request):
    catacters = Caracteres.objects.get(user=request.user)
    score = catacters.calculate_total_score()  # This will update and return the score
    return render(request, "marriage_tun/home.html", {'score': score})


@login_required
def searching_suitable_partenaire_by_score(request):
    auth_caracter = Caracteres.objects.get(user=request.user)
    suitable_partners = Caracteres.objects.filter(Q(score__lte=auth_caracter.score+10) & Q(score__gte=auth_caracter.score-10)).exclude(user__genre=request.user.genre)
    if suitable_partners:
        message = "suitable partners founded successfully!"
    else:
        message = "No suitable partners found!"

    return render(request, "marriage_tun/suitable_partners.html", {'suitable_partners': suitable_partners,"message":message})

    
def get_all_users_score(request):
    caracters = Caracteres.objects.all()
    return render(request, "marriage_tun/get_all_score.html",{"caracters":caracters})



@login_required
def send_a_message(request,id):
    form = MessageForm()
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.receiver = UserRegister.objects.get(id=id)
            message.save()
            messages.success(request, "u're message sended succefully!")
        else:
            messages.error(request, "Invalid data!")
            form = MessageForm(request.POST)
    return render(request, "marriage_tun/send_a_message.html",{"form":form})



@login_required    
def get_my_messages(request):
    messages = Message.objects.filter(Q(sender=request.user) | Q(receiver=request.user))
    return render(request, "marriage_tun/get_my_messages.html",{"messages":messages})


@login_required
def delete_a_message(request,id):
    message = Message.objects.get(id=id)
    message.delete()
    return redirect('get_my_messages')
