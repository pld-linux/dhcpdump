Summary:	Parse tcpdump DHCP packets
Summary(pl):	Analiza pakietów DHCP z tcpdumpa
Name:		dhcpdump
Version:	1.7
Release:	1
License:	Free (See LICENSE)
Group:		Applications
Source0:	http://www.mavetju.org/download/%{name}-%{version}.tar.gz
# Source0-md5:	c606c20b2d6a875efce9eed0c6109061
URL:		http://sf.net/projects/mavetju/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	perl-tools-pod
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A post-processor of tcpdump output to analyze sniffed DHCP packets.

%description -l pl
Postprocesor wyj¶cia tcpdumpa do analizy przechwyconych pakietów DHCP.


%prep
%setup -q
rm -f dhcpdump.1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
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
