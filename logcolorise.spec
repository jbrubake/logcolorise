%define ver      1.0.7
%define rel      1
%define prefix   /usr/local

Summary: A context highlighter for syslog log files.
Name: logcolorise
Version: %ver
Release: %rel
Source: logcolorise-%ver.tar.gz
URL: http://www.linuxsupportline.com/~pgp/linux/linux.html#Scripts
Copyright: GPL
Group: Applications/Text
Packager: Michael T. Babcock <mikebabcock@pobox.com>

%description
LogColoriser is a PERL script that takes a syslog generated log
as it's STDIN and creates ANSI context-highlighted output that
looks much nicer than the original.

%prep
%setup
%build
%install

%files 
%doc AUTHORS COPYING ChangeLog README THANKS TODO
%{prefix}/bin/logcolorise.pl
