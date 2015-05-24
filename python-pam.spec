%define module  pam
%define name    python-%{module}
%define version 0.5.0
%define release 1

Name: 		    %{name}
Version: 	    %{version}
Release: 	    %{release}
Summary:        Python bindings for PAM
License:        GPL
Group:          Development/Python
URL:            http://www.pangalactic.org/PyPAM
Source:         PyPAM-%{version}.tar.gz
BuildRequires:  pam-devel
BuildRequires:  python2-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
This release supports the core PAM API. There is still some missing
functionality, but it should implement enough of the API for most
needs. There is not much in the way of documentation at this point. If
you are familiar with the PAM API, a quick glance at the sample program
should get you going.

%prep
%setup -q -n PyPAM-%{version}
rm examples/pamexample

%build
export CFLAGS="$RPM_OPT_FLAGS" 
export LDFLAGS='-ldl'
python2 setup.py build

%install
python2 setup.py install --prefix=%{_prefix} --root=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS NEWS README ChangeLog COPYING examples
%{_libdir}/python%{py2_ver}/site-packages/*

