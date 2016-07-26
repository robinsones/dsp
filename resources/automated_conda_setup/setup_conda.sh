#!/usr/bin/env bash

# Michelle L. Gill
# 2016/07/26
# https://gist.github.com/mlgill/4302c24ad1c8999577fd2f6cd03d8d2b/edit

# set environment path--use $HOME, not ~, if you want to use absolute path
env_path="$HOME/miniconda"

# set environment name
env_name="datasci"

# set python version: 2.7 3.4 3.5 etc
python_ver=2.7

# set packages to be installed (do not list python itself)
packages="numpy scipy matplotlib seaborn pandas statsmodels jupyter notebook nbconvert dill sqlalchemy BeautifulSoup4 html5lib lxml"

######################################

# get python major version (2 or 3)
python_base_ver=`echo $python_ver | cut -d'.' -f1`

echo "Using Python $python_ver..."

# set Linux/Darwin url
if [[ `uname` == "Darwin" ]]; then
    echo "Detected Mac OS X..."
    os_ver="MacOSX"
else
    echo "Detected Linux..."
    os_ver="Linux"
fi
url="http://repo.continuum.io/miniconda/Miniconda$python_base_ver-latest-$os_ver-x86_64.sh"

# set install script name
script_name="miniconda.sh"

unset PYTHONHOME
unset PYTHONPATH

# download the installation script
echo "Downloading conda installation script..."

if [[ -e $script_name ]]; then
    rm $script_name
fi

curl $url -s -o $script_name 

# create temporary conda installation
echo "Creating conda installation at $env_path..."

if [[ -e $env_path ]]; then
    rm -rf $env_path
fi

bash $script_name -b -f -p $env_path >> /dev/null

rm $script_name

# setup path and create environment
echo "Creating conda environment..."

export PATH=$env_path:$PATH

packages="python=$python_ver $packages"
$env_path/bin/conda create --quiet -y -n $env_name $packages >> /dev/null

echo "Finished creating conda environment..."

