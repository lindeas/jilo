# Changelog

All notable changes to this project will be documented in this file.

---

## Unreleased

#### Links
- upstream: https://code.lindeas.com/lindeas/jilo/compare/v0.1.1...HEAD
- codeberg: https://codeberg.org/lindeas/jilo/compare/v0.1.1...HEAD
- github: https://github.com/lindeas/jilo/compare/v0.1.1...HEAD
- gitlab: https://gitlab.com/lindeas/jilo/-/compare/v0.1.1...HEAD

### Added
- Added 'jitsi_components' table to handle events related to the platform health
- Added jicofo starting, xmpp registering and started events
- Added jvb added, removed and lost events
- Added jvb health-check scheduled and stopped events
- Added "no operational bridges" and "no bridge available" events
- Added "jitsi-component" service level events search in jilo-cli

### Changed

### Fixed

---

## 0.1.1 - 2024-06-18

#### Links
- upstream: https://code.lindeas.com/lindeas/jilo/compare/v0.1...v0.1.1
- codeberg: https://codeberg.org/lindeas/jilo/compare/v0.1...v0.1.1
- github: https://github.com/lindeas/jilo/compare/v0.1...v0.1.1
- gitlab: https://gitlab.com/lindeas/jilo/-/compare/v0.1...v0.1.1

### Added
- Initial changelog following the keepachangelog.com format
- Added "silent" option to jilo-cli, suitable for scripting
- Added time duration and number of participants in conferences listings
- Added man page
- Added build resources and scripts for DEB and RPM packages
- Initial build of the DEB and RPM packages
- Added DEB repository

### Changed
- Updated the way jilo-cli handles multiple options, added filtering conferences by time period

### Fixed
- Fixed an error in double counting of conferences in jilo-cli


## 0.1 - 2024-06-12

#### Links
- upstream: https://code.lindeas.com/lindeas/jilo/releases/tag/v0.1
- codeberg: https://codeberg.org/lindeas/jilo/releases/tag/v0.1
- github: https://github.com/lindeas/jilo/releases/tag/v0.1
- gitlab: https://gitlab.com/lindeas/jilo/-/releases/v0.1

### Added
- Initial version of jilo and jilo-cli
- Basic functionality for JVB and Jicofo logs scanning
- Searching through conferences, participants, events and in time periods
- Detecting logs rotation and saving last parsed line
- Support for both SQLite3 and MySQL/MariaDB
- Minimal external dependencies, using Bash built-in commands as much as possible
