%define url_ver %(echo %{version}|cut -d. -f1,2)

%define api 1.0
%define major 0
%define libname %mklibname %{name} %{api} %{major}
%define girname %mklibname %{name}-gir %{api}
%define devname %mklibname -d %{name}

Summary:	Tool and library mainly made to create Cabinet files
Name:		gcab
Version:	1.1
Release:	2
Group:		Development/Databases
License:	GPLv2+
Url:		http://www.gnome.org/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gcab/%{url_ver}/%{name}-%{version}.tar.xz

BuildRequires:	intltool
BuildRequires:	vala-tools
BuildRequires:	vala-devel
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires: pkgconfig(zlib)
BuildRequires: gtk-doc
BuildRequires: meson
BuildRequires: git-core

%description
Tool and library mainly made to create Cabinet files.
 - creation supports plain and basic MSZIP compression
 - can open and list files from cabinet, no extraction

%package -n %{libname}
Summary:	A support library for %{name}
Group:		System/Libraries

%description -n %{libname}
A support library for %{name}.

%package -n %{girname}
Summary:	GObject Introspection interface description for %{name}
Group:		System/Libraries

%description -n %{girname}
GObject Introspection interface description for %{name}.

%package -n %{devname}
Summary:        Development files for %{name}
Group:          Development/Other
Requires:	%{libname} = %{version}
Requires:	%{girname} = %{version}
Requires:	%{name} = %{version}

%description -n %{devname}
Development files for %{name}.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name}

%files -f %{name}.lang
%{_bindir}/gcab
%{_mandir}/man1/gcab*

%files -n %{libname}
%{_libdir}/lib%{name}-%{api}.so.%{major}*

%files -n %{girname}
%{_libdir}/girepository-1.0/GCab-%{api}.typelib

%files -n %{devname}
%{_includedir}/lib%{name}-%{api}/*
%{_libdir}/lib%{name}-%{api}.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gir-1.0/GCab-%{api}.gir
%{_datadir}/vala/vapi/libgcab-%{api}.*
%doc %{_datadir}/gtk-doc/html/%{name}
