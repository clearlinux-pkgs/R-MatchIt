#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v21
# autospec commit: f4a13a5
#
Name     : R-MatchIt
Version  : 4.7.0
Release  : 59
URL      : https://ftp.osuosl.org/pub/cran/src/contrib/MatchIt_4.7.0.tar.gz
Source0  : https://ftp.osuosl.org/pub/cran/src/contrib/MatchIt_4.7.0.tar.gz
Summary  : Nonparametric Preprocessing for Parametric Causal Inference
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-MatchIt-lib = %{version}-%{release}
Requires: R-Rcpp
Requires: R-RcppProgress
Requires: R-backports
Requires: R-chk
Requires: R-rlang
BuildRequires : R-Rcpp
BuildRequires : R-RcppProgress
BuildRequires : R-backports
BuildRequires : R-chk
BuildRequires : R-rlang
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
control groups with similar covariate distributions -- can be
    used to match exactly on covariates, to match on propensity
    scores, or perform a variety of other matching procedures.  The
    package also implements a series of recommendations offered in

%package dev
Summary: dev components for the R-MatchIt package.
Group: Development
Requires: R-MatchIt-lib = %{version}-%{release}
Provides: R-MatchIt-devel = %{version}-%{release}
Requires: R-MatchIt = %{version}-%{release}

%description dev
dev components for the R-MatchIt package.


%package lib
Summary: lib components for the R-MatchIt package.
Group: Libraries

%description lib
lib components for the R-MatchIt package.


%prep
%setup -q -n MatchIt
pushd ..
cp -a MatchIt buildavx2
popd
pushd ..
cp -a MatchIt buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1736783706

%install
export SOURCE_DATE_EPOCH=1736783706
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/MatchIt/CITATION
/usr/lib64/R/library/MatchIt/DESCRIPTION
/usr/lib64/R/library/MatchIt/INDEX
/usr/lib64/R/library/MatchIt/Meta/Rd.rds
/usr/lib64/R/library/MatchIt/Meta/data.rds
/usr/lib64/R/library/MatchIt/Meta/features.rds
/usr/lib64/R/library/MatchIt/Meta/hsearch.rds
/usr/lib64/R/library/MatchIt/Meta/links.rds
/usr/lib64/R/library/MatchIt/Meta/nsInfo.rds
/usr/lib64/R/library/MatchIt/Meta/package.rds
/usr/lib64/R/library/MatchIt/Meta/vignette.rds
/usr/lib64/R/library/MatchIt/NAMESPACE
/usr/lib64/R/library/MatchIt/NEWS.md
/usr/lib64/R/library/MatchIt/R/MatchIt
/usr/lib64/R/library/MatchIt/R/MatchIt.rdb
/usr/lib64/R/library/MatchIt/R/MatchIt.rdx
/usr/lib64/R/library/MatchIt/data/Rdata.rdb
/usr/lib64/R/library/MatchIt/data/Rdata.rds
/usr/lib64/R/library/MatchIt/data/Rdata.rdx
/usr/lib64/R/library/MatchIt/doc/MatchIt.Rmd
/usr/lib64/R/library/MatchIt/doc/MatchIt.html
/usr/lib64/R/library/MatchIt/doc/assessing-balance.Rmd
/usr/lib64/R/library/MatchIt/doc/assessing-balance.html
/usr/lib64/R/library/MatchIt/doc/estimating-effects.Rmd
/usr/lib64/R/library/MatchIt/doc/estimating-effects.html
/usr/lib64/R/library/MatchIt/doc/index.html
/usr/lib64/R/library/MatchIt/doc/matching-methods.Rmd
/usr/lib64/R/library/MatchIt/doc/matching-methods.html
/usr/lib64/R/library/MatchIt/doc/sampling-weights.Rmd
/usr/lib64/R/library/MatchIt/doc/sampling-weights.html
/usr/lib64/R/library/MatchIt/help/AnIndex
/usr/lib64/R/library/MatchIt/help/MatchIt.rdb
/usr/lib64/R/library/MatchIt/help/MatchIt.rdx
/usr/lib64/R/library/MatchIt/help/aliases.rds
/usr/lib64/R/library/MatchIt/help/figures/README-unnamed-chunk-4-1.png
/usr/lib64/R/library/MatchIt/help/figures/README-unnamed-chunk-5-1.png
/usr/lib64/R/library/MatchIt/help/figures/README-unnamed-chunk-6-1.png
/usr/lib64/R/library/MatchIt/help/figures/logo.png
/usr/lib64/R/library/MatchIt/help/macros/macros.Rd
/usr/lib64/R/library/MatchIt/help/paths.rds
/usr/lib64/R/library/MatchIt/html/00Index.html
/usr/lib64/R/library/MatchIt/html/R.css

%files dev
%defattr(-,root,root,-)
/usr/lib64/R/library/MatchIt/include/MatchIt.h
/usr/lib64/R/library/MatchIt/include/MatchIt_RcppExports.h

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/R/library/MatchIt/libs/MatchIt.so
/V4/usr/lib64/R/library/MatchIt/libs/MatchIt.so
/usr/lib64/R/library/MatchIt/libs/MatchIt.so
