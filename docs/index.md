# Background
Todo

# Tool
Our tool establishes Docker containers with configurable network conditions,
then runs target behaviors such as browsing the internet, and collects data on
the network traffic generated using
[network-stats](https://github.com/parkeraddison/network-stats/tree/5e4173d310faf40b7f35262e0a18e447ba91e5dc).

To use the tool, you must configure your desired network conditions and behaviors.

Source code for the tool can be found at [network-data-generation](https://github.com/parkeraddison/network-data-generation).

## Requirements
The data collcetion tool runs on Linux. You will need:
* [Docker 19.03+](https://docs.docker.com/get-docker/)
* [Docker Compose 1.27+](https://docs.docker.com/compose/install/)
* [GNU Make](https://www.gnu.org/software/make/)

## Configuration
See [tool.json](tool.json) for configuration:
| Key | Description |
| --- | --- |
| behaviors | List of one or more target behaviors. All target behaviors will be
run for each specified set of network conditions. For possible values see 
[Target
behaviors](https://github.com/parkeraddison/generating-and-analyzing-network-traffic-in-diverse-network-conditions#target-behaviors).
|
| conditions | TODO |
| vpn | TODO |

## Setup

# Analysis


