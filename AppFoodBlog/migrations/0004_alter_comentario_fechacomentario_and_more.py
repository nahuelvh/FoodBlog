# Generated by Django 4.0.3 on 2022-04-09 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppFoodBlog', '0003_alter_comentario_fechacomentario_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='fechaComentario',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='imagen',
            name='fechaSubida',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='posteo',
            name='fechaPublicacion',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
