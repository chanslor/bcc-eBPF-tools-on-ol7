Name:    bcc-eBPF-tools-on-ol7
Summary: bcc-eBPF-tools-on-ol7
Version: 1
Release: 1
Group:   Applications/System
License: GPLv2+
Packager: michael.chanslor@gmail.com

Source0: https://github.com/chanslor/bcc-eBPF-tools-on-ol7/archive/master.tar.gz#/%{name}-%{version}-%{release}.tar.gz

BuildRoot:  /var/tmp/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires: yum-utils
AutoReqProv: no


%description
ply - A dynamic tracer for Linux

%prep
pwd
ls -alrth
#make sure you remove prep when only using Source0 with no .tar

%setup

%build

%install
###mkdir -p $RPM_BUILD_ROOT/etc/cron.d/



%clean

%files
%defattr(0644,root,root)


%post


%changelog
