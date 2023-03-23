from django.urls import path
from .views import * 

urlpatterns = [
    path('',home,name='home'),
    path('base/',base,name='base'),
    path('navToCreateContact/',navToCreateContactForm,name='navToCreateContact'),
    path('navToEditContact/',navToEditContactForm,name='navToEditContactForm'),
    path('list/',ListContactsView.as_view(),name='listContacts'),
    path('create/',CreateContactsView.as_view(),name='createContacts'),
    path('retrieve/<str:user_input>/',RetrieveContactsView.as_view(),name='retrieveContact'),
    path('update/<str:user_input>/',UpdateContactsView.as_view(),name='updateContact'),
    path('destroy/<int:pk>/',DestroyContactsView.as_view(),name='destroyContact'),
    
]