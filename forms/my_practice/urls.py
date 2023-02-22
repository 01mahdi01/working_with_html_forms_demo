from django.urls import path
from . import views

urlpatterns = [
    path("", views.startingpage,name="start"),
    path('signuppage/', views.signuppage,name="signup"),
    path('login/',views.loginpage,name="login"),
    path('authentication/',views.authentication,name='list'),

    path('signup/',views.signup,name="test"),
    
    path('product_list_page/',views.productlist,name="listpage"),
    # path('<slug>',views.chosenproductpage,name="thepruduct"),
    path('vote/<pvote>/<uvote>/',views.vvote,name="vote"),
    
]
