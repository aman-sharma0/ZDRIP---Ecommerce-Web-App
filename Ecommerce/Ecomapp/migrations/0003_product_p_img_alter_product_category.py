# Generated by Django 5.0.1 on 2024-02-26 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecomapp', '0002_alter_product_category_alter_product_is_active_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='p_img',
            field=models.ImageField(default=0, upload_to='image'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.IntegerField(choices=[(1, 'mobile'), (2, 'shoes'), (3, 'cloths')], verbose_name='Category'),
        ),
    ]
