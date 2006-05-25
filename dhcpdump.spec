Summary:	Parse tcpdump DHCP packets
Summary(pl):	Analiza pakietów DHCP z tcpdumpa
Name:		dhcpdump
Version:	1.6
Release:	0.1
License:	GPL (?)
Group:		Applications
Source0:	http://www.mavetju.org/download/%{name}-%{version}.tar.gz
# Source0-md5:	736adf06370eee5f921344fd6388d477
URL:		http://sf.net/projects/mavetju/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A post-processor of tcpdump output to analyze sniffed DHCP packets.

%description -l pl
Postprocesor wyj¶cia tcpdumpa do analizy przechwyconych pakietów DHCP.


%prep
%setup -q

%build
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
%doc CHANGES CONTACT
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/dhcpdump.1*
