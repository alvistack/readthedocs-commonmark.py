# Copyright 2025 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-commonmark
Epoch: 100
Version: 0.9.1
Release: 1%{?dist}
BuildArch: noarch
Summary: Python CommonMark parser
License: BSD-3-Clause
URL: https://github.com/readthedocs/commonmark.py/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
commonmark.py is a pure Python port of jgm's commonmark.js, a Markdown
parser and renderer for the CommonMark specification, using only native
modules. Once both this project and the CommonMark specification are
stable we will release the first 1.0 version and attempt to keep up to
date with changes in commonmark.js.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-CommonMark
Summary: Python CommonMark parser
Requires: python3
Provides: python3-CommonMark = %{epoch}:%{version}-%{release}
Provides: python3-commonmark = %{epoch}:%{version}-%{release}
Provides: python3dist(commonmark) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-commonmark = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(commonmark) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-commonmark = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(commonmark) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-CommonMark
commonmark.py is a pure Python port of jgm's commonmark.js, a Markdown
parser and renderer for the CommonMark specification, using only native
modules. Once both this project and the CommonMark specification are
stable we will release the first 1.0 version and attempt to keep up to
date with changes in commonmark.js.

%files -n python%{python3_version_nodots}-CommonMark
%license LICENSE
%{_bindir}/*
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500)
%package -n python3-CommonMark
Summary: Python CommonMark parser
Requires: python3
Provides: python3-commonmark = %{epoch}:%{version}-%{release}
Provides: python3dist(commonmark) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-commonmark = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(commonmark) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-commonmark = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(commonmark) = %{epoch}:%{version}-%{release}

%description -n python3-CommonMark
commonmark.py is a pure Python port of jgm's commonmark.js, a Markdown
parser and renderer for the CommonMark specification, using only native
modules. Once both this project and the CommonMark specification are
stable we will release the first 1.0 version and attempt to keep up to
date with changes in commonmark.js.

%files -n python3-CommonMark
%license LICENSE
%{_bindir}/*
%{python3_sitelib}/*
%endif

%changelog
