Summary:	An open source Linux client for Google Drive
Summary(pl.UTF-8):	Linuksowy, mające otwarte źródła klient Google Drive
Name:		grive2
Version:	0.5.1
Release:	7
License:	GPL v2
Group:		Applications/Networking
#Source0Download: https://github.com/vitalif/grive2/releases
Source0:	https://github.com/vitalif/grive2/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	2ffb02ae2ddaba51fc8f31bb322efd93
Patch0:		binutils-2.34.patch
URL:		https://github.com/vitalif/grive2
BuildRequires:	binutils-devel
BuildRequires:	boost-devel >= 1.40.0
BuildRequires:	cmake >= 2.8
BuildRequires:	curl-devel
BuildRequires:	expat-devel
BuildRequires:	libgcrypt-devel
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	openssl-devel
BuildRequires:	pkgconfig
BuildRequires:	yajl-devel
Obsoletes:	grive < 0.3.0-1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The purpose of this project is to provide an independent
implementation of Google Drive client. It uses the Google Document
List API to talk to the servers in Google.

%description -l pl.UTF-8
Celem tego projektu jest zapewnienie niezależnej implementacji klienta
Google Drive. Do komunikacji z serwerami Google'a wykorzystuje API
Google Document List.

%prep
%setup -q
%patch0 -p1

%build
install -d build
cd build
%cmake ..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/grive
%dir %{_prefix}/lib/grive
%attr(755,root,root) %{_prefix}/lib/grive/grive-sync.sh
%{systemduserunitdir}/grive-changes@.service
%{systemduserunitdir}/grive-timer@.service
%{systemduserunitdir}/grive-timer@.timer
%{_mandir}/man1/grive.1*
