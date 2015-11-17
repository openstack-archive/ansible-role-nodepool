# Copyright 2015 Red Hat, Inc.
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

import os

from ansible import utils

from ansible import callbacks
from ansible.playbook import PlayBook

rolename = os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..'))

extra_vars = {
    'rolename': rolename
}

stats = callbacks.AggregateStats()
playbook_callbacks = callbacks.PlaybookCallbacks(verbose=utils.VERBOSITY)
runner_callbacks = callbacks.PlaybookRunnerCallbacks(
    stats, verbose=utils.VERBOSITY)


playbook = PlayBook(
    callbacks=playbook_callbacks,
    extra_vars=extra_vars,
    host_list='tests/inventory',
    playbook='tests/test.yaml',
    runner_callbacks=runner_callbacks,
    stats=stats)

playbook.run()
playbook.run()

for host in sorted(playbook.stats.processed.keys()):
    print(playbook.stats.summarize(host))
