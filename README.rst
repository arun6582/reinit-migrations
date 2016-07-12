**Installation**

*pip install django-manage-reset-migrations*



**Release 0.1**

**Usage**

Add django_manage_reset_migrations to INSTALLED_APPS

*./manage reset_migrations*

It will delete all the applied migrations from the disk and the db. Useful when migration files are too many and it slows down the computer. Reset migrations using this utility and run makemigration then fake all of them.

**Release 0.2**

**Usage**

Add django_manage_reset_migrations to INSTALLED_APPS

*./manage reset_migrations*

This will delete migrations for all apps from db and disk

./manage reset_migrations --apps app1 app2 app3 ...*

This will delete migration for app1, app2, app3 only.



*As always pull requests are welcome :)*