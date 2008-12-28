%define module  pam
%define name    python-%{module}
%define version 0.5.0
%define release %mkrel 4

Name: 		    %{name}
Version: 	    %{version}
Release: 	    %{release}
Summary:        Python bindings for PAM
License:        GPL
Group:          Development/Python
URL:            http://www.pangalactic.org/PyPAM
Source:         PyPAM-%{version}.tar.bz2
BuildRequires:  pam-devel
BuildRequires:  python-devel
#Source2:        setup.py
#Patch:          %{tarname}-%{version}.patch
#Patch1:         %{tarname}-%{version}-dl.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
This release supports the core PAM API. There is still some missing
functionality, but it should implement enough of the API for most
needs. There is not much in the way of documentation at this point. If
you are familiar with the PAM API, a quick glance at the sample program
should get you going.

%prep
%setup -q -n PyPAM-%{version}
#cp %{S:2} .
#%patch
#%patch1
rm examples/pamexample

%build
export CFLAGS="$RPM_OPT_FLAGS" 
python setup.py build

%install
python setup.py install --prefix=%{_prefix} --root=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS NEWS README ChangeLog COPYING examples
%{_libdir}/python%{pyver}/site-packages/*

