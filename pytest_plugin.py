"""
    to test scripted pytest control
"""

import pytest

LOGFILE = "pytest.log"
with open(LOGFILE, "w") as f:
    print("", file=f)


def log(*args):
    with open(LOGFILE, "a") as f:
        print(*args, file=f)


def parse_object(x):
    args = []
    if not isinstance(x, object):
        return f"{x}"
    for key in dir(x):
        if not key.startswith("_"):
            args.append(f"\n\t\t{key}={getattr(x, key)}")
    return args


class MyPytestPlugin:
    """
    Hooks to get info from pytest
    """

    def __init__(self) -> None:
        pass

    # pylint: disable=unused-argument
    def pytest_collection_modifyitems(self, config, items):
        log("<<<<< collection done. >>>>>>", config, items)

    def pytest_sessionstart(self, session):
        log("*" * 10)
        log("session started", session)
        log("*" * 10)

    def pytest_sessionfinish(self, session, exitstatus):
        log("-" * 10)
        log("session finished", *parse_object(session), exitstatus)

    def pytest_runtest_logstart(self, nodeid, location):
        log("<<<<< log start >>>>>>", nodeid, location)

    def pytest_runtest_logfinish(self, nodeid, location):
        log("<<<<< log finish >>>>>>", nodeid, location)

    @pytest.hookimpl(hookwrapper=True)
    def pytest_runtest_protocol(self, item, nextitem):
        log("<<<<< protocol >>>>>>", item, nextitem)
        outcome = yield
        log("<<<<< protocol outcome >>>>>>", *parse_object(outcome))

    def pytest_collectreport(self, report):
        log("<<<<< collect report >>>>>>", report)

    def pytest_report_teststatus(self, report):
        log("<<<<< test status >>>>>>", *parse_object(report))

    def pytest_runtest_setup(self, item):
        log("<<<<< setup >>>>>>", item)

    def pytest_runtest_call(self, item):
        log("<<<<< runtest call >>>>>>", item)

    def pytest_runtest_teardown(self, item):
        log("<<<<< runtest teardown >>>>>>", item)


def pytest_configure(config):
    config.pluginmanager.register(MyPytestPlugin())
    log("my test plugin registered")
