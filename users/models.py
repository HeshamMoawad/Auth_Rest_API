from django.db import models
from django.contrib.auth.models import AbstractUser


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


class MacAddress(models.Model):
    user = models.ForeignKey(Agent,on_delete=models.CASCADE,default=0)
    mac_address = models.CharField(max_length=30,verbose_name='MacAddress',null=True,unique=True)
    agent_name = models.CharField(max_length=100,verbose_name='Agent Name',null=True,blank=True)

    def __str__(self):
        return self.agent_name

    class Meta:
        verbose_name = 'Mac Address'
        verbose_name_plural = "Mac Addresses"


class TelegramBot(models.Model):
    name = models.CharField(max_length=100,verbose_name='Bot Name')
    key = models.CharField(max_length=150,verbose_name='Bot Key')
    url = models.CharField(max_length=150,verbose_name='Bot Url',blank=True)

    class Meta:
        verbose_name ="telegram Bot"
        verbose_name_plural = "telegram Bots"

    def __str__(self):
        return self.name


class ChatInfo(models.Model):
    bot = models.ForeignKey(TelegramBot,on_delete=models.CASCADE,related_name="telegrambot")
    chat_id = models.BigIntegerField(verbose_name='Chat ID')
    chat_name = models.CharField(max_length=100,verbose_name='Chat Name')

    class Meta:
        verbose_name ="chat info"
        verbose_name_plural = "chats info"

    def __str__(self):
        return self.chat_name or self.chat_id


