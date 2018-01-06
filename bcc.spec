%define name bcc
%define version 9.9
%define build_timestamp %{lua: print(os.date("%Y%m%d"))}

Name: %{name}
Summary: bcc - Tools for BPF-based Linux IO analysis, networking, monitoring, and more
Version: %{version}
Release: %{build_timestamp}

Group:   Applications/System
License: GPLv2+
Packager: michael.chanslor@gmail.com

URL: https://github.com/iovisor/
Source0: https://github.com/iovisor/bcc/archive/master.tar.gz#/%{name}-%{version}-%{release}.tar.gz

BuildRoot:  /var/tmp/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires: yum-utils
AutoReqProv: no


%description
bcc - Tools for BPF-based Linux IO analysis, networking, monitoring, and more

%prep
%autosetup -n %{name}-master -p1

pwd
ls -alrth
#make sure you remove prep when only using Source0 with no .tar

###%setup

%build
cmake3 -G "Unix Makefiles" -DCMAKE_INSTALL_PREFIX=/usr ../bcc
make
make install


%install
mkdir -p $RPM_BUILD_ROOT/usr/share/bcc/tools


%files
%defattr(-,root,root)


%clean
%{__rm} -rf %{buildroot}


%post


%changelog
