Name:           promu
Version:        0.1.0
Release:        1
Summary:       	Promu is the utility tool for Prometheus projects
Source0:	https://github.com/prometheus/promu/archive/v%{version}.tar.gz
License:        ASL 2.0
URL:            https://github.com/prometheus/promu/
BuildRequires:	golang

%description
%{summary}

%prep
%setup -q

# set working directory
mkdir -p src/github.com/prometheus
ln -s ../../../ src/github.com/prometheus/promu

%build
export GOPATH=$(pwd):%{gopath}
make build

%install
install -D -p -m 0755 promu-%{version} %{buildroot}/bin/promu

%files
/bin/promu
