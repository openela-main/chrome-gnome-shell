%global debug_package %{nil}
%global source_name gnome-browser-connector

Name:           chrome-gnome-shell
Version:        42.1
Release:        1%{?dist}
Summary:        Support for managing GNOME Shell Extensions through web browsers

License:        GPLv3+
URL:            https://gitlab.gnome.org/GNOME/%{source_name}
Source0:        https://download.gnome.org/sources/%{source_name}/42/%{source_name}-%{version}.tar.xz

BuildRequires:  desktop-file-utils
BuildRequires:  meson
BuildRequires:  python3-devel
BuildRequires:  python3-gobject-base

Requires:       dbus
Requires:       gnome-shell
Requires:       hicolor-icon-theme
Requires:       mozilla-filesystem
Requires:       python3-gobject-base

Patch1: 0001-Don-t-use-enhanced-annotations.patch

%description
Browser extension for Google Chrome/Chromium, Firefox, Vivaldi, Opera (and
other Browser Extension, Chrome Extension or WebExtensions capable browsers)
and native host messaging connector that provides integration with GNOME Shell
and the corresponding extensions repository https://extensions.gnome.org.

%prep
%autosetup -p1 -n %{source_name}-%{version}

%build
%meson
%meson_build

%install
%meson_install

%check
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/org.gnome.BrowserConnector.desktop

%files
%license LICENSE
%doc NEWS README.md
%{_sysconfdir}/chromium/
%{_sysconfdir}/opt/chrome/
%{_bindir}/gnome-browser-connector
%{_bindir}/gnome-browser-connector-host
%{python3_sitelib}/gnome_browser_connector/
%{_libdir}/mozilla/native-messaging-hosts/
%{_datadir}/applications/org.gnome.BrowserConnector.desktop
%{_datadir}/dbus-1/services/org.gnome.BrowserConnector.service
%{_datadir}/icons/hicolor/*/apps/org.gnome.BrowserConnector.png

%changelog
* Wed May 17 2023 Florian Müllner <fmuellner@redhat.com> - 42.1-1
- Update to gnome-browser-connector-42.1
  Resolves: #2209628

* Mon Jan 25 2021 Florian Müllner <fmuellner@redhat.com> - 10.1-7
- Disable updates support
  Resolves: #1802105

* Fri Jul 12 2019 Florian Müllner <fmuellner@redhat.com> - 10.1-6
- Install icons in 'hicolor' instead of 'gnome'
  Related: #1694203

* Thu Jul 12 2019 Tomas Pelka <tpelka@redhat.com> - 10.1-5
- bump release num to correctly start gating process

  Related: #1694203

* Thu Jul 11 2019 Florian Müllner <fmuellner@redhat.com> - 10.1-4
- Adjust Fedora spec to build on RHEL:
  - build missing BuildRequire

  Related: #1694203

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
