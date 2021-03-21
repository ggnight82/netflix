from django.db import models

# Create your models here.

class Genres(models.Model):
    genre_genre = models.CharField(max_length=20)

    def __str__(self):
        return self.genre_genre


class Actors(models.Model):
    actor_name = models.CharField(max_length=20)

    def __str__(self):
        return self.actor_name

class Productions(models.Model):
    productions_name = models.CharField(max_length=20)

    def __str__(self):
        return self.productions_name

    
class Contents(models.Model):
    contents_id = models.BigAutoField(help_text="CONTENTS ID", primary_key=True) 
    contents_title = models.CharField(max_length=50)
    contents_description = models.TextField()
    contents_created_at = models.DateTimeField(auto_now_add=True)
    contents_updated_at = models.DateTimeField(auto_now=True)
    contents_genre = models.ManyToManyField(Genres)
    contents_actor = models.ManyToManyField(Actors)
    contents_productions = models.OneToOneField(Productions,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.contents_title

class Videos(models.Model):
    video_season = models.IntegerField(default=0)
    video_episode = models.IntegerField(default=0)
    video_id = models.BigAutoField(help_text="VIDEO ID", primary_key=True)
    video_file = models.FileField(upload_to="../MEDIA",null=True)
    contents_id = models.ForeignKey(Contents, related_name="content", on_delete=models.CASCADE, db_column="post_id")

    def __str__(self):
        return self.contents
