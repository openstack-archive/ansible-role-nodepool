=====================
ansible-role-nodepool
=====================

Ansible role to manage Nodepool

* License: Apache License, Version 2.0
* Documentation: https://ansible-role-nodepool.readthedocs.org
* Source: https://git.openstack.org/cgit/openstack/ansible-role-nodepool
* Bugs: https://bugs.launchpad.net/ansible-role-nodepool

Description
-----------

Nodepool is a system for launching single-use test nodes on demand based on
images built with cached data. It is designed to work with any OpenStack based
cloud, and is part of a suite of tools that form a comprehensive test system
including Jenkins and Zuul.

Requirements
------------

* pip3 to be installed if using nodepool_install_method: (git|pip)

Packages
~~~~~~~~

Package repository index files should be up to date before using this role, we
do not manage them.

Sudo
~~~~

You will be required to create the appropriate sudoers file if you plan on
creating DIBs.

Role Variables
--------------


.. literalinclude:: ../../defaults/main.yaml
   :language: yaml
   :start-after: under the License.

Dependencies
------------

Example Playbook
----------------

.. code-block:: yaml

    - name: Install nodepool
      hosts: nodepool
      roles:
        - ansible-role-nodepool
