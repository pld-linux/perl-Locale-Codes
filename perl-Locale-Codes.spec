%include	/usr/lib/rpm/macros.perl
Summary:	Locale-Codes perl module
Summary(pl):	Modu³ perla Locale-Codes
Name:		perl-Locale-Codes
Version:	1.06
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Locale/Locale-Codes-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Locale-Codes contains two modules which can be used to process ISO two
letter codes for identifying language and country.

%description -l pl
Locale-Codes zawiera dwa modu³y umo¿liwiaj±ce przetwarzanie
dwuliterowych kodów ISO identyfikuj±cych jêzyk i kraj.

%prep
%setup -q -n Locale-Codes-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf ChangeLog README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Locale/*.pm
%{_mandir}/man3/*
