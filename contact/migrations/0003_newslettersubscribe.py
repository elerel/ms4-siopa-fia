# Generated by Django 3.2.4 on 2021-07-15 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_alter_contact_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsletterSubscribe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=50)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Newsletter Subscription',
            },
        ),
    ]
