# Generated by Django 4.0.3 on 2022-04-15 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppFoodBlog', '0007_alter_imagen_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='posteo',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='imagenes/'),
        ),
        migrations.DeleteModel(
            name='Imagen',
        ),
    ]
