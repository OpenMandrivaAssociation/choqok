Name:    choqok
Version: 0.9.4
Release: %mkrel 2
Summary: KDE Micro-Blogging Client
Source0: http://d10xg45o6p6dbl.cloudfront.net/projects/c/choqok/%name-%version.tar.bz2
License: GPLv2+
Group: Office
Url:          http://choqok.gnufolks.org/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: kdelibs4-devel

%description
Choqok is a Free/Open Source micro-blogging client for K Desktop 

%files -f %name.lang
%defattr(-,root,root)
%_kde_bindir/choqok                           
%_kde_libdir/kde4/choqok_*.so              
%_kde_libdir/kde4/kcm_choqok_*.so
%_kde_datadir/applications/kde4/choqok.desktop
%_kde_appsdir/choqok
%_kde_appsdir/choqok_nowlistening/nowlisteningui.rc
%_kde_datadir/config.kcfg/choqokappearancesettings.kcfg
%_kde_datadir/config.kcfg/choqokbehaviorsettings.kcfg
%_kde_datadir/config.kcfg/nowlisteningsettings.kcfg
%_kde_iconsdir/*/*/*/*
%_kde_datadir/kde4/services/choqok_*.desktop
%_kde_datadir/kde4/servicetypes/choqok*.desktop

#-------------------------------------------------------------------

%define choqok_major 0
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

%define twitterapihelper_major 0
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

#--------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
rm -rf %{buildroot}
%{makeinstall_std} -C build


%find_lang %name --with-html

%clean
rm -rf %{buildroot}
