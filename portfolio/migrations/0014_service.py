# Generated by Django 5.2.1 on 2025-06-24 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0013_alter_sociallink_phone_number_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('icon', models.CharField(help_text='Example: 💻 or 🧪', max_length=10)),
            ],
        ),
    ]
