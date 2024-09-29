from django.urls import path
from .views import edit_profile_view, profile_view,showcase_view
from .views import add_project_view, edit_project_view, delete_project_view
from .views import (
    portfolio_view, add_work_experience, edit_work_experience,
    add_education, edit_education, add_certification, edit_certification
)

urlpatterns = [
     path('', portfolio_view, name='portfolio_view'),
    path('profile/', profile_view, name='profile_view'),
    path('profile/edit/', edit_profile_view, name='edit_profile'),
    path('portfolio/work-experience/add/', add_work_experience, name='add_work_experience'),
    path('portfolio/work-experience/edit/<int:pk>/', edit_work_experience, name='edit_work_experience'),
    path('portfolio/education/add/', add_education, name='add_education'),
    path('portfolio/education/edit/<int:pk>/', edit_education, name='edit_education'),
    path('portfolio/certification/add/', add_certification, name='add_certification'),
    path('portfolio/certification/edit/<int:pk>/', edit_certification, name='edit_certification'),
    path('add-project/', add_project_view, name='add_project'),
    path('portfolio/edit-project/<int:project_id>/', edit_project_view, name='edit_project'),
    path('portfolio/delete-project/<int:project_id>/', delete_project_view, name='delete_project'),
    path('showcase/', showcase_view, name='showcase_view'),
]
