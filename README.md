# Generating and Analyzing Network Traffic in Diverse Network Conditions

Analysis and documentation to support the use of our data generation tool.

The source code for the tool itself can be found at [`network-data-generation`](https://github.com/parkeraddison/network-data-generation).

**Table of contents:**
- [Getting started](#getting-started)
  - [Requirements](#requirements)
- [Using the tool](#using-the-tool)
  - [Configuration](#configuration)
  - [Environment file and secrets](#environment-file-and-secrets)
  - [Running](#running)
  - [Data](#data)
- [Generating analysis](#generating-analysis)
- [FAQ](#faq)
- [Citing](#citing)

## Getting started

You can start using this tool and conducting analysis of different network conditions by running:
```bash
git clone \
https://github.com/parkeraddison/generating-and-analyzing-network-traffic-in-diverse-network-conditions.git \
--recursive
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
| behaviors | List of one or more target behaviors. All target behaviors will be run for each specified set of network conditions. For possible values see [Target behaviors](#target-behaviors). |
| conditions | List of nested configuration specifying desired network conditions. E.g. `[{"latency": "50ms", "bandwidth": "10Mbps"}]`. For configuration see [Conditions config](#conditions-config). |
| vpn | Nested configuration for a VPN connection. For configuration see [VPN Config](#vpn-config). |

<a name="target-behaviors"></a>
**Target behaviors**
| Value | Description |
| --- | --- |
| ping | Ping a DNS server once every three seconds. |
| script | Run a script that replicates the `ping` behavior. **Will be deprecated**. |
| none | Do nothing. |
| browsing | Run a script to endlessly browse Twitter. |
| streaming | Run a script to endlessly watch YouTube. |

<a name="conditions-config"></a>
**Conditions config**
| Key | Description |
| --- | --- |
| latency | Milliseconds. The desired amount of network latency to be injected. E.g. `"50ms"` |
| bandwidth | Megabits per second. The desired download speed. E.g. `"10Mbps"` |

<a name="vpn-config"></a>
**VPN config**
| Key | Description |
| --- | --- |
| enabled | `true` or `false`. Whether or not a VPN should be used. **WIP** |
| server | URL or IP to the desired VPN service. E.g. `"vpn.ucsd.edu"`. **WIP** |

### Environment file and secrets

The containers will need secret variables that store things like VPN or website login credentials.

Please create a file named `.env` and place it in this directory. Inside the file, add the login information for your VPN:
```
VPN_USERNAME=<your UCSD username>
VPN_USERGROUP=<the 'group' to use for the VPN -- probably "2-Step Secured - allthruucsd">
VPN_PASSWORD=<your UCSD password>
```

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

After the tool has been stopped, data can be found in `data/`.

## Generating analysis

Once data is collected, analysis can be done to demonstrate disparity in the data between different network conditions. **WIP**

## FAQ

1. **The tool isn't working. It fails silently, or fails to launch behaviors or network-stats.**
   Make sure that all submodules have been cloned. You can do this by running
   ```bash
   git submodule update --init --recursive
   ```

## Citing

If you choose to use this tool, please cite it with the following BibTeX entry: **WIP**
```bibtex
@misc{tbd2021,
  author = {Addison, Parker and
            Altekar, Sahil and
            Yaseen, Danial},
  title  = {tbd},
  school = {University of California, San Diego},
  year   = 2021,
  url    = {https://github.com/parkeraddison/generating-and-analyzing-network-traffic-in-diverse-network-conditions}
}
```
