from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
class Tag(models.Model):
    caption = models.CharField(max_length = 20)

    def __str__(self):
        return self.caption

class Author(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    email_address = models.EmailField()

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self):
        return self.full_name()

class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    date = models.DateField(auto_now = True)
    image = models.ImageField(upload_to="posts", null=True)
    supportingimage = models.ImageField(upload_to="posts", null=True, blank=True)
    supportingimage2 = models.ImageField(upload_to="posts", null=True, blank=True)
    supportingimage3 = models.ImageField(upload_to="posts", null=True, blank=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    content2 = models.TextField(validators=[MinLengthValidator(10)], null=True)
    content3 = models.TextField(validators=[MinLengthValidator(10)], null= True)
    excerpt = models.CharField(max_length = 100)
    slug = models.SlugField(unique=True, db_index = True)
    author = models.ForeignKey(
        Author, on_delete=models.SET_NULL, null=True, related_name="posts")
    tags = models.ManyToManyField(Tag)

   







