from django.urls import path
from . import views
from .views import IndexPage,NewPersonPage,DietForm,DetailForm,ViewPage

urlpatterns = [
    # path('',views.PersonListView(),name='add-user'),
    # path('add/',views.PersonCreateView(), name = 'create-user'),
    # path('<int:pk>/',views.PersonUpdateView(),name='update_user')
    path('',IndexPage.as_view(),name='index'),
    path('new_person/',NewPersonPage.as_view(),name='new_person'),
    path('add_diet/',DietForm.as_view(),name='add_diet'),
    path('add_details/',DetailForm.as_view(),name= 'add_details'),
    path('view_page/',ViewPage.as_view(),name='view_page')
]