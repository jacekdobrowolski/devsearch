# Generated by Django 4.1.6 on 2023-02-09 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0003_tag_project_vote_ratio_project_vote_total_review_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="featured_image",
            field=models.ImageField(
                blank=True, default="default.jpg", null=True, upload_to=""
            ),
        ),
    ]