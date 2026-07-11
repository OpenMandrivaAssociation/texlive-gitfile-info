%global tl_name gitfile-info
%global tl_revision 79121

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.5
Release:	%{tl_revision}.1
Summary:	Get git metadata for a specific file
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/support/gitfile-info
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gitfile-info.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gitfile-info.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gitfile-info.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
If you are using git to control versions of LaTeX-files, you may want to
show yourself or other users or devs the current version of the file,
information about the author and last edited date. All packages for git
known make that kind of information available for the whole repository.
But sometimes you have a lot of files within the same repository in
different versions, from different authors etc. Perhaps you also split
up a big project in small files and want to show within the document who
had edited what. This package gives you the opportunity to do so.

