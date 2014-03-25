#!/bin/bash
if
    ! grep "$1.*cleanlog" /var/spool/cron/$2
then
    echo "0 0 * * * /var/www/$1/manage.py cleanlogs" >> /var/spool/cron/$2
    echo "Added \"0 0 * * * /var/www/$1/manage.py cleanlogs\" to /var/spool/cron/$2"
else
    echo "\"0 0 * * * /var/www/$1/manage.py cleanlogs\" already added."
fi

if
    ! grep "$1.*cleanup" /var/spool/cron/$1
then
    echo "0 0 * * * /var/www/$1/manage.py cleanup" >> /var/spool/cron/$2
    echo "Added \"0 0 * * * /var/www/$1/manage.py cleanup\" to /var/spool/cron/$2"
else
    echo "\"0 0 * * * /var/www/$1/manage.py cleanup\" already added."
fi

if
    ! grep "$1.*handle_mailbox_operations" /var/spool/cron/$2
then
    echo "* * * * * /var/www/$1/manage.py handle_mailbox_operations" >> /var/spool/cron/$2
    echo "Added \"* * * * * /var/www/$1/manage.py handle_mailbox_operations\" to /var/spool/cron/$2"
else
    echo "\"* * * * * /var/www/$1/manage.py handle_mailbox_operations\" already added."
fi
