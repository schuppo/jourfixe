#!/bin/bash
if
    ! iptables -L | grep 'http[^a-z]'
then
    iptables -A INPUT -p tcp --dport 80 -j ACCEPT
fi
#
# Save settings
#
 /sbin/service iptables save
#
# List rules
#
 iptables -L -v
