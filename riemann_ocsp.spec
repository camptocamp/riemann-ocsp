%define debug_package %{nil}

Summary:        submit nagios events to riemann
Name:           riemann-ocsp
Version:        0.1
Release:        2%{?dist}
URL:            https://github.com/camptocamp/riemann-ocsp
Source:         %{name}-%{version}.tar.gz
License:        GPLv2+
Group:          System Environment/Daemons
BuildRoot:      %{_tmppath}/%{name}-%{version}-root
BuildRequires:  golang, git

%description
send nagios events to riemann using submit_ocsp

%prep
%setup -q

%build
export GOPATH="$(pwd)"
go get -d
go build

%install
install -d %{buildroot}%{_bindir}
install -p -m 0755 %{name}-%{version} %{buildroot}%{_bindir}/riemann_ocsp

%clean
rm -rf %{buildroot}

%files
%{_bindir}/riemann_ocsp

%changelog
* Fri Oct 23 2015 Marc Fournier <marc.fournier@camptocamp.com> 0.1-2
- Make specfile more sensible

* Tue Dec 03 2013 Marc Fournier <marc.fournier@camptocamp.com> 0.1-1
- Initial release
