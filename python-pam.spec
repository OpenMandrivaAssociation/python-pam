%define module pam
%define oname python_pam

Name:		python-pam
Version:	2.0.2
Release:	1
Summary:	Python bindings for PAM
License:	MIT
Group:		Development/Python
URL:		https://github.com/FirefighterBlu3/python-pam
Source0:	%{URL}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)

%description
This release supports the core PAM API. There is still some missing
functionality, but it should implement enough of the API for most
needs. There is not much in the way of documentation at this point. If
you are familiar with the PAM API, a quick glance at the sample program
should get you going.

%files
%doc LICENSE README.md
%{python_sitelib}/%{module}
%{python_sitelib}/%{oname}-%{version}.dist-info
