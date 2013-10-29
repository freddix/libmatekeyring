Summary:	Framework for managing passwords and other secrets
Name:		libmatekeyring
Version:	1.6.0
Release:	1
License:	LGPL v2+/GPL v2+
Group:		Libraries
Source0:	http://pub.mate-desktop.org/releases/1.6/%{name}-%{version}.tar.xz
# Source0-md5:	f2f5408aca0cc0f9b914f3a910fcb5c8
URL:		http://wiki.mate-desktop.org/libmatekeyring
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dbus-devel
BuildRequires:	gettext-devel
BuildRequires:	libgcrypt-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The library libmatekeyring is used by applications to integrate with
the MATE keyring system.

%package devel
Summary:	Headers for MATE keyring library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	dbus-devel

%description devel
Headers for MATE keyring library.

%package apidocs
Summary:	MATE keyring API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
MATE keyring API documentation.

%prep
%setup -q

%build
%{__gtkdocize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules		\
	--disable-static		\
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %ghost %{_libdir}/libmate-keyring.so.?
%attr(755,root,root) %{_libdir}/libmate-keyring.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmate-keyring.so
%{_includedir}/mate-keyring-1
%{_pkgconfigdir}/mate-keyring-1.pc

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/mate-keyring

