%global debug_package %{nil}

Name:           chrome-gnome-shell
Version:        10.1
Release:        14%{?dist}
Summary:        Support for managing GNOME Shell Extensions through web browsers

License:        GPLv3+
URL:            https://wiki.gnome.org/Projects/GnomeShellIntegrationForChrome
Source0:        https://download.gnome.org/sources/%{name}/%{version}/%{name}-%{version}.tar.xz

# Backported from upstream
Patch0:         0001-build-Install-icons-in-hicolor-theme.patch

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  python3-devel
BuildRequires:  /usr/bin/base64
BuildRequires:  /usr/bin/head
BuildRequires:  /usr/bin/jq
BuildRequires:  /usr/bin/sha256sum
BuildRequires:  /usr/bin/tr

Requires:       dbus
Requires:       gnome-shell
Requires:       hicolor-icon-theme
Requires:       mozilla-filesystem
Requires:       python3-gobject-base
Requires:       python3-requests

%description
Browser extension for Google Chrome/Chromium, Firefox, Vivaldi, Opera (and
other Browser Extension, Chrome Extension or WebExtensions capable browsers)
and native host messaging connector that provides integration with GNOME Shell
and the corresponding extensions repository https://extensions.gnome.org.

%prep
%autosetup -p1

%build
%cmake -DBUILD_EXTENSION=OFF \
    -DCMAKE_INSTALL_LIBDIR=%{_lib} \
    -DPython_ADDITIONAL_VERSIONS=3
%cmake_build

%install
%cmake_install

%check
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/org.gnome.ChromeGnomeShell.desktop

%files
%license LICENSE
%{_sysconfdir}/chromium/
%{_sysconfdir}/opt/chrome/
%{_bindir}/chrome-gnome-shell
%{_libdir}/mozilla/native-messaging-hosts/
%{python3_sitelib}/chrome_gnome_shell-*.egg-info
%{_datadir}/applications/org.gnome.ChromeGnomeShell.desktop
%{_datadir}/dbus-1/services/org.gnome.ChromeGnomeShell.service
%{_datadir}/icons/hicolor/*/apps/org.gnome.ChromeGnomeShell.png

%changelog
* Mon Aug 09 2021 Mohan Boddu <mboddu@redhat.com> - 10.1-14
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Thu Apr 15 2021 Mohan Boddu <mboddu@redhat.com> - 10.1-13
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Fri Feb 05 2021 Kalev Lember <klember@redhat.com> - 10.1-12
- Install icons into hicolor icon theme

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 10.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 10.1-10
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 10.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 10.1-8
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 10.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 10.1-6
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 10.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 10.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 10.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 10.1-2
- Rebuilt for Python 3.7

* Wed Apr 04 2018 Pete Walter <pwalter@fedoraproject.org> - 10.1-1
- Update to 10.1

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 22 2017 Pete Walter <pwalter@fedoraproject.org> - 9-1
- Update to 9

* Fri Mar 10 2017 Pete Walter <pwalter@fedoraproject.org> - 8.2-2
- Package review fixes (#1343710)
- Validate the desktop file
- Don't own /etc/opt directory
- Depend on mozilla-filesystem instead of co-owning mozilla directories
- Depend on dbus and gnome-icon-theme/hicolor-icon-theme for directory
  ownership

* Fri Mar 03 2017 Pete Walter <pwalter@fedoraproject.org> - 8.2-1
- Update to 8.2
- Simplify files list
- Build with Python 3 (#1343710)
- Add missing python3-requests dependency (#1343710)
- Update package description

* Tue Jun 07 2016 Pete Walter <pwalter@fedoraproject.org> - 6.1-1
- Update to 6.1

* Sat May 14 2016 Maxim Orlov <murmansksity@gmail.com> - 6-1
- Update to Ver.6
- Fix "orphaned directory"

* Mon Apr 11 2016 Maxim Orlov <murmansksity@gmail.com> - 5.2-1
- Initial package.
