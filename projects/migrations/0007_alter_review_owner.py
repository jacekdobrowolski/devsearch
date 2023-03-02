# Generated by Django 4.1.7 on 2023-03-02 19:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_profile_location_skill"),
        ("projects", "0006_alter_project_options_review_owner_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="review",
            name="owner",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="users.profile"
            ),
        ),
    ]