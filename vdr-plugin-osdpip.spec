
%define plugin	osdpip
%define name	vdr-plugin-%plugin
%define version	0.0.9
%define rel	1

Summary:	VDR plugin: OSD Picture-in-Picture
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://www.magoa.net/linux/
Source:		http://home.arcor.de/andreas.regel/files/vdr-%plugin-%version.tgz
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	vdr-devel >= 1.6.0
BuildRequires:	libffmpeg-devel
Requires:	vdr-abi = %vdr_abi

%description
OSD Picture-in-Picture is a PlugIn that displays the current channel in a
small box on the screen (default upper right corner). You can switch up and
down now, watching the progress of the previous channel in the box.

%prep
%setup -q -n %plugin-%version
%vdr_plugin_prep

%build
# needed for build on 2009.0:
ln -sf %{_includedir}/libavcodec ffmpeg
# needed for build on 2008.1:
VDR_PLUGIN_FLAGS="%vdr_plugin_flags -I$(pkg-config --cflags libavcodec)"
%vdr_plugin_build

%install
rm -rf %{buildroot}
%vdr_plugin_install

%clean
rm -rf %{buildroot}

%post
%vdr_plugin_post %plugin

%postun
%vdr_plugin_postun %plugin

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README COPYING HISTORY TODO


