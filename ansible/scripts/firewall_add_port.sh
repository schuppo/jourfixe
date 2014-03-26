#!/bin/bash
if
    ! iptables-save | grep -- '-A INPUT -p tcp -m tcp --dport $1 -j ACCEPT'
then
    iptables -I INPUT 1 -p tcp --dport $1 -j ACCEPT
fi
