from django.db import models

# Create your models here.


from django.db import models

# ----------------------------
# Example: Defining a Simple Model
# ----------------------------

# Here is an example of a basic model class. It represents a 'Book' in the system:
class Book(models.Model):
    title = models.CharField(max_length=100)  # Title of the book (up to 100 characters)
    author = models.CharField(max_length=100)  # Author's name
    published_date = models.DateField()  # Publication date of the book
    is_available = models.BooleanField(default=True)  # Availability of the book

    def __str__(self):
        return f"{self.title} by {self.author}"


