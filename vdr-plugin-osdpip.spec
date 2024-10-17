
%define plugin	osdpip
%define name	vdr-plugin-%plugin
%define version	0.1.0
%define rel	1

Summary:	VDR plugin: OSD Picture-in-Picture
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		https://projects.vdr-developer.org/projects/show/plg-osdpip
Source:		http://projects.vdr-developer.org/attachments/download/267/vdr-%plugin-%version.tgz
Patch0:		osdpip-recent-ffmpeg.patch
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	vdr-devel >= 1.6.0-7
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
VDR_PLUGIN_EXTRA_FLAGS="-D__STDC_CONSTANT_MACROS"
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


