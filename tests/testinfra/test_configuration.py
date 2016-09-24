"""
Role tests
"""
import pytest


# pytestmark = pytest.mark.docker_images(
pytestmark = pytest.mark.docker_images(
    'infopen/ubuntu-trusty-ssh:0.1.0',
    'infopen/ubuntu-xenial-ssh-py27:0.2.0'
)


def test_groups(Group):
    """
    Tests about groups
    """

    group_a = Group('my-group')
    assert group_a.exists is False

    group_b = Group('my-group2')
    assert group_b.exists is True
    assert group_b.gid == 1500

    group_c = Group('my-user3')
    assert group_c.exists is True
    assert group_c.gid == 1501


def test_not_existing_user(User):
    """
    Tests user not exists if state is 'absent'
    """

    user = User('my-user')
    assert user.exists is False


def test_user_with_default_values(User, File):
    """
    Tests user exists if state is 'present'
    """

    user = User('my-user2')
    assert user.exists is True
    assert user.group == 'my-user2'

    # Home testing
    assert File('/home/my-user2').exists is True
    assert File('/home/my-user2').is_directory is True
    assert File('/home/my-user2').mode == 0o700
    assert File('/home/my-user2').user == 'my-user2'
    assert File('/home/my-user2').group == 'my-user2'


def test_user_with_custom_values(User, File):
    """
    Tests user exists if state is 'present' and custom values
    """

    user = User('my-user3')
    assert user.exists is True
    assert user.uid == 1501
    assert user.gid == 1501
    assert user.group == 'my-user3'
    assert user.groups == ['my-user3', 'my-group2']
    assert user.home == '/var/foo'
    assert user.shell == '/bin/sh'

    # Home testing
    assert File('/var/foo').exists is True
    assert File('/var/foo').is_directory is True
    assert File('/var/foo').mode == 0o755
    assert File('/var/foo').user == 'my-user3'
    assert File('/var/foo').group == 'my-group2'

    # Skeleton testing
    assert File('/var/foo/foo_bar').exists is True
    assert File('/var/foo/foo_bar').is_directory is True
    assert File('/var/foo/foo.test').exists is True
    assert File('/var/foo/foo.test').is_file is True
    assert File('/var/foo/foo_bar/.bar.test').exists is True
    assert File('/var/foo/foo_bar/.bar.test').is_file is True
