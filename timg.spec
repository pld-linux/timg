Summary:	A user-friendly viewer for terminals
Summary(pl.UTF-8):	Przeglądarka obrazków na terminal
Name:		timg
Version:	1.4.2
Release:	1
License:	GPL v2
Group:		Applications/Graphics
Source0:	https://github.com/hzeller/timg/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	1d0e05483125911bae1fda09a1159317
URL:		https://timg.sh/
BuildRequires:	GraphicsMagick-c++-devel
BuildRequires:	cmake
BuildRequires:	ffmpeg-devel
BuildRequires:	libjpeg-turbo-devel
BuildRequires:	ninja
BuildRequires:	openslide-devel
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libX11-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A user-friendly viewer that uses 24-Bit color capabilities and unicode
character blocks to display images, animations and videos in the
terminal.

%description -l pl.UTF-8
Przyjazna użytkownikowi przeglądarka obrazków, który korzysta z
24-bitowego koloru i unikodowych znaków bloków, żeby wyświetlać
obrazki, animacje i wideo na terminalu.

%prep
%setup -q

%build
install -d build
cd build
%cmake -G Ninja \
	../
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/timg
%{_mandir}/man1/timg.1*
