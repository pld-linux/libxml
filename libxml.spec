Summary:	libXML library
Summary(pl):	Biblioteka libxml
Name:		libxml
Version:	1.0.0
Release:	1
Copyright:	LGPL
Group:		Libraries
Group(pl):	Biblioteki
Source:		ftp://ftp.gnome.org/pub/GNOME/sources/%{name}-%{version}.tar.gz
BuildRoot:	/tmp/%{name}-%{version}-root
URL:		http://www.gnome.org
Prereq:		/sbin/install-info
Conflicts:	glibc <= 2.0.7

%description
This library allows you to manipulate XML files.

%description -l pl
Biblioteka libxml umo¿liwia manipulowaie zawarto¶ci± plików XML.

%package devel
Summary:	Header files etc to develop libxml applications
Summary(pl):	Pliki nag³ówkowe i inne do libxml
Group:		Development/libraries
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Header files etc you can use to develop libxml applications.

%description -l pl devel
Pakiet ten zaziewra pliki nag³ówkowe i inne do libxml niezbêdne przy
tworzeniu aplikacji opartych o t± bibliotekê.

%package static
Summary:	Static libxml libraries
Summary(pl):	Biblioteka statyczna libxml
Group:		Development/libraries
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Static libxml libraries.

%description -l pl static
Biblioteka statyczna libxml.

%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure \
	--prefix=/usr
make

%install
rm -rf $RPM_BUILD_ROOT
make install prefix=$RPM_BUILD_ROOT/usr

strip $RPM_BUILD_ROOT/usr/lib/lib*.so.*.*

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%attr(755,root,root) /usr/lib/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO doc/{*.gif,*.html,html/*}
%attr(755,root,root) /usr/bin/xml-config
%attr(755,root,root) /usr/lib/lib*.so
%attr(755,root,root) /usr/lib/*.sh
/usr/include/gnome-xml

%files static
%attr(644,root,root) /usr/lib/lib*.a

%changelog
* Fri Feb 26 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.99.8-1]
- added "Conflicts: glibc <= 2.0.7" for prevent install
  with proper version glibc,
- changed prefix to /usr,
- changed all Group fields,
- %doc moved to devel,
- removed lib*.la files from static,
- added pl translation.

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
