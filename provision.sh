#!/usr/bin/env bash
sed -i 's/^mesg n$/tty -s \&\& mesg n/g' /root/.profile
sudo mkdir -p /etc/ansible
sudo locale-gen de_DE.UTF-8
printf '[vagrant]\nlocalhost\n' | sudo tee /etc/ansible/hosts > /dev/null
echo Running provisioner: ansible

