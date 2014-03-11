#!/usr/bin/env bash
sudo rpm --import http://mirror.centos.org/centos/RPM-GPG-KEY-CentOS-6
sudo yum -y install yum-priorities

echo copying CentOS-Base.repo to /etc/yum.repos.de/
cp /vagrant/templates/CentOS-Base.repo /etc/yum.repos.d/

sudo rpm --import http://dl.fedoraproject.org/pub/epel/RPM-GPG-KEY-EPEL-6
sudo rpm -Uvh http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm

echo copying epel.repo to /etc/yum.repos.de/
cp /vagrant/templates/epel.repo /etc/yum.repos.d/

sudo yum -y install ansible

sudo mkdir -p /etc/ansible
printf '[vagrant]\nlocalhost\n' | sudo tee /etc/ansible/hosts > /dev/null
echo Running provisioner: ansible
PYTHONUNBUFFERED=1 ansible-playbook -c local /vagrant/ansible/playbook.yml

# sudo rpm -Uvh http://mirror.webtatic.com/yum/el6/latest.rpm
# sudo rpm --import http://repo.webtatic.com/yum/RPM-GPG-KEY-webtatic-andy
# sudo yum -y install php55w php55w-mysql mysql-server zsh git
# cp /vagrant/.ssh/config /$HOME/.ssh/
# git clone git@github.com:schuppo/dotfiles.git /home/vagrant/.dotfiles
