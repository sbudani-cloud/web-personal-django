from django.db import models

class Post(models.Model):
    title = models.CharField(max_length = 255)
    slug = models.SlugField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    description = models.CharField(max_length=1250)
    
    class Meta:
        ordering = ('-created_at',)
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments',on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    
    class Meta:
            ordering = ('-created_at',)
    
    def __str__(self):
            return f'{self.name} - {self.post.title}'
        
class Tag(models.Model):
    category = models.CharField(max_length=60)
    posts = models.ManyToManyField(Post, related_name="tags")
    
    def __str__(self):
        return f'{self.category}'