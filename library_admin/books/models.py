from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    review_text = models.TextField()
    rating = models.IntegerField()

    def __str__(self):
        return f"{self.book.title} - Rating: {self.rating}"
