# Generated by Django 3.1.5 on 2021-01-31 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
