#!/bin/bash
if
    ! grep "$1.*cleanlog" /var/spool/cron/root
then
    echo "0 0 * * * /var/www/sites/$1/manage.py cleanlogs" >> /var/spool/cron/root
    echo "Added \"0 0 * * * /var/www/sites/$1/manage.py cleanlogs\" to /var/spool/cron/root"
else
    echo "\"0 0 * * * /var/www/sites/$1/manage.py cleanlogs\" already added."
fi

if
    ! grep "$1.*cleanup" /var/spool/cron/root
then
    echo "0 0 * * * /var/www/sites/$1/manage.py cleanup" >> /var/spool/cron/root
    echo "Added \"0 0 * * * /var/www/sites/$1/manage.py cleanup\" to /var/spool/cron/root"
else
    echo "\"0 0 * * * /var/www/sites/$1/manage.py cleanup\" already added."
fi
