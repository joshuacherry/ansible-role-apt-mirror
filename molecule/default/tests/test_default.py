"""
Runs Default tests
Available Modules: http://testinfra.readthedocs.io/en/latest/modules.html

"""
import os
import testinfra.utils.ansible_runner

TESTINFRA_HOSTS = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_apt_mirror_is_installed(host):
    """
    Tests that apt-mirror is installed
    """
    apt_mirror = host.package("apt-mirror")
    assert apt_mirror.is_installed


def test_apt_mirror_list_file(host):
    """
    Tests that the mirror.list file is created correctly
    """
    mirror = host.file('/etc/apt/mirror.list')
    assert 'set base_path    /var/spool/apt-mirror' in mirror.content_string


def test_apt_sources_list_file(host):
    """
    Tests that the sources.list file is created correctly
    """
    sources = host.file('/etc/apt/sources.list')
    assert 'Configured to point to upstream' in sources.content_string


def test_apt_cron_file(host):
    """
    Tests that the cron entry file is created correctly
    """
    cron = host.file('/etc/cron.d/apt-mirror')
    assert '@daily apt-mirror /usr/bin/apt-mirror' in cron.content_string
