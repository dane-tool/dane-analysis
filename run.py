# run.py
# ======
#
# For checkpoint purposes in the data science capstone course.
#

import argparse
import subprocess

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument(
        'targets',
        help="""
init  : Parses and sets up the tool to use your configuration at `config/tool.json`.
run   : Builds all images, initializes configuration, then starts the data collection tool.
build : Builds local Docker images needed to run the data collection tool.
start : Starts up the tool using pre-built images and pre-initialized configuration.
stop  : Gracefully halts the data collection tool.
down  : Ensures all Docker resources for the tool are stopped and removed.
        """,
        nargs='*'
    )
    args = parser.parse_args()
    targets = args.targets

    proc_opts = {
        'stdout': subprocess.PIPE
    }

    if len(targets) == 0:
        targets.append('run')

    # The init target is special because we can run it with Python locally.
    if 'init' in targets:

        targets.remove('init')

        subprocess.Popen(
            ['python', 'tool/setup/build_compose.py', '-s', 'tool/', '-c', 'config/tool.json'],
            **proc_opts
        ).wait()

    # All other targets must launch Docker, and are run through the Makefile.
    for target in targets:
        subprocess.Popen(
            ['make', target],
            **proc_opts
        ).wait()
