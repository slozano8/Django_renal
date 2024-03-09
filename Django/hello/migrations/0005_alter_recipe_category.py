# Generated by Django 5.0.2 on 2024-03-09 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0004_rename_title_recipe_name_remove_recipe_content_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='category',
            field=models.CharField(choices=[('breakfast', 'Breakfast'), ('lunch', 'Lunch'), ('dinner', 'Dinner')], default='other', max_length=50),
        ),
    ]
