Summary:	libXML library
Summary(pl):	Biblioteka libxml
Name:		libxml
Version:	1.0.0
Release:	4
Copyright:	LGPL
Group:		Libraries
Group(pl):	Biblioteki
Source:		ftp://ftp.gnome.org/pub/GNOME/sources/%{name}-%{version}.tar.gz
Patch0:		libxml-zlib.patch
Patch1:		libxml-VERSION.patch
URL:		http://rufus.w3.org/veillard/XML/messages/
Prereq:		/sbin/install-info
Conflicts:	glibc <= 2.0.7
BuildRoot:	/tmp/%{name}-%{version}-root

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
%patch0 -p1
%patch1 -p1

%build
automake
libtoolize --force
aclocal
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure \
	--prefix=/usr/X11R6
make

%install
rm -rf $RPM_BUILD_ROOT
make install prefix=$RPM_BUILD_ROOT/usr/X11R6

strip $RPM_BUILD_ROOT/usr/X11R6/lib/lib*.so.*.*

gzip -9nf AUTHORS ChangeLog NEWS README TODO doc/{*.{html,gif},html/*}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%attr(755,root,root) /usr/X11R6/lib/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc {AUTHORS,ChangeLog,NEWS,README,TODO}.gz doc/{*.{gif,html}.gz,html/*}
%attr(755,root,root) /usr/X11R6/bin/xml-config
%attr(755,root,root) /usr/X11R6/lib/lib*.so
%attr(755,root,root) /usr/X11R6/lib/*.sh
/usr/X11R6/include/gnome-xml

%files static
%attr(644,root,root) /usr/X11R6/lib/lib*.a

%changelog
* Wed Apr 21 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.0.0-4]
- removed "Conflicts: glibc <= 2.0.7" (not neccessary now),
- removed bogus "Prereq: /sbin/install-info",
- recompiles on new rpm.

* Thu Apr  1 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.0.0-3]
- added proper URl,
- changed install prefix to /usr/X11R6 (gnome-libs requure
  $gnomeprefix=xmlprefix),
- fixed raporting xml library version by xml-config script.

* Sun Mar 14 1999 Micha³ Kuratczyk <kura@pld.org.pl>
  [1.0.0-2]
- added gzipping documentation

* Thu Mar 11 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.0.0-1]
- fixed not linking libxml with libz (libxml-zlib.patch).

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
