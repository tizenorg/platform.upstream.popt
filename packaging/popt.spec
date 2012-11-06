#
# spec file for package popt
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           popt
Version:        1.16
Release:        0
License:        SUSE-XFree86-1.0
#!BuildIgnore:  rpmlint-Factory
Summary:        A C library for parsing command line parameters
Url:            http://www.rpm5.org/
Group:          System Environment/Libraries
Source:         popt-%{version}.tar.bz2
Source2:        baselibs.conf
BuildRequires:  pkgconfig
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Popt is a C library for parsing command line parameters.  Popt was
heavily influenced by the getopt() and getopt_long() functions. It
improves on them by allowing more powerful argument expansion. Popt can
parse arbitrary argv[] style arrays and automatically set variables
based on command line arguments.  Popt allows command line arguments to
be aliased via configuration files and includes utility functions for
parsing arbitrary strings into argv[] arrays using shell-like rules.

%package -n libpopt
Summary:        A C library for parsing command line parameters
Group:          System Environment/Libraries
Provides:       popt = %{version}
Obsoletes:      popt < %{version}

%description -n libpopt
Popt is a C library for parsing command line parameters.  Popt was
heavily influenced by the getopt() and getopt_long() functions. It
improves on them by allowing more powerful argument expansion. Popt can
parse arbitrary argv[] style arrays and automatically set variables
based on command line arguments.  Popt allows command line arguments to
be aliased via configuration files and includes utility functions for
parsing arbitrary strings into argv[] arrays using shell-like rules.

%package devel
Summary:        Development files for the popt library
Group:          Development/Libraries
Requires:       libpopt = %{version}

%description devel
The popt-devel package includes header files and libraries necessary
for developing programs which use the popt C library. It contains the
API documentation of the popt library, too.

%prep
%setup -q
%build
%configure --with-pic --disable-static
make %{?_smp_mflags}

%install
%make_install

%if "%{_libdir}" != "%{_prefix}/lib"
install -d -m755 %{buildroot}/%{_libdir}/pkgconfig
mv %{buildroot}%{_prefix}/lib/pkgconfig/%{name}.pc %{buildroot}/%{_libdir}/pkgconfig/%{name}.pc
%endif

%find_lang %{name}

%post -n libpopt -p /sbin/ldconfig

%postun -n libpopt -p /sbin/ldconfig

%files -n libpopt -f %{name}.lang
%defattr(-,root,root)
%doc CHANGES COPYING
%{_libdir}/libpopt.so.*

%files devel
%defattr(-,root,root)
%doc README
%{_libdir}/libpopt.so
%{_includedir}/popt.h
%{_mandir}/man3/popt.3*
%{_libdir}/pkgconfig/popt.pc

%changelog
