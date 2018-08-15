# Copyright 2018 Red Hat, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.


def test_nodepool_user(host):
    user = host.user('nodepool')
    assert user.exists
    assert user.name == 'nodepool'
    assert user.group == 'nodepool'
    assert user.home == '/var/lib/nodepool'


def test_nodepool_builder_service(host):
    f = host.file('/etc/systemd/system/nodepool-builder.service')
    assert f.exists
    assert f.is_file
    assert f.user == 'root'
    assert f.group == 'root'
    assert f.mode == '0o644'

    service = host.service('nodepool-builder')
    assert service.is_running
    assert service.is_enabled


def test_nodepool_launcher_service(host):
    f = host.file('/etc/systemd/system/nodepool-launcher.service')
    assert f.exists
    assert f.is_file
    assert f.user == 'root'
    assert f.group == 'root'
    assert f.mode == '0o644'

    service = host.service('nodepool-launcher')
    assert service.is_running
    assert service.is_enabled
