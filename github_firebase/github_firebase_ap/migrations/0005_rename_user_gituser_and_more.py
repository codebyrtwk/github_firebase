# Generated by Django 4.2 on 2023-04-20 15:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('github_firebase_ap', '0004_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='GitUser',
        ),
        migrations.RenameField(
            model_name='gituser',
            old_name='usernamex',
            new_name='username',
        ),
    ]