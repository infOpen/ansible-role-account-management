# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  config.vm.define "ubuntu-trusty" do |trusty|
    trusty.vm.box = "ubuntu/trusty64"
  end

  config.vm.define "centos-6.5" do |centos65|
    centos65.vm.box = "nrel/CentOS-6.5-x86_64"
  end

  config.vm.define "centos-7" do |centos7|
    centos7.vm.box = "centos7"
  end

  # Create symlink to vagrant test playbook
  config.vm.provision "shell" do |sh|
    sh.inline = "ln -fs /vagrant/tests/test_vagrant.yml /vagrant/test_vagrant.yml"
  end

  # Ansible provisionning
  config.vm.provision "ansible_local" do |ansible|
    ansible.playbook  = "test_vagrant.yml"
  end

end

