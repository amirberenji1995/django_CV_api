# Generated by Django 3.1.1 on 2021-06-24 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('image_processing', '0002_delete_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original', models.ImageField(upload_to='')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('processed', models.ImageField(blank=True, upload_to='')),
                ('scale', models.FloatField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
