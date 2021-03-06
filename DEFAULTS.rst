.. vim: foldmarker=[[[,]]]:foldmethod=marker

pip ansible role default variables
==================================

.. contents:: Sections
   :local:

rundeck packaging
-----------------------

.. envvar:: rundeck_docker_imagen

   rundeck docker image

::

  rundeck_docker_image: melodous/rundeck




.. envvar:: rundeck_version

   rundeck docker image version (TAG)

::

  rundeck_version: 2.8.2




.. envvar:: rundeck_docker_labels

   Yaml dictionary which maps Docker labels.
   os_environment: Name of the environment, example: Production, by default "default".
   os_contianer_type: Type of the container, by default rundeck.

::

  rundeck_docker_labels:
    os_environment: "{{ docker_os_environment | default('default') }}"
    os_contianer_type: rundeck




rundeck configuration
---------------------------

.. envvar:: rundeck_group

   rundeck group name

::

  rundeck_group: rundeck




.. envvar:: rundeck_group_id

   rundeck group id

::

  rundeck_group_id: 110




.. envvar:: rundeck_user

   rundeck user name

::

  rundeck_user: rundeck




.. envvar:: rundeck_user_id

   rundeck user id

::

  rundeck_user_id: 106




.. envvar:: conf_dir

   Configuration directory

::

  rundeck_conf_dir: /etc/rundeck




.. envvar:: rundeck_data_dir

   Data directory

::

  rundeck_data_dir: /var/lib/rundeck




.. envvar:: rundeck_log_dir

   Log directory

::

  rundeck_log_dir: /var/log/rundeck




.. envvar:: rundeck_server_url

   Url of the rundeck server

::

  rundeck_server_url: "{{ ansible_hostname }}"




.. envvar:: rundeck_loglevel

   Default log level

::

  rundeck_loglevel: INFO



