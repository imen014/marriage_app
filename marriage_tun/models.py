from django.db import models
from django.contrib.auth.models import AbstractUser


class UserRegister(AbstractUser):
    HOMME = 'homme'
    FEMME = 'femme'
    GENRE = [
        (HOMME, 'Homme'),
        (FEMME, 'Femme')
    ]
    SINGLE = 'single'
    MARRIED = 'married'
    DIVORCED = 'divorced'
    STATUS = [
        (SINGLE,'single'),
        (MARRIED,'married'),
        (DIVORCED,'divorced')
    ]
    genre = models.CharField(max_length=200, choices=GENRE)
    profil_photo = models.ImageField(upload_to='profile_pics/', blank=True, null=True, default='profile_pics/aucun_photo.png')
    phone_number = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    status = models.CharField(max_length=200, choices=STATUS)
    birthdate = models.DateField(null=True, blank=True)
    spiritual_belief = models.CharField(max_length=100, choices=[
        ('Agnostic', 'Agnostic'),
        ('Atheist', 'Atheist'),
        ('Christian', 'Christian'),
        ('Muslim', 'Muslim'),
        ('Hindu', 'Hindu'),
        ('Buddhist', 'Buddhist'),
        ('Other', 'Other')
    ], blank=True, null=True)
    
class ScoreChoices(models.IntegerChoices):
    NO = 0, "No"
    YES = 1, "Yes"


    
    
class Caracteres(models.Model):
    user = models.ForeignKey(UserRegister, on_delete=models.CASCADE)
    nerveux = models.IntegerField(choices=ScoreChoices.choices,default=ScoreChoices.NO)
    nice = models.IntegerField(choices=ScoreChoices.choices,default=ScoreChoices.NO)
    generous = models.IntegerField(choices=ScoreChoices.choices,default=ScoreChoices.NO)
    likes_outings = models.IntegerField(choices=ScoreChoices.choices,default=ScoreChoices.NO)
    frugal = models.IntegerField(choices=ScoreChoices.choices,default=ScoreChoices.NO) #mou9tased
    misspent =  models.IntegerField(choices=ScoreChoices.choices,default=ScoreChoices.NO) #moubadher
    available =  models.IntegerField(choices=ScoreChoices.choices,default=ScoreChoices.NO) #mouté7
    smoker =  models.IntegerField(choices=ScoreChoices.choices,default=ScoreChoices.NO) 
    drinks_wine =  models.IntegerField(choices=ScoreChoices.choices,default=ScoreChoices.NO) 
    chapel =  models.IntegerField(choices=ScoreChoices.choices,default=ScoreChoices.NO) #mousalli
    regular_prayer =  models.IntegerField(choices=ScoreChoices.choices,default=ScoreChoices.NO) #mou7afedh 3ala esalawét
    has_car =  models.IntegerField(choices=ScoreChoices.choices,default=ScoreChoices.NO)
    has_house =  models.IntegerField(choices=ScoreChoices.choices,default=ScoreChoices.NO)
    has_bank_account =  models.IntegerField(choices=ScoreChoices.choices,default=ScoreChoices.NO)
    riche =  models.IntegerField(choices=ScoreChoices.choices,default=ScoreChoices.NO)
    polygamous_relationships =  models.IntegerField(choices=ScoreChoices.choices,default=ScoreChoices.NO) #mouta3aded l'3ala9at
    score = models.IntegerField(default=0)  # New field to store the score

    def calculate_total_score(self):
        # Define the scoring for each field
        scoring_fields = {
            'nerveux': -10,
            'nice': 5,
            'generous': 15,
            'likes_outings': 20,
            'frugal': 5,
            'misspent': -5,
            'available': 10,
            'smoker': -20,
            'drinks_wine': -20,
            'chapel': 100,
            'regular_prayer': 100,
            'has_car': 30,
            'has_house': 50,
            'has_bank_account': 50,
            'riche': 100,
            'polygamous_relationships': -100
        }
        total_score = sum(
            scoring_fields[field] for field in scoring_fields
            if getattr(self, field) == ScoreChoices.YES
        )
        
        return total_score
    
    def save(self, *args, **kwargs):
        # Calculate and save the score each time the instance is saved
        self.score = self.calculate_total_score()
        super().save(*args, **kwargs)  # Call the original save() method

    def get_nervous_text(self):
        return "Yes" if self.nerveux == ScoreChoices.YES else "No"

    def get_nice_text(self):
        return "Yes" if self.nice == ScoreChoices.YES else "No"

    def get_generous_text(self):
        return "Yes" if self.generous == ScoreChoices.YES else "No"

    def get_likes_outings_text(self):
        return "Yes" if self.likes_outings == ScoreChoices.YES else "No"

    def get_frugal_text(self):
        return "Yes" if self.frugal == ScoreChoices.YES else "No"

    def get_misspent_text(self):
        return "Yes" if self.misspent == ScoreChoices.YES else "No"

    def get_available_text(self):
        return "Yes" if self.available == ScoreChoices.YES else "No"

    def get_smoker_text(self):
        return "Yes" if self.smoker == ScoreChoices.YES else "No"

    def get_drinks_wine_text(self):
        return "Yes" if self.drinks_wine == ScoreChoices.YES else "No"

    def get_chapel_text(self):
        return "Yes" if self.chapel == ScoreChoices.YES else "No"

    def get_regular_prayer_text(self):
        return "Yes" if self.regular_prayer == ScoreChoices.YES else "No"

    def get_has_car_text(self):
        return "Yes" if self.has_car == ScoreChoices.YES else "No"

    def get_has_house_text(self):
        return "Yes" if self.has_house == ScoreChoices.YES else "No"

    def get_has_bank_account_text(self):
        return "Yes" if self.has_bank_account == ScoreChoices.YES else "No"

    def get_riche_text(self):
        return "Yes" if self.riche == ScoreChoices.YES else "No"

    def get_polygamous_relationships_text(self):
        return "Yes" if self.polygamous_relationships == ScoreChoices.YES else "No"



class WantedCaracteres(models.Model):
    user = models.ForeignKey(UserRegister, on_delete=models.CASCADE)
    nerveux = models.IntegerField(choices=ScoreChoices.choices,default=ScoreChoices.NO)
    nice = models.IntegerField(choices=ScoreChoices.choices,default=ScoreChoices.NO)
    generous = models.IntegerField(choices=ScoreChoices.choices,default=ScoreChoices.NO)
    likes_outings = models.IntegerField(choices=ScoreChoices.choices,default=ScoreChoices.NO)
    frugal = models.IntegerField(choices=ScoreChoices.choices,default=ScoreChoices.NO) #mou9tased
    misspent =  models.IntegerField(choices=ScoreChoices.choices,default=ScoreChoices.NO) #moubadher
    available =  models.IntegerField(choices=ScoreChoices.choices,default=ScoreChoices.NO) #mouté7
    smoker =  models.IntegerField(choices=ScoreChoices.choices,default=ScoreChoices.NO) 
    drinks_wine =  models.IntegerField(choices=ScoreChoices.choices,default=ScoreChoices.NO) 
    chapel =  models.IntegerField(choices=ScoreChoices.choices,default=ScoreChoices.NO) #mousalli
    regular_prayer =  models.IntegerField(choices=ScoreChoices.choices,default=ScoreChoices.NO) #mou7afedh 3ala esalawét
    has_car =  models.IntegerField(choices=ScoreChoices.choices,default=ScoreChoices.NO)
    has_house =  models.IntegerField(choices=ScoreChoices.choices,default=ScoreChoices.NO)
    has_bank_account =  models.IntegerField(choices=ScoreChoices.choices,default=ScoreChoices.NO)
    riche =  models.IntegerField(choices=ScoreChoices.choices,default=ScoreChoices.NO)
    polygamous_relationships =  models.IntegerField(choices=ScoreChoices.choices,default=ScoreChoices.NO) #mouta3aded l'3ala9at
    score = models.IntegerField(default=0)  # New field to store the score

    def calculate_total_score(self):
        # Define the scoring for each field
        scoring_fields = {
            'nerveux': -10,
            'nice': 5,
            'generous': 15,
            'likes_outings': 20,
            'frugal': 5,
            'misspent': -5,
            'available': 10,
            'smoker': -20,
            'drinks_wine': -20,
            'chapel': 100,
            'regular_prayer': 100,
            'has_car': 30,
            'has_house': 50,
            'has_bank_account': 50,
            'riche': 100,
            'polygamous_relationships': -100
        }
        total_score = sum(
            scoring_fields[field] for field in scoring_fields
            if getattr(self, field) == ScoreChoices.YES
        )
        
        return total_score
    

    def save(self, *args, **kwargs):
        # Calculate and save the score each time the instance is saved
        self.score = self.calculate_total_score()
        super().save(*args, **kwargs)  # Call the original save() method

    def get_nervous_text(self):
        return "Yes" if self.nerveux == ScoreChoices.YES else "No"

    def get_nice_text(self):
        return "Yes" if self.nice == ScoreChoices.YES else "No"

    def get_generous_text(self):
        return "Yes" if self.generous == ScoreChoices.YES else "No"

    def get_likes_outings_text(self):
        return "Yes" if self.likes_outings == ScoreChoices.YES else "No"

    def get_frugal_text(self):
        return "Yes" if self.frugal == ScoreChoices.YES else "No"

    def get_misspent_text(self):
        return "Yes" if self.misspent == ScoreChoices.YES else "No"

    def get_available_text(self):
        return "Yes" if self.available == ScoreChoices.YES else "No"

    def get_smoker_text(self):
        return "Yes" if self.smoker == ScoreChoices.YES else "No"

    def get_drinks_wine_text(self):
        return "Yes" if self.drinks_wine == ScoreChoices.YES else "No"

    def get_chapel_text(self):
        return "Yes" if self.chapel == ScoreChoices.YES else "No"

    def get_regular_prayer_text(self):
        return "Yes" if self.regular_prayer == ScoreChoices.YES else "No"

    def get_has_car_text(self):
        return "Yes" if self.has_car == ScoreChoices.YES else "No"

    def get_has_house_text(self):
        return "Yes" if self.has_house == ScoreChoices.YES else "No"

    def get_has_bank_account_text(self):
        return "Yes" if self.has_bank_account == ScoreChoices.YES else "No"

    def get_riche_text(self):
        return "Yes" if self.riche == ScoreChoices.YES else "No"

    def get_polygamous_relationships_text(self):
        return "Yes" if self.polygamous_relationships == ScoreChoices.YES else "No"

   

class Message(models.Model):
  
    sender = models.ForeignKey(
        UserRegister, on_delete=models.CASCADE, related_name='message_sender'
    )
    receiver = models.ForeignKey(
        UserRegister, on_delete=models.CASCADE, related_name='message_receiver'
    )
    creation_date = models.DateField(auto_now_add=True)
    message_content = models.CharField(max_length=200)
    message_title = models.CharField(max_length=50)

    def __str__(self):
        return f"Contact from {self.user_asked_date} to {self.user_to_confirm_date} - {self.state}"
