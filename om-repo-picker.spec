Name:		om-repo-picker
Version:	1.2.4
Release:	1
Summary:	OpenMandriva Lx package repository selector
License:	GPLv2
Group:		System/Configuration/Other
URL:		https://github.com/OpenMandrivaSoftware/om-repo-picker
Source0:	https://github.com/OpenMandrivaSoftware/om-repo-picker/archive/%{version}/%{name}-%{version}.tar.gz
Requires:	openmandriva-repos >= 4.0-1
Requires:	dnf
Requires:	dnf-command(config-manager)
BuildRequires:	cmake cmake(ECM) ninja cmake(Qt5Core) cmake(Qt5Gui) cmake(Qt5Widgets)

%description
OpenMandriva Lx package repository selector.

%prep
%autosetup -p1
%cmake -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
%{_bindir}/om-repo-picker
%{_datadir}/icons/hicolor/scalable/apps/om-repopicker.svg
%{_datadir}/applications/*.desktop
