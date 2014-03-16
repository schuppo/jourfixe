#!/bin/bash
if
    ! grep "$1.*cleanlog" /var/spool/cron/postfix
then
    echo "0 0 * * * /var/www/sites/$1/manage.py cleanlogs" >> /var/spool/cron/root
    echo "Added \"0 0 * * * /var/www/sites/$1/manage.py cleanlogs\" to /var/spool/cron/postfix"
else
    echo "\"0 0 * * * /var/www/sites/$1/manage.py cleanlogs\" already added."
fi

if
    ! grep "$1.*cleanup" /var/spool/cron/postfix
then
    echo "0 0 * * * /var/www/sites/$1/manage.py cleanup" >> /var/spool/cron/postfix
    echo "Added \"0 0 * * * /var/www/sites/$1/manage.py cleanup\" to /var/spool/cron/postfix"
else
    echo "\"0 0 * * * /var/www/sites/$1/manage.py cleanup\" already added."
fi

if
    ! grep "$1.*handle_mailbox_operations" /var/spool/cron/postfix
then
    echo "* * * * * /var/www/sites/$1/manage.py handle_mailbox_operations" >> /var/spool/cron/postfix
    echo "Added \"* * * * * /var/www/sites/$1/manage.py handle_mailbox_operations\" to /var/spool/cron/postfix"
else
    echo "\"* * * * * /var/www/sites/$1/manage.py handle_mailbox_operations\" already added."
fi
