
Summary: Greasemonkey extension for firefox
Name: firefox-ext-greasemonkey
Version: 0.8.20100408.6
Release: 8
License: MIT
Group:	Networking/WWW
URL:	https://addons.mozilla.org/en-US/firefox/addon/748
Source: http://releases.mozilla.org/pub/mozilla.org/addons/748/greasemonkey-%{version}-fx.xpi
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
Requires:	mozilla-firefox >= %{firefox_version}
BuildRequires:	firefox-devel
Buildarch: noarch

%description
Allows you to customize the way a webpage displays using small bits of
JavaScript.  Hundreds of scripts, for a wide variety of popular sites, are
already available at http://userscripts.org.  You can write your own scripts,
too. Check out http://wiki.greasespot.net/ to get started.

%prep
%setup -q -c -n %{name}-%{version}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{firefox_extdir}

hash="$(sed -n '/.*em:id="\(.*\)"/{s//\1/p;q}' install.rdf)"
if [ -z "$hash" ]; then
    hash="$(sed -n '/.*em:id>\(.*\)<\/em:id>.*/{s//\1/p;q}' install.rdf)"
fi
if [ -z "$hash" ]; then
    echo "Failed to find plugin hash."
    exit 1
fi
extdir="%{firefox_extdir}/"
mkdir -p "%{buildroot}$extdir"
cp -af %SOURCE0 "%{buildroot}$extdir/$hash.xpi"

%clean
rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%{firefox_extdir}



%changelog
* Wed Jan 19 2011 Thierry Vignaud <tv@mandriva.org> 0.8.20100408.6-7mdv2011.0
+ Revision: 631670
- prevent need to rebuild for every new firefox
- only package .xpi

* Wed Jan 05 2011 Thierry Vignaud <tv@mandriva.org> 0.8.20100408.6-6mdv2011.0
+ Revision: 628867
- rebuild for new firefox

* Sun Sep 26 2010 Thierry Vignaud <tv@mandriva.org> 0.8.20100408.6-5mdv2011.0
+ Revision: 581105
- rebuild for new firefox
- rebuild for new firefox

* Tue Jul 27 2010 Funda Wang <fwang@mandriva.org> 0.8.20100408.6-3mdv2011.0
+ Revision: 561155
- rebuild for ff 3.6.8

* Mon Jun 28 2010 Frederic Crozat <fcrozat@mandriva.com> 0.8.20100408.6-2mdv2010.1
+ Revision: 549358
- rebuild with FF 3.6.6

  + Funda Wang <fwang@mandriva.org>
    - new verison 0.8.20100408.6

* Sun Apr 04 2010 Funda Wang <fwang@mandriva.org> 0.8.20100211.5-2mdv2010.1
+ Revision: 531096
- rebuild

* Sat Mar 27 2010 Thierry Vignaud <tv@mandriva.org> 0.8.20100211.5-1mdv2010.1
+ Revision: 528044
- import firefox-ext-greasemonkey


* Sat Mar 27 2010 Thierry Vignaud <tvignaud@mandriva.com> 0.8.20100211.5-1mdv2010.1
- initial creation

