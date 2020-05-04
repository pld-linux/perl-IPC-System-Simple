#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	IPC
%define		pnam	System-Simple
Summary:	IPC::System::Simple - Run commands simply, with detailed diagnostics
Summary(pl.UTF-8):	IPC::System::Simple - proste uruchamianie poleceń ze szczegółową diagnostyką
Name:		perl-IPC-System-Simple
Version:	1.30
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/IPC/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e68341fd958fd013b3521d909904f675
URL:		https://metacpan.org/release/IPC-System-Simple
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.30
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl-Scalar-List-Utils
BuildRequires:	perl-Test-Simple
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Calling Perl's in-built system() function is easy, determining if it
was successful is hard. Let's face it, $? isn't the nicest variable in
the world to play with, and even if you do check it, producing a
well-formatted error string takes a lot of work.

IPC::System::Simple takes the hard work out of calling external
commands. In fact, if you want to be really lazy, you can just write:

    use IPC::System::Simple qw(system);

and all of your system commands will either succeed (run to completion
and return a zero exit value), or die with rich diagnostic messages.

The IPC::System::Simple module also provides a simple replacement to
Perl's backticks operator.

%description -l pl.UTF-8
Wywołanie wbudowanej funkcji Perla system() jest łatwe, ale
stwierdzenie, czy się powiodło, jest trudne. $? nie jest najładniejszą
zmienną do obsługi, a nawet jeśli się ją sprawdzi, przygotowanie
dobrze sformatowanej informacji o błędzie wymaga dużo pracy.

IPC::System::Simple bierze na siebie tę ciężką pracę przy wywoływaniu
poleceń zewnętrznych. Będąc naprawdę leniwym, wystarczy napisać:

    use IPC::System::Simple qw(system);

i wszystkie wywołania systemowe albo się powiodą (zakończą i zwrócą
zerowy kod wyjścia), albo zakończą śmiercią ze szczegółowym
komunikatem diagnostycznym.

Moduł IPC::System::Simple udostępnia także prosty zamiennik operatora
Perla ``.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/IPC/System/Simple.pm
%{_mandir}/man3/IPC::System::Simple.3pm*
%{_examplesdir}/%{name}-%{version}
