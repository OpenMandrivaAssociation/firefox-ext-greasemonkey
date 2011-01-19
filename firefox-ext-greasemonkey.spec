
Summary: Greasemonkey extension for firefox
Name: firefox-ext-greasemonkey
Version: 0.8.20100408.6
Release: %mkrel 7
License: MIT
Group:	Networking/WWW
URL:	https://addons.mozilla.org/en-US/firefox/addon/748
Source: http://releases.mozilla.org/pub/mozilla.org/addons/748/greasemonkey-%{version}-fx.xpi
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
Requires:	mozilla-firefox >= %{firefox_epoch}:%{firefox_version}
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

