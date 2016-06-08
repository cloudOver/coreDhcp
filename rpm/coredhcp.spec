Name: coredhcp
Version: 16.06.01
Release: 1%{?dist}
URL: http://www.cloudover.org/corecluster/
Packager: Maciej Nabozny <maciej.nabozny@cloudover.io>
Summary: DHCP support for isolated networks in CoreCluster
License: GPLv3

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires: corecluster
Requires: dnsmasq

%description
Dhcp support for isolated networks in CoreCluster

%install
rm -rf $RPM_BUILD_ROOT
cd coredhcp/
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
/usr/local/lib/python2.7/dist-packages/
