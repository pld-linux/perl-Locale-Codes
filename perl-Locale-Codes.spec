%include	/usr/lib/rpm/macros.perl
%define	pdir	Locale
%define	pnam	Codes
Summary:	Locale::Codes perl module
Summary(pl):	Modu� perla Locale::Codes
Name:		perl-Locale-Codes
Version:	2.04
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
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
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{perl_sitelib}/Locale/*.pm
%{perl_sitelib}/Locale/*.pod
%{_mandir}/man3/*
