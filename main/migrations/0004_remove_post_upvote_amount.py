# Generated by Django 2.2.7 on 2021-05-05 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210505_1425'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='upvote_amount',
        ),
    ]
