#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-forcats
Version  : 0.3.0
Release  : 6
URL      : https://cran.r-project.org/src/contrib/forcats_0.3.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/forcats_0.3.0.tar.gz
Summary  : Tools for Working with Categorical Variables (Factors)
Group    : Development/Tools
License  : GPL-3.0
Requires: R-rlang
Requires: R-tibble
BuildRequires : R-rlang
BuildRequires : R-tibble
BuildRequires : clr-R-helpers

%description
specified levels to front, ordering by first appearance, reversing, and
    randomly shuffling), and tools for modifying factor levels (including
    collapsing rare levels into other, 'anonymising', and manually 'recoding').

%prep
%setup -q -c -n forcats

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1521248978

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1521248978
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
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
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library forcats
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library forcats
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library forcats
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library forcats|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/forcats/DESCRIPTION
/usr/lib64/R/library/forcats/INDEX
/usr/lib64/R/library/forcats/Meta/Rd.rds
/usr/lib64/R/library/forcats/Meta/data.rds
/usr/lib64/R/library/forcats/Meta/features.rds
/usr/lib64/R/library/forcats/Meta/hsearch.rds
/usr/lib64/R/library/forcats/Meta/links.rds
/usr/lib64/R/library/forcats/Meta/nsInfo.rds
/usr/lib64/R/library/forcats/Meta/package.rds
/usr/lib64/R/library/forcats/NAMESPACE
/usr/lib64/R/library/forcats/NEWS.md
/usr/lib64/R/library/forcats/R/forcats
/usr/lib64/R/library/forcats/R/forcats.rdb
/usr/lib64/R/library/forcats/R/forcats.rdx
/usr/lib64/R/library/forcats/data/Rdata.rdb
/usr/lib64/R/library/forcats/data/Rdata.rds
/usr/lib64/R/library/forcats/data/Rdata.rdx
/usr/lib64/R/library/forcats/help/AnIndex
/usr/lib64/R/library/forcats/help/aliases.rds
/usr/lib64/R/library/forcats/help/figures/logo.png
/usr/lib64/R/library/forcats/help/forcats.rdb
/usr/lib64/R/library/forcats/help/forcats.rdx
/usr/lib64/R/library/forcats/help/paths.rds
/usr/lib64/R/library/forcats/html/00Index.html
/usr/lib64/R/library/forcats/html/R.css
