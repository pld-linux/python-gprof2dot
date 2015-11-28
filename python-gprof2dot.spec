# TODO
# - better group
%define 	module	gprof2dot
Summary:	Generate a dot graph from the output of several profiles.
Name:		python-%{module}
Version:	1.0
Release:	0.2
License:	LGPL
Group:		Development/Languages/Python
Source0:	http://pypi.python.org/packages/source/g/%{module}/%{module}-%{version}.zip
# Source0-md5:	519db08c9529c02479537cc5dc68fecb
URL:		http://python-mock.sourceforge.net/
BuildRequires:	python-distribute
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.228
Requires(post,preun):	/sbin/chkconfig
Requires:	graphviz
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Generate a dot graph from the output of several profiles.


%prep
%setup -q -n %{module}-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(644,root,root,755)
%doc PKG-INFO
%attr(755, root,root) %{_bindir}/%{module}
%{py_sitescriptdir}/%{module}
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/%{module}-*.egg-info
%endif
