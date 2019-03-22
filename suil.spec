%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

Name:           suil
Version:        0.10.2
Release:        1
Summary:        Lightweight C library for loading and wrapping LV2 plugin UIs

%define lib_major       0
%define lib_name        %mklibname %{name} %{lib_major}
%define lib_name_devel  %mklibname %{name} -d

Source0:        http://download.drobilla.net/%{name}-%{version}.tar.bz2
Patch0:         suil-0.10.0-linking.patch
URL:            http://drobilla.net/software/%{name}/
License:        MIT-like
Group:          System/Libraries

BuildRequires:	doxygen
BuildRequires:	graphviz
BuildRequires:	waf
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(serd-0)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  qt5-devel
BuildRequires:  pkgconfig(lv2)
BuildRequires:  pkgconfig(sratom-0)
BuildRequires:  python2-devel

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
%{_libdir}/lib%{name}-%{lib_major}.so
%dir %{_includedir}/%{name}-%{lib_major}/%{name}
%{_includedir}/%{name}-%{lib_major}/%{name}/*.h
%{_libdir}/pkgconfig/%{name}-%{lib_major}.pc

#-----------------------------------
%package -n %{_lib}%{name}-x11-in-gtk2
Summary:        Shared object for GTK2 hosts displaying X11 LV2 GUIs
Group:          System/Libraries
Requires:       %{lib_name} = %{version}-%{release}
Provides:       %{name}-x11-in-gtk2 = %{version}-%{release}

%description -n %{_lib}%{name}-x11-in-gtk2
Shared object for GTK2 hosts displaying X11 LV2 GUIs

%files -n %{_lib}%{name}-x11-in-gtk2
%{_libdir}/%{name}-0/libsuil_x11_in_gtk2.so

#-----------------------------------
%package -n %{_lib}%{name}-x11-in-qt5
Summary:	Shared object for Qt5 hosts displaying X11 LV2 GUIs
Group:		System/Libraries
Requires:	%{lib_name} = %{version}-%{release}
Provides:	%{name}-x11-in-qt5 = %{version}-%{release}

%description -n %{_lib}%{name}-x11-in-qt5
Shared object for Qt5 hosts displaying X11 LV2 GUIs

%files -n %{_lib}%{name}-x11-in-qt5
%{_libdir}/%{name}-0/libsuil_x11_in_qt5.so
#-----------------------------------
%package -n %{_lib}%{name}-qt5-in-gtk2
Summary:	Shared object for GTK2 hosts displaying Qt5 LV2 GUIs
Group:		System/Libraries
Requires:	%{lib_name} = %{version}-%{release}
Provides:	%{name}-qt5-in-gtk2 = %{version}-%{release}

%description -n %{_lib}%{name}-qt5-in-gtk2
Shared object for GTK2 hosts displaying Qt5 LV2 GUIs

%files -n %{_lib}%{name}-qt5-in-gtk2
%{_libdir}/%{name}-%{lib_major}/lib%{name}_qt5_in_gtk2.so

#-----------------------------------
%package -n %{_lib}%{name}-gtk2-in-qt5
Summary:	Shared object for Qt5 hosts displaying GTK2 LV2 GUIs
Group:		System/Libraries
Requires:	gtk2
Requires:	%{lib_name} = %{version}-%{release}
Provides:	%{name}-gtk2-in-qt5 = %{version}-%{release}

%description -n %{_lib}%{name}-gtk2-in-qt5
Shared object for Qt5 hosts displaying GTK2 LV2 GUIs

%files -n %{_lib}%{name}-gtk2-in-qt5
%{_libdir}/%{name}-%{lib_major}/lib%{name}_gtk2_in_qt5.so

#-----------------------------------

%prep
%setup -q
%autopatch -p1

%build
export CXXFLAGS="%{optflags}"
export LINKFLAGS="%{ldflags}"
%{__python2} waf configure \
    --prefix=%{_prefix} \
    --libdir=%{_libdir} \
    --mandir=%{_mandir} \
    --docdir=%{_docdir}/%{name} \
    --docs
%{__python2} waf build -v %{?_smp_mflags}

%install
%{__python2} waf install --destdir=%{buildroot}
