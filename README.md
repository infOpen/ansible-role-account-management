# account-management

[![Build Status](https://img.shields.io/travis/infOpen/ansible-role-account-management/master.svg?label=travis_master)](https://travis-ci.org/infOpen/ansible-role-account-management)
[![Build Status](https://img.shields.io/travis/infOpen/ansible-role-account-management/develop.svg?label=travis_develop)](https://travis-ci.org/infOpen/ansible-role-account-management)
[![Updates](https://pyup.io/repos/github/infOpen/ansible-role-account-management/shield.svg)](https://pyup.io/repos/github/infOpen/ansible-role-account-management/)
[![Python 3](https://pyup.io/repos/github/infOpen/ansible-role-account-management/python-3-shield.svg)](https://pyup.io/repos/github/infOpen/ansible-role-account-management/)
[![Ansible Role](https://img.shields.io/ansible/role/12337.svg)](https://galaxy.ansible.com/infOpen/account-management/)

Install account-management package.

## Requirements

This role requires Ansible 2.4 or higher,
and platform requirements are listed in the metadata file.

## Testing

This role use [Molecule](https://github.com/metacloud/molecule/) to run tests.

Local and Travis tests run tests on Docker by default.
See molecule documentation to use other backend.

Currently, tests are done on:
- CentOS 7
- Debian Jessie
- Debian Stretch
- Ubuntu Xenial
- Ubuntu Bionic

and use:
- Ansible 2.4.x
- Ansible 2.5.x
- Ansible 2.6.x
- Ansible 2.7.x

### Running tests

#### Using Docker driver

```
$ tox
```

You can also configure molecule options and molecule command using environment variables:
* `MOLECULE_OPTIONS` Default: "--debug"
* `MOLECULE_COMMAND` Default: "test"

```
$ MOLECULE_OPTIONS='' MOLECULE_COMMAND=converge tox
```

## Role Variables

### Default role variables

``` yaml
# List of groups to create
account_management_groups: []

# List of users to create
account_management_users: []

# Default home mode
account_management_default_home_mode: '0700'
```

### List of groups to create

* Variable name: account_management_groups
* Default value: []
* Template :

```yaml
- name         : my-group     # Name of group
  gid          : 1500         # Set the GID       (Default : False)
  state        : absent       # Should exists ?   (Default : present)
  is_system    : True         # Is system group ? (Default : False)
```

### List of users to create

* Variable name: account_management_users
* Default value: []
* Template :

```yaml
- name         : my-user      # Name of user
  append       : False        # Add or replace add groups (Default : True)
  comment      : "Foobar"     # Describe user             (Default : '')
  createhome   : False        # Explicit                  (Default : True)
  expires      : 1486509032   # Expire account at this ts (Default : omit)
  home_mode    : 0750         # Permissions for home      (Default : 0700)
  home_group   : "my-user"    # Home group permission     (Default : primary group)
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
  secure_home  : True         # Remove home access from other
  authorized_public_keys : [] # Public ssh keys used for authentication
  exclusive_public_keys  : False # Only listed keys exists in authorized-keys
                                 # (Default : True)
```

* Template used for authorized keys entries

```yaml
- filename : "/etc/public-keys/foo.key"   # Filename where is the public key
  state    : "absent"                     # Used for auth (Default : present))
  key_options : ""                        # Add ssh options for this key
```

* Notes :
  - encrypted password can be created by the following command :

```yaml
      python -c 'import crypt; print crypt.crypt("password", "$1$salt$")'
```

## Dependencies

None

## Example Playbook

``` yaml
- hosts: servers
  roles:
    - { role: infOpen.account-management }
```

## License

MIT

## Author Information

Alexandre Chaussier (for Infopen company)
- http://www.infopen.pro
- a.chaussier [at] infopen.pro
