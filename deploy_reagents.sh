#! /bin/bash
# 

NEW_VERSION=$1
if [ -z $NEW_VERSION ]; then 
   echo "You must specify a version with dots e.g. 0.0.4"
   exit 2;
fi

DESTINATION_DIR="/var/www"
MEDIA_DIR="$DESTINATION_DIR/reagents_db_media"
NEW_VERSION_DIR="reagents_db_$NEW_VERSION"
rm -rf $NEW_VERSION_DIR
mkdir -p $NEW_VERSION_DIR
cd $NEW_VERSION_DIR

DIST_DIR="/home/rribeiro/routines/deploy/$NEW_VERSION_DIR/Reagents-db/dist"

git clone http://gitlab.neuro/swp/Reagents-db.git -q

cd "Reagents-db"

git checkout production -q

python setup.py -q sdist --formats=zip

unzip -q "$DIST_DIR/Reagents DB-$NEW_VERSION.zip" -d "$DIST_DIR"

mv "$DIST_DIR/Reagents DB-$NEW_VERSION" "$DESTINATION_DIR/$NEW_VERSION_DIR"
#cp -r "$DESTINATION_DIR/reagents_db/media" "$DESTINATION_DIR/$NEW_VERSION_DIR"
ln -s "$MEDIA_DIR" "$DESTINATION_DIR/$NEW_VERSION_DIR/media"

#echo "New version to be installed: $DESTINATION_DIR/$NEW_VERSION_DIR"

chown -R rribeiro:rribeiro "$DESTINATION_DIR/$NEW_VERSION_DIR"
#chmod -R o+w "$DESTINATION_DIR/$NEW_VERSION_DIR/media"

sudo -u rribeiro python manage.py makemigrations reagents
sudo -u rribeiro python manage.py migrate

# remove old symlink
rm "$DESTINATION_DIR/reagents_db"

# point to new deploy
ln -s "$DESTINATION_DIR/$NEW_VERSION_DIR" "$DESTINATION_DIR/reagents_db"

service apache2 reload
