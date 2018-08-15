def test_nodepool_launcher_is_running(Service):
    nodepool_launcher = Service('nodepool-launcher')

    assert nodepool_launcher.is_running
    assert nodepool_launcher.is_enabled
