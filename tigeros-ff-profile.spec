Name:           tigeros-ff-profile
Version:        1.0
Release:        3%{?dist}

Summary:        TigerOS default profile for Firefox
License:        GPLv3+
URL:            https://github.com/RITlug/tigeros-ff-profile

Source0:        %{name}-%{version}-%{release}.tar.gz
BuildArch:      noarch
Requires:       firefox

%description
This package contains the default bookmarks for TigerOS.

%prep
%setup -q

%install
%{__mkdir_p} %{buildroot}/etc/skel/
install -d -m 755 .mozilla/ %{buildroot}/etc/skel/.mozilla/

%files
%license LICENSE
/etc/skel/.mozilla

%changelog
* Wed May 16 2018 Tim Zabel <tjz8659@rit.edu> - 1.0-3
- Fedora 28 rebuild

* Wed Aug 30 2017 Aidan Kahrs <axk4545@rit.edu> - 1.0-2
- rebuild for Fedora 26

* Mon May 08 2017 Aidan Kahrs <axk4545@rit.edu> - 1.0-1
- Initial version
