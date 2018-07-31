**Installation**
*pip install reinit-migrations*

**Release 0.1**
**Usage**
Add reinit_migrations to INSTALLED_APPS
*./manage reinit_migrations*
It will delete all the applied migrations from the disk and the db. Useful when migration files are too many and it slows down the computer. Reset migrations using this utility and run makemigration then fake all of them.

**Release 0.2**
**Usage**
Add reinit_migrations to INSTALLED_APPS
*./manage reinit_migrations*
This will delete migrations for all apps from db and disk
./manage reinit_migrations --apps app1 app2 app3 ...*
This will delete migration for app1, app2, app3 only.

**Release 0.4**
Separate your apps into three lists
DEFAULT = [django framework apps]
THIRD_PARTY_APPS = [third party apps]
LOCAL_APPS = [your apps]
this app will work on LOCAL_APPS only.

*As always pull requests are welcome :)*
