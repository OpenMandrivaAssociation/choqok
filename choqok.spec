Name:		choqok
Version:	1.6.0
Release:	3
Summary:	KDE Micro-Blogging Client
License:	GPLv3
Group:		Graphical desktop/KDE
URL:		http://choqok.gnufolks.org/
Source0:	http://download.kde.org/stable/choqok/1.6/src/%{name}-%{version}.tar.xz
Patch0:		choqok-0.9.85-dbus-service-dir.patch
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5Archive)
BuildRequires:	cmake(KF5Attica)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5ConfigWidgets)
BuildRequires:	cmake(KF5CoreAddons) 
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5Emoticons)
BuildRequires:	cmake(KF5GlobalAccel)
BuildRequires:	cmake(KF5GuiAddons)
BuildRequires:	cmake(KF5KCMUtils)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	cmake(KF5NotifyConfig)
BuildRequires:	cmake(KF5Parts)
BuildRequires:	cmake(KF5Service)
BuildRequires:	cmake(KF5Sonnet)
BuildRequires:	cmake(KF5TextWidgets)
BuildRequires:	cmake(KF5Wallet)
BuildRequires:	cmake(KF5WebKit)
BuildRequires:	cmake(KF5WidgetsAddons)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	qt5-qttools
BuildRequires:	pkgconfig(Qt5Concurrent)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5DBus)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Network)
BuildRequires:	pkgconfig(Qt5Widgets)

BuildRequires:	pkgconfig(qca2-qt5)
BuildRequires:	pkgconfig(qoauth-qt5)

%description
Choqok is a Free/Open Source micro-blogging client for K Desktop 

%files -f %{name}.lang
%{_datadir}/dbus-1/services/org.kde.choqok.service
%{_bindir}/choqok
%{_qt5_plugindir}/*.so
%{_kde5_applicationsdir}/org.kde.choqok.desktop
%{_datadir}/choqok
%{_datadir}/config.kcfg/*.kcfg
%{_iconsdir}/*/*/*/*
%{_kde5_services}/choqok_*.desktop
%{_kde5_servicetypes}/choqok*.desktop
%{_datadir}/kxmlgui5/*
%{_datadir}/knotifications5/choqok
%{_datadir}/metainfo/org.kde.choqok.appdata.xml
%{_libdir}/qt5/plugins/kf5/parts/konqchoqokplugin.so
%{_datadir}/kservices5/ServiceMenus/choqok*.desktop
%{_datadir}/kservices5/konqchoqok.desktop

#-------------------------------------------------------------------

%define choqok_major 1
%define libchoqok %mklibname choqok %{choqok_major}

%package -n %{libchoqok}
Summary:	%{name} library
Group:		System/Libraries

%description -n %{libchoqok}
%{name} library.

%files -n %{libchoqok}
%{_libdir}/libchoqok.so.%{choqok_major}*

#-------------------------------------------------------------------

%define twitterapihelper_major 1
%define libtwitterapihelper %mklibname twitterapihelper %{twitterapihelper_major}

%package -n %{libtwitterapihelper}
Summary:	%{name} library
Group:		System/Libraries

%description -n %{libtwitterapihelper}
%{name} library.

%files -n %{libtwitterapihelper}
%{_libdir}/libtwitterapihelper.so.%{twitterapihelper_major}*

#-------------------------------------------------------------------

%define gnusocialapihelper_major 1
%define libgnusocialapihelper %mklibname gnusocialapihelper %{gnusocialapihelper_major}

%package -n %{libgnusocialapihelper}
Summary:        %{name} library
Group:          System/Libraries

%description -n %{libgnusocialapihelper}
%{name} library.

%files -n %{libgnusocialapihelper}
%{_libdir}/libgnusocialapihelper.so.%{gnusocialapihelper_major}*


#-------------------------------------------------------------------

%package devel
Summary:	%{name} development files
Group:		Development/KDE and Qt
Requires:	%{libchoqok} = %{version}-%{release}
Conflicts:	%{name} < 0.2.3

%description devel
This package contains header files needed if you wish to build applications
based on %{name}.

%files devel
%{_libdir}/libchoqok.so
%{_libdir}/libgnusocialapihelper.so
%{_libdir}/libtwitterapihelper.so
%{_includedir}/choqok
%{_datadir}/cmake/modules/*.cmake

#--------------------------------------------------------------------
%prep
%setup -q
%patch0 -p0

# Find QtOauth-qt5
sed -i -e 's|NAMES qoauth|NAMES qoauth5|' cmake/modules/FindQtOAuth.cmake
sed -i -e 's|QUIET qoauth|QUIET qoauth-qt5|' cmake/modules/FindQtOAuth.cmake
#sed -i -e 's|QtOAuth/interface.h|interface.h|' cmake/modules/FindQtOAuth.cmake
%build
%cmake_kde5
%ninja

%install
%ninja_install -C build

# Remove it to avoid file conflicts with kdepimlibs4-devel 4.10
rm -f %{buildroot}%{_kde_appsdir}/cmake/modules/FindQtOAuth.cmake

%find_lang %{name} --with-html
