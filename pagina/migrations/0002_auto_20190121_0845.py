# Generated by Django 2.1.3 on 2019-01-21 11:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postagem',
            name='linkedin',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='pagina.Linkedin'),
        ),
    ]
