#!/bin/bash
if
    ! /sbin/iptables -L | grep 'http[^a-z]'
then
    /sbin/iptables -A INPUT -p tcp --dport 80 -j ACCEPT
fi
#
# Save settings
#
 /sbin/service iptables save
#
# List rules
#
 /sbin/iptables -L -v
