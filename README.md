# ansible-role-apt-mirror

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Build Status](https://travis-ci.org/joshuacherry/ansible-role-apt-mirror.svg?branch=master)](https://travis-ci.org/joshuacherry/ansible-role-apt-mirror)
![Ansible](https://img.shields.io/badge/ansible-2.4.3.0-blue.svg)
![Ansible](https://img.shields.io/badge/ansible-2.5.0-blue.svg)

Configures sources.list and/or [apt-mirror](https://apt-mirror.github.io/) on Ubuntu.

## Requirements

- Ansible
  - Tested Versions:
    - 2.4.3.0
    - 2.5.0

## Install

### Install from GitHub

`ansible-galaxy install git+https://github.com/joshuacherry/ansible-role-apt-mirror.git`

## Features

- apt-mirror on server
- apt sources on client

| OS            |
| :------------ |
| Ubuntu 16.04  |

## Versioning

[Semantic Versioning](http://semver.org/)

For the versions available, see the [tags on this repository](https://github.com/joshuacherry/ansible-role-apt-mirror/tags).

Additionaly you can see what change in each version in the [CHANGELOG.md](CHANGELOG.md) file.

## Role variables

Look to the [defaults](defaults/main.yml) properties file to see the possible configuration properties.

## Testing

This role includes a Vagrantfile used with a Docker-based test harness that approximates the Travis CI setup for integration testing. Using Vagrant allows all contributors to test on the same platform and avoid false test failures due to untested or incompatible docker versions.

1. Install [Vagrant](https://www.vagrantup.com/) and [VirtualBox](https://www.virtualbox.org/).
1. Run `vagrant up` from the same directory as the Vagrantfile in this repository.
1. SSH into the VM with: `vagrant ssh`
1. Run tests with `molecule`.

### Testing with Docker and tox

Tox will test against the configured dependencies in [tox.ini](tox.ini). This allows you to test the role against multiple version of ansible, molecule, python, and more. Once the dependencies are set, tox will run the same molecule command to test code.

```bash
cd /ansible-role-apt-mirror
tox
```

### Testing with Docker and molecule

```bash
cd /ansible-role-apt-mirror
molecule test
```

See `molecule` for more information including a full list of available commands.

### interactive debugging

You can use log into a docker image created by molecule for interactive testing with the below commands.

```bash
cd /ansible-role-apt-mirror
molecule converge
# Ubuntu
docker exec -it ubuntu /bin/bash
# CentOS
docker exec -it centos /bin/bash
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