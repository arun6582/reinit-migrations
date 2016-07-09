from django.core.management.base import BaseCommand, CommandError
from django.db.migrations import recorder
from django.db.migrations import loader
import os
import logging
import importlib

logger = logging.getLogger(__name__)


def delete_migration_file(file_name):
    logger.debug("Deleting file %s.py" % file_name)
    os.remove("%s.py" % file_name)
    logger.debug("Deleting file %s.pyc" % file_name)
    os.remove("%s.pyc" % file_name)

def get_migration_files(app_label, migration_file_name):
    migrations_module = loader.MigrationLoader.migrations_module(app_label)
    path = importlib.import_module(migrations_module).__file__
    directory = os.path.dirname(path)
    return "%s/%s" % (directory, migration_file_name)

class Command(BaseCommand):
    help = "Deletes all migrations and deletes all migrations from django_migrations table"
    
    def handle(self, *args, **options):
        from django.db import connection
        connection = connection
        migrations_applied = recorder.MigrationRecorder(connection).Migration.objects.all()
        for i in migrations_applied:
            delete_migration_file(get_migration_files(i.app, i.name))
        logger.debug("Deleting migration records from db")
        migrations_applied.delete()
