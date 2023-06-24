from django.db import models
from django.urls import reverse
from core.settings import AUTH_USER_MODEL

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
    
class Task(models.Model):
    state = models.ForeignKey("State", on_delete=models.CASCADE)
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=255)
    due_task = models.DateField()
    
    class Meta:
        ordering = ["state", "user", "titulo", "due_task"]

    def get_absoluted_url(self):
        return reverse('task', args=[str(self.id)])
    
    def __str__(self):
        return f"titulo: {self.titulo}"
    
class Comments(models.Model):
    task = models.ForeignKey("Task", on_delete=models.CASCADE)
    body = models.CharField(max_length=250)
    
    class Meta:
        ordering = ["task", "body"]

    def get_absoluted_url(self):
        return reverse('comments', args=[str(self.id)])
    
    def __str__(self):
        return f"task: {self.task}, body: {self.body}"