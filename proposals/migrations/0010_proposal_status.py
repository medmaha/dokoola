# Generated by Django 5.0.2 on 2024-05-31 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proposals', '0009_proposal_deleted_proposal_uid_alter_proposal_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='proposal',
            name='status',
            field=models.CharField(choices=[('ACCEPTED', 'Accepted'), ('DECLINED', 'Declined'), ('PENDING', 'Pending')], default='PENDING', max_length=200),
        ),
    ]