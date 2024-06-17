Name: jilo
Version: 0.1.1
Release: 1%{?dist}
Summary: Jitsi logs observer
License: GPLv2
URL: https://lindeas.com/jilo
Source0: %{name}-%{version}.tar.gz
BuildArch: noarch
BuildRequires: bash
Requires: bash
Requires: (sqlite or mysql or mariadb)
Requires: coreutils
Requires: util-linux

%description
Bash scripts for collecting and displaying information about conference events from Jitsi Meet logs.
This package contains the 'jilo' logs collecting tool and 'jilo-cli' command line events searching tool.

%prep
%setup -q

%install
# directories
mkdir -p %{buildroot}/etc
mkdir -p %{buildroot}/usr/bin
mkdir -p %{buildroot}/usr/share/doc/%{name}
mkdir -p %{buildroot}/usr/share/man/man8

# then copy the files
cp %{sourcedir}/jilo.conf %{buildroot}/etc/jilo.conf
cp %{sourcedir}/jilo %{buildroot}/usr/bin/
cp %{sourcedir}/jilo-cli %{buildroot}/usr/bin/
cp %{sourcedir}/CHANGELOG.md %{buildroot}/usr/share/doc/%{name}/
cp %{sourcedir}/LICENSE %{buildroot}/usr/share/doc/%{name}/
cp %{sourcedir}/README.md %{buildroot}/usr/share/doc/%{name}/
cp %{sourcedir}/TODO.md %{buildroot}/usr/share/doc/%{name}/
cp %{sourcedir}/log-regexps.md %{buildroot}/usr/share/doc/%{name}/
cp %{sourcedir}/man-jilo.8 %{buildroot}/usr/share/man/man8/jilo.8

%files
/etc/jilo.conf
/usr/bin/jilo
/usr/bin/jilo-cli
/usr/share/doc/%{name}/CHANGELOG.md
/usr/share/doc/%{name}/LICENSE
/usr/share/doc/%{name}/README.md
/usr/share/doc/%{name}/TODO.md
/usr/share/doc/%{name}/log-regexps.md
/usr/share/man/man8/jilo.8

%changelog
* Wed Jun 12 2024  Yasen Pramatarov <yasen@lindeas.com> 0.1.1
- Initial build
