# Generated by Django 4.2.4 on 2023-08-28 17:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_telegrambot_chatid'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ChatID',
            new_name='ChatInfo',
        ),
        migrations.AlterModelOptions(
            name='chatinfo',
            options={'verbose_name': 'chat info', 'verbose_name_plural': 'chats info'},
        ),
    ]