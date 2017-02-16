# Champalimaud Reagents DB

Database to manage reagents stock.

Model spreadsheet: https://docs.google.com/spreadsheets/d/1FXhRND7HAgtGgicinPEjvEGMtVt9KIZo0T8W_9JtOdU


![cover image](https://bytebucket.org/fchampalimaud/reagents-db/raw/2094c0add6a176c77e71d3ff47319d18b0caa4d4/cover_image.png?token=1bda18209bf8b1e6382a8b7121eb0b9295b3966d)

## Setting environment

### Set up python dependencies:

	mkvirtualenv -p /usr/local/bin/python2 reagents_db
	workon reagents_db
	pip install -r requirements.txt

### Set up database

	dump database in production environment
	import dump to local database

### Set up Django:

    python manage.py createsuperuser # alternative 1: create new super user
    python manage.py changepassword root # alternative 2: change root password
    create file reagents_db/dev-settings.cfg to override Django settings (usually to override database settings)

## Updating data model

(first, install gsheet2django)

    gsheet2django 1FXhRND7HAgtGgicinPEjvEGMtVt9KIZo0T8W_9JtOdU
    python manage.py makemigrations reagents
    python manage.py migrate


# Running
(optional: Add reagents.local to hostnames first!)

    python manage.py runserver reagents.local:8383

# Deploy

1. Merge current changes to production branch.
2. Build the Jenkins Job "reagents-db"
3. Login on cnp-intranet.champalimaud.pt and reload apache server

## Packaging (optional)
In principle, there is no need for packaging because Jenkins will do the hard work but anyway this is how to do it:

	python setup.py sdist --formats=zip

