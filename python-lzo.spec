%define python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")

Summary:	LZO bindings for Python
Name:		python-lzo
Version:	1.08
Release:	6
Source0:	http://www.oberhumer.com/opensource/lzo/download/LZO-v1/%{name}-%{version}.tar.gz
Patch0:		python-lzo-1.08-build-against-lzo2.patch
Patch1:		python-lzo-1.08-nowarning.patch
URL:		https://www.oberhumer.com/opensource/lzo/
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



%changelog
* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 1.08-5mdv2010.0
+ Revision: 442310
- rebuild

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 1.08-4mdv2009.0
+ Revision: 259701
- rebuild

* Fri Jul 25 2008 Thierry Vignaud <tv@mandriva.org> 1.08-3mdv2009.0
+ Revision: 247507
- rebuild
- fix no-buildroot-tag

* Tue Dec 18 2007 Per Ã˜yvind Karlsen <peroyvind@mandriva.org> 1.08-1mdv2008.1
+ Revision: 131996
- manually add python_sitearch macro due to rpm 4.4.2.2 crap^H^H^?\196?\164^Hbreakage
- fix buildrequires
- import python-lzo


* Tue Dec 12 2007 Per Øyvind Karlsen <pkarlsen@mandriva.com> 1.08-1mdv2008.1
- Initial release
