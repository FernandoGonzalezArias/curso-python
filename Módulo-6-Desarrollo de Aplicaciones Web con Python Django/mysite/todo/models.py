from django.db import models
from django.urls import reverse

# Create your models here.
class State(models.Model):
    
    name = models.CharField(max_length=20)
    color = models.CharField(max_length=6)
    idDone = models.BooleanField()
    
    class Meta:
        ordering = ["name"]
        
    def get_absoluted_url(self):
        return reverse('state', args=[str(self.id)])
        
    def __str__(self):
        return f"name: {self.name}, color: {self.color}, isDone: {self.idDone}"
    
class Author(models.model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    
    class Meta:
        ordering = ["first_name", "last_name"]
        
    def get_absoluted_url(self):
        return reverse('author', args=[str(self.id)])
    
    def __str__(self):
        return f"first_name: {self.first_name}, last_name: {self.last_name}"
    
class Task(models.Model):
    state = models.ForeignKey("State", on_delete=models.CASCADE)
    author = models.ForeignKey("Author", on_delete=models.CASCADE)
    titulo = models.CharField(max_length=255)
    due_task = models.DateField()
    
    class Meta:
        ordering = ["state", "author", "titulo", "due_task"]

    def get_absoluted_url(self):
        return reverse('task', args=[str(self.id)])
    
    def __str__(self):
        return "titulo: {self.titulo}"
    
class Comments(models.Model):
    task = models.ForeignKey("Task", on_delete=models.CASCADE)
    body = models.CharField(max_length=250)
    
    class Meta:
        ordering = ["task", "body"]

    def get_absoluted_url(self):
        return reverse('comments', args=[str(self.id)])
    
    def __str__(self):
        return f"task: {self.task}, body: {self.body}"