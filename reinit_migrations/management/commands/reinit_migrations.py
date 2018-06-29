from django.core.management.base import BaseCommand
from django.db.migrations import recorder
from django.db.migrations import loader
import os
import importlib


def delete_migration_file(file_name):
    try:
        message = "Deleting file %s.py" % file_name
        print(message)
        os.remove("%s.py" % file_name)
    except Exception as e:
        print(str(e))


def get_migration_files(app_label, migration_file_name):
    migrations_module, _ = loader.MigrationLoader.migrations_module(app_label)
    path = importlib.import_module(migrations_module).__file__
    directory = os.path.dirname(path)
    return "%s/%s" % (directory, migration_file_name)


class Command(BaseCommand):
    help = "Deletes all migrations and deletes all migrations from \
django_migrations table"

    def add_arguments(self, parser):
        parser.add_argument('--apps', nargs='+')

    def get_apps(self, local_only=True):
        from django.conf import settings
        if local_only:
            apps = settings.LOCAL_APPS
        else:
            apps = settings.INSTALLED_APPS
        return apps

    def handle(self, *args, **options):
        from django.db import connection
        connection = connection
        allowed_apps = self.get_apps()
        if options.get('apps', None):
            migrations_applied = recorder.MigrationRecorder(
                connection
            ).Migration.objects.filter(
                app__in=filter(lambda x: x in allowed_apps, options['apps'])
            )
        else:
            migrations_applied = recorder.MigrationRecorder(
                connection).Migration.objects.filter(app__in=allowed_apps)
        for i in migrations_applied:
            delete_migration_file(get_migration_files(i.app, i.name))
        message = "Deleting migration records from db"
        print(message)
        migrations_applied.delete()
