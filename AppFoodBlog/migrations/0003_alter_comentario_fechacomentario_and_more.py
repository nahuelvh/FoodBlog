# Generated by Django 4.0.3 on 2022-04-09 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppFoodBlog', '0002_remove_posteo_usuario_comentario_user_posteo_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='fechaComentario',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='imagen',
            name='fechaSubida',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='posteo',
            name='fechaPublicacion',
            field=models.DateTimeField(),
        ),
    ]