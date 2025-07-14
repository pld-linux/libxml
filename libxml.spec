#
# Conditional build:
%bcond_without	static_libs	# don't build static library

Summary:	libXML library
Summary(es.UTF-8):	Biblioteca libXML
Summary(pl.UTF-8):	Biblioteka libxml
Summary(pt_BR.UTF-8):	Biblioteca libXML
Summary(ru.UTF-8):	Библиотека XML
Summary(uk.UTF-8):	Бібліотека XML
Name:		libxml
Version:	1.8.17
Release:	14
Epoch:		1
License:	LGPL
Group:		Libraries
Source0:	ftp://xmlsoft.org/old/%{name}-%{version}.tar.gz
# Source0-md5:	53846294aa850a7d042948176d1d19dc
Patch0:		%{name}-am15.patch
Patch1:		%{name}-pmake.patch
Patch2:		%{name}-urlbound.patch
Patch3:		%{name}-man.patch
Patch4:		%{name}-CAN-2004-0989.patch
Patch5:		%{name}-open.patch
Patch6:		format-security.patch
URL:		http://xmlsoft.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library allows you to manipulate XML files.

%description -l es.UTF-8
Esta biblioteca permite manipulación de archivos XML.

%description -l pl.UTF-8
Biblioteka libxml umożliwia manipulowanie zawartością plików XML.

%description -l pt_BR.UTF-8
Esta biblioteca permite a manipulação de arquivos XML.

%description -l ru.UTF-8
Пакет libxml содержит библиотеку XML, которая позволяет манипулировать
XML файлами. XML (eXtensible Markup Language) - это формат данных для
обмена структурированными документами через Web.

%description -l uk.UTF-8
Пакет libxml містить бібліотеку XML, яка дозволяє маніпулювати XML
файлами. XML (eXtensible Markup Language) - це формат даних для обміну
струкурованими документами через Web.

%package devel
Summary:	Header files etc to develop libxml applications
Summary(es.UTF-8):	Archivos de inclusión para desarrollo de aplicaciones libXML
Summary(pl.UTF-8):	Pliki nagłówkowe i inne do tworzenia aplikacji używających libxml
Summary(pt_BR.UTF-8):	Arquivos de inclusão para desenvolvimento de aplicações que usem a biblioteca libxml
Summary(ru.UTF-8):	Хедеры и другие файлы для разработки libxml приложений
Summary(uk.UTF-8):	Хедери та інші файли для розробки libxml програм
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	gtk-doc-common
Requires:	zlib-devel

%description devel
Header files etc you can use to develop libxml applications.

%description devel -l es.UTF-8
Biblioteca y archivos de inclusión para desarrollo de aplicaciones
libXML.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki nagłówkowe i inne do libxml niezbędne przy
tworzeniu aplikacji opartych o tę bibliotekę.

%description devel -l pt_BR.UTF-8
Bibliotecas e arquivos de inclusão para desenvolvimento de aplicações
que usem a biblioteca libxml.

%description devel -l ru.UTF-8
Пакет libxml-devel содержит хедеры и другие файлы для разработки
libxml приложений.

%description devel -l uk.UTF-8
Пакет libxml-devel містить хедери та інші файли для розробки libxml
програм.

%package static
Summary:	Static libxml library
Summary(pl.UTF-8):	Biblioteka statyczna libxml
Summary(pt_BR.UTF-8):	Bibliotecas estáticas para desenvolvimento de aplicações que usem a biblioteca libxml
Summary(ru.UTF-8):	Статические библиотеки для разработки libxml приложений
Summary(uk.UTF-8):	Статичні бібліотеки для розробки libxml програм
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static libxml library.

%description static -l pl.UTF-8
Biblioteka statyczna libxml.

%description static -l pt_BR.UTF-8
Bibliotecas estáticas para desenvolvimento de aplicações que usem a
biblioteca libxml.

%description static -l ru.UTF-8
Пакет libxml-static содержит cтатические библиотеки для разработки
libxml приложений.

%description static -l uk.UTF-8
Пакет libxml-static містить cтатичні бібліотеки для розробки libxml
програм.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1
%patch -P5 -p1
%patch -P6 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--with-html-dir=%{_gtkdocdir} \
	%{!?with_static_libs:--disable-static}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	HTML_DIR=%{_gtkdocdir} \
	pkgconfigdir=%{_pkgconfigdir}

install -d $RPM_BUILD_ROOT%{_mandir}/man1
cp -p debian/xml-config.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libxml.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xml-config
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%attr(755,root,root) %{_libdir}/*.sh
%{_includedir}/gnome-xml
%{_pkgconfigdir}/*
%{_gtkdocdir}/gnome-xml
%{_mandir}/man1/xml-config.1*

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
%endif
