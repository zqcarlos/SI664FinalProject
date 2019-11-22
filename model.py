from django.db import models

# Create your models here.

class Nationality(models.Model):
    nation_name = models.CharField(max_length=30,null=True)
    nation_flag = models.CharField(max_length=255,null = True)
    ages = models.ManyToManyField('Age', through='Player')
    clubs = models.ManyToManyField('Club', through='Player')
    def __str__(self):
        return self.nation_name

class Overall_Score(models.Model):
    score = models.IntegerField(null=True)
    nations = models.ManyToManyField('Nationality', through='Player')
    clubs = models.ForeignKey('Club', on_delete=models.CASCADE)
    def __str__(self):
        return self.score

class Potential_Score(models.Model):
    score = models.IntegerField(null=True)
    clubs = models.ForeignKey('Club', on_delete=models.CASCADE)
    def __str__(self):
        return self.score

class Position(models.Model):
    position_name = models.CharField(max_length=30,null=True)
    def __str__(self):
        return self.position_name

class Club(models.Model):
    club_name = models.CharField(max_length=30 ,null=True)
    club_logo = models.CharField(max_length=255,null=True)
    nations = models.ManyToManyField('Nationality', through='Player')
    def __str__(self) :
        return self.club_name


class Age(models.Model):
    num=models.IntegerField(null=True)
    def __str__(self) :
        return self.num

class Player(models.Model):
    player_id = models.IntegerField(null = True)
    player_name = models.CharField(max_length=30, null=True)
    player_photo = models.CharField(max_length=30, null = True)
    join_date = models.DateField(null = True)

    age = models.ForeignKey(Age, on_delete=models.CASCADE)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    nation = models.ForeignKey(Nationality, on_delete=models.CASCADE)
    overall_score = models.ForeignKey(Overall_Score, on_delete=models.CASCADE)
    potential_score = models.ForeignKey(Potential_Score, on_delete=models.CASCADE)
    def __str__(self):
        return self.player_name