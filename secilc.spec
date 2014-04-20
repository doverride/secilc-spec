%global commit 4203d31701471b14b520bfab5ce95577d9970676
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global checkout %(c=%{commit}; echo ${c:0:12})

Name:           secilc
Version:        0
Release:        0.1git%{shortcommit}%{?dist}
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
* Sun Apr 20 2014 "Dominick Grift <dac.override@gmail.com>" - 0-0.1git4203d31
- Initial SELinux Common Intermediate Language (CIL) Compiler RPM spec file
