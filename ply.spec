Name:    ply
Summary: ply - A dynamic tracer for Linux
Version: 1
Release: 1
Group:   Applications/System
License: GPLv2+
Packager: michael.chanslor@gmail.com

URL: https://github.com/iovisor/ply
Source0: https://github.com/iovisor/ply/archive/master.tar.gz#/%{name}-%{version}-%{release}.tar.gz

BuildRoot:  /var/tmp/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires: yum-utils
AutoReqProv: no


%description
ply - A dynamic tracer for Linux

%prep
%autosetup -n %{name}-master -p1

pwd
ls -alrth
#make sure you remove prep when only using Source0 with no .tar

###%setup

%build
#git clone https://github.com/iovisor/ply.git
#cd ply
./autogen.sh
./configure
make
make install

%install
mkdir -p $RPM_BUILD_ROOT/usr/local/sbin/
cp src/ply $RPM_BUILD_ROOT/usr/local/sbin/


%files
%defattr(0755,root,root)
/usr/local/sbin/ply

%clean
%{__rm} -rf %{buildroot}


%post


%changelog
