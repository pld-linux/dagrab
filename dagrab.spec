Summary:	Get *.wav files from audio cd's.
Summary(pl):	Kopiuje sciezki audio do plikow *.wav.
Name:		dagrab
Version:	0.3.5
Release:	1
License:	GPL
Group:		Application/Sound
Group(pl):	Aplikacje/D¼wiêk
Source: 	http://web.tiscalinet.it:/marcellou/dagrab-%{version}.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
DAGRAB is a  program for reading audio tracks from an IDE cdrom drive into wav
sound files.

%description -l pl
DAGRAB to program do zgrywania scie¿ek audio z cdromów IDE do plików wav.

%prep
%setup -q

%build
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_defaultdocdir}/%{name}}

install -s %{name} $RPM_BUILD_ROOT%{_bindir}
install -s dagmp3cd $RPM_BUILD_ROOT%{_bindir}
install -s dagmp3enc $RPM_BUILD_ROOT%{_bindir}

install dagrab.1 $RPM_BUILD_ROOT%{_mandir}/man1

gzip -9nf README INSTALL *.lsm \
	$RPM_BUILD_ROOT%{_mandir}/man1/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%doc *.gz 
%{_mandir}/man1/*
