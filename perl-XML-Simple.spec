%include	/usr/lib/rpm/macros.perl
%define	pdir	XML
%define	pnam	Simple
Summary:	XML::Simple perl module
Summary(pl):	Modu³ perla XML::Simple
Name:		perl-XML-Simple
Version:	2.02
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl-Storable
BuildRequires:	perl-XML-Parser >= 2.00
BuildRequires:	perl-devel >= 5.6.1
BuildRequires:	rpm-perlprov >= 3.0.3-16
Requires:	perl-XML-Parser >= 2.00
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XML::Simple - Trivial API for reading and writing XML (esp config
files)

%description -l pl
XML::Simple - trywialny interfejs do zapisywania i odczytywania plików
XML - zw³aszcza plików konfiguracyjnych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}
%{__make} test

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Changes
%doc %{_mandir}/man3/*
%{perl_sitelib}/XML/Simple.pm
