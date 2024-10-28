
from django.contrib import admin
from django.urls import path
from marriage_tun import views
from marriage_app import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.register, name="register"),
    path('login/', views.login_user, name="login"),
    path('home/', views.home, name="home"),
    path('logout/', views.logout_user, name="logout_user"),
    path('account_deletion/', views.delete_my_profil , name="account_deletion"),
    path('get_my_profil/', views.get_my_profil , name="get_my_profil"),
    path('create_auth_profil/', views.create_auth_profil , name="create_auth_profil"),
    path('get_auth_caracters/', views.get_auth_caracters , name="get_auth_caracters"),
    path('delete_my_caracters/', views.delete_my_caracters , name="delete_my_caracters"),
    path('update_auth_caracters/', views.update_auth_caracters , name="update_auth_caracters"),
    path('create_wanted_profil/', views.create_wanted_profil , name="create_wanted_profil"),
    path('get_wanted_caracters/', views.get_wanted_caracters , name="get_wanted_caracters"),
    path('delete_wanted_caracters/', views.delete_wanted_caracters , name="delete_wanted_caracters"),
    path('update_wanted_caracters/', views.update_wanted_caracters , name="update_wanted_caracters"),
    path('get_user_profil/<int:id>/', views.get_user_profil , name="get_user_profil"),
    path('matching_partenaires/', views.matching_partenaires , name="matching_partenaires"),
    path('get_auth_score/', views.get_auth_score , name="get_auth_score"),
    path('searching_suitable_partenaire_by_score/', views.searching_suitable_partenaire_by_score , name="searching_suitable_partenaire_by_score"),
    path('get_all_users_score/', views.get_all_users_score , name="get_all_users_score"),
    path('send_a_message/<int:id>/', views.send_a_message , name="send_a_message"),
    path('get_my_messages/', views.get_my_messages , name="get_my_messages"),
    path('delete_a_message/<int:id>/', views.delete_a_message , name="delete_a_message"),


]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

