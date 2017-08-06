"""
Role tests
"""

import pytest
from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


@pytest.mark.parametrize('name,gid', [
    ('my-group', None),
    ('my-group2', 1500),
    ('my-user3', 1501),
])
def test_groups(host, name, gid):
    """
    Tests about groups
    """

    group = host.group(name)

    if gid is None:
        assert group.exists is False
    else:
        assert group.exists
        assert group.gid == gid


def test_not_existing_user(host):
    """
    Tests user not exists if state is 'absent'
    """

    assert host.user('my-user').exists is False


def test_user_with_default_values(host):
    """
    Tests user exists if state is 'present'
    """

    user = host.user('my-user2')
    assert user.exists is True
    assert user.group == 'my-user2'

    # Home testing
    user_home = host.file('/home/my-user2')
    assert user_home.exists is True
    assert user_home.is_directory is True
    assert user_home.mode == 0o700
    assert user_home.user == 'my-user2'
    assert user_home.group == 'my-user2'


def test_user_with_custom_values(host):
    """
    Tests user exists if state is 'present' and custom values
    """

    user = host.user('my-user3')
    assert user.exists is True
    assert user.uid == 1501
    assert user.gid == 1501
    assert user.group == 'my-user3'
    assert user.groups == ['my-user3', 'my-group2']
    assert user.home == '/var/foo'
    assert user.shell == '/bin/sh'

    # Home testing
    user_home = host.file('/var/foo')
    assert user_home.exists is True
    assert user_home.is_directory is True
    assert user_home.mode == 0o755
    assert user_home.user == 'my-user3'
    assert user_home.group == 'my-group2'

    # Skeleton testing
    assert host.file('/var/foo/foo_bar').exists is True
    assert host.file('/var/foo/foo_bar').is_directory is True
    assert host.file('/var/foo/foo.test').exists is True
    assert host.file('/var/foo/foo.test').is_file is True
    assert host.file('/var/foo/foo_bar/.bar.test').exists is True
    assert host.file('/var/foo/foo_bar/.bar.test').is_file is True
