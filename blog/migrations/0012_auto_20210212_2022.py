# Generated by Django 3.1.6 on 2021-02-12 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20210209_2143'),
    ]

    operations = [
        migrations.AddField(
            model_name='postblogmodel',
            name='link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='postworkmodel',
            name='link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
