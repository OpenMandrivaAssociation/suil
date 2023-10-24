%global build_ldflags %{build_ldflags} -Wl,--undefined-version

Name:           suil
Version:        0.10.20
Release:        1
Summary:        Lightweight C library for loading and wrapping LV2 plugin UIs

%define lib_major       0
%define lib_name        %mklibname %{name} %{lib_major}
%define lib_name_devel  %mklibname %{name} -d

Source0:        https://download.drobilla.net/%{name}-%{version}.tar.xz
#Patch0:         suil-0.10.0-linking.patch
URL:            https://drobilla.net/software/suil/
License:        MIT-like
Group:          System/Libraries

BuildRequires:	doxygen
BuildRequires:	graphviz
BuildRequires:	meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(serd-0)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  qt5-devel
BuildRequires:  pkgconfig(lv2)
BuildRequires:  pkgconfig(sratom-0)
BuildRequires:  python3-devel
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(x11)
BuildRequires:	qt5-qtbase-devel
BuildRequires:  python3dist(sphinx)

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
%doc COPYING
%{_libdir}/lib%{name}-%{lib_major}.so.*
%{_libdir}/suil-0/libsuil_x11.so

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
%package -n %{_lib}%{name}-x11-in-gtk3
Summary:	Shared object for GTK3 hosts displaying X11 LV2 GUIs
Group:		System/Libraries
Requires:	%{lib_name} = %{version}-%{release}
Provides:	%{name}-x11-in-gtk3 = %{version}-%{release}

%description -n %{_lib}%{name}-x11-in-gtk3
Shared object for gtk3 hosts displaying X11 LV2 GUIs

%files -n %{_lib}%{name}-x11-in-gtk3
%{_libdir}/%{name}-0/libsuil_x11_in_gtk3.so
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
%package -n %{_lib}%{name}-qt5-in-gtk3
Summary:	Shared object for GTK3 hosts displaying Qt5 LV2 GUIs
Group:		System/Libraries
Requires:	%{lib_name} = %{version}-%{release}
Provides:	%{name}-qt5-in-gtk3 = %{version}-%{release}

%description -n %{_lib}%{name}-qt5-in-gtk3
Shared object for GTK3 hosts displaying Qt5 LV2 GUIs

%files -n %{_lib}%{name}-qt5-in-gtk3
%{_libdir}/%{name}-%{lib_major}/lib%{name}_qt5_in_gtk3.so

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
export LDFLAGS="%{optflags} -lX11"
%meson  \
        -Dgtk2=enabled \
        -Dgtk3=enabled \
        -Dqt5=enabled \
        -Dx11=enabled \
        -Ddocs=disabled \
        -Dsinglehtml=disabled \
        -Dhtml=disabled
%meson_build

%install
%meson_install
