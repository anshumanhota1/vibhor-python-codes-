# Generated by Django 2.2 on 2020-03-19 07:10

from django.db import migrations, models
import posts.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('slug', models.SlugField(unique=True)),
                ('height_field', models.IntegerField(default=0)),
                ('width_field', models.IntegerField(default=0)),
                ('image', models.ImageField(blank=True, height_field=models.IntegerField(default=0), null=True, upload_to=posts.models.upload, width_field=models.IntegerField(default=0))),
                ('content', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-timestamp', '-last_updated'],
            },
        ),
    ]
