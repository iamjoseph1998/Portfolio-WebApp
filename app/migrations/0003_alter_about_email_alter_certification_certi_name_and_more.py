# Generated by Django 4.0.2 on 2022-02-24 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_eduaction_education'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='email',
            field=models.EmailField(max_length=70, unique=True),
        ),
        migrations.AlterField(
            model_name='certification',
            name='certi_name',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='education',
            name='degree_name',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='experience',
            name='join_date',
            field=models.DateField(unique=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='proj_github_link',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='skill',
            name='skill',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]