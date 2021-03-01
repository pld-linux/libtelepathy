Summary:	A GLib library to ease writing telepathy clients
Summary(pl.UTF-8):	Biblioteka oparta na GLib dla aplikacji służących do komunikacji
Name:		libtelepathy
Version:	0.3.3
Release:	5
License:	LGPL v2.1+
Group:		Libraries
Source0:	https://telepathy.freedesktop.org/releases/libtelepathy/%{name}-%{version}.tar.gz
# Source0-md5:	490ca1a0c614d4466394b72d43bf7370
Patch0:		%{name}-makefile.patch
URL:		https://telepathy.freedesktop.org/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.8
BuildRequires:	dbus-devel >= 0.93
BuildRequires:	dbus-glib-devel >= 0.73
BuildRequires:	glib2-devel >= 1:2.10
BuildRequires:	libtool
BuildRequires:	libxslt-progs
BuildRequires:	pkgconfig
BuildRequires:	python >= 2.3
BuildRequires:	python-modules >= 2.3
BuildRequires:	telepathy-glib-devel >= 0.7.3
Requires:	dbus-libs >= 0.93
Requires:	dbus-glib >= 0.73
Requires:	glib2 >= 1:2.10
Requires:	telepathy-glib >= 0.7.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libtelepathy is a D-Bus framework for unifying real time
communication, including instant messaging, voice calls and video
calls. It abstracts differences between protocols to provide a unified
interface for applications.

%description -l pl.UTF-8
libtelepathy jest szkieletem opartym na D-Bus ujednolicającym
komunikację w czasie rzeczywistym, włączając w to komunikatory
oraz komunikację głosową i za pośrednictwem wideo. Zasłania
warstwą abstrakcji różnice pomiędzy protokołami dostarczając
jednolity interfejs dla aplikacji.

%package devel
Summary:	Header files for libtelepathy library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libtelepathy
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	dbus-devel >= 0.93
Requires:	dbus-glib-devel >= 0.73
Requires:	glib2-devel >= 1:2.10
Requires:	telepathy-glib-devel >= 0.7.3

%description devel
Header files for libtelepathy library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libtelepathy.

%package static
Summary:	Static libtelepathy library
Summary(pl.UTF-8):	Statyczna biblioteka libtelepathy
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libtelepathy library.

%description static -l pl.UTF-8
Statyczna biblioteka libtelepathy.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libtelepathy.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libtelepathy.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtelepathy.so.2

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libtelepathy.so
%{_includedir}/telepathy-1.0/libtelepathy
%{_pkgconfigdir}/libtelepathy.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libtelepathy.a
