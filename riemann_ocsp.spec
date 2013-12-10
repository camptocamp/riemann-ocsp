Summary:        submit nagios events to riemann
Name:           riemann-ocsp
Version:        0.1
Release:        1%{?dist}
URL:            https://github.com/camptocamp/riemann-ocsp
Source:         %{name}-%{version}.tar.gz
License:        GPLv2+
Group:          System Environment/Daemons
BuildRoot:      %{_tmppath}/%{name}-%{version}-root
BuildRequires:  golang

%description
send nagios events to riemann using submit_ocsp

%prep
%setup -q

%install
rm -rf %{buildroot}/usr/bin
%{__mkdir} -p %{buildroot}
export GOPATH=%{buildroot}
go get -d
go build -o %{buildroot}/usr/bin/riemann_ocsp
rm -fr %{buildroot}/src

%files
%{_bindir}/riemann_ocsp

%changelog
* Tue Dec 03 2013 Marc Fournier <marc.fournier@camptocamp.com> 0.1-1
- Initial release
