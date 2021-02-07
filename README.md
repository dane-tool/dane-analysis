# Generating and Analyzing Network Traffic in Diverse Network Conditions

Analysis and documentation to support the use of our data generation tool.

**Table of contents:**
- [Getting started](#getting-started)
  - [Requirements](#requirements)
- [Using the tool](#using-the-tool)
  - [Configuration](#configuration)
  - [Running](#running)
  - [Data](#data)
- [Generating analysis](#generating-analysis)
- [Citing](#citing)

## Getting started

You can start using this tool and conducting analysis of different network conditions by running:
```bash
git clone https://github.com/parkeraddison/generating-and-analyzing-network-traffic-in-diverse-network-conditions --recursive
```

### Requirements

The data collection tool runs on Linux. You will need:
- [**Docker 19.03+**](https://docs.docker.com/get-docker/)
- [**Docker Compose 1.27+**](https://docs.docker.com/compose/install/)
- [**GNU Make**](https://www.gnu.org/software/make/)

The data analysis runs on all systems. You will need:
- **WIP**

## Using the tool

Our tool establishes Docker containers with configurable network conditions, then runs target behaviors such as browsing the internet, and collects data on the network traffic generated using [`network-stats`](https://github.com/Viasat/network-stats).

To use the tool, you must configure your desired network conditions and behaviors.

Source code for the tool can be found at [`network-data-generation`](https://github.com/parkeraddison/network-data-generation).

### Configuration

See [`tool.json`](config/tool.json) for configuration:

| Key | Description |
| --- | --- |
| behaviors | List of one or more target behaviors. All target behaviors will be run for each specified set of network conditions. For possible values see [target-behavior]. |
| conditions | List of nested configuration specifying desired network conditions. E.g. `[{"latency": "50ms", "bandwidth": "10Mbps"}]`. For configuration see [condition-config]. |
| vpn | Nested configuration for a VPN connection. For configuration see [vpn-config]. |
| envFile | Filepath to a file used to store secret environment variables such as VPN and website login information. **TODO** |
| dataDir | Path to directory where the data will be collected. **WIP** |

[target-behavior]: <>

| target-behavior | Description |
| --- | --- |
| ping | Ping a DNS server once every three seconds. |
| script | Run a script that replicates the `ping` behavior. **Will be deprecated**. |
| none | Do nothing. |
| browsing | Run a script to endlessly browse Twitter. **WIP** |
| streaming | Run a script to endlessly watch YouTube. **WIP** |

[condition-config]: <>

| condition-config | Description |
| --- | --- |
| latency | Milliseconds. The desired amount of network latency to be injected. E.g. `"50ms"` |
| bandwidth | Megabits per second. The desired download speed. E.g. `"10Mbps"` |

[vpn-config]: <>

| vpn-config | Description |
| --- | --- |
| enabled | `true` or `false`. Whether or not a VPN should be used. **WIP** |
| server | URL or IP to the desired VPN service. E.g. `"vpn.ucsd.edu"`. **WIP** |

### Running

Once you're satisfied with your configuration, simply open a terminal to this directory, and run
```bash
make
```

When you're done collecting data, open a new terminal in this directory and run
```bash
make stop
```

### Data

After the tool has been stopped, data can be found in `tool/data/`.

## Generating analysis

Once data is collected, analysis can be done to demonstrate disparity in the data between different network conditions. **WIP**

## Citing

If you choose to use this tool, please cite it with the following BibTeX entry: **WIP**
```bibtex
```
