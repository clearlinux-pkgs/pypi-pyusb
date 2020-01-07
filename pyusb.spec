#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x084C5584542E1574 (wcosta@mozilla.com)
#
Name     : pyusb
Version  : 1.0.2
Release  : 5
URL      : https://files.pythonhosted.org/packages/5f/34/2095e821c01225377dda4ebdbd53d8316d6abb243c9bee43d3888fa91dd6/pyusb-1.0.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/5f/34/2095e821c01225377dda4ebdbd53d8316d6abb243c9bee43d3888fa91dd6/pyusb-1.0.2.tar.gz
Source99 : https://files.pythonhosted.org/packages/5f/34/2095e821c01225377dda4ebdbd53d8316d6abb243c9bee43d3888fa91dd6/pyusb-1.0.2.tar.gz.asc
Summary  : Python USB access module
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pyusb-license = %{version}-%{release}
Requires: pyusb-python = %{version}-%{release}
Requires: pyusb-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
=======================================
PyUSB 1.0 - Easy USB access from Python
=======================================

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

%description python3
python3 components for the pyusb package.


%prep
%setup -q -n pyusb-1.0.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1549216182
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pyusb
cp LICENSE %{buildroot}/usr/share/package-licenses/pyusb/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pyusb/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
