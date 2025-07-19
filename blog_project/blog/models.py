from django.db import models
from django.utils.text import slugify
from django.utils import timezone

class Comment(models.Model):
    post = models.ForeignKey(BlogPost, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    body = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Comment by {self.name} on {self.post}'


class BlogPost(models.Model):
    CATEGORY_CHOICES = [
        ('tech', 'Tech'),
        ('lifestyle', 'Lifestyle'),
        ('travel', 'Travel'),
        ('food', 'Food'),
        ('education', 'Education'),
    ]

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    content = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Auto-generate slug from title if not provided
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
