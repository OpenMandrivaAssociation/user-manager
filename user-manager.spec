%define plasmaver %(echo %{version} |cut -d. -f1-3)
%define stable %([ "`echo %{plasmaver} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary: 	Plasma user manager
Name: 		user-manager
Version:	5.19.5
Release:	5
Source0: 	http://download.kde.org/%{stable}/plasma/%{plasmaver}/%{name}-%{version}.tar.xz
# https://phabricator.kde.org/D27514
Patch0:		https://phabricator.kde.org/file/data/day64xchqj7rmddc4b67/PHID-FILE-yopf3tvm56hlmgzlysmx/D27514.diff
Url: 		https://kde.org/
License: 	GPL
Group: 		System/Libraries
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5KCMUtils)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5IconThemes)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5DBus)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(pwquality)
BuildRequires:	pkgconfig(libxcrypt)
Requires:	accountsservice
Requires:	pam_pwquality
Requires:	desktop-common-data

%description
Plasma user manager.

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

# (tpg) use our own faces, and put them on top of the list, so this explain afaces name :)
ln -sf /usr/share/mdk/faces %{buildroot}%{_datadir}/user-manager/avatars/afaces

%find_lang user_manager || touch user_manager.lang

%files -f user_manager.lang
%{_datadir}/qlogging-categories5/user-manager.categories
%{_libdir}/qt5/plugins/user_manager.so
%{_datadir}/kservices5/user_manager.desktop
%{_datadir}/user-manager
