#!bin/bash

#create database
mysql -u $USER -p $PASSWORD -e "create database if not exists $DATABASE;"

#dbmate make migrations
DATABASE_URL="mysql://$USER:$PASSWORD@$HOST:$PORT/$DATABASE"
dbmate -u $DATABASE_URL up

#run application
python main.py