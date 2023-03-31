Name:		texlive-buctthesis
Version:	64004
Release:	2
Summary:	Beijing University of Chemical Technology Thesis Template
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/buctthesis
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/buctthesis.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/buctthesis.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/buctthesis.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides a LaTeX class and template for Beijing
University of Chemical Technology, supporting bachelor, master,
and doctor theses.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/xelatex/buctthesis
%{_texmfdistdir}/tex/xelatex/buctthesis
%doc %{_texmfdistdir}/doc/xelatex/buctthesis

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
