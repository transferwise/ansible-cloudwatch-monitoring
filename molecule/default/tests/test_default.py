import os
import testinfra.utils.ansible_runner

# uses https://testinfra.readthedocs.io/en/latest/modules.html#modules

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_setup_file(host):
    f = host.file('/tmp/CloudWatchMonitoringScripts.zip')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_script_directory(host):
    f = host.file('/opt/aws-scripts-mon')

    assert f.exists
    assert f.is_directory
    assert f.user == 'root'
    assert f.group == 'root'


def test_script_file(host):
    f = host.file('/opt/aws-scripts-mon/cw-put-instance-data.sh')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'
    assert f.contains('export')
    assert f.contains('--TEST')
    assert f.contains('--BIGGER_TEST')
    assert f.contains('--WOAH')
    assert f.contains('/opt/aws-scripts-mon/')
