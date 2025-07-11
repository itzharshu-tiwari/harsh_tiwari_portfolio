# Generated by Django 5.2.1 on 2025-06-24 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0009_sociallink'),
    ]

    operations = [
        migrations.CreateModel(
            name='Connect',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform', models.CharField(max_length=50)),
                ('icon_class', models.CharField(max_length=50)),
                ('url', models.URLField(blank=True, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('display_text', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='SocialLink',
        ),
    ]
