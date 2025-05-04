# Conditional build:

%define		module	mysqlclient
Summary:	A Python interface to MySQL (MySQLdb compatible)
Summary(pl.UTF-8):	Interfejs Pythona do MySQL (kompatybilny z MySQLdb)
Name:		python3-%{module}
Version:	2.2.7
Release:	1
License:	GPL
Group:		Libraries/Python
Source0:	https://pypi.python.org/packages/source/m/mysqlclient/mysqlclient-%{version}.tar.gz
# Source0-md5:	95868b0f5c4c0eada33d18ca959cc512
URL:		https://pypi.python.org/pypi/mysqlclient
BuildRequires:	python3-devel >= 1:3.3
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
Requires:	python3-modules
Requires:	python3-modules
Provides:	python3-MySQLdb
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

%prep
%setup -q -n %{module}-%{version}

%build
%py3_build %{?with_tests:test}

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{py3_sitedir}/MySQLdb/*.so
%dir %{py3_sitedir}/MySQLdb
%{py3_sitedir}/MySQLdb/*.py
%{py3_sitedir}/MySQLdb/__pycache__
%dir %{py3_sitedir}/MySQLdb/constants
%{py3_sitedir}/MySQLdb/constants/*.py
%{py3_sitedir}/MySQLdb/constants/__pycache__
%{py3_sitedir}/*.egg-info
