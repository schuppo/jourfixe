#!/usr/bin/env bash
sudo rpm --import http://mirror.centos.org/centos/RPM-GPG-KEY-CentOS-6
sudo yum -y install yum-priorities

echo Copying CentOS-Base.repo to /etc/yum.repos.d/
cp /vagrant/templates/CentOS-Base.repo /etc/yum.repos.d/

sudo rpm --import http://dl.fedoraproject.org/pub/epel/RPM-GPG-KEY-EPEL-6
sudo rpm -Uvh http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm

echo Copying epel.repo to /etc/yum.repos.de/
cp /vagrant/templates/epel.repo /etc/yum.repos.d/

sudo yum -y install ansible libselinux-python

sudo mkdir -p /etc/ansible
printf '[vagrant]\nlocalhost\n' | sudo tee /etc/ansible/hosts > /dev/null
echo Running provisioner: ansible

