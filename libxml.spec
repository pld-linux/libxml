Summary:	libXML library
Summary(es):	Biblioteca libXML
Summary(pl):	Biblioteka libxml
Summary(pt_BR):	Biblioteca libXML
Summary(ru):	���������� XML
Summary(uk):	��̦����� XML
Name:		libxml
Version:	1.8.17
Release:	7
Epoch:		1
License:	LGPL
Group:		Libraries
Source0:	ftp://xmlsoft.org/old/%{name}-%{version}.tar.gz
Patch0:		%{name}-am15.patch
Patch1:		%{name}-pmake.patch
URL:		http://xmlsoft.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library allows you to manipulate XML files.

%description -l es
Esta biblioteca permite manipulaci�n de archivos XML.

%description -l pl
Biblioteka libxml umo�liwia manipulowanie zawarto�ci� plik�w XML.

%description -l pt_BR
Esta biblioteca permite a manipula��o de arquivos XML.

%description -l ru
����� libxml �������� ���������� XML, ������� ��������� ��������������
XML �������. XML (eXtensible Markup Language) - ��� ������ ������ ���
������ ������������������ ����������� ����� Web.

%description -l uk
����� libxml ͦ����� ¦�̦����� XML, ��� ������Ѥ ��Φ�������� XML
�������. XML (eXtensible Markup Language) - �� ������ ����� ��� ��ͦ��
�������������� ����������� ����� Web.

%package devel
Summary:	Header files etc to develop libxml applications
Summary(es):	Biblioteca y archivos de inclusi�n para desarrollo de aplicaciones libXML
Summary(pl):	Pliki nag��wkowe i inne do libxml
Summary(pt_BR):	Bibliotecas e arquivos de inclus�o para desenvolvimento de aplica��es que usem a biblioteca libxml
Summary(ru):	������ � ������ ����� ��� ���������� libxml ����������
Summary(uk):	������ �� ��ۦ ����� ��� �������� libxml �������
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	zlib-devel

%description devel
Header files etc you can use to develop libxml applications.

%description devel -l es
Biblioteca y archivos de inclusi�n para desarrollo de aplicaciones
libXML.

%description devel -l pl
Pakiet ten zawiera pliki nag��wkowe i inne do libxml niezb�dne przy
tworzeniu aplikacji opartych o t� bibliotek�.

%description devel -l pt_BR
Bibliotecas e arquivos de inclus�o para desenvolvimento de aplica��es
que usem a biblioteca libxml.

%description devel -l ru
����� libxml-devel �������� ������ � ������ ����� ��� ����������
libxml ����������.

%description devel -l uk
����� libxml-devel ͦ����� ������ �� ��ۦ ����� ��� �������� libxml
�������.

%package static
Summary:	Static libxml libraries
Summary(es):	Static libraries to develop libxml applications
Summary(pl):	Biblioteka statyczna libxml
Summary(pt_BR):	Bibliotecas est�ticas para desenvolvimento de aplica��es que usem a biblioteca libxml
Summary(ru):	����������� ���������� ��� ���������� libxml ����������
Summary(uk):	������Φ ¦�̦����� ��� �������� libxml �������
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static libxml libraries.

%description static -l es
Static libraries, you can use to develop libxml applications.

%description static -l pl
Biblioteka statyczna libxml.

%description static -l pt_BR
Bibliotecas est�ticas para desenvolvimento de aplica��es que usem a
biblioteca libxml.

%description static -l ru
����� libxml-static �������� c���������� ���������� ��� ����������
libxml ����������.

%description static -l uk
����� libxml-static ͦ����� c�����Φ ¦�̦����� ��� �������� libxml
�������.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO doc/{*.{gif,html},html/*}
%attr(755,root,root) %{_bindir}/xml-config
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%attr(755,root,root) %{_libdir}/*.sh
%{_includedir}/gnome-xml
%{_pkgconfigdir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
