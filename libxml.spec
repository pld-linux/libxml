Summary:	libXML library
Summary(pl):	Biblioteka libxml
Name:		libxml
Version:	1.8.15
Release:	1
Epoch:		1
License:	LGPL
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Source0:	ftp://xmlsoft.org/%{name}-%{version}.tar.gz
URL:		http://xmlsoft.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
This library allows you to manipulate XML files.

%description -l pl
Biblioteka libxml umo¿liwia manipulowanie zawarto¶ci± plików XML.

%package devel
Summary:	Header files etc to develop libxml applications
Summary(pl):	Pliki nag³ówkowe i inne do libxml
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}
Requires:	zlib-devel

%description devel
Header files etc you can use to develop libxml applications.

%description -l pl devel
Pakiet ten zawiera pliki nag³ówkowe i inne do libxml niezbêdne przy
tworzeniu aplikacji opartych o tê bibliotekê.

%package static
Summary:	Static libxml libraries
Summary(pl):	Biblioteka statyczna libxml
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Static libxml libraries.

%description -l pl static
Biblioteka statyczna libxml.

%prep
%setup -q

%build
libtoolize --copy --force
aclocal
autoconf
automake -a -c
%configure 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

gzip -9nf AUTHORS ChangeLog NEWS README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc {AUTHORS,ChangeLog,NEWS,README,TODO}.gz doc/{*.{gif,html},html/*}
%attr(755,root,root) %{_bindir}/xml-config
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%attr(755,root,root) %{_libdir}/*.sh
%{_includedir}/gnome-xml
%{_pkgconfigdir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
