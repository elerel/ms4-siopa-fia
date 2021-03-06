# Generated by Django 3.2.4 on 2021-08-08 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210704_2005'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='body_one',
            field=models.TextField(default='Paragraph 1'),
        ),
        migrations.AddField(
            model_name='blog',
            name='body_three',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='body_two',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='body',
            field=models.TextField(default='Intro', max_length=200),
        ),
    ]
