#Installation

pip install django_manage_reset_migrations

#Usage
Add django_manage_reset_migrations to INSTALLED_APPS

./manage reset_migrations

It will delete all the applied migrations from the disk and the db.
Useful when migrations files are too many and it slows down the computer.
Reset migrations using this utility and run makemigration then fake all of them.
