# Generated by Django 5.1 on 2024-08-22 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0002_alter_emp_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('testimonial', models.TextField()),
                ('picture', models.ImageField(upload_to='testimonial/')),
                ('rating', models.IntegerField(max_length=1)),
            ],
        ),
    ]
