Summary:	API to access display driver functionality for ATI graphics cards
Name:		amd-adl-sdk
Version:	5.0
Release:	1
License:	AMD-ADL
Group:		Applications
Source0:	ADL_SDK_%{version}.zip
# Source0-md5:	e78ecf95b0eb238dac5d9bc5fcb6d764
URL:		http://developer.amd.com/sdks/adlsdk/
BuildRequires:	unzip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
API to access display driver functionality for ATI graphics cards.

%package devel
Summary:	Header files and development documentation for amd-adl-sdk
Group:		Development/Libraries

%description devel
Header files and development documentation for amd-adl-sdk.

%prep
%setup -q -c

%build
%{__cc} %{rpmcflags} %{rpmcppflags} %{rpmldflags} \
	-o adlutil/adlutil -DLINUX=1 -ldl -I$(pwd)/include \
	adlutil/main.c

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_sbindir},%{_includedir}}

install adlutil/adlutil $RPM_BUILD_ROOT%{_sbindir}
cp -a include/*.h $RPM_BUILD_ROOT%{_includedir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc adlutil/*.doc
%attr(755,root,root) %{_sbindir}/adlutil

%files devel
%defattr(644,root,root,755)
%doc Public-Documents/*.{pdf,doc} Public-Documents/html/*
%{_includedir}/*.h
