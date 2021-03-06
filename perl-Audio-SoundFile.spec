#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Audio
%define		pnam	SoundFile
Summary:	Audio::SoundFile Perl module - interface to libsndfile, a sound I/O library
Summary(pl.UTF-8):	Moduł Perla Audio::SoundFile - interfejs do libsndfile
Name:		perl-Audio-SoundFile
Version:	0.16
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	cbb84d7ffb4a8fc5389d7239696bda3c
URL:		http://search.cpan.org/dist/Audio-SoundFile/
BuildRequires:	libsndfile-devel >= 1.0.0
BuildRequires:	perl-PDL
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides interface to libsndfile. With this library, you
will be able to read, write, and manipulate sound data of more than 10
formats. Also, in addition to read/write interface using usual Perl
scalar, this module provides interface using PDL object directly.
Since PDL provides efficient method to handle large bytestream, sound
processing is much faster if this module and PDL is used in pair.

%description -l pl.UTF-8
Ten moduł udostępnia interfejs do libsndfile. Biblioteka ta pozwala na
odczyt, zapis i obróbkę danych dźwiękowych w ponad 10 formatach.
Ponadto, oprócz interfejsu używającego perlowych skalarów, ten moduł
udostępnia interfejs używający bezpośrednio obiektu PDL. Ponieważ PDL
udostępnia wydajne sposoby na obsługę dużych strumieni danych,
przetwarzanie dźwięku jest szybsze przy współpracy z PDL.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README*
%{perl_vendorarch}/Audio/SoundFile.pm
%{perl_vendorarch}/Audio/SoundFile
%dir %{perl_vendorarch}/auto/Audio/SoundFile
%dir %{perl_vendorarch}/auto/Audio/SoundFile/*
%attr(755,root,root) %{perl_vendorarch}/auto/Audio/SoundFile/*/*.so
%{_mandir}/man3/*
