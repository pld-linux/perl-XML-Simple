%include	/usr/lib/rpm/macros.perl
Summary:	XML-Simple perl module
Summary(pl):	Modu³ perla XML-Simple
Name:		perl-XML-Simple
Version:	1.05
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://tp.cpan.org/CPAN/authors/id/G/GR/GRANTM/XML-Simple-1.05.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl
BuildRequires:	perl-XML-Parser
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XML::Simple - Trivial API for reading and writing XML (esp config files)

%description -l pl
XML::Simple - trywialny interfejs do zapisywania i odczytywania plików XML -
zw³aszcza plików konfiguracyjnych.

%prep
%setup -q -n XML-Simple-%{version}

%build
perl Makefile.PL
%{__make}
%{__make} test

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT
gzip -9nf README Changes

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%doc %{_mandir}/man3/*
%{perl_sitelib}/XML/Simple.pm
%{perl_sitearch}/auto/XML/Simple/.packlist
