# Generated by Django 2.2.11 on 2020-03-16 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funds', '0078_auto_20200316_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reminder',
            name='action',
            field=models.CharField(choices=[('reviewers_review', 'Remind reviewers to Review')], default='reviewers_review', max_length=50),
        ),
    ]
