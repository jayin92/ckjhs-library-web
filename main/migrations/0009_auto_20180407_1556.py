# Generated by Django 2.0.3 on 2018-04-07 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20180407_1526'),
    ]

    operations = [
        migrations.AddField(
            model_name='borrows',
            name='author',
            field=models.CharField(default='test', max_length=100),
        ),
        migrations.AddField(
            model_name='borrows',
            name='pubtime',
            field=models.CharField(default='test', max_length=100),
        ),
    ]
