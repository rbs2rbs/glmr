# Generated by Django 2.1.7 on 2019-07-17 12:28

from django.db import migrations
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0008_auto_20190223_1556'),
    ]

    operations = [
        migrations.AddField(
            model_name='postagem',
            name='resumo',
            field=markdownx.models.MarkdownxField(default='renan'),
            preserve_default=False,
        ),
    ]
