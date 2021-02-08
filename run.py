# run.py
# ======
#
# For checkpoint purposes in the data science capstone course.
#

import argparse
import subprocess

if __name__ == '__main__':

    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument(
        'targets',
        help="""You may specify the following targets:

init  : Parses and sets up the tool to use your configuration at `config/tool.json`.
run   : Builds all images, initializes configuration, then starts the data collection tool.
build : Builds local Docker images needed to run the data collection tool.
start : Starts up the tool using pre-built images and pre-initialized configuration.
stop  : Gracefully halts the data collection tool.
down  : Ensures all Docker resources for the tool are stopped and removed.
test  : Check that you have recent version of Docker and Compose.

Defaults to `run` if no targets are specified.
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

    # The test target is used for checkpoint purposes, and should simply return
    # a message explaining that this will not work on DSMLP because the cluster
    # does not support running Docker in Docker.
    if 'test' in targets:

        # If Docker and Compose are installed, then we can actually just print a
        # message saying all is good.
        is_docker_installed = subprocess.getoutput('docker version -f "{{.Client.Version}}"') >= '19.0.0'
        is_compose_installed = subprocess.getoutput('docker-compose version --short') >= '1.27.0'

        if is_docker_installed and is_compose_installed:
            print(
                """
All good. You have a recent version of Docker and Compose installed!

Try running with `--help` to see the other targets you can try.
                """
            )
        else:
            print(
                """
Hi there, thanks for running the checkpoint test on this repository.

| You may notice that nothing is happening, and that's because a large component
| of our capstone project is creating a data collection tool which gathers
| network traffic data from a variety of configurable network conditions.
|
| The tool involves running Docker containers, and therefore cannot be run
| within DSMLP or any other system which lacks access to Docker and Compose.
|
| Without access to Docker, the only runnable target is `init`.

Please sure that you've cloned this repository with `--recursive` otherwise the
tool submodule will be empty and all targets will fail!

If you wish to see the tool in its own repository, visit:
  https://github.com/parkeraddison/network-data-generation
                """
            )

        exit(0)

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
