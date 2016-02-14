# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0004_auto_20160207_1215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useranswer',
            name='their_answer',
            field=models.ForeignKey(related_name='match_answer', blank=True, to='questions.Answer', null=True),
        ),
    ]
