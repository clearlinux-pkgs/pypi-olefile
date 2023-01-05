#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-olefile
Version  : 0.46
Release  : 56
URL      : https://files.pythonhosted.org/packages/34/81/e1ac43c6b45b4c5f8d9352396a14144bba52c8fec72a80f425f6a4d653ad/olefile-0.46.zip
Source0  : https://files.pythonhosted.org/packages/34/81/e1ac43c6b45b4c5f8d9352396a14144bba52c8fec72a80f425f6a4d653ad/olefile-0.46.zip
Summary  : Python package to parse, read and write Microsoft OLE2 files (Structured Storage or Compound Document, Microsoft Office)
Group    : Development/Tools
License  : BSD-2-Clause BSD-3-Clause
Requires: pypi-olefile-license = %{version}-%{release}
Requires: pypi-olefile-python = %{version}-%{release}
Requires: pypi-olefile-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
=======
        
        |Build Status TravisCI| |Build Status AppVeyor| |Coverage Status|
        |Documentation Status| |PyPI| |Can I Use Python 3?| |Say Thanks!|

%package license
Summary: license components for the pypi-olefile package.
Group: Default

%description license
license components for the pypi-olefile package.


%package python
Summary: python components for the pypi-olefile package.
Group: Default
Requires: pypi-olefile-python3 = %{version}-%{release}

%description python
python components for the pypi-olefile package.


%package python3
Summary: python3 components for the pypi-olefile package.
Group: Default
Requires: python3-core
Provides: pypi(olefile)

%description python3
python3 components for the pypi-olefile package.


%prep
%setup -q -n olefile-0.46
cd %{_builddir}/olefile-0.46
pushd ..
cp -a olefile-0.46 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1672294727
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-olefile
cp %{_builddir}/olefile-%{version}/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-olefile/39139a785b98452f34e53f1dd9916f6a6d0a8ebf || :
cp %{_builddir}/olefile-%{version}/doc/License.rst %{buildroot}/usr/share/package-licenses/pypi-olefile/b26f237ee1e7c24a2f98969fee5228ce94b4d8b7 || :
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-olefile/39139a785b98452f34e53f1dd9916f6a6d0a8ebf
/usr/share/package-licenses/pypi-olefile/b26f237ee1e7c24a2f98969fee5228ce94b4d8b7

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
