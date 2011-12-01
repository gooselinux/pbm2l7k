Name:           pbm2l7k
Version:        990321
Release:        8%{?dist}
Summary:        Converts PBM stream to Lexmark 7000, 7200 and 5700 printer language

Group:          System Environment/Libraries
License:        GPLv2
URL:            http://www.ibiblio.org/pub/linux/hardware/drivers/lexmark7000linux-%{version}.lsm
Source0:        http://www.ibiblio.org/pub/linux/hardware/drivers/lexmark7000linux-%{version}.tar.gz
Patch0:         pbm2l7k-990321-paths.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
This is a filter to convert pbmraw data such as produced by ghostscript to
the printer language of Lexmark 7000, 7200 and 5700 printers.  It is meant
to be used by the PostScript Description files of the drivers from the
foomatic package.

%prep
%setup -q -c

# Use installed path to find data files.
%patch0 -b .paths

%build
# The included Makefile is badly written
%{__cc} -DDATADIR=\"%{_datadir}/%{name}\" %{optflags} -o pbm2l7k pbm2l7k.c

%install
rm -rf $RPM_BUILD_ROOT
%{__mkdir} -p $RPM_BUILD_ROOT/%{_bindir}
%{__install} pbm2l7k $RPM_BUILD_ROOT/%{_bindir}
# Foomatic driver refers to this filter as pbm2lex
%{__ln_s} pbm2l7k $RPM_BUILD_ROOT/%{_bindir}/pbm2lex
%{__mkdir} -p $RPM_BUILD_ROOT/%{_datadir}/%{name}
%{__install} pr5700.prn $RPM_BUILD_ROOT/%{_datadir}/%{name}
%{__install} pr7000.prn $RPM_BUILD_ROOT/%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/pbm2l7k
%{_bindir}/pbm2lex
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/pr5700.prn
%{_datadir}/%{name}/pr7000.prn
%doc README lexmarkprotocol.txt

%changelog
* Fri Mar  5 2010 Tim Waugh <twaugh@redhat.com> - 990321-8
- Added comment to patch.

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 990321-7.1
- Rebuilt for RHEL 6

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 990321-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 990321-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Sep 21 2008 Ville Skyttä <ville.skytta at iki.fi> - 990321-5
- Fix Patch0:/%%patch mismatch.

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 990321-4
- Autorebuild for GCC 4.3

* Fri Aug 3 2007 Lubomir Kundrak <lkundrak@redhat.com> 990321-3
- Modify the License tag in accordance with the new guidelines

* Mon Jul 2 2007 Lubomir Kundrak <lkundrak@redhat.com> 990321-2
- Changed one absolute symlink to relative (#243951)
- Fixed the patch filename

* Fri Jun 8 2007 Lubomir Kundrak <lkundrak@redhat.com> 990321-1
- Initial package
