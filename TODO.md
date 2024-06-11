* ~~Incorporate all scripts into a single one~~
* ~~Default configs for~~
    - ~~files locations (logs, scripts, etc.)~~
    - ~~check for database integrity~~
    - ~~checks needed (if there is JVB, parse its logs, if not - don't, etc.)~~
* Option to upload the data to a remote DB for displaying in Grafana
    - ~~MariaDB/MySQL~~
    - Prometheus
    - InfluxDB
* Add more stats:
    - ~~participants (join/leave time and details)~~
    - issues
    - errors
    - ~~info about JVBs used~~
---
* FIXMEs:
    - ~~long commandline options work ok in jilo-cli, but not in jilo - update them as in cli~~
    - ~~finish SQL refactoring, move to separate tables for conferences and participants, linked by id~~
    - update jilo-cli to work with new SQL
    - fix sqlite and mysql schemas differences with the new SQL
