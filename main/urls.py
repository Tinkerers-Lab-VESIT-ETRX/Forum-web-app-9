from django.urls import path
from . import views

urlpatterns = [
	path('register', views.registerPage, name='register'),
	path('login', views.loginPage, name='login'),
	path('logout', views.logoutPage, name='logout'),
	path('', views.homePage, name='index'),
	path('new-forum', views.newForumPage, name='new-forum'),
	path('forum/<int:id>', views.forumPage, name='forum'),
	path('reply', views.replyPage, name='reply')
]