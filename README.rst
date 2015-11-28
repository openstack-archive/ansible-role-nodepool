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

Package repository index files should be up to date before using this role, we
do not manage them.

Role Variables
--------------

.. code-block:: yaml

    # Name of the user to be created.
    # Default: nodepool
    nodepool_user_name: nodepool

    # Name of the group to be created.
    # Default: nodepool
    nodepool_user_group: nodepool

    # Path of home directory to be created.
    # Default: /var/lib/nodepool
    nodepool_user_home: /var/lib/nodepool

    # Path to folder containing elements/ and scripts/ used by nodepool.
    # Default: ""
    nodepool_elements_dir: ""

    # Path to folder containing elements/ and scripts/ used by nodepool.
    # Default: ""
    nodepool_scripts_dir: ""

Dependencies
------------

Example Playbook
----------------

.. code-block:: yaml

    - name: Install nodepool
      hosts: nodepool
      roles:
        - ansible-role-nodepool
