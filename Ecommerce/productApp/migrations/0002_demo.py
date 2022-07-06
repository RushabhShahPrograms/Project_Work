# Generated by Django 4.0.6 on 2022-07-05 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Demo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=99, unique=True)),
                ('profile_pic', models.ImageField(default='profile_pic/p1.jpg', upload_to='profile_pic')),
            ],
        ),
    ]
