# Generated by Django 5.0.6 on 2024-06-24 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0014_alter_perfil_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='../media/'),
        ),
    ]
