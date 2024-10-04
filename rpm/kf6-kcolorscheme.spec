%global  kf_version 6.6.0

Name:    kf6-kcolorscheme
Version: 6.6.0
Release: 0%{?dist}
Summary: Classes to read and interact with KColorScheme
License: BSD-2-Clause and CC0-1.0 and LGPL-2.0-or-later and LGPL-2.1-only and LGPL-3.0-only and (LGPL-2.1-only OR LGPL-3.0-only)
URL:     https://invent.kde.org/frameworks/kcolorscheme
Source0:    %{name}-%{version}.tar.bz2

BuildRequires:  kf6-extra-cmake-modules >= %{kf_version}
BuildRequires:  clang
BuildRequires:  cmake
BuildRequires:	kf6-rpm-macros
BuildRequires:  kf6-kconfig-devel
BuildRequires:  kf6-kguiaddons-devel
BuildRequires:  kf6-ki18n-devel
BuildRequires:  qt6-qtdeclarative-devel
BuildRequires:  qt6-qttools-devel
BuildRequires:  pkgconfig(xkbcommon)


%description
%summary.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%prep
%autosetup -n %{name}-%{version}/upstream -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang kcolorscheme6 --all-name

%files -f kcolorscheme6.lang
%doc README.md
%license LICENSES/*
%{_kf6_datadir}/qlogging-categories6/kcolorscheme.categories
%{_kf6_libdir}/libKF6ColorScheme.so.*

%files devel
%{_kf6_includedir}/KColorScheme
%{_kf6_libdir}/cmake/KF6ColorScheme
%{_kf6_libdir}/libKF6ColorScheme.so
%{_qt6_docdir}/*.tags

%files doc
%{_qt6_docdir}/*.qch
