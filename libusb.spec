#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libusb
Version  : 1.0.22
Release  : 22
URL      : https://sourceforge.net/projects/libusb/files/libusb-1.0/libusb-1.0.22/libusb-1.0.22.tar.bz2
Source0  : https://sourceforge.net/projects/libusb/files/libusb-1.0/libusb-1.0.22/libusb-1.0.22.tar.bz2
Summary  : C API for USB device access from Linux, Mac OS X, Windows, OpenBSD/NetBSD and Solaris userspace
Group    : Development/Tools
License  : LGPL-2.0+ LGPL-2.1
Requires: libusb-lib
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : systemd-dev
BuildRequires : systemd-dev32

%description
libusb is a library for USB device access from Linux, Mac OS X, Windows,
OpenBSD/NetBSD and Haiku userspace.  It is written in C (Haiku backend in C++)
and licensed under the GNU Lesser General Public License version 2.1 or, at
your option, any later version.

%package dev
Summary: dev components for the libusb package.
Group: Development
Requires: libusb-lib
Provides: libusb-devel

%description dev
dev components for the libusb package.


%package dev32
Summary: dev32 components for the libusb package.
Group: Default
Requires: libusb-lib32
Requires: libusb-dev

%description dev32
dev32 components for the libusb package.


%package lib
Summary: lib components for the libusb package.
Group: Libraries

%description lib
lib components for the libusb package.


%package lib32
Summary: lib32 components for the libusb package.
Group: Default

%description lib32
lib32 components for the libusb package.


%prep
%setup -q -n libusb-1.0.22
pushd ..
cp -a libusb-1.0.22 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1522108185
export CFLAGS="$CFLAGS -Os -fdata-sections -ffunction-sections -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -Os -fdata-sections -ffunction-sections -fno-semantic-interposition "
export FFLAGS="$CFLAGS -Os -fdata-sections -ffunction-sections -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -Os -fdata-sections -ffunction-sections -fno-semantic-interposition "
%configure --disable-static
make

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export CFLAGS="$CFLAGS -m32"
export CXXFLAGS="$CXXFLAGS -m32"
export LDFLAGS="$LDFLAGS -m32"
%configure --disable-static    --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make
popd
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 check

%install
export SOURCE_DATE_EPOCH=1522108185
rm -rf %{buildroot}
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/libusb-1.0/libusb.h
/usr/lib64/libusb-1.0.so
/usr/lib64/pkgconfig/libusb-1.0.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libusb-1.0.so
/usr/lib32/pkgconfig/32libusb-1.0.pc
/usr/lib32/pkgconfig/libusb-1.0.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libusb-1.0.so.0
/usr/lib64/libusb-1.0.so.0.1.0

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libusb-1.0.so.0
/usr/lib32/libusb-1.0.so.0.1.0
