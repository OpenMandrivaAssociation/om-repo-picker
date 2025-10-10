Name:		om-repo-picker
Version:	1.3.8
Release:	2
Summary:	OpenMandriva Lx package repository selector
License:	GPLv2
Group:		System/Configuration/Other
URL:		https://github.com/OpenMandrivaSoftware/om-repo-picker
Source0:	https://github.com/OpenMandrivaSoftware/om-repo-picker/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Requires:	openmandriva-repos >= 4.0-1
Requires:	dnf
Requires:	dnf5-command(config-manager)
# More precisely: pkexec
Requires:	polkit
Requires:	%{name}-cli = %{EVRD}
BuildRequires:	cmake(ECM) cmake(Qt6Core) cmake(Qt6Gui) cmake(Qt6Widgets) cmake(Qt6LinguistTools)
BuildSystem:	cmake

%description
OpenMandriva Lx package repository selector.

%package cli
Summary:	Command line tools to work with OpenMandriva repositories
Group:		System/Configuration/Other
Requires:	dnf >= 5.0

%description cli
Command line tools to work with OpenMandriva repositories

%files
%{_bindir}/om-repo-picker
%{_datadir}/icons/hicolor/scalable/apps/om-repopicker.svg
%{_datadir}/applications/*.desktop

%files cli
%{_bindir}/enable-repo
%{_bindir}/disable-repo
