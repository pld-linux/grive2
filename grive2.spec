Summary:	An open source Linux client for Google Drive
Summary(pl.UTF-8):	Linuksowy, mające otwarte źródła klient Google Drive
Name:		grive2
Version:	0.5.3
Release:	1
License:	GPL v2
Group:		Applications/Networking
#Source0Download: https://github.com/vitalif/grive2/releases
Source0:	https://github.com/vitalif/grive2/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	583b463b6f9cc561dc1abf0373916f5c
Patch0:		missing-includes.patch
Patch1:		libgcrypt1.10.patch
URL:		https://github.com/vitalif/grive2
BuildRequires:	binutils-devel
BuildRequires:	boost-devel >= 1.40.0
BuildRequires:	cmake >= 2.8
BuildRequires:	curl-devel
BuildRequires:	libgcrypt-devel
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.682
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
%patch -P0 -p1
%patch -P1 -p1

%build
install -d build
cd build
%cmake .. \
	-DHAVE_SYSTEMD=1

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
%dir %{_libexecdir}/grive
%attr(755,root,root) %{_libexecdir}/grive/grive-sync.sh
%{systemduserunitdir}/grive@.service
%{systemduserunitdir}/grive-changes@.service
%{systemduserunitdir}/grive-timer@.service
%{systemduserunitdir}/grive-timer@.timer
%{_mandir}/man1/grive.1*
