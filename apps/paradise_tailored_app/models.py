from django.db import models


class Destination(models.Model):
    title = models.CharField(max_length=300)
    country = models.CharField(max_length=300)
    city = models.CharField(max_length=300)
    description = models.TextField()
    swimming = models.CharField(max_length=300)
    price = models.CharField(max_length=300)
    hiking = models.CharField(max_length=300)
    dining = models.CharField(max_length=300)
    luxury = models.CharField(max_length=300)
    shopping = models.CharField(max_length=300)
    fishing = models.CharField(max_length=300)
    surfing = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Question(models.Model):
    question_text = models.CharField(max_length=500)
    category = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category


class Choice(models.Model):
    question = models.ForeignKey(Question,related_name="choices" , on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=500)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

class Subscriber(models.Model):
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    email = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email