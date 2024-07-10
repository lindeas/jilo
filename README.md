# jilo - JItsi Logs Observer

## overview

Bash scripts for collecting and displaying information about conference events from Jitsi Meet logs.

This is the command line tools repository. For a web interface to query Jilo, go to the **"[jilo-web](https://work.lindeas.com/redirect.php?url=jilo-web)"** repository.

The webpage for this project is https://lindeas.com/jilo. There you will find information about both Jilo and Jilo Web.

The main git repo of **Jilo** is:
- https://code.lindeas.com/lindeas/jilo

It is mirrored at:
- https://codeberg.org/lindeas/jilo
- https://github.com/lindeas/jilo
- https://gitlab.com/lindeas/jilo

You can use any of these git repos to get the program.

You are welcome to send feedback with issues, comments and pull requests to a git mirror you prefer.

## version

Current version: **0.1.1** released on **2024-06-18**

## components

Currently this has two components:

- `jilo` is the script for collecting data from the logs.
It is meant to be installed and run on the server and it needs read permissions for the logs.
Currently it works with Videobridge and Jicofo log files.
You can run it with cron to periodically update the new data from the logs.

- `jilo-cli` is a command line client for displaying stats from an already populated jilo database
It needs access to the jilo database.

## installation

You can install it in the following ways:

- use the latest deb package from the **[APT repo](https://lindeas.com/debian)** - recommended for Debian/Ubuntu
- use the latest **RPM package** - recommended for rpm-based systems
- download the latest release from the **"Releases"** section here
- clone the **git repo**:
```bash
git clone https://github.com/lindeas/jilo.git
cd jilo
```

## config

The config file **jilo.conf** overrides the default settings.
For more details check the comments in the scripts or use the --help option

## database

The database can be an SQLite file or MySQL/MariaDB database. The default is local sqlite file.

## running

You can run `jilo` once or add it to a crontab. If you run it periodically it will keep track of all.
events, detecting when the logs rotate and continuing from where it left on the previous run.

Use `jilo-cli` to visualize the info from the database that was gathered previously with `jilo`

`jilo-cli` can search for conference and participant events, and display events in a given time period..
Where appropriate, combine `jilo-cli` with sort, wc and other tools to get total numbers.
