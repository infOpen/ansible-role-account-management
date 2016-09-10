# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  config.vm.define "ubuntu-trusty" do |trusty|
    trusty.vm.box = "ubuntu/trusty64"
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

