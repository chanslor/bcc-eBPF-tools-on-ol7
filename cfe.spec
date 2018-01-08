%define name cfe
%define version 3
%define release 9.1

Name:    %{name}
Summary: CFE CLANG collection of modular and reusable compiler and toolchain technologies
Version: %{version}
Release: %{release}

Group:   Applications/System
License: GPLv2+
Packager: michael.chanslor@gmail.com

URL: http://llvm.org/
Source0: http://releases.llvm.org/3.9.1/cfe-3.9.1.src.tar.xz#/%{name}-%{version}-%{release}.tar.xz

BuildRoot:  /var/tmp/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

AutoReqProv: no

%define debug_package %{nil}
%define __jar_repack %{nil}

%description
CFE CLANG The LLVM Project is a collection of modular and reusable compiler and toolchain technologies. Despite its name, LLVM has little to do with traditional virtual machines. The name "LLVM" itself is not an acronym; it is the full name of the project.



%prep
%autosetup -n %{name}-%{version}.%{release}.src -p1


###%setup

%build
mkdir cfe-build
cd cfe-build
cmake3 -G "Unix Makefiles" -DCMAKE_INSTALL_PREFIX=/usr ../
make


%install
cd cfe-build
make install DESTDIR=$RPM_BUILD_ROOT


%files
%defattr(-,root,root)
/usr/include/clang
/usr/include/clang-c
/usr/lib/clang/3.9.1
/usr/lib/libclangBasic.a
/usr/lib/libclangLex.a
/usr/lib/libclangParse.a
/usr/lib/libclangAST.a
/usr/lib/libclangASTMatchers.a
/usr/lib/libclangDynamicASTMatchers.a
/usr/lib/libclangSema.a
/usr/lib/libclangCodeGen.a
/usr/lib/libclangAnalysis.a
/usr/lib/libclangEdit.a
/usr/lib/libclangRewrite.a
/usr/lib/libclangARCMigrate.a
/usr/lib/libclangDriver.a
/usr/lib/libclangSerialization.a
/usr/lib/libclangFrontend.a
/usr/lib/libclangRewriteFrontend.a
/usr/lib/libclangFrontendTool.a
/usr/lib/libclangTooling.a
/usr/lib/libclangToolingCore.a
/usr/lib/libclangIndex.a
/usr/lib/libclangStaticAnalyzerCore.a
/usr/lib/libclangStaticAnalyzerCheckers.a
/usr/lib/libclangStaticAnalyzerFrontend.a
/usr/lib/libclangFormat.a
/usr/bin/clang-3.9
/usr/bin/clang
/usr/bin/clang-cl
/usr/bin/clang++
/usr/bin/clang-format
/usr/share/clang/clang-format-bbedit.applescript
/usr/share/clang/clang-format-diff.py
/usr/share/clang/clang-format-sublime.py
/usr/share/clang/clang-format.el
/usr/share/clang/clang-format.py
/usr/bin/git-clang-format
/usr/bin/c-index-test
/usr/bin/clang-check
/usr/bin/scan-build
/usr/libexec/ccc-analyzer
/usr/libexec/c++-analyzer
/usr/share/scan-build/scanview.css
/usr/share/scan-build/sorttable.js
/usr/bin/scan-view
/usr/share/scan-view/ScanView.py
/usr/share/scan-view/Reporter.py
/usr/share/scan-view/startfile.py
/usr/share/scan-view/FileRadar.scpt
/usr/share/scan-view/GetRadarVersion.scpt
/usr/share/scan-view/bugcatcher.ico
/usr/lib/libclang.so.3.9
/usr/lib/libclang.so
/usr/lib/cmake/clang
/usr/share/clang
/usr/share/man/man1/scan-build.1.gz
/usr/share/scan-view



%clean
%{__rm} -rf %{buildroot}


%post


%changelog
