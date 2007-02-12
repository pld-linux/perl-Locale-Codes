#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Locale
%define		pnam	Codes
Summary:	Locale::Codes Perl module
Summary(cs.UTF-8):   Modul Locale::Codes pro Perl
Summary(da.UTF-8):   Perlmodul Locale::Codes
Summary(de.UTF-8):   Locale::Codes Perl Modul
Summary(es.UTF-8):   Módulo de Perl Locale::Codes
Summary(fr.UTF-8):   Module Perl Locale::Codes
Summary(it.UTF-8):   Modulo di Perl Locale::Codes
Summary(ja.UTF-8):   Locale::Codes Perl モジュール
Summary(ko.UTF-8):   Locale::Codes 펄 모줄
Summary(nb.UTF-8):   Perlmodul Locale::Codes
Summary(pl.UTF-8):   Moduł Perla Locale::Codes
Summary(pt.UTF-8):   Módulo de Perl Locale::Codes
Summary(pt_BR.UTF-8):   Módulo Perl Locale::Codes
Summary(ru.UTF-8):   Модуль для Perl Locale::Codes
Summary(sv.UTF-8):   Locale::Codes Perlmodul
Summary(uk.UTF-8):   Модуль для Perl Locale::Codes
Summary(zh_CN.UTF-8):   Locale::Codes Perl 模块
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

%description -l pl.UTF-8
Locale::Codes zawiera dwa moduły umożliwiające przetwarzanie
dwuliterowych kodów ISO identyfikujących język i kraj.

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
