%define name bcc
%define version 1
%define release 1.0

Name:    %{name}
Summary: bcc - Tools for BPF-based Linux IO analysis, networking, monitoring, and more
Version: %{version}
Release: %{release}

Group:   Applications/System
License: GPLv2+
Packager: michael.chanslor@gmail.com

URL: https://github.com/iovisor/
Source0: https://github.com/iovisor/bcc/archive/master.tar.gz#/%{name}-%{version}-%{release}.tar.gz

BuildRoot:  /var/tmp/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires: yum-utils
AutoReqProv: no

%define debug_package %{nil}


%description
bcc - Tools for BPF-based Linux IO analysis, networking, monitoring, and more

%prep
%autosetup -n %{name}-master -p1

pwd
ls -alrth
#make sure you remove prep when only using Source0 with no .tar

###%setup

%build
cmake3 -G "Unix Makefiles" -DCMAKE_INSTALL_PREFIX=/usr
make

%install
make install DESTDIR=$RPM_BUILD_ROOT


%files
%defattr(-,root,root)
/usr/include/bcc
/usr/lib/python2.7
/usr/lib64/libbcc.so
/usr/lib64/libbcc.so.0
/usr/lib64/libbpf.so
/usr/lib64/libbpf.so.0
/usr/lib64/libbcc.so.EAD-HASH-NOTFOUND
/usr/lib64/libbpf.so.EAD-HASH-NOTFOUND
/usr/lib64/pkgconfig/libbcc.pc
/usr/share/bcc/examples
/usr/share/bcc/introspection/bps
/usr/share/bcc/man
/usr/share/bcc/tools


%clean
%{__rm} -rf %{buildroot}


%post


%changelog
