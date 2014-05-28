# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.22
# 
# >> macros
# << macros

Name:       phonon-qt5
Summary:    Multimedia framework api
Version:    4.7.99
Release:    1
Group:      System/Base
License:    GPLv2+
URL:        http://www.kde.org
Source0:    %{name}-%{version}.tar.xz
Source100:  phonon-qt5.yaml
Source101:  phonon-qt5-rpmlintrc
Requires:   kf5-filesystem
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libpulse-mainloop-glib) > 0.9.15
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  cmake
BuildRequires:  kf5-rpm-macros
BuildRequires:  qt5-tools


%description
Multimedia framework api



%package devel
Summary:    Development files for %{name}
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains the files necessary to develop applications
that use %{name}.



%prep
%setup -q -n %{name}-%{version}/upstream

# >> setup
# << setup

%build
# >> build pre
mkdir -p %{_target_platform}-Qt5
pushd %{_target_platform}-Qt5
%{cmake} \
-DPHONON_BUILD_PHONON4QT5:BOOL=ON \
-DPHONON_INSTALL_QT_EXTENSIONS_INTO_SYSTEM_QT:BOOL=ON \
# from kf5 macros...
-DBUILD_SHARED_LIBS:BOOL=ON \
-DBUILD_TESTING:BOOL=FALSE \
-DCMAKE_BUILD_TYPE=%{_kf5_buildtype} \
-DCMAKE_INSTALL_PREFIX:PATH=%{_kf5_prefix} \
-DCMAKE_VERBOSE_MAKEFILE:BOOL=ON \
-DBIN_INSTALL_DIR:PATH=%{_kf5_bindir} \
-DINCLUDE_INSTALL_DIR:PATH=%{_includedir} \
-DLIB_INSTALL_DIR:PATH=%{_lib} \
%if "%{?_lib}" == "lib64"
%{?_cmake_lib_suffix64} \
%endif
-DKCFG_INSTALL_DIR:PATH=%{_datadir}/config.kcfg \
-DPLUGIN_INSTALL_DIR:PATH=%{_kf5_plugindir} \
-DQT_PLUGIN_INSTALL_DIR:PATH=%{_qt5_plugindir} \
-DQML_INSTALL_DIR:PATH=%{_kf5_qmldir} \
-DIMPORTS_INSTALL_DIR:PATH=%{_qt5_importdir} \
-DECM_MKSPECS_INSTALL_DIR:PATH=%{_kf5_datadir}/qt5/mkspecs/modules \
-DSYSCONF_INSTALL_DIR:PATH=%{_kf5_sysconfdir} \
-DLIBEXEC_INSTALL_DIR:PATH=%{_libexecdir} \
-DKF5_LIBEXEC_INSTALL_DIR=%{_kf5_libexecdir} \
-DKF5_INCLUDE_INSTALL_DIR=%{_kf5_includedir}
..
popd

make %{?_smp_mflags} -C %{_target_platform}-Qt5
# << build pre



# >> build post
# << build post
%install
rm -rf %{buildroot}
# >> install pre
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}-Qt5
mkdir -p %{buildroot}%{_qt5_plugindir}/phonon4qt5_backend
# << install pre

# >> install post
# << install post









%files
%defattr(-,root,root,-)
%doc COPYING.LIB
%dir %{_datadir}/phonon4qt5
%{_kf5_libdir}/libphonon4qt5.so.4*
%{_kf5_libdir}/libphonon4qt5experimental.so.4*
%dir %{_qt5_plugindir}/phonon4qt5_backend/
%{_datadir}/dbus-1/interfaces/org.kde.Phonon4Qt5.AudioOutput.xml
# >> files
# << files


%files devel
%defattr(-,root,root,-)
%{_datadir}/phonon4qt5/buildsystem/
%dir %{_kf5_libdir}/cmake/
%{_kf5_libdir}/cmake/phonon4qt5/
%{_includedir}/phonon4qt5/
%{_kf5_libdir}/libphonon4qt5.so
%{_kf5_libdir}/libphonon4qt5experimental.so
%{_kf5_libdir}/pkgconfig/phonon4qt5.pc
%{_datadir}/qt5/mkspecs/modules/qt_phonon4qt5.pri
# >> files devel
# << files devel

