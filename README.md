Welcome to rundeck Ansible Role’s documentation!
================================================

Role Name
---------

A brief description of the role goes here.

### Requirements

Any pre-requisites that may not be covered by Ansible itself or the role
should be mentioned here. For instance, if the role uses the EC2 module,
it may be a good idea to mention in this section that the boto package
is required.

### Dependencies

A list of other roles hosted on Galaxy should go here, plus any details
in regards to parameters that may need to be set for other roles, or
variables that are used from other roles.

### Example Playbook

Including an example of how to use your role (for instance, with
variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
        - { role: username.rolename, x: 42 }

pip ansible role default variables
----------------------------------

#### Sections

-   rundeck packaging
-   rundeck configuration

### rundeck packaging

`rundeck_docker_imagen`

> rundeck docker image

    rundeck_docker_image: melodous/rundeck

`rundeck_version`

> rundeck docker image version (TAG)

    rundeck_version: 2.8.2

`rundeck_docker_labels`

> Yaml dictionary which maps Docker labels. os\_environment: Name of the
> environment, example: Production, by default “default”.
> os\_contianer\_type: Type of the container, by default rundeck.

    rundeck_docker_labels:
      os_environment: "{{ docker_os_environment | default('default') }}"
      os_contianer_type: rundeck

### rundeck configuration

`rundeck_group`

> rundeck group name

    rundeck_group: rundeck

`rundeck_group_id`

> rundeck group id

    rundeck_group_id: 110

`rundeck_user`

> rundeck user name

    rundeck_user: rundeck

`rundeck_user_id`

> rundeck user id

    rundeck_user_id: 106

`conf_dir`

> Configuration directory

    rundeck_conf_dir: /etc/rundeck

`rundeck_data_dir`

> Data directory

    rundeck_data_dir: /var/lib/rundeck

`rundeck_log_dir`

> Log directory

    rundeck_log_dir: /var/log/rundeck

`rundeck_server_url`

> Url of the rundeck server

    rundeck_server_url: "{{ ansible_hostname }}"

`rundeck_loglevel`

> Default log level

    rundeck_loglevel: INFO

Changelog
---------

**rundeck**

This project adheres to Semantic Versioning and human-readable
changelog.

### rundeck master - unreleased

##### Added

-   First addition

##### Changed

-   First change

### rundeck v0.0.0 - DATE

##### Added

-   Initial version

Copyright
---------

rundeck

Copyright (C) DATE User/Company &lt;<email@email.com>&gt;

LICENSE
