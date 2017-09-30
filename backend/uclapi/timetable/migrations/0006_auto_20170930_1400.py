# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-30 14:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0005_auto_20170930_1327'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='ccalmaps',
            table='UCZMNHO.NOSH_OWNER_CCALMAPS',
        ),
        migrations.AlterModelTable(
            name='classgrps',
            table='UCZMNHO.NOSH_OWNER_CLASSGRPS',
        ),
        migrations.AlterModelTable(
            name='classifications',
            table='UCZMNHO.NOSH_OWNER_CLASSIFICATIONS',
        ),
        migrations.AlterModelTable(
            name='contact',
            table='UCZMNHO.NOSH_OWNER_CONTACT',
        ),
        migrations.AlterModelTable(
            name='course',
            table='UCZMNHO.NOSH_OWNER_COURSE',
        ),
        migrations.AlterModelTable(
            name='crsavailmodules',
            table='UCZMNHO.NOSH_OWNER_CRSAVAILMODULES',
        ),
        migrations.AlterModelTable(
            name='crscompmodules',
            table='UCZMNHO.NOSH_OWNER_CRSCOMPMODULES',
        ),
        migrations.AlterModelTable(
            name='depts',
            table='UCZMNHO.NOSH_OWNER_DEPTS',
        ),
        migrations.AlterModelTable(
            name='equipment',
            table='UCZMNHO.NOSH_OWNER_EQUIPMENT',
        ),
        migrations.AlterModelTable(
            name='features',
            table='UCZMNHO.NOSH_OWNER_FEATURES',
        ),
        migrations.AlterModelTable(
            name='lecturer',
            table='UCZMNHO.NOSH_OWNER_LECTURER',
        ),
        migrations.AlterModelTable(
            name='module',
            table='UCZMNHO.NOSH_OWNER_MODULE',
        ),
        migrations.AlterModelTable(
            name='rooms',
            table='UCZMNHO.NOSH_OWNER_ROOMS',
        ),
        migrations.AlterModelTable(
            name='sites',
            table='UCZMNHO.NOSH_OWNER_SITES',
        ),
        migrations.AlterModelTable(
            name='slotdetails',
            table='UCZMNHO.NOSH_OWNER_SLOTDETAILS',
        ),
        migrations.AlterModelTable(
            name='sources',
            table='UCZMNHO.NOSH_OWNER_SOURCES',
        ),
        migrations.AlterModelTable(
            name='students',
            table='UCZMNHO.NOSH_OWNER_STUDENTS',
        ),
        migrations.AlterModelTable(
            name='stumodules',
            table='UCZMNHO.NOSH_OWNER_STUMODULES',
        ),
        migrations.AlterModelTable(
            name='weekmapnumeric',
            table='UCZMNHO.NOSH_OWNER_WEEKMAPNUMERIC',
        ),
        migrations.AlterModelTable(
            name='weekmapstring',
            table='UCZMNHO.NOSH_OWNER_WEEKMAPSTRING',
        ),
        migrations.AlterModelTable(
            name='weekstructure',
            table='UCZMNHO.NOSH_OWNER_WEEKSTRUCTURE',
        ),
    ]
