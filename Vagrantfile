# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  # All Vagrant configuration is done here. The most common configuration
  # options are documented and commented below. For a complete reference,
  # please see the online documentation at vagrantup.com.

  # Every Vagrant virtual environment requires a box to build off of.
    config.vm.box = "chef/centos-6.5"
    config.vm.define :site do |config|
        config.vm.provider :virtualbox do |v|
            # set memory to > 1GB
            #v.customize [ "modifyvm", :id, "--memory", "1100" ]
        end
        config.vm.host_name = "centos"

        # set lavish permission so that everything is executable
        #

        config.vm.synced_folder "./", "/vagrant", :mount_options => ['dmode=777', 'fmode=666'] #, :nfs=>true

        config.vm.network :private_network, ip: "10.10.10.10"

        # forward to port 8888
        config.vm.network "forwarded_port", guest: 80, host: 8888

        config.vm.provision :shell, :path => "provision.sh"
    end
end
