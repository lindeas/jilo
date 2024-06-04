# jilo

JItsi Logs Observer

Currently this has two components:

- **jilo** is the script for collecting data from the logs.
It is meant to be installed and run on the server and it needs read permissions for the logs.
Currently it works with Videobridge and Jicofo log files.
You can run it with cron to periodically update the new data from the logs.

- **jilo-cli** is a command line client for displaying stats from an already populated jilo database
It needs access to the jilo database.

The database can be an SQLite file or MySQL/MariaDB database. The default is local sqlite file.

The config file **jilo.conf** overrides the default settings.
For more details check the comments in the scripts or use the --help option
