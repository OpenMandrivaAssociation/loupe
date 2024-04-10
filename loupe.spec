%define _empty_manifest_terminate_build 0

Name:           loupe
Version:        46.2
Release:        1
Summary:        A simple image viewer application
License:        GPL-3.0-or-later
URL:            https://gitlab.gnome.org/GNOME/loupe
Source0:        https://download.gnome.org/sources/loupe/45/loupe-%{version}.tar.xz
#Source2:        vendor.tar.xz
#Source3:        cargo_config

BuildRequires:  appstream-util
BuildRequires:  cargo
BuildRequires:  meson itstool
BuildRequires:  gettext
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gtk4) >= 4.10
BuildRequires:  pkgconfig(gweather4) >= 4.0.0
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libadwaita-1) >= 1.3.99
#BuildRequires:  pkgconfig(libheif) >= 1.14.2
BuildRequires:  pkgconfig(libssh2)
BuildRequires:  pkgconfig(libseccomp)

Requires:       glycin-loaders

%description
%{summary} written with GTK4 and Rust.

%prep
%autosetup -p1 
#-a2
#mkdir .cargo
#cp %{SOURCE3} .cargo/config

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name} %{?no_lang_C}

%files -f %{name}.lang
%license COPYING.md
%doc README.md
%doc %{_datadir}/help/*/loupe/
%{_bindir}/%{name}
%{_datadir}/applications/org.gnome.Loupe.desktop
%{_datadir}/dbus-1/services/org.gnome.Loupe.service
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.Loupe.Devel.svg
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.Loupe.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.Loupe-symbolic.svg
%{_datadir}/metainfo/org.gnome.Loupe.metainfo.xml
%{_datadir}/glib-2.0/schemas/org.gnome.Loupe.gschema.xml
