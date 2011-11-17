Name:		choqok
Version:	1.2
Release:	%mkrel 1
Summary:	KDE Micro-Blogging Client
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
Patch0:		choqok-0.9.85-dbus-service-dir.patch
License:	GPLv3
Group:		Graphical desktop/KDE
Url:		http://choqok.gnufolks.org/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	kdelibs4-devel
BuildRequires:	qjson-devel
BuildRequires:	qoauth-devel
BuildRequires:	attica-devel
BuildRequires:	libindicate-qt-devel
Requires:	kdebase4-runtime

%description
Choqok is a Free/Open Source micro-blogging client for K Desktop 

%files -f %name.lang
%defattr(-,root,root)
%_kde_bindir/choqok
%_kde_libdir/kde4/*.so
%_kde_datadir/applications/kde4/choqok.desktop
%_kde_appsdir/choqok*
%_kde_appsdir/khtml/kpartplugins/*
%_kde_datadir/config.kcfg/*.kcfg
%_kde_iconsdir/*/*/*/*
%_kde_services/choqok_*.desktop
%_kde_servicetypes/choqok*.desktop
%_kde_services/ServiceMenus/*.desktop
%_datadir/dbus-1/services/org.kde.choqok.service

#-------------------------------------------------------------------

%define choqok_major 1
%define libchoqok %mklibname choqok %{choqok_major}

%package -n %libchoqok
Summary: %name library
Group: System/Libraries

%description -n %libchoqok
%name library.

%files -n %libchoqok
%defattr(-,root,root)
%_kde_libdir/libchoqok.so.%{choqok_major}*

#-------------------------------------------------------------------

%define twitterapihelper_major 1
%define libtwitterapihelper %mklibname twitterapihelper %twitterapihelper_major

%package -n %libtwitterapihelper
Summary: %name library
Group: System/Libraries

%description -n %libtwitterapihelper
%name library.

%files -n %libtwitterapihelper
%defattr(-,root,root)
%_kde_libdir/libtwitterapihelper.so.%{twitterapihelper_major}*

#-------------------------------------------------------------------

%package devel
Summary: %name development files
Group: Development/KDE and Qt
Requires: %{libchoqok} = %{version}-%{release}
Conflicts: %{name} < 0.2.3

%description devel
This package contains header files needed if you wish to build applications
based on %name.

%files devel
%defattr(-,root,root)
%_kde_libdir/libchoqok.so
%_kde_libdir/libtwitterapihelper.so
%_kde_includedir/choqok
%_kde_appsdir/cmake/modules/*

#--------------------------------------------------------------------

%prep
%setup -q
%patch0 -p0

%build
%cmake_kde4
%make

%install
rm -rf %{buildroot}
%{makeinstall_std} -C build

%find_lang %name --with-html

%clean
rm -rf %{buildroot}
