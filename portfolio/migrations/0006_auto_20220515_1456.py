# Generated by Django 2.2.13 on 2022-05-15 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_contactus'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactus',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='contactus',
            name='last_name',
        ),
        migrations.AddField(
            model_name='contactus',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
