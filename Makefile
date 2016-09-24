# Check all prerequites are OK
check-prerequisites:
ifeq (, $(shell which docker))
	$(error "No docker in $(PATH), consider install docker package")
endif


# Get or set SSH vars
check-ssh-vars:
SSH_PRIVATE_KEY ?= $(HOME)/.ssh/id_rsa
SSH_PUBLIC_KEY ?= $(HOME)/.ssh/id_rsa.pub


# Clean all
clean: clean-test clean-pyc


# Clean test environments
clean-test:
	rm -fr .tox/
	rm -f .coverage
	rm -fr reports/


# Clean python files
clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +


# Target used to execute tests on all tox environments
test-docker: check-prerequisites check-ssh-vars
test-docker: export SSH_PRIVATE_KEY_PATH = $(SSH_PRIVATE_KEY)
test-docker: export SSH_PUBLIC_KEY_PATH = $(SSH_PUBLIC_KEY)
test-docker:
	tox


# Target used to execute tests on one tox environment
test-env: check-prerequisites check-ssh-vars
test-env: export SSH_PRIVATE_KEY_PATH = $(SSH_PRIVATE_KEY)
test-env: export SSH_PUBLIC_KEY_PATH = $(SSH_PUBLIC_KEY)
test-env:
ifndef TOXENV
	$(error TOXENV is undefined)
endif
	tox -e "${TOXENV}"


test-vagrant:
	vagrant up
	vagrant provision
	vagrant ssh-config > .vagrant/ssh-config
	testinfra --hosts=account_management_trusty --ssh-config=.vagrant/ssh-config --noconftest
	testinfra --hosts=account_management_xenial --ssh-config=.vagrant/ssh-config --noconftest
