%define python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")

Summary:	LZO bindings for Python
Name:		python-lzo
Version:	1.08
Release:	%mkrel 5
Source0:	http://www.oberhumer.com/opensource/lzo/download/LZO-v1/%{name}-%{version}.tar.gz
Patch0:		python-lzo-1.08-build-against-lzo2.patch
Patch1:		python-lzo-1.08-nowarning.patch
URL:		http://www.oberhumer.com/opensource/lzo/
License:	GPLv2
Group:		Development/Python
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	liblzo-devel python-devel

%description
Python-LZO provides Python bindings for LZO, i.e. you can access
the LZO library from your Python scripts thereby compressing ordinary
Python strings.

%prep
%setup -q
%patch0 -p1 -b .lzo2
%patch1 -p1 -b .nowarning

%build
python setup.py build

%install
rm -rf %{buildroot}
python setup.py install --root=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{python_sitearch}/lzo.so
%{python_sitearch}/python_lzo*egg-info

