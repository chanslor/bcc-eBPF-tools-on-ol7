%define name llvm
%define version 3
%define release 9.1

Name:    %{name}
Summary: LLVM collection of modular and reusable compiler and toolchain technologies
Version: %{version}
Release: %{release}

Group:   Applications/System
License: GPLv2+
Packager: michael.chanslor@gmail.com

URL: http://llvm.org/
Source0: http://releases.llvm.org/3.9.1/llvm-3.9.1.src.tar.xz#/%{name}-%{version}-%{release}.tar.xz

BuildRoot:  /var/tmp/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

AutoReqProv: no

%define debug_package %{nil}

%description
The LLVM Project is a collection of modular and reusable compiler and toolchain technologies. Despite its name, LLVM has little to do with traditional virtual machines. The name "LLVM" itself is not an acronym; it is the full name of the project.



%prep
%autosetup -n %{name}-%{version}.%{release}.src -p1


###%setup

%build
mkdir llvm-build
cd llvm-build
cmake3 -G "Unix Makefiles" -DLLVM_TARGETS_TO_BUILD="BPF;X86"  -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr ../
make

%install
cd llvm-build
make install DESTDIR=$RPM_BUILD_ROOT


%files
%defattr(-,root,root)
/usr/bin/bugpoint
/usr/bin/llc
/usr/bin/lli
/usr/bin/llvm-ar
/usr/bin/llvm-as
/usr/bin/llvm-bcanalyzer
/usr/bin/llvm-c-test
/usr/bin/llvm-config
/usr/bin/llvm-cov
/usr/bin/llvm-cxxdump
/usr/bin/llvm-diff
/usr/bin/llvm-dis
/usr/bin/llvm-dsymutil
/usr/bin/llvm-dwarfdump
/usr/bin/llvm-dwp
/usr/bin/llvm-extract
/usr/bin/llvm-lib
/usr/bin/llvm-link
/usr/bin/llvm-lto
/usr/bin/llvm-mc
/usr/bin/llvm-mcmarkup
/usr/bin/llvm-nm
/usr/bin/llvm-objdump
/usr/bin/llvm-pdbdump
/usr/bin/llvm-profdata
/usr/bin/llvm-ranlib
/usr/bin/llvm-readobj
/usr/bin/llvm-rtdyld
/usr/bin/llvm-size
/usr/bin/llvm-split
/usr/bin/llvm-stress
/usr/bin/llvm-symbolizer
/usr/bin/llvm-tblgen
/usr/bin/obj2yaml
/usr/bin/opt
/usr/bin/sancov
/usr/bin/sanstats
/usr/bin/verify-uselistorder
/usr/bin/yaml2obj
/usr/lib/BugpointPasses.so
/usr/lib/LLVMHello.so
/usr/lib/cmake/llvm
/usr/lib/libLLVMAnalysis.a
/usr/lib/libLLVMAsmParser.a
/usr/lib/libLLVMAsmPrinter.a
/usr/lib/libLLVMBPFAsmPrinter.a
/usr/lib/libLLVMBPFCodeGen.a
/usr/lib/libLLVMBPFDesc.a
/usr/lib/libLLVMBPFInfo.a
/usr/lib/libLLVMBitReader.a
/usr/lib/libLLVMBitWriter.a
/usr/lib/libLLVMCodeGen.a
/usr/lib/libLLVMCore.a
/usr/lib/libLLVMCoverage.a
/usr/lib/libLLVMDebugInfoCodeView.a
/usr/lib/libLLVMDebugInfoDWARF.a
/usr/lib/libLLVMDebugInfoPDB.a
/usr/lib/libLLVMExecutionEngine.a
/usr/lib/libLLVMGlobalISel.a
/usr/lib/libLLVMIRReader.a
/usr/lib/libLLVMInstCombine.a
/usr/lib/libLLVMInstrumentation.a
/usr/lib/libLLVMInterpreter.a
/usr/lib/libLLVMLTO.a
/usr/lib/libLLVMLibDriver.a
/usr/lib/libLLVMLineEditor.a
/usr/lib/libLLVMLinker.a
/usr/lib/libLLVMMC.a
/usr/lib/libLLVMMCDisassembler.a
/usr/lib/libLLVMMCJIT.a
/usr/lib/libLLVMMCParser.a
/usr/lib/libLLVMMIRParser.a
/usr/lib/libLLVMObjCARCOpts.a
/usr/lib/libLLVMObject.a
/usr/lib/libLLVMObjectYAML.a
/usr/lib/libLLVMOption.a
/usr/lib/libLLVMOrcJIT.a
/usr/lib/libLLVMPasses.a
/usr/lib/libLLVMProfileData.a
/usr/lib/libLLVMRuntimeDyld.a
/usr/lib/libLLVMScalarOpts.a
/usr/lib/libLLVMSelectionDAG.a
/usr/lib/libLLVMSupport.a
/usr/lib/libLLVMSymbolize.a
/usr/lib/libLLVMTableGen.a
/usr/lib/libLLVMTarget.a
/usr/lib/libLLVMTransformUtils.a
/usr/lib/libLLVMVectorize.a
/usr/lib/libLLVMX86AsmParser.a
/usr/lib/libLLVMX86AsmPrinter.a
/usr/lib/libLLVMX86CodeGen.a
/usr/lib/libLLVMX86Desc.a
/usr/lib/libLLVMX86Disassembler.a
/usr/lib/libLLVMX86Info.a
/usr/lib/libLLVMX86Utils.a
/usr/lib/libLLVMipo.a
/usr/lib/libLTO.so
/usr/include/llvm



%clean
%{__rm} -rf %{buildroot}


%post


%changelog
