Reagents DB
=======================

Database to manage reagents stock.

Model spreadsheet: https://docs.google.com/spreadsheets/d/1FXhRND7HAgtGgicinPEjvEGMtVt9KIZo0T8W_9JtOdU

----

Updating data model

(first, install gsheet2django)

$: gsheet2django 1FXhRND7HAgtGgicinPEjvEGMtVt9KIZo0T8W_9JtOdU
$: python manage.py migrate

Packaging
$: python setup.py sdist --formats=zip

Uploading

