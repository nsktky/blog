# Generated by Django 3.1.6 on 2021-02-03 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20210202_2240'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categorymodel',
            old_name='category',
            new_name='name',
        ),
    ]