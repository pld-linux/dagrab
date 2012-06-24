Summary:	Get *.wav files from audio cd's
Summary(pl):	Kopiuje sciezki audio do plikow *.wav
Name:		dagrab
Version:	0.3.5
Release:	1
License:	GPL
Group:		Applications/Sound
Group(pl):	Aplikacje/D�wi�k
Source0:	http://web.tiscalinet.it/marcellou/%{name}-%{version}.tar.gz
Patch0:		dagrab-fix_script.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
DAGRAB is a program for reading audio tracks from an IDE cdrom drive
into wav sound files.

%description -l pl
DAGRAB to program do zgrywania scie�ek audio z cdrom�w IDE do plik�w
wav.

%prep
%setup -q
%patch -p1

%build
make CFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install -s dagrab $RPM_BUILD_ROOT%{_bindir}
install dagmp3cd dagmp3enc $RPM_BUILD_ROOT%{_bindir}

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
