# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

| Change Type   | Description                            |
| :------------ | :------------------------------------- |
| Added         | for new features.                      |
| Changed       | for changes in existing functionality. |
| Deprecated    | for soon-to-be removed features.       |
| Removed       | for now removed features.              |
| Fixed         | for any bug fixes.                     |
| Security      | in case of vulnerabilities.            |

## [Unreleased]

## [1.0.1] - 2018-04-17

### Changed

- Travis now uses a matrix of tests for each tox scenario
- Moved .yamllint into molecule scenario
- Updated README
- Changed Vagrantfile to use most recent ansible and docker-compose
- Molecule default scenario will build platforms based on environmental variables set in tox ( MOLECULE_DISTRO & MOLECULE_DOCKER_COMMAND )
- Updated Tox to test multiple operating systems and ansible versions

[Unreleased]: https://github.com/joshuacherry/ansible-role-apt-mirror/compare/1.0.0...HEAD
[1.0.1]: https://github.com/joshuacherry/example-ansible-role/compare/1.0.0...1.0.1