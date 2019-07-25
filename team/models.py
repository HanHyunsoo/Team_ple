from django.db import models
from account.models import User


# Create your models here.
class Team(models.Model):
    """
    invitation_code 초대코드를 primary_key로 할까 고민중
    또 어떤 방식으로 생성해야할지 고민중
    """
    team_leader = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    team_name = models.CharField(blank=False, max_length=20)
    introduce = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    team_photo_url = models.ImageField(upload_to='images/team/{}/'.format(id), blank=True)
    created_date = models.DateTimeField(auto_now_add=True, editable=False)
    members = models.ManyToManyField(User, related_name='members', through='TeamMember')

    def __str__(self):
        return self.team_name


class TeamMember(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username, self.team.team_name


