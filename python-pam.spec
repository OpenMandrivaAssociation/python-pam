Name: 		    python-pam
Version: 	    1.8.4
Release: 	    4
Summary:        Python bindings for PAM
License:        GPL
Group:          Development/Python
BuildArch:	noarch
URL:            https://github.com/FirefighterBlu3/python-pam
Source0:        https://pypi.python.org/packages/source/p/%{name}/%{name}-%{version}.tar.gz
BuildRequires:  pam-devel
BuildRequires:  pkgconfig(python)
BuildRequires:	python3egg(setuptools)

%description
This release supports the core PAM API. There is still some missing
functionality, but it should implement enough of the API for most
needs. There is not much in the way of documentation at this point. If
you are familiar with the PAM API, a quick glance at the sample program
should get you going.

%prep
%setup -q

%build
export CFLAGS="$RPM_OPT_FLAGS" 
export LDFLAGS='-ldl'
python setup.py build

%install
python setup.py install --prefix=%{_prefix} --root=%{buildroot}

%files
%doc LICENSE README.md
%{python_sitelib}/*
