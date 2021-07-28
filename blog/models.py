from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='child_set', on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    text = models.TextField()

    def __str__(self):
        return self.text
