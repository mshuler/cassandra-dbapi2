Name:           python26-cql
Version:        1.0.9
Release:        1
Summary:        DB-API 2.0 compliant client library for Cassandra/CQL

Group:          Applications/Databases
License:        ASL 2.0
URL:            http://code.google.com/a/apache-extras.org/p/cassandra-dbapi2/
Source0:        http://cassandra-dbapi2.apache-extras.org.codespot.com/files/cql-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:       /usr/bin/python2.6, python26-thrift

%global __python python2.6
%global python26_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")

# Turn off the brp-python-bytecompile script, cause in RHEL 5 it only believes in python2.4
%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')

%description
CQL is an SQL-like query language for the highly scalable distributed database
Cassandra. This package provides a Python driver for making queries to a
Cassandra installation using CQL, using the standard Python database API
("DB-API 2.0").

%prep
%setup -q -n cql-%{version}


%build
%{__python} setup.py build


%install
rm -rf %{buildroot}
%{__python} setup.py install -c -O1 --skip-build --root %{buildroot}


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc README CHANGES.txt
%{python26_sitelib}/cql/
%{python26_sitelib}/cql*.egg-info


%changelog
