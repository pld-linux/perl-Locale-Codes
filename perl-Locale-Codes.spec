#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Locale
%define		pnam	Codes
Summary:	Locale::Codes Perl module
Summary(cs):	Modul Locale::Codes pro Perl
Summary(da):	Perlmodul Locale::Codes
Summary(de):	Locale::Codes Perl Modul
Summary(es):	M�dulo de Perl Locale::Codes
Summary(fr):	Module Perl Locale::Codes
Summary(it):	Modulo di Perl Locale::Codes
Summary(ja):	Locale::Codes Perl �⥸�塼��
Summary(ko):	Locale::Codes �� ����
Summary(nb):	Perlmodul Locale::Codes
Summary(pl):	Modu� Perla Locale::Codes
Summary(pt):	M�dulo de Perl Locale::Codes
Summary(pt_BR):	M�dulo Perl Locale::Codes
Summary(ru):	������ ��� Perl Locale::Codes
Summary(sv):	Locale::Codes Perlmodul
Summary(uk):	������ ��� Perl Locale::Codes
Summary(zh_CN):	Locale::Codes Perl ģ��
Name:		perl-Locale-Codes
Version:	2.07
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	af0537cc4a882096d0320612c440df6d
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Locale::Codes contains two modules which can be used to process ISO two
letter codes for identifying language and country.

%description -l pl
Locale::Codes zawiera dwa modu�y umo�liwiaj�ce przetwarzanie
dwuliterowych kod�w ISO identyfikuj�cych j�zyk i kraj.

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
%doc ChangeLog README
%{perl_vendorlib}/Locale/*.pm
%{_mandir}/man3/*
