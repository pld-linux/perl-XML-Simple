#
# Conditional build:
%bcond_without tests # do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	XML
%define	pnam	Simple
Summary:	XML::Simple - easy API to read/write XML (esp config files)
Summary(pl):	XML::Simple - proste API do czytania/zapisu XML-a (zw³. plików konfiguracyjnych)
Name:		perl-XML-Simple
Version:	2.11
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	94e51ad14e348324ef8933fbf8ad9fb2
BuildRequires:	perl-Storable
BuildRequires:	perl-XML-Parser >= 2.00
BuildRequires:	perl-devel >= 5.6.1
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
# not really necessary - only to resolve dependencies:
BuildRequires:	perl-XML-SAX
%endif
Requires:	perl-XML-Parser >= 2.00
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The XML::Simple module provides a simple API layer on top of an
underlying XML parsing module (either XML::Parser or one of the SAX2
parser modules).

%description -l pl
Modu³ XML::Simple udostêpnia prost± warstwê API w oparciu o zasadniczy
modu³ analizy XML-a (albo XML::Parser, albo jeden z modu³ów
analizuj±cych SAX2).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Changes
%doc %{_mandir}/man3/*
%{perl_vendorlib}/XML/Simple.pm
