Summary:	Get *.wav files from audio cd's
Summary(pl):	Kopiuje sciezki audio do plikow *.wav
Name:		dagrab
Version:	0.3.5
Release:	1
License:	GPL
Group:		Applications/Sound
Source0:	http://web.tiscalinet.it/marcellou/%{name}-%{version}.tar.gz
Patch0:		%{name}-fix_script.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DAGRAB is a program for reading audio tracks from an IDE cdrom drive
into wav sound files.

%description -l pl
DAGRAB to program do zgrywania scie¿ek audio z cdromów IDE do plików
wav.

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
