# Generated by Django 4.2.1 on 2023-05-30 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_book', '0003_alter_profile_profileimg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profileimg',
            field=models.ImageField(default='social_book/blank-profile-picture.png', upload_to='social_book/profile'),
        ),
    ]