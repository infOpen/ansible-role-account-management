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


def test_user_with_default_values(User):
    """
    Tests user exists if state is 'present'
    """

    user = User('my-user2')
    assert user.exists is True
