# Generated by Django 4.1.5 on 2023-02-09 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_alter_message_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
