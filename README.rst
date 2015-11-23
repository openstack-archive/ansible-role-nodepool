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

Packages
~~~~~~~~

Repo index files should be up to date before using this role.

Role Variables
--------------

Dependencies
------------

Example Playbook
----------------

.. code-block:: yaml

    - name: Install nodepool
      hosts: nodepool
      roles:
        - ansible-role-nodepool
