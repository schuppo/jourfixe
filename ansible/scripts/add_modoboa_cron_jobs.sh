#!/bin/bash
if
    ! grep 'modoboa_server.*cleanlog' /var/spool/cron/root
then
    echo "0 0 * * * /var/www/sites/modoboa_server/manage.py cleanlogs" >> /var/spool/cron/root
    echo 'Added "0 0 * * * /var/www/sites/modoboa_server/manage.py cleanlogs" to /var/spool/cron/root'
else
    echo '"0 0 * * * /var/www/sites/modoboa_server/manage.py cleanlogs" already added.'
fi

if
    ! grep 'modoboa_server.*cleanup' /var/spool/cron/root
then
    echo "0 0 * * * /var/www/sites/modoboa_server/manage.py cleanup" >> /var/spool/cron/root
    echo 'Added "0 0 * * * /var/www/sites/modoboa_server/manage.py cleanup" to /var/spool/cron/root'
else
    echo '"0 0 * * * /var/www/sites/modoboa_server/manage.py cleanup" already added.'
fi
