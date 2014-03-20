#!/bin/bash
openssl req -new -x509 -days 3650 -nodes -out /etc/postfix/certs/cert.pem -keyout /etc/postfix/certs/key.pem
