#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-MatchIt
Version  : 4.1.0
Release  : 27
URL      : https://cran.r-project.org/src/contrib/MatchIt_4.1.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/MatchIt_4.1.0.tar.gz
Summary  : Nonparametric Preprocessing for Parametric Causal Inference
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-MatchIt-lib = %{version}-%{release}
Requires: R-Rcpp
Requires: R-RcppProgress
Requires: R-backports
Requires: R-lmtest
Requires: R-sandwich
BuildRequires : R-Rcpp
BuildRequires : R-RcppProgress
BuildRequires : R-backports
BuildRequires : R-lmtest
BuildRequires : R-sandwich
BuildRequires : buildreq-R

%description
control groups with similar covariate distributions -- can be
    used to match exactly on covariates, to match on propensity
    scores, or perform a variety of other matching procedures.  The
    package also implements a series of recommendations offered in

%package lib
Summary: lib components for the R-MatchIt package.
Group: Libraries

%description lib
lib components for the R-MatchIt package.


%prep
%setup -q -c -n MatchIt
cd %{_builddir}/MatchIt

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1608160841

%install
export SOURCE_DATE_EPOCH=1608160841
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library MatchIt
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library MatchIt
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library MatchIt
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc MatchIt || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/MatchIt/CITATION
/usr/lib64/R/library/MatchIt/DESCRIPTION
/usr/lib64/R/library/MatchIt/INDEX
/usr/lib64/R/library/MatchIt/Meta/Rd.rds
/usr/lib64/R/library/MatchIt/Meta/data.rds
/usr/lib64/R/library/MatchIt/Meta/demo.rds
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
/usr/lib64/R/library/MatchIt/demo/analysis.R
/usr/lib64/R/library/MatchIt/demo/cem.R
/usr/lib64/R/library/MatchIt/demo/exact.R
/usr/lib64/R/library/MatchIt/demo/full.R
/usr/lib64/R/library/MatchIt/demo/genetic.R
/usr/lib64/R/library/MatchIt/demo/match.data.R
/usr/lib64/R/library/MatchIt/demo/nearest.R
/usr/lib64/R/library/MatchIt/demo/optimal.R
/usr/lib64/R/library/MatchIt/demo/subclass.R
/usr/lib64/R/library/MatchIt/doc/MatchIt.R
/usr/lib64/R/library/MatchIt/doc/MatchIt.Rmd
/usr/lib64/R/library/MatchIt/doc/MatchIt.html
/usr/lib64/R/library/MatchIt/doc/assessing-balance.R
/usr/lib64/R/library/MatchIt/doc/assessing-balance.Rmd
/usr/lib64/R/library/MatchIt/doc/assessing-balance.html
/usr/lib64/R/library/MatchIt/doc/estimating-effects.R
/usr/lib64/R/library/MatchIt/doc/estimating-effects.Rmd
/usr/lib64/R/library/MatchIt/doc/estimating-effects.html
/usr/lib64/R/library/MatchIt/doc/index.html
/usr/lib64/R/library/MatchIt/doc/matching-methods.R
/usr/lib64/R/library/MatchIt/doc/matching-methods.Rmd
/usr/lib64/R/library/MatchIt/doc/matching-methods.html
/usr/lib64/R/library/MatchIt/doc/sampling-weights.R
/usr/lib64/R/library/MatchIt/doc/sampling-weights.Rmd
/usr/lib64/R/library/MatchIt/doc/sampling-weights.html
/usr/lib64/R/library/MatchIt/figures/README-unnamed-chunk-2-1.png
/usr/lib64/R/library/MatchIt/figures/README-unnamed-chunk-2-2.png
/usr/lib64/R/library/MatchIt/figures/README-unnamed-chunk-4-1.png
/usr/lib64/R/library/MatchIt/figures/README-unnamed-chunk-6-1.png
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
/usr/lib64/R/library/MatchIt/include/MatchIt.h
/usr/lib64/R/library/MatchIt/include/MatchIt_RcppExports.h

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/MatchIt/libs/MatchIt.so
