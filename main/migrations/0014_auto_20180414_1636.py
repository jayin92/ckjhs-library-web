# Generated by Django 2.0.3 on 2018-04-14 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20180414_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='book_author',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='books',
            name='book_barcode',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='books',
            name='book_borrowid',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='books',
            name='book_borrowname',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='books',
            name='book_isbn',
            field=models.CharField(blank=True, max_length=13, null=True),
        ),
        migrations.AlterField(
            model_name='books',
            name='book_pubtime',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='books',
            name='book_title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]