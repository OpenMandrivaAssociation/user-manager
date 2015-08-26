%define plasmaver %(echo %{version} |cut -d. -f1-3)
%define stable %([ "`echo %{plasmaver} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary: 	Plasma user manager
Name: 		user-manager
Version: 	5.4.0
Release: 	1
Source0: 	http://download.kde.org/%{stable}/plasma/%{plasmaver}/%{name}-%{version}.tar.xz
Url: 		http://kde.org/
License: 	GPL
Group: 		System/Libraries
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5KDELibs4Support)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Widgets)

%description
Plasma user manager.

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%files
