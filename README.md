# ansible-role-apt-mirror

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Build Status](https://travis-ci.org/joshuacherry/ansible-role-apt-mirror.svg?branch=master)](https://travis-ci.org/joshuacherry/ansible-role-apt-mirror)
![Ansible](https://img.shields.io/badge/ansible-2.5-blue.svg)
![Ansible](https://img.shields.io/badge/ansible-2.6-blue.svg)
![Ansible](https://img.shields.io/badge/ansible-2.7-blue.svg)

Configures sources.list and/or [apt-mirror](https://apt-mirror.github.io/) on Ubuntu.

## Requirements

- Ansible
  - Tested Versions:
    - 2.5
    - 2.6
    - 2.7

## Install

### Install from GitHub

`ansible-galaxy install git+https://github.com/joshuacherry/ansible-role-apt-mirror.git`

## Features

- apt-mirror on server
- apt sources on client

| OS            |
| :------------ |
| Ubuntu 16.04  |
| Ubuntu 18.04  |

## Versioning

[Semantic Versioning](http://semver.org/)

For the versions available, see the [tags on this repository](https://github.com/joshuacherry/ansible-role-apt-mirror/tags).

Additionaly you can see what change in each version in the [CHANGELOG.md](CHANGELOG.md) file.

## Role variables

Look to the [defaults](defaults/main.yml) properties file to see the possible configuration properties.

## Testing

This role includes a Vagrantfile used with a Docker-based test harness that approximates the Travis CI setup for integration testing. Using Vagrant allows all contributors to test on the same platform and avoid false test failures due to untested or incompatible docker versions.

This molecule configuration depends on docker images from [https://hub.docker.com/u/joshuacherry/](https://hub.docker.com/u/joshuacherry/) to quickly test the role against a variety of operating systems.

1. Install [Vagrant](https://www.vagrantup.com/) and [VirtualBox](https://www.virtualbox.org/).
1. Run `vagrant up` from the same directory as the Vagrantfile in this repository.
1. SSH into the VM with: `vagrant ssh`
1. Run tests with `molecule`.

### Testing with Docker and tox

Tox will test against the configured dependencies in [tox.ini](tox.ini). This allows you to test the role against multiple version of ansible, molecule, python, and more. Once the dependencies are set, tox will run the same molecule command to test code.

Due to how Virtualbox mounts shared folders, it is recommended to copy the role into a local directory within the virtual machine before running tox, otherwise the python environments will perform significantly slower. Run the below commands each time you make a change to the source code and need to test against all scenarios defined in [tox.ini](tox.ini)

```bash
rsync -ua /ansible-role-apt-mirror/ ~/ansible-role-apt-mirror/ --delete
cd ~/ansible-role-apt-mirror
tox
```

### Testing with Docker and molecule

This method will only test the code with the most recent version of Ansible, tox testing should be used before commits to master so that all scenarios can be tested.

```bash
cd /ansible-role-apt-mirror
molecule test
```

See `molecule` for more information including a full list of available commands.

### interactive debugging

You can use log into a docker image created by molecule for interactive testing with the below commands. As defined in [molecule.yml](molecule/default/molecule.yml), the default instance is set to `ubuntu1604`. If you wish to test other operating systems, you must define the environment variables `MOLECULE_DISTRO` and `MOLECULE_DOCKER_COMMAND`. A table of supported options are below.

```bash
cd /ansible-role-apt-mirror
export MOLECULE_DISTRO=ubuntu1604
export MOLECULE_DOCKER_COMMAND=/lib/systemd/systemd
molecule converge
docker exec -it instance /bin/bash
```

## Example Playbook

```yaml
---
- name: Playbook for ansible-role-apt-mirror
  hosts: all

  tasks:
  - include_role:
      name: ansible-role-apt-mirror
  vars:
    apt_mirror_client: true
    apt_mirror_server: true
    apt_mirror_ubuntu_mirror: archive.ubuntu.com/ubuntu
    apt_mirror_repos:
      - "deb-amd64 http://{{ apt_mirror_ubuntu_mirror }} xenial main restricted universe multiverse"
      - "deb-amd64 http://{{ apt_mirror_ubuntu_mirror }} xenial-security main restricted universe multiverse"
      - "deb-amd64 http://{{ apt_mirror_ubuntu_mirror }} xenial-updates main restricted universe multiverse"
      - "deb-src http://{{ apt_mirror_ubuntu_mirror }} xenial main restricted universe multiverse"
      - "deb-src http://{{ apt_mirror_ubuntu_mirror }} xenial-security main restricted universe multiverse"
      - "deb-src http://{{ apt_mirror_ubuntu_mirror }} xenial-updates main restricted universe multiverse"
    apt_mirror_client_repos:
      - "deb http://{{ apt_mirror_ubuntu_mirror }} xenial main restricted universe multiverse"
      - "deb http://{{ apt_mirror_ubuntu_mirror }} xenial-security main restricted universe multiverse"
      - "deb http://{{ apt_mirror_ubuntu_mirror }} xenial-updates main restricted universe multiverse"
      - "deb-src http://{{ apt_mirror_ubuntu_mirror }} xenial main restricted universe multiverse"
      - "deb-src http://{{ apt_mirror_ubuntu_mirror }} xenial-security main restricted universe multiverse"
      - "deb-src http://{{ apt_mirror_ubuntu_mirror }} xenial-updates main restricted universe multiverse"
    apt_mirror_schedule:
      - name: apt-mirror updates
        special_time: daily
        job: /usr/bin/apt-mirror > /var/spool/apt-mirror/var/cron.log
        cron_file: apt-mirror
    enable_apt_mirror: true
```