# Generated by Django 3.2.19 on 2023-06-08 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='IQ_test_pass_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
