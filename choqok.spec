Name:		choqok
Version:	1.3
Release:	1
Summary:	KDE Micro-Blogging Client
License:	GPLv3
Group:		Graphical desktop/KDE
URL:		http://choqok.gnufolks.org/
Source0:	http://downloads.sourceforge.net/choqok/%{name}-%{version}.tar.bz2
Patch0:		choqok-0.9.85-dbus-service-dir.patch
Patch1:		choqok-1.2-l10n-ru.patch
BuildRequires:	kdelibs4-devel
BuildRequires:	qjson-devel
BuildRequires:	qoauth-devel
BuildRequires:	attica-devel
BuildRequires:	libindicate-qt-devel
Requires:	kdebase4-runtime

%description
Choqok is a Free/Open Source micro-blogging client for K Desktop 

%files -f %name.lang
%{_datadir}/dbus-1/services/org.kde.choqok.service
%{_kde_bindir}/choqok
%{_kde_libdir}/kde4/*.so
%{_kde_applicationsdir}/choqok.desktop
%{_kde_appsdir}/choqok*
%{_kde_appsdir}/khtml/kpartplugins/*
%{_kde_datadir}/config.kcfg/*.kcfg
%{_kde_iconsdir}/*/*/*/*
%{_kde_services}/choqok_*.desktop
%{_kde_services}/ServiceMenus/*.desktop
%{_kde_servicetypes}/choqok*.desktop

#-------------------------------------------------------------------

%define choqok_major 1
%define libchoqok %mklibname choqok %{choqok_major}

%package -n %{libchoqok}
Summary: %name library
Group: System/Libraries

%description -n %{libchoqok}
%name library.

%files -n %{libchoqok}
%{_kde_libdir}/libchoqok.so.%{choqok_major}*

#-------------------------------------------------------------------

%define twitterapihelper_major 1
%define libtwitterapihelper %mklibname twitterapihelper %twitterapihelper_major

%package -n %{libtwitterapihelper}
Summary: %{name} library
Group: System/Libraries

%description -n %{libtwitterapihelper}
%name library.

%files -n %{libtwitterapihelper}
%{_kde_libdir}/libtwitterapihelper.so.%{twitterapihelper_major}*

#-------------------------------------------------------------------

%package devel
Summary: %{name} development files
Group: Development/KDE and Qt
Requires: %{libchoqok} = %{version}-%{release}
Conflicts: %{name} < 0.2.3

%description devel
This package contains header files needed if you wish to build applications
based on %{name}.

%files devel
%{_kde_libdir}/libchoqok.so
%{_kde_libdir}/libtwitterapihelper.so
%{_kde_includedir}/choqok
%{_kde_appsdir}/cmake/modules/*.cmake

#--------------------------------------------------------------------
%prep
%setup -q
%patch0 -p0
#%patch1 -p1

%build
%cmake_kde4
%make

%install
%{makeinstall_std} -C build

%find_lang %name --with-html
