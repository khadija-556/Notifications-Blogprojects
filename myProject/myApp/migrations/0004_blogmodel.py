# Generated by Django 5.0.2 on 2024-03-02 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0003_delete_job_m_alter_custom_user_user_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_title', models.CharField(max_length=100, null=True)),
                ('blog_describtion', models.CharField(max_length=300, null=True)),
                ('date', models.DateField(auto_now_add=True, null=True)),
            ],
        ),
    ]
