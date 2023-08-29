# Generated by Django 4.2.4 on 2023-08-25 13:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_agent_macadress_macaddress'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='macaddress',
            options={'verbose_name': 'Mac Address', 'verbose_name_plural': 'Mac Addresses'},
        ),
        migrations.RemoveField(
            model_name='macaddress',
            name='mac_adress',
        ),
        migrations.AddField(
            model_name='macaddress',
            name='mac_address',
            field=models.CharField(max_length=30, null=True, verbose_name='MacAddress'),
        ),
        migrations.AlterField(
            model_name='macaddress',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='users.agent'),
        ),
    ]