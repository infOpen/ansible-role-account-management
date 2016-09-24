# account-management

[![Build Status](https://travis-ci.org/infOpen/ansible-role-account-management.svg?branch=master)](https://travis-ci.org/infOpen/ansible-role-account-management)

Manage users and groups, with authorized keys.

## Requirements

This role requires Ansible 2.0 or higher, and platform requirements are listed
in the metadata file.

## Testing

This role has some testing methods:

### Automatically with Travis

Tests runs automatically on Travis on push, release, pr, ... using docker testing containers

### Locally with Docker

You can use Docker to run tests on ephemeral containers.

```
make test-docker
```

### Locally with Vagrant

You can use Vagrant to run tests on virtual machines.

```
make test-vagrant
```

## Role Variables

Follow the possible variables with their default values

### List of groups to create

* Variable name: account_management_groups
* Default value: []
* Template :
```
- name         : my-group     # Name of group
  gid          : 1500         # Set the GID       (Default : False)
  state        : absent       # Should exists ?   (Default : present)
  is_system    : True         # Is system group ? (Default : False)
```

### List of users to create

* Variable name: account_management_users
* Default value: []
* Template :
```
- name         : my-user      # Name of user
  append       : False        # Add or replace add groups (Default : True)
  comment      : "Foobar"     # Describe user             (Default : '')
  createhome   : False        # Explicit                  (Default : True)
  home_mode    : 0750         # Permissions for home      (Default : 0700)
  group        : "my-user"    # Primary user group        (Default : username)
  groups       : []           # Additionnal groups
  uid          : 1500         # Set the UID               (Default : False)
  password     : "qsdqdqsd"   # Encrypted password        (Default : False)
  state        : absent       # Should exists ?           (Default : present)
  is_system    : True         # Is system user ?          (Default : False)
  remove       : True         # Should be removed ?       (Default : False)
  skeleton     : /skels/foo   # Skeleton used at create   (Default : False)
  home         : "/var/foo"   # Home path  (Default : /home/username)
  shell        : "/bin/sh"    # User shell (Default : /usr/sbin/nologin)
  authorized_public_keys : [] # Public ssh keys used for authentication
  exclusive_public_keys  : False # Only listed keys exists in authorized-keys
                                 # (Default : True)
```
* Template used for authorized keys entries
```
- filename : "/etc/public-keys/foo.key"   # Filename where is the public key
  state    : "absent"                     # Used for auth (Default : present))
  key_options : ""                        # Add ssh options for this key
```
* Notes :
  - encrypted password can be created by the following command :
```
      python -c 'import crypt; print crypt.crypt("password", "$1$salt$")'
```


## Dependencies

None

## Example Playbook

    - hosts: servers
      roles:
         - { role: achaussier.account-management }

## License

MIT

## Author Information

Alexandre Chaussier (for Infopen company)
- http://www.infopen.pro
- a.chaussier [at] infopen.pro
