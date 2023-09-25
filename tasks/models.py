from django.db import models
from django.contrib.auth.models import AbstractUser , User

# Create your models here.

Tasks_Status = (
    ("Opened","Opened") ,
    ("Done","Done") ,
    ("Cancelled","Cancelled"),
)

class Agent(AbstractUser):
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='marketer_user_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='agent permissions',
    )
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='marketer_user_set',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name ="agent"
        verbose_name_plural = "agents"

    def __str__(self):
        return self.username



class Task(models.Model):
    agent = models.ForeignKey(Agent,on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Task Name',max_length=50)
    description = models.TextField(verbose_name='Descreption of task',max_length=1000)
    published_at = models.DateTimeField(verbose_name='Published At',auto_now_add=True)
    deadline_date = models.DateField(verbose_name='Deadline Date',blank=True,null=True)
    deadline_time = models.TimeField(verbose_name='Deadline Time',blank=True,null=True)
    status = models.CharField(
                verbose_name = 'Task Status' ,
                max_length = 50 ,
                choices = Tasks_Status ,
                default = "Opened" ,
            )
    agent_note = models.CharField(verbose_name="Agent Note",max_length=500,null=True,blank=True)

    def __str__(self):
        return f"{self.name} - {self.agent} - {self.status}"
    
        