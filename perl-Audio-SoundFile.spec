#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Audio
%define		pnam	SoundFile
Summary:	Audio::SoundFile Perl module - interface to libsndfile, a sound I/O library
Summary(pl):	Modu³ Perla Audio::SoundFile - interfejs do libsndfile
Name:		perl-Audio-SoundFile
Version:	0.15
Release:	3
License:	Artistic or GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
Patch0:		%{name}-libsndfile1.patch
BuildRequires:	libsndfile-devel >= 1.0.0
BuildRequires:	perl >= 5.6
BuildRequires:	perl-PDL
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides interface to libsndfile. With this library, you
will be able to read, write, and manipulate sound data of more than 10
formats. Also, in addition to read/write interface using usual Perl
scalar, this module provides interface using PDL object directly.
Since PDL provides efficient method to handle large bytestream, sound
processing is much faster if this module and PDL is used in pair.

%description -l pl
Ten modu³ udostêpnia interfejs do libsndfile. Biblioteka ta pozwala na
odczyt, zapis i obróbkê danych d¼wiêkowych w ponad 10 formatach.
Ponadto, oprócz interfejsu u¿ywaj±cego perlowych skalarów, ten modu³
udostêpnia interfejs u¿ywaj±cy bezpo¶rednio obiektu PDL. Poniewa¿ PDL
udostêpnia wydajne sposoby na obs³ugê du¿ych strumieni danych,
przetwarzanie d¼wiêku jest szybsze przy wspó³pracy z PDL.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch -p1

%build
%{__perl} Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README*
%{perl_sitearch}/Audio/SoundFile.pm
%{perl_sitearch}/Audio/SoundFile
%dir %{perl_sitearch}/auto/Audio/SoundFile
%dir %{perl_sitearch}/auto/Audio/SoundFile/*
%{perl_sitearch}/auto/Audio/SoundFile/*/*.bs
%attr(755,root,root) %{perl_sitearch}/auto/Audio/SoundFile/*/*.so
%{_mandir}/man3/*
