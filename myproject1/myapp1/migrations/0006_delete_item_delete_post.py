# Generated by Django 5.1.3 on 2024-11-16 13:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0005_rename_jpravi_person'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Item',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
