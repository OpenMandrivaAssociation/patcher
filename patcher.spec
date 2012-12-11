Name:		patcher
Version:	0.6
Release:	%mkrel 12
License:	GPLv2+
Group:		Development/Other
Summary:	Quick creation of patches against a project source tree
Source0:	http://labix.org/download/patcher/%{name}-%{version}.tar.bz2
# (misc) patch sent to upstream by mail on 12/01/2009 
# the patch silence warnings on python 2.6
Patch0:		patcher-0.6-python26.patch
Url:		http://labix.org/patcher
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	python-devel
BuildArch:	noarch 
%description
Patcher is a tool for quick creation of patches against a project source tree. 
Patcher functionality resembles a lightweight version control system.
It has no repository, and only controls differences between a pristine version 
and a working copy. 

%prep
%setup -q 
%patch0 -p0

%build

%install
rm -rf $RPM_BUILD_ROOT
python ./setup.py install --prefix=$RPM_BUILD_ROOT/%_prefix
find $RPM_BUILD_ROOT/%_prefix -name '*pyc' | xargs rm -Rf

# remove rpmlint warning
perl -pi -e 's|^#!/usr/bin/python.*||' $RPM_BUILD_ROOT/%py_puresitedir/%{name}/{commands,}/*py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc LICENSE README
%_bindir/*
%py_puresitedir/%{name}/
%py_puresitedir/*.egg-info




%changelog
* Sun Oct 31 2010 Rémy Clouard <shikamaru@mandriva.org> 0.6-12mdv2011.0
+ Revision: 590913
- rebuild for new python

* Fri Oct 29 2010 Michael Scherer <misc@mandriva.org> 0.6-11mdv2011.0
+ Revision: 590167
- rebuild for python 2.7

  + Sandro Cazzaniga <kharec@mandriva.org>
    - Fix the last rpmlint warning
    - Clean spec file

* Fri Feb 05 2010 Michael Scherer <misc@mandriva.org> 0.6-9mdv2010.1
+ Revision: 501057
- add a URL for Source0
- fix License
- clean useless Requires ( as python-base and python were merged )
- fix rpmlint warning
- fix License
- fix compilation on 64 bits arch

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 0.6-8mdv2010.0
+ Revision: 440496
- rebuild

* Mon Jan 12 2009 Michael Scherer <misc@mandriva.org> 0.6-7mdv2009.1
+ Revision: 328795
- add patch to silence warning about md5 and python 2.6

* Wed Dec 24 2008 Michael Scherer <misc@mandriva.org> 0.6-6mdv2009.1
+ Revision: 318444
- fix build on x86_64
- rebuild for new python
- rebuild for new python

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 0.6-5mdv2009.0
+ Revision: 255047
- rebuild
- more standard summary

* Mon Feb 18 2008 Michael Scherer <misc@mandriva.org> 0.6-3mdv2008.1
+ Revision: 172126
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - fix summary-ended-with-dot


* Wed Nov 29 2006 Michael Scherer <misc@mandriva.org> 0.6-2mdv2007.0
+ Revision: 88392
- update for new python

* Wed Aug 09 2006 Olivier Thauvin <nanardon@mandriva.org> 0.6-1mdv2007.0
+ Revision: 54268
- sync sources
- 0.6
- update url
- Import patcher

