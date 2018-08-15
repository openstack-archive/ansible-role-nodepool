def test_nodepool_launcher_is_running(host):
    nodepool_launcher = host.service('nodepool-launcher')

    assert nodepool_launcher.is_running
    assert nodepool_launcher.is_enabled
