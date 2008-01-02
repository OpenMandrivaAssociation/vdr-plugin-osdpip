
%define plugin	osdpip
%define name	vdr-plugin-%plugin
%define version	0.0.8
%define rel	13

Summary:	VDR plugin: OSD Picture-in-Picture
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://www.magoa.net/linux/
Source:		http://www.magoa.net/linux/files/vdr-%plugin-%version.tar.bz2
Patch0:		osdpip-0.0.8-include.patch
Patch1:		vdr-osdpip-0.0.8-extra-qualification.patch
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	vdr-devel >= 1.4.1-6
BuildRequires:	libffmpeg-devel
Requires:	vdr-abi = %vdr_abi

%description
OSD Picture-in-Picture is a PlugIn that displays the current channel in a
small box on the screen (default upper right corner). You can switch up and
down now, watching the progress of the previous channel in the box. Quality is
not too good yet, and only I-Frames are displayed.
The plugin supports four modes:
- greyscaled (16 shades of grey)
- greyscaled (256 shades of grey)
- 256 colors with fixed palette
- 128 colors with variable palette
They all work with an ordinary vdr installation.
The plugin has the possibility to choose the PiP size (in the setup menu from
predefined sizes) and position (by moving it around using the cursor keys) as
well as crop dimensions.

%prep
%setup -q -n %plugin-%version

%patch0 -p1 -b .include
%patch1 -p1 -b .extra

%build
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


