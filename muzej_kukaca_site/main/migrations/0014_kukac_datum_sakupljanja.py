# Generated by Django 3.2.8 on 2022-02-21 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20220221_0750'),
    ]

    operations = [
        migrations.AddField(
            model_name='kukac',
            name='datum_sakupljanja',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]