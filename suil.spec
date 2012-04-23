%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

Name:           suil
Version:        0.6.0
Release:        1
Summary:        Lightweight C library for loading and wrapping LV2 plugin UIs

%define lib_major       0
%define lib_name        %mklibname %{name} %{lib_major}
%define lib_name_devel  %mklibname %{name} -d

Source0:         http://download.drobilla.net/%{name}-%{version}.tar.bz2
URL:            http://drobilla.net/software/%{name}/
License:        MIT-like
Group:          System/Libraries

BuildRequires:  waf, pkgconfig
BuildRequires:  serd-devel
BuildRequires:  lv2core-devel >= 0.4
BuildRequires:  lv2-ui-devel
BuildRequires:  gtk2-devel
BuildRequires:  qt4-devel

%description
Suil is a lightweight C library for loading and wrapping LV2 plugin UIs.

Suil makes it possible to load a UI of any toolkit in a host using any
other toolkit (assuming the toolkits are both supported by Suil).
Hosts do not need to build against or link to foreign toolkit libraries
to use UIs written with that toolkit (Suil performs its magic at
runtime using dynamically loaded modules). The API is designed such that
hosts do not need to explicitly support particular toolkits whatsoever.
If Suil supports a particular toolkit, then all hosts that use Suil will
support that toolkit.

#-----------------------------------
%package -n %{lib_name}

Summary:        Lightweight RDF syntax library
Group:          System/Libraries

%description -n %{lib_name}
Suil is a lightweight C library for loading and wrapping LV2 plugin UIs.

Suil makes it possible to load a UI of any toolkit in a host using any
other toolkit (assuming the toolkits are both supported by Suil).
Hosts do not need to build against or link to foreign toolkit libraries
to use UIs written with that toolkit (Suil performs its magic at
runtime using dynamically loaded modules). The API is designed such that
hosts do not need to explicitly support particular toolkits whatsoever.
If Suil supports a particular toolkit, then all hosts that use Suil will
support that toolkit.

%files -n %{lib_name}
%doc COPYING README
%defattr(-,root,root,-)
%{_libdir}/lib%{name}-%{lib_major}.so.*

#-----------------------------------
%package -n %{lib_name_devel}
Summary:        Headers for the sord RDF storage library
Group:          System/Libraries
Requires:       %{lib_name} = %{version}-%{release}
Requires:       pkgconfig
Provides:       %{name}-devel = %{version}-%{release}

%description -n %{lib_name_devel}
Development files needed to build applications against suil.

%files -n %{lib_name_devel}
%defattr(-,root,root,-)
%{_libdir}/lib%{name}-%{lib_major}.so
%dir %{_includedir}/%{name}-%{lib_major}/%{name}
%{_includedir}/%{name}-%{lib_major}/%{name}/*.h
%{_libdir}/pkgconfig/%{name}-%{lib_major}.pc

#-----------------------------------
%package -n %{_lib}%{name}-qt4-in-gtk2
Summary:        Shared object for GTK2 hosts displaying Qt4 LV2 GUIs
Group:          System/Libraries
Requires:       qtgui
Requires:       %{lib_name} = %{version}-%{release}
Provides:       %{name}-qt4-in-gtk2 = %{version}-%{release}

%description -n %{_lib}%{name}-qt4-in-gtk2
Shared object for GTK2 hosts displaying Qt4 LV2 GUIs

%files -n %{_lib}%{name}-qt4-in-gtk2
%defattr(-,root,root,-)
%{_libdir}/%{name}-%{lib_major}/lib%{name}_qt4_in_gtk2.so

#-----------------------------------
%package -n %{_lib}%{name}-gtk2-in-qt4
Summary:        Shared object for Qt4 hosts displaying GTK2 LV2 GUIs
Group:          System/Libraries
Requires:       gtk2
Requires:       %{lib_name} = %{version}-%{release}
Provides:       %{name}-gtk2-in-qt4 = %{version}-%{release}

%description -n %{_lib}%{name}-gtk2-in-qt4
Shared object for Qt4 hosts displaying GTK2 LV2 GUIs

%files -n %{_lib}%{name}-gtk2-in-qt4
%defattr(-,root,root,-)
%{_libdir}/%{name}-%{lib_major}/lib%{name}_gtk2_in_qt4.so

#-----------------------------------

%prep
%setup -q

%build
./waf configure --prefix=%{_prefix} --libdir=%{_libdir} \
--lv2dir=%{_libdir}/lv2
./waf

%install
rm -rf %{buildroot}

./waf install --destdir=%{buildroot}

%clean
rm -rf %{buildroot}

