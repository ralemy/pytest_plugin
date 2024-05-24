# pytest_plugin
An example custom plugin for pytest

# Description

The demo consists of two files, one is the `pytest_plugin.py` which contains the plugin that shows how we can trap the progress of pytest through the tests. the other one is `sample_test.py` which contains an example test to run and see the effects of the plugin.

# Running from commandline

To run from command line issue the following command in a Python 3.11 virtual environment with pytest installed:
```
PYTHONPATH='.' pytest -p pytest_plugin sample_test.py
```
when finished, you can examine the `pytest.log` file to see the messages as testing progresses.

# Running in VS Code

in a VS Code workspace that has python extension and has set up for pytest, look for the `.vscode` directory and the `settings.json` file inside it.
the file should contain the following structure at the root of the json object:
```
{
        ".",
        "-p",
        "pytest_plugin"
}
```
