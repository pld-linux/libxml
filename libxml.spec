Summary:	libXML library
Summary(pl):	Biblioteka libxml2
Name:		libxml
Version:	2.3.0
Release:	1
License:	LGPL
Group:		Libraries
Group(de):	Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
Source0:	ftp://ftp.gnome.org/pub/GNOME/stable/sources/libxml/%{name}2-%{version}.tar.gz
Patch0:		%{name}-remake.patch
URL:		http://xmlsoft.org/
Requires:	iconv
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	iconv
BuildRequires:	zlib-devel
BuildRequires:	ncurses-devel
BuildRequires:	readline-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
This library allows you to manipulate XML files.

%description -l pl
Biblioteka libxml umo¿liwia manipulowaie zawarto¶ci± plików XML.

%package devel
Summary:	Header files etc to develop libxml applications
Summary(pl):	Pliki nag³ówkowe i inne do libxml
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
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
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Static libxml libraries.

%description -l pl static
Biblioteka statyczna libxml.

%prep
%setup -q -n %{name}2-%{version} 
%patch -p1

%build
libtoolize --copy --force
aclocal
autoconf
automake -a -c
%configure 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_aclocaldir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir}

gzip -9nf AUTHORS ChangeLog NEWS README TODO

%clean
#rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xmllint
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_mandir}/man1/xmllint.1*

%files devel
%defattr(644,root,root,755)
%doc *.gz doc/{*.{gif,html},html/*}
%attr(755,root,root) %{_bindir}/xml-config
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%attr(755,root,root) %{_libdir}/*.sh
%{_libdir}/pkgconfig/*
%{_aclocaldir}/*.m4
%{_includedir}/libxml
%{_mandir}/man1/xml-config.1*
%{_mandir}/man4/libxml.4*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
