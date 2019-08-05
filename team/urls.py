from django.urls import path
from . import views
app_name = 'team'
urlpatterns = [
    path('create_team/<int:user_id>/',views.create_team, name='create_team'),
    path('<int:team_id>/<int:user_id>/', views.detail_team, name="detail_team"),
    path('<int:team_id>/<int:user_id>', views.add_member,name="add_member"),
    path('<int:team_id>/<int:user_id>/expulsion_member/', views.expulsion_member, name="expulsion_member"),
    # path('<int:team_id>/<int:user_id>/team_delete/', views.team_delete, name="team_delete"),
    path('<int:team_id>/<int:user_id>/leave_team/',views.leave_team, name='leave_team'),
    
]