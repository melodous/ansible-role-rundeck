def test_rundeck_server_running_and_enabled(Command, Service):
    # Check that docker service is running and enabled
    docker_service = Service("docker")
    assert docker_service.is_running
    assert docker_service.is_enabled
    # Check that rundeck service is running and enabled
    rundeck_service = Service("rundeck")
    assert rundeck_service.is_running
    assert rundeck_service.is_enabled


def test_rundeck_start_stop(Command, Service):
    Command.run_expect([0], "systemctl stop rundeck")
    rundeck_service = Service("rundeck")
    assert not rundeck_service.is_running
    Command.run_expect([0], "systemctl start rundeck")
    assert rundeck_service.is_running
    Command.run_expect([0], "systemctl restart rundeck")
    assert rundeck_service.is_running
