#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pyusb
Version  : 1.1.1
Release  : 15
URL      : https://files.pythonhosted.org/packages/b9/8d/25c4e446a07e918eb39b5af25c4a83a89db95ae44e4ed5a46c3c53b0a4d6/pyusb-1.1.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/b9/8d/25c4e446a07e918eb39b5af25c4a83a89db95ae44e4ed5a46c3c53b0a4d6/pyusb-1.1.1.tar.gz
Summary  : Python USB access module
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pyusb-license = %{version}-%{release}
Requires: pyusb-python = %{version}-%{release}
Requires: pyusb-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : setuptools
BuildRequires : setuptools_scm-python
BuildRequires : tox
BuildRequires : virtualenv

%description
PyUSB offers easy USB devices communication in Python.
        It should work without additional code in any environment with
        Python >= 2.4, ctypes and a pre-built USB backend library

%package license
Summary: license components for the pyusb package.
Group: Default

%description license
license components for the pyusb package.


%package python
Summary: python components for the pyusb package.
Group: Default
Requires: pyusb-python3 = %{version}-%{release}

%description python
python components for the pyusb package.


%package python3
Summary: python3 components for the pyusb package.
Group: Default
Requires: python3-core
Provides: pypi(pyusb)

%description python3
python3 components for the pyusb package.


%prep
%setup -q -n pyusb-1.1.1
cd %{_builddir}/pyusb-1.1.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1611173140
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pyusb
cp %{_builddir}/pyusb-1.1.1/LICENSE %{buildroot}/usr/share/package-licenses/pyusb/db7a78de40a2b6d5a57d10bbb3d3e0ad89b1f9c6
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pyusb/db7a78de40a2b6d5a57d10bbb3d3e0ad89b1f9c6

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
