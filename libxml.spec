Summary:     libXML library
Name:        libxml
Version:     0.99
Release:     1
Copyright:   LGPL
Group:       X11/Libraries
Source:      ftp://ftp.gnome.org/pub/GNOME/sources/%{name}-%{version}.tar.gz
BuildRoot:   /tmp/%{name}-%{version}-root
URL:         http://www.gnome.org
Prereq:      /sbin/install-info

%description
This library allows you to manipulate XML files.

%package devel
Summary:     Header files etc to develop libxml applications
Group:       X11/libraries
Requires:    %{name} = %{version}

%description devel
Header files etc you can use to develop libxml applications.

%package static
Summary:     Static libxml libraries
Group:       X11/libraries
Requires:    %{name}-devel = %{version}

%description static
Static libxml libraries.

%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure \
	--prefix=/usr/X11R6
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

strip $RPM_BUILD_ROOT/usr/X11R6/lib/lib*.so.*.*

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-, root, root)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755, root, root) /usr/X11R6/lib/lib*.so.*.*

%files devel
%defattr(644, root, root, 755)
%attr(755, root, root) /usr/X11R6/bin/xml-config
%attr(755, root, root) /usr/X11R6/lib/lib*.so
%attr(755, root, root) /usr/X11R6/lib/*.sh
/usr/X11R6/include/gnome-xml

%files static
%attr(644, root, root) /usr/X11R6/lib/*a

%changelog
* Mon Jan 04 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.99-1]
- added /usr/X11R6/bin/xml-config,
- fixed permission on /usr/X11R6/lib/lib*.so*,
- added LDFLAGS="-s" to ./configure enviroment.

* Fri Sep 25 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.30-2]
- added -q %setup parameter,
- changed Buildroot to /tmp/%%{name}-%%{version}-root,
- added using %%{name} and %%{version} in Source,
- added static subpackage,
- removed COPYING* from %doc,
- added full %attr description in %files,
- added stripping shared libraries.

* Thu Sep 24 1998 Michael Fulbright <msf@redhat.com>
- Built release 0.30
