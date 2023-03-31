Name:		texlive-gitfile-info
Version:	51928
Release:	2
Summary:	Get git metadata for a specific file
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/gitfile-info
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gitfile-info.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gitfile-info.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gitfile-info.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
If you are using git to control versions of LaTeX-files, you
may want to show yourself or other users or devs the current
version of the file, information about the author and last
edited date. All packages for git known make that kind of
information available for the whole repository. But sometimes
you have a lot of files within the same repository in different
versions, from different authors etc. Perhaps you also split up
a big project in small files and want to show within the
document who had edited what. This package gives you the
opportunity to do so.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/support/gitfile-info
%{_texmfdistdir}/tex/latex/gitfile-info
%doc %{_texmfdistdir}/doc/support/gitfile-info

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
