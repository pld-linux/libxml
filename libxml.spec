Summary:	libXML library
Summary(pl):	Biblioteka libxml
Name:		libxml
Version:	1.8.6
Release:	1
License:	LGPL
Group:		Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
Source:		ftp://ftp.gnome.org/pub/GNOME/stable/sources/libxml/%{name}-%{version}.tar.gz
Patch0:		libxml-zlib.patch
URL:		http://xmlsoft.org/
BuildRequires:	zlib-devel
BuildRoot:	/tmp/%{name}-%{version}-root

%define		_prefix		/usr/X11R6

%description
This library allows you to manipulate XML files.

%description -l pl
Biblioteka libxml umo¿liwia manipulowaie zawarto¶ci± plików XML.

%package devel
Summary:	Header files etc to develop libxml applications
Summary(pl):	Pliki nag³ówkowe i inne do libxml
Group:		Development/Libraries
Group(fr):	Development/Librairies
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
Group:		Development/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Static libxml libraries.

%description -l pl static
Biblioteka statyczna libxml.

%prep
%setup -q
%patch0 -p1

%build
automake
LDFLAGS="-s"; export LDFLAGS
%configure 
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/lib*.so.*.*

gzip -9nf AUTHORS ChangeLog NEWS README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc {AUTHORS,ChangeLog,NEWS,README,TODO}.gz doc/{*.{gif,html},html/*}
%attr(755,root,root) %{_bindir}/xml-config
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%attr(755,root,root) %{_libdir}/*.sh
%{_includedir}/gnome-xml

%files static
%attr(644,root,root) %{_libdir}/lib*.a
