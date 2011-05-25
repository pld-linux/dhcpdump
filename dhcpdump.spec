Summary:	Parse tcpdump DHCP packets
Summary(pl.UTF-8):	Analiza pakietów DHCP z tcpdumpa
Name:		dhcpdump
Version:	1.8
Release:	1
License:	Free (See LICENSE)
Group:		Applications
Source0:	http://www.mavetju.org/download/%{name}-%{version}.tar.gz
# Source0-md5:	099c786997c424f196414f9575f1fb90
URL:		http://sf.net/projects/mavetju/
BuildRequires:	perl-tools-pod
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A post-processor of tcpdump output to analyze sniffed DHCP packets.

%description -l pl.UTF-8
Postprocesor wyjścia tcpdumpa do analizy przechwyconych pakietów DHCP.

%prep
%setup -q
rm -f dhcpdump.1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES CONTACT LICENSE
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/dhcpdump.1*
