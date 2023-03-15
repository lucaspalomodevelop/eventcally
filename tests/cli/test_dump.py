def test_all(client, seeder, app, utils):
    user_id, admin_unit_id = seeder.setup_base()
    seeder.create_event(admin_unit_id, "RRULE:FREQ=DAILY;COUNT=7")
    seeder.create_event_with_co_organizers(admin_unit_id)

    runner = app.test_cli_runner()
    result = runner.invoke(args=["dump", "all"])
    assert result.exit_code == 0

    utils.get_endpoint_ok("developer")
    utils.get_endpoint_ok("dump_files", path="all.zip")
