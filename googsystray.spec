Summary:	System tray app for Google Voice, GMail, Google Calendar, Google Reader, and Google Wave
Summary(hu.UTF-8):	Rendszertálca alkalmazás a Google Voice, GMail, Google Calendar, Google Reader és Google Wave oldalakhoz
Name:		googsystray
Version:	1.3.1
Release:	1
License:	GPL v3
Group:		Applications
Source0:	http://downloads.sourceforge.net/project/googsystray/%{name}-%{version}/googsystray-%{version}.tar.gz
# Source0-md5:	437e8f398dc6a11809a066f10d0c0a9f
URL:		http://googsystray.sourceforge.net/
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-devel-tools
Requires:	python-gnome-desktop-keyring
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Googsystray is a system tray app for Google Voice, GMail, Google
Calendar, Google Reader, and Google Wave.

%description -l hu.UTF-8
Googsystray egy rendszertálca alkalmazás a Google Voice, GMail, Google
Calendar, Google Reader és Google Wave oldalakhoz.

%prep
%setup -q

%build
%{__python} setup.py build \
	--executable %{__python}

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--optimize=2 \
	--root $RPM_BUILD_ROOT

%py_postclean

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc CREDITS CHANGELOG TODO
%attr(755,root,root) %{_bindir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_desktopdir}/%{name}-settings.desktop
%{_iconsdir}/%{name}.png
%{_iconsdir}/hicolor/*/apps/googsystray.png
%{py_sitescriptdir}/*.egg-info
%{py_sitescriptdir}/%{name}
