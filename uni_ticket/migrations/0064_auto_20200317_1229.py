# Generated by Django 3.0.3 on 2020-03-17 11:29

from django.db import migrations, models
import uni_ticket.models


class Migration(migrations.Migration):

    dependencies = [
        ('uni_ticket', '0063_auto_20200317_1228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticketcategorycondition',
            name='attachment',
            field=models.FileField(blank=True, null=True, upload_to=uni_ticket.models._attachment_upload),
        ),
    ]
