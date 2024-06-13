# Changelog

All notable changes to this project will be documented in this file.

---

## Unreleased

#### Links
- upstream: https://code.lindeas.com/lindeas/jilo/compare/v0.1...HEAD
- codeberg: https://codeberg.org/lindeas/jilo/compare/v0.1...HEAD
- github: https://github.com/lindeas/jilo/compare/v0.1...HEAD
- gitlab: https://gitlab.com/lindeas/jilo/-/compare/v0.1...HEAD

### Added
- Initial changelog following the keepachangelog.com format

### Changed
- Updated the way jilo-cli handles multiple options, added filtering conferences by time period

---

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