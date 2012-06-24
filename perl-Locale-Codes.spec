%include	/usr/lib/rpm/macros.perl
Summary:	Locale-Codes perl module
Summary(pl):	Modu� perla Locale-Codes
Name:		perl-Locale-Codes
Version:	1.00
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Locale/Locale-Codes-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Locale-Codes contains two modules which can be used to process ISO two letter 
codes for identifying language and country. 

%description -l pl
Locale-Codes zawiera dwa modu�y umo�liwiaj�ce przetwarzanie dwuliterowych 
kod�w ISO identyfikuj�cych j�zyk i kraj.

%prep
%setup -q -n Locale-Codes-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Locale
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        ChangeLog README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {ChangeLog,README}.gz

%{perl_sitelib}/Locale/Country.pm
%{perl_sitelib}/Locale/Language.pm

%{perl_sitearch}/auto/Locale/.packlist

%{_mandir}/man3/*
