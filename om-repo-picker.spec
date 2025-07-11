Name:		om-repo-picker
Version:	1.3.7
Release:	1
Summary:	OpenMandriva Lx package repository selector
License:	GPLv2
Group:		System/Configuration/Other
URL:		https://github.com/OpenMandrivaSoftware/om-repo-picker
Source0:	https://github.com/OpenMandrivaSoftware/om-repo-picker/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Requires:	openmandriva-repos >= 4.0-1
Requires:	dnf
Requires:	dnf-command(config-manager)
# More precisely: pkexec
Requires:	polkit
BuildRequires:	cmake cmake(ECM) ninja cmake(Qt6Core) cmake(Qt6Gui) cmake(Qt6Widgets) cmake(Qt6LinguistTools)

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
