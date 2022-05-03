# Generated by Django 4.0.4 on 2022-05-03 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "questions",
            "0002_ask_created_at_ask_updated_at_customer_created_at_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="ask",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="customer",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="question",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]