Summary:	Get *.WAV files from audio cd's
Summary(pl):	Kopiuje scie¿ki audio do plików *.WAV
Name:		dagrab
Version:	0.3.5
Release:	1
License:	GPL
Group:		Applications/Sound
Source0:	http://web.tiscalinet.it/marcellou/%{name}-%{version}.tar.gz
# Source0-md5:	96e77ffddad5c8f63d4e411f4e033d14
Patch0:		%{name}-fix_script.patch
URL:		http://web.tiscali.it/marcellou/dagrab.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DAGRAB is a program for reading audio tracks from an IDE cdrom drive
into WAV sound files.

%description -l pl
DAGRAB to program do zgrywania ¶cie¿ek audio z cdromów IDE do plików
WAV.

%prep
%setup -q
%patch -p1

%build
%{__make} CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install dagrab $RPM_BUILD_ROOT%{_bindir}
install dagmp3cd dagmp3enc $RPM_BUILD_ROOT%{_bindir}

install dagrab.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%doc README INSTALL *.lsm
%{_mandir}/man1/*
