#
# Conditional build:
%bcond_with	tests	# do not perform "make test"

%define		pdir	Locale
%define		pnam	Codes
Summary:	Locale::Codes - a distribution of modules to handle locale codes
Summary(pl.UTF-8):	Locale::Codes - zbiór modułów do obsługi kodów lokalizacji
Name:		perl-Locale-Codes
Version:	3.63
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Locale/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	5c8e19b1157c28877de3bab6b99ee06b
URL:		https://metacpan.org/release/Locale-Codes
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.30
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl-File-Find-Rule
BuildRequires:	perl-Test-Inter >= 1.09
BuildRequires:	perl-Test-Pod
BuildRequires:	perl-Test-Pod-Coverage
BuildRequires:	perl-Test-Simple
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Locale::Codes contains five modules which can be used to process ISO
codes for identifying country, currency, language and script.

%description -l pl.UTF-8
Locale::Codes zawiera pięć modułów umożliwiających przetwarzanie
kodów ISO identyfikujących kraj, walutę, język i pismo.

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

%{__rm} $RPM_BUILD_ROOT%{perl_vendorlib}/Locale/*.pod
%{__rm} $RPM_BUILD_ROOT%{perl_vendorlib}/Locale/Codes/*.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes LICENSE README.first
%{perl_vendorlib}/Locale/Codes.pm
%dir %{perl_vendorlib}/Locale/Codes
%{perl_vendorlib}/Locale/Codes/*.pm
%{perl_vendorlib}/Locale/Country.pm
%{perl_vendorlib}/Locale/Currency.pm
%{perl_vendorlib}/Locale/Language.pm
%{perl_vendorlib}/Locale/Script.pm
%{_mandir}/man3/Locale::Codes*.3pm*
%{_mandir}/man3/Locale::Country.3pm*
%{_mandir}/man3/Locale::Currency.3pm*
%{_mandir}/man3/Locale::Language.3pm*
%{_mandir}/man3/Locale::Script.3pm*
