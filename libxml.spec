Summary:	libXML library
Summary(es):	Biblioteca libXML
Summary(pl):	Biblioteka libxml
Summary(pt_BR):	Biblioteca libXML
Summary(ru):	Библиотека XML
Summary(uk):	Б╕бл╕отека XML
Name:		libxml
Version:	1.8.17
Release:	9
Epoch:		1
License:	LGPL
Group:		Libraries
Source0:	ftp://xmlsoft.org/old/%{name}-%{version}.tar.gz
# Source0-md5: 53846294aa850a7d042948176d1d19dc
Patch0:		%{name}-am15.patch
Patch1:		%{name}-pmake.patch
Patch2:		%{name}-urlbound.patch
Patch3:		%{name}-man.patch
URL:		http://xmlsoft.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library allows you to manipulate XML files.

%description -l es
Esta biblioteca permite manipulaciСn de archivos XML.

%description -l pl
Biblioteka libxml umo©liwia manipulowanie zawarto╤ci╠ plikСw XML.

%description -l pt_BR
Esta biblioteca permite a manipulaГЦo de arquivos XML.

%description -l ru
Пакет libxml содержит библиотеку XML, которая позволяет манипулировать
XML файлами. XML (eXtensible Markup Language) - это формат данных для
обмена структурированными документами через Web.

%description -l uk
Пакет libxml м╕стить б╕бл╕отеку XML, яка дозволя╓ ман╕пулювати XML
файлами. XML (eXtensible Markup Language) - це формат даних для обм╕ну
струкурованими документами через Web.

%package devel
Summary:	Header files etc to develop libxml applications
Summary(es):	Archivos de inclusiСn para desarrollo de aplicaciones libXML
Summary(pl):	Pliki nagЁСwkowe i inne do tworzenia aplikacji u©ywaj╠cych libxml
Summary(pt_BR):	Arquivos de inclusЦo para desenvolvimento de aplicaГУes que usem a biblioteca libxml
Summary(ru):	Хедеры и другие файлы для разработки libxml приложений
Summary(uk):	Хедери та ╕нш╕ файли для розробки libxml програм
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	gtk-doc-common
Requires:	zlib-devel

%description devel
Header files etc you can use to develop libxml applications.

%description devel -l es
Biblioteca y archivos de inclusiСn para desarrollo de aplicaciones
libXML.

%description devel -l pl
Pakiet ten zawiera pliki nagЁСwkowe i inne do libxml niezbЙdne przy
tworzeniu aplikacji opartych o tЙ bibliotekЙ.

%description devel -l pt_BR
Bibliotecas e arquivos de inclusЦo para desenvolvimento de aplicaГУes
que usem a biblioteca libxml.

%description devel -l ru
Пакет libxml-devel содержит хедеры и другие файлы для разработки
libxml приложений.

%description devel -l uk
Пакет libxml-devel м╕стить хедери та ╕нш╕ файли для розробки libxml
програм.

%package static
Summary:	Static libxml library
Summary(pl):	Biblioteka statyczna libxml
Summary(pt_BR):	Bibliotecas estАticas para desenvolvimento de aplicaГУes que usem a biblioteca libxml
Summary(ru):	Статические библиотеки для разработки libxml приложений
Summary(uk):	Статичн╕ б╕бл╕отеки для розробки libxml програм
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static libxml library.

%description static -l pl
Biblioteka statyczna libxml.

%description static -l pt_BR
Bibliotecas estАticas para desenvolvimento de aplicaГУes que usem a
biblioteca libxml.

%description static -l ru
Пакет libxml-static содержит cтатические библиотеки для разработки
libxml приложений.

%description static -l uk
Пакет libxml-static м╕стить cтатичн╕ б╕бл╕отеки для розробки libxml
програм.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--with-html-dir=%{_gtkdocdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	HTML_DIR=%{_gtkdocdir} \
	pkgconfigdir=%{_pkgconfigdir}

install -d $RPM_BUILD_ROOT%{_mandir}/man1
install debian/xml-config.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/lib*.so.*.*

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

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
