%global commit c13ce01bafc9208ce8de322d47188bdc7e945e7d
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           secilc
Version:        0
Release:        0.15git%{shortcommit}%{?dist}
Summary:        SELinux Common Intermediate Language (CIL) Compiler

License:        BSD
URL:            http://github.com/SELinuxProject/cil/wiki/
Source0:        https://github.com/SELinuxProject/cil/archive/%{commit}/cil-%{commit}.tar.gz

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  bison gcc >= 4.5.1 libsepol-static >= 2.1.4 lcov >= 1.9 flex >= 2.5.35 make coreutils xmlto dblatex

%description
The SELinux CIL Compiler is a compiler that converts the CIL language as
described on the CIL design wiki into a policy.conf file. Please see the
CIL Design Wiki at http://userspace.selinuxproject.org/trac/wiki/CilDesign
for more information about the goals and features on the CIL language.

%package reference-guide
Summary:        SELinux Common Intermediate Language (CIL) Reference Guide
Group:          System Environment/Base

BuildArch:      noarch

%description reference-guide
SELinux Common Intermediate Language (CIL) Docbook Reference Guide

%files reference-guide
%defattr(-,root,root)
%doc %{_usr}/share/doc/%{name}/pdf/


%prep
%setup -qn cil-%{commit}


%build
/usr/bin/make clean
/usr/bin/make LIBDIR="%{_libdir}" CFLAGS="%{optflags}"
/usr/bin/make -C docs pdf

%install
/usr/bin/rm -rf ${RPM_BUILD_ROOT}
%{__mkdir} -p ${RPM_BUILD_ROOT}%{_bindir}
/usr/bin/cp -p secilc ${RPM_BUILD_ROOT}%{_bindir}/
%{__mkdir} -p ${RPM_BUILD_ROOT}%{_usr}/share/doc/%{name}
/usr/bin/cp COPYING ${RPM_BUILD_ROOT}%{_usr}/share/doc/%{name}/

%{__mkdir} -p ${RPM_BUILD_ROOT}%{_usr}/share/doc/%{name}/pdf/
/usr/bin/cp docs/pdf/CIL_Reference_Guide.pdf ${RPM_BUILD_ROOT}%{_usr}/share/doc/%{name}/pdf/

%clean
/usr/bin/rm -rf ${RPM_BUILD_ROOT}


%files
%defattr(-,root,root)
%{_bindir}/secilc
%doc %{_usr}/share/doc/%{name}



%changelog
* Thu Aug 21 2014 "Dominick Grift <dac.override@gmail.com>" - 0-0.15gitc13ce01
- Update to upstream

* Sat Aug 2 2014 "Dominick Grift <dac.override@gmail.com>" - 0-0.14gitc97fff6
- Update to upstream

* Sat Jul 26 2014 "Dominick Grift <dac.override@gmail.com>" - 0-0.13gitd70efd5
- Update to upstream

* Wed Jul 16 2014 "Dominick Grift <dac.override@gmail.com>" - 0-0.12git803af32
- Update to upstream

* Fri Jul 11 2014 "Dominick Grift <dac.override@gmail.com>" - 0-0.11git2a1fe5d
- Update to upstream

* Wed Jul 9 2014 "Dominick Grift <dac.override@gmail.com>" - 0-0.10git7427f48
- Update to upstream

* Wed Jul 2 2014 "Dominick Grift <dac.override@gmail.com>" - 0-0.9gitb3a8292
- Update to upstream

* Wed Jul 2 2014 "Dominick Grift <dac.override@gmail.com>" - 0-0.8git9170e30
- Update to upstream

* Thu May 22 2014 "Dominick Grift <dac.override@gmail.com>" - 0-0.7git994905f
- Update to upstream

* Thu May 15 2014 "Dominick Grift <dac.override@gmail.com>" - 0-0.6gite44f9da
- Update to upstream

* Sat Apr 26 2014 "Dominick Grift <dac.override@gmail.com>" - 0-0.5gite3b35c0
- Various clean ups
- Support for mls true or false statement

* Wed Apr 23 2014 "Dominick Grift <dac.override@gmail.com>" - 0-0.4git7889715
- Possible other fix for boolean issue

* Tue Apr 22 2014 "Dominick Grift <dac.override@gmail.com>" - 0-0.3gitc50b6ef
- Version bump

* Tue Apr 22 2014 "Dominick Grift <dac.override@gmail.com>" - 0-0.2gitc50b6ef
- Possible fix for boolean issues

* Sun Apr 20 2014 "Dominick Grift <dac.override@gmail.com>" - 0-0.1git4203d31
- Initial SELinux Common Intermediate Language (CIL) Compiler RPM spec file
