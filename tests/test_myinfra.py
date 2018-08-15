def test_nodepool_builder_is_running(host):
    service = host.service('nodepool-builder')
    assert service.is_running
    assert service.is_enabled


def test_nodepool_launcher_is_running(host):
    service = host.service('nodepool-launcher')
    assert service.is_running
    assert service.is_enabled
