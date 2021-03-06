# Generated by Django 4.0 on 2021-12-30 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PostModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image1', models.ImageField(upload_to='images')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='images')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='images')),
                ('image4', models.ImageField(blank=True, null=True, upload_to='images')),
                ('image5', models.ImageField(blank=True, null=True, upload_to='images')),
                ('image6', models.ImageField(blank=True, null=True, upload_to='images')),
                ('image7', models.ImageField(blank=True, null=True, upload_to='images')),
                ('Title', models.CharField(max_length=100)),
                ('Description', models.TextField(max_length=1500)),
                ('type1', models.CharField(choices=[('global news', 'global news'), ('hacker news', 'hacker news'), ('technical news', 'technical news'), ('web news', 'web news'), ('automobile news', 'automobile news'), ('game news', 'game news'), ('site news', 'site news')], max_length=16)),
            ],
        ),
    ]
