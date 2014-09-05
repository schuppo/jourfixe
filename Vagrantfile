# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "precise64"
  config.vm.box_url = "http://files.vagrantup.com/precise64.box"
  config.vm.define :site do |config|
    config.vm.provider :virtualbox do |v|
      v.customize [ "modifyvm", :id, "--memory", "1100" ]
      v.customize ["modifyvm", :id, "--name", "hosteurope"]
    end

    config.vm.host_name = "mail.fritz.box"
    config.vm.network :private_network, ip: "10.0.0.10"
    config.vm.network "forwarded_port", guest: 80, host: 8181

    nfs_setting = RUBY_PLATFORM =~ /darwin/ || RUBY_PLATFORM =~ /linux/
    config.vm.synced_folder "./sites", "/var/www/sites", id: "vagrant-root" , :nfs => nfs_setting
    config.vm.provision :shell, :path => "provision.sh"
    config.vm.provision :shell, :inline =>
    "if [[ ! -f /apt-get-run ]]; then sudo apt-get update && sudo touch /apt-get-run; fi"

    config.ssh.forward_agent = true
    config.ssh.pty = true
  end
end
