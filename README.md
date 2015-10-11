account-management
==================

[![Build Status](https://travis-ci.org/infOpen/ansible-role-account-management.svg?branch=master)](https://travis-ci.org/infOpen/ansible-role-account-management)

Manage users and groups, with sudo rules and authorized keys.

Requirements
------------

This role requires Ansible 1.4 or higher, and platform requirements are listed
in the metadata file.

Role Variables
--------------

Follow the possible variables with their default values

    # List of sudoers.d subdirectory to create
    account_management_sudo_directories :
      - groups
      - users

    # List of groups to create
    #
    # Template :
    # - name         : my-group     # Name of group
    #   gid          : 1500         # Set the GID       (Default : False)
    #   state        : absent       # Should exists ?   (Default : present)
    #   is_system    : True         # Is system group ? (Default : False)
    #   sudo_rules   : []           # Sudo rules for the group
    #   sudo_sub_dir : "groups"     # Where store sudoers rule
    account_management_groups : []

    # List of users to create
    #
    # Template :
    # - name         : my-user      # Name of user
    #   append       : False        # Add or replace add groups (Default : True)
    #   comment      : "Foobar"     # Describe user             (Default : '')
    #   createhome   : False        # Explicit                  (Default : True)
    #   home_mode    : 0750         # Permissions for home      (Default : 0700)
    #   group        : "my-user"    # Primary user group        (Default : username)
    #   groups       : []           # Additionnal groups
    #   uid          : 1500         # Set the UID               (Default : False)
    #   password     : "qsdqdqsd"   # Encrypted password        (Default : False)
    #   state        : absent       # Should exists ?           (Default : present)
    #   is_system    : True         # Is system user ?          (Default : False)
    #   remove       : True         # Should be removed ?       (Default : False)
    #   skeleton     : /skels/foo   # Skeleton used at create   (Default : False)
    #   home         : "/var/foo"   # Home path  (Default : /home/username)
    #   shell        : "/bin/sh"    # User shell (Default : /usr/sbin/nologin)
    #   sudo_rules   : []           # Sudo rules for the user
    #   sudo_sub_dir : "users"      # Where store sudoers rule
    #   authorized_public_keys : [] # Public ssh keys used for authentication
    #   exclusive_public_keys  : False # Only listed keys exists in authorized-keys
    #                                  # (Default : True)
    #
    # Template used for authorized keys entries
    # - filename : "/etc/public-keys/foo.key"   # Filename where is the public key
    #   state    : "absent"                     # Used for auth (Default : present))
    #   key_options : ""                        # Add ssh options for this key
    #
    # Notes :
    #   - encrypted password can be created by the followin command :
    #       python -c 'import crypt; print crypt.crypt("password", "$1$salt$")'
    account_management_users : []


Specific OS family vars :

    # Debian
    account_management_packages :
      - sudo

Dependencies
------------

None

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: achaussier.account-management }

License
-------

MIT

Author Information
------------------

Alexandre Chaussier (for Infopen company)
- http://www.infopen.pro
- a.chaussier [at] infopen.pro
