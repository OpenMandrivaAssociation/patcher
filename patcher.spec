Name:		patcher
Version: 0.6
Release:    %mkrel 6
License:	GPL
Group:		Development/Other
Summary:    Quick creation of patches against a project source tree
Source0:    %{name}-%{version}.tar.bz2
Url:		http://labix.org/patcher
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: python-devel
# needed for opt-parse
Requires:      python  
BuildArch:  noarch 
%description
Patcher is a tool for quick creation of patches against a project source tree. 
Patcher functionality ressembles a lightweight version control system.
It has no repository, and only controls differences between a pristine version 
and a working copy. 

%prep
%setup -q 

%build

%install
rm -rf $RPM_BUILD_ROOT
python ./setup.py install --prefix=$RPM_BUILD_ROOT/%_prefix
find $RPM_BUILD_ROOT/%_prefix -name '*pyc' | xargs rm -Rf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc LICENSE README
%_bindir/*
%py_sitedir/%{name}/
%py_puresitedir/*.egg-info


