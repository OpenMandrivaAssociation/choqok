Name:		choqok
Version:	1.3
Release:	2
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
Requires:	kdebase4-runtime

%description
Choqok is a Free/Open Source micro-blogging client for K Desktop 

%files -f %{name}.lang
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
Summary:	%{name} library
Group:		System/Libraries

%description -n %{libchoqok}
%{name} library.

%files -n %{libchoqok}
%{_kde_libdir}/libchoqok.so.%{choqok_major}*

#-------------------------------------------------------------------

%define twitterapihelper_major 1
%define libtwitterapihelper %mklibname twitterapihelper %{twitterapihelper_major}

%package -n %{libtwitterapihelper}
Summary:	%{name} library
Group:		System/Libraries

%description -n %{libtwitterapihelper}
%{name} library.

%files -n %{libtwitterapihelper}
%{_kde_libdir}/libtwitterapihelper.so.%{twitterapihelper_major}*

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
%makeinstall_std -C build

%find_lang %{name} --with-html


%changelog
* Thu Apr 26 2012 Crispin Boylan <crisb@mandriva.org> 1.3-1
+ Revision: 793513
- New release

* Wed Jan 18 2012 Andrey Smirnov <asmirnov@mandriva.org> 1.2-5
+ Revision: 762145
- Updated Russian translation

  + Zé <ze@mandriva.org>
    - is build against kdelibs and i missed that part, add back kde macros

* Thu Dec 29 2011 Zé <ze@mandriva.org> 1.2-4
+ Revision: 748207
- clean defattr and BR
- clean duplicated files (doc files are listed using find_lang macro)
- another case where prefix should not be used
- bump release to build against new attica

* Sat Nov 26 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.2-3
+ Revision: 733502
- rebuild against new kde

* Thu Nov 17 2011 Sergio Rafael Lemke <sergio@mandriva.com> 1.2-2
+ Revision: 731440
- Update from version 1.1 to 1.2

* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 1.1-2
+ Revision: 663373
- mass rebuild

* Sat Apr 02 2011 Funda Wang <fwang@mandriva.org> 1.1-1
+ Revision: 649921
- new version 1.1

* Sun Feb 27 2011 Funda Wang <fwang@mandriva.org> 1.0-3
+ Revision: 640281
- rebuild to obsolete old packages

* Sun Feb 20 2011 Sergio Rafael Lemke <sergio@mandriva.com> 1.0-2
+ Revision: 638913
- Disabled video thumbnailer plugin as default, it's causing random crashes

* Sat Jan 29 2011 Sergio Rafael Lemke <sergio@mandriva.com> 1.0-1
+ Revision: 633764
- Updated License and Group

  + Funda Wang <fwang@mandriva.org>
    - 1.0

* Tue Dec 07 2010 Funda Wang <fwang@mandriva.org> 0.9.98-1mdv2011.0
+ Revision: 613613
- new version 0.9.98

* Fri Oct 15 2010 Funda Wang <fwang@mandriva.org> 0.9.92-1mdv2011.0
+ Revision: 585806
- new version 0.9.92

  + John Balcaen <mikala@mandriva.org>
    - Use qjson-devel instead of libqjson-devel as BR

* Wed Sep 01 2010 Funda Wang <fwang@mandriva.org> 0.9.90-1mdv2011.0
+ Revision: 575098
- new version 0.9.90

* Fri Aug 20 2010 Funda Wang <fwang@mandriva.org> 0.9.85-1mdv2011.0
+ Revision: 571486
- new version 0.9.85

* Tue Mar 09 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.9.55-1mdv2010.1
+ Revision: 517206
- New version 0.9.55
  Add kdebase4-runtime as Requires
  Fix file list

* Fri Nov 20 2009 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.9.4-2mdv2010.1
+ Revision: 467583
- rebuild due to ABI breakage...

* Sat Nov 07 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.9.4-1mdv2010.1
+ Revision: 462445
- Add description
- import choqok

