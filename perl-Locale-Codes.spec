#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Locale
%define		pnam	Codes
Summary:	Locale::Codes Perl module
Summary(cs):	Modul Locale::Codes pro Perl
Summary(da):	Perlmodul Locale::Codes
Summary(de):	Locale::Codes Perl Modul
Summary(es):	Módulo de Perl Locale::Codes
Summary(fr):	Module Perl Locale::Codes
Summary(it):	Modulo di Perl Locale::Codes
Summary(ja):	Locale::Codes Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	Locale::Codes ÆÞ ¸ðÁÙ
Summary(no):	Perlmodul Locale::Codes
Summary(pl):	Modu³ Perla Locale::Codes
Summary(pt):	Módulo de Perl Locale::Codes
Summary(pt_BR):	Módulo Perl Locale::Codes
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl Locale::Codes
Summary(sv):	Locale::Codes Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl Locale::Codes
Summary(zh_CN):	Locale::Codes Perl Ä£¿é
Name:		perl-Locale-Codes
Version:	2.06
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Locale::Codes contains two modules which can be used to process ISO two
letter codes for identifying language and country.

%description -l pl
Locale::Codes zawiera dwa modu³y umo¿liwiaj±ce przetwarzanie
dwuliterowych kodów ISO identyfikuj±cych jêzyk i kraj.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{perl_sitelib}/Locale/*.pm
%{_mandir}/man3/*
