# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_review_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='salon',
            name='zipcode',
            field=models.CharField(default='06518', max_length=10),
            preserve_default=False,
        ),
    ]
