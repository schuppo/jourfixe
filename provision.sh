#!/usr/bin/env bash
sudo mkdir -p /etc/ansible
printf '[vagrant]\nlocalhost\n' | sudo tee /etc/ansible/hosts > /dev/null
echo Running provisioner: ansible

