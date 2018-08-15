def test_nodepool_user(host):
    user = host.user('nodepool')
    assert user.exists
    assert user.name == 'nodepool'
    assert user.group == 'nodepool'
    assert user.home == '/var/lib/nodepool'

def test_nodepool_builder_service(host):
    service = host.service('nodepool-builder')
    assert service.is_running
    assert service.is_enabled


def test_nodepool_launcher_service(host):
    service = host.service('nodepool-launcher')
    assert service.is_running
    assert service.is_enabled
