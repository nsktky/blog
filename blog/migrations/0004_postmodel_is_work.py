# Generated by Django 3.1.5 on 2021-02-02 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_postmodel_published_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='is_work',
            field=models.BooleanField(default=False),
        ),
    ]
