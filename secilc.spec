%global commit e3b35c0a18037738a3b196b9bae59d47986cd945
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global checkout %(c=%{commit}; echo ${c:0:12})

Name:           secilc
Version:        0
Release:        0.5git%{shortcommit}%{?dist}
Summary:        SELinux Common Intermediate Language (CIL) Compiler

License:        BSD
URL:            http://userspace.selinuxproject.org/trac/wiki/CilDesign
Source0:        http://bitbucket.org/jwcarter/secilc/get/%{shortcommit}.tar.gz

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  bison gcc >= 4.5.1 libsepol-static >= 2.1.4 lcov >= 1.9 flex >= 2.5.35 make coreutils

%description
The SELinux CIL Compiler is a compiler that converts the CIL language as
described on the CIL design wiki into a policy.conf file. Please see the
CIL Design Wiki at http://userspace.selinuxproject.org/trac/wiki/CilDesign
for more information about the goals and features on the CIL language.


%prep
%setup -qn jwcarter-secilc-%{checkout}


%build
/usr/bin/make clean
/usr/bin/make LIBDIR="%{_libdir}" CFLAGS="%{optflags}"


%install
/usr/bin/rm -rf ${RPM_BUILD_ROOT}
%{__mkdir} -p ${RPM_BUILD_ROOT}%{_bindir}
/usr/bin/cp -p secilc ${RPM_BUILD_ROOT}%{_bindir}/
%{__mkdir} -p ${RPM_BUILD_ROOT}%{_usr}/share/doc/%{name}
/usr/bin/cp COPYING ${RPM_BUILD_ROOT}%{_usr}/share/doc/%{name}/

%clean
/usr/bin/rm -rf ${RPM_BUILD_ROOT}


%files
%defattr(-,root,root)
%{_bindir}/secilc
%doc %{_usr}/share/doc/%{name}



%changelog
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
