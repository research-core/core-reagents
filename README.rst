Reagents DB
=======================

Database to manage reagents stock.

Model spreadsheet: https://docs.google.com/spreadsheets/d/1FXhRND7HAgtGgicinPEjvEGMtVt9KIZo0T8W_9JtOdU

----

Updating data model

(first, install gsheet2django)

$: gsheet2django 1FXhRND7HAgtGgicinPEjvEGMtVt9KIZo0T8W_9JtOdU
$: python manage.py makemigrations reagents
$: python manage.py migrate

Running
# Add reagents.local to hostnames first!
$: python manage.py runserver reagents.local:8383

Packaging
$: python setup.py sdist --formats=zip

Uploading
$ scp dist/Reagents\ DB-X.Y.Z.zip rribeiro@cnp-intranet.champalimaud.pt:/home/rribeiro/uploads

Installing
$: cd ~/uploads
$: unzip Reagents\ DB-X.Y.Z.zip
$: sudo mv Reagents\ DB-X.Y.Z /var/www/
$: cd /www/var/
$: sudo ln -s Reagents\ DB-X.Y.Z/ reagents_db
$: cp -r Reagents\ DB-X.Y.Y/media Reagents\ DB-X.Y.Z/
$: chmod -R o+w media