# Generated by Django 4.0.3 on 2022-04-20 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppFoodBlog', '0012_alter_comentario_fechacomentario_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posteo',
            name='fechaImagen',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
