# Generated by Django 5.1.2 on 2024-10-28 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LatestApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_Category', models.CharField(blank=True, max_length=100, null=True)),
                ('Product_Name', models.CharField(blank=True, max_length=100, null=True)),
                ('Product_Description', models.TextField(blank=True, max_length=200, null=True)),
                ('Product_Price', models.CharField(blank=True, max_length=100, null=True)),
                ('Product_Image', models.ImageField(blank=True, null=True, upload_to='product_images')),
            ],
        ),
        migrations.AddField(
            model_name='categorydb',
            name='Category_Image',
            field=models.ImageField(blank=True, null=True, upload_to='category_images'),
        ),
    ]
