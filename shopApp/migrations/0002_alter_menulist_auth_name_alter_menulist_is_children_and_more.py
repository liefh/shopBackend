# Generated by Django 4.2.7 on 2023-11-15 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menulist',
            name='auth_name',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='menulist',
            name='is_children',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='menulist',
            name='parent_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='menulist',
            name='path',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
