# Conditional build:
%bcond_without  python2 # CPython 2.x module
%bcond_without  python3 # CPython 3.x module

%define		module	mysqlclient
Summary:	A Python interface to MySQL (MySQLdb compatible)
Summary(pl.UTF-8):	Interfejs Pythona do MySQL (kompatybilny z MySQLdb)
Name:		python-%{module}
Version:	1.3.6
Release:	5
License:	GPL
Group:		Libraries/Python
Source0:	https://pypi.python.org/packages/source/m/mysqlclient/mysqlclient-%{version}.tar.gz
# Source0-md5:	58d7c9c617a4286a88db290e7857d3aa
URL:		https://pypi.python.org/pypi/mysqlclient
BuildRequires:	rpmbuild(macros) >= 1.710
%if %{with python2}
BuildRequires:	python-devel >= 1:2.7
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-devel >= 1:3.3
%endif
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
Requires:	python-modules
Provides:	python-MySQLdb
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mysqlclient is a fork of MySQL-python. It adds Python 3.3 support and
merges some pull requests.

MySQLdb is an interface to the popular MySQL database server for
Python.

%description -l pl.UTF-8
mysqlclient to fork MySQL-python. Dodaje obsługę Pythona 3.3 oraz
nakłada kilka patchy.

MySQLdb to pythonowy interfejs do MySQL-a.

%package -n python3-%{module}
Summary:	A Python interface to MySQL (MySQLdb compatible)
Summary(pl.UTF-8):	Interfejs Pythona do MySQL (kompatybilny z MySQLdb)
Group:		Libraries/Python
%pyrequires_eq	python3
Requires:	python3-modules
Provides:	python3-MySQLdb

%description -n python3-%{module}
mysqlclient is a fork of MySQL-python. It adds Python 3.3 support and
merges some pull requests.

MySQLdb is an interface to the popular MySQL database server for Python

%description -n python3-%{module} -l pl.UTF-8
mysqlclient to fork MySQL-python. Dodaje obsługę Pythona 3.3 oraz
nakłada kilka patchy.

MySQLdb to pythonowy interfejs do MySQL-a.

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install \
	--optimize 2 \
	--root=$RPM_BUILD_ROOT
%endif

%if %{with python3}
%py3_install \
	--optimize 2 \
	--root=$RPM_BUILD_ROOT
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/*.so
%{py_sitedir}/*.py?
%dir %{py_sitedir}/MySQLdb
%{py_sitedir}/MySQLdb/*.py?
%dir %{py_sitedir}/MySQLdb/constants
%{py_sitedir}/MySQLdb/constants/*.py?
%{py_sitedir}/*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%attr(755,root,root) %{py3_sitedir}/*.so
%{py3_sitedir}/*.py
%{py3_sitedir}/__pycache__
%dir %{py3_sitedir}/MySQLdb
%{py3_sitedir}/MySQLdb/*.py
%{py3_sitedir}/MySQLdb/__pycache__
%dir %{py3_sitedir}/MySQLdb/constants
%{py3_sitedir}/MySQLdb/constants/*.py
%{py3_sitedir}/MySQLdb/constants/__pycache__
%{py3_sitedir}/*.egg-info
%endif

