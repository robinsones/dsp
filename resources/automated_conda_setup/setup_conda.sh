#!/usr/bin/env bash

# Michelle L. Gill
# 2016/07/26
# https://gist.github.com/mlgill/4302c24ad1c8999577fd2f6cd03d8d2b

# set environment path--use $HOME, not ~, if you want to use absolute path
# otherwise the path will be relative to the current path.
#env_path="$HOME/miniconda"
env_path="/Volumes/Files/metis_course/resources/automated_conda_setup/tmp"

# set environment name
# NOTE: there's not an easy way to determine if an existing environment
# has the same name. Conda itself will throw an error during installation
# of second environment.
env_name="datasci"

# set python version: 2.7, 3.4, 3.5, etc
python_ver=3.4

# set packages to be installed (do not list python itself)
# be sure to name/spell them exactly as Conda does or installation will fail
packages="psutil numpy scipy matplotlib seaborn pandas statsmodels jupyter notebook nbconvert sqlalchemy BeautifulSoup4 html5lib lxml"

################# USER SET VARIABLES ABOVE THIS LINE #####################

# get python major version (2 or 3)
python_base_ver=`echo $python_ver | cut -d'.' -f1`

echo "Using Python $python_ver."

if [[ -e $env_path ]]; then

    if [[ ! -e $env_path/bin/conda ]]; then

        # the destination directory does not seem to contain a Conda installation
        # don't want to risk overwriting files, so time to bail...

        echo "There doesn't appear to be a Conda installation at $env_path."
        echo "Quitting without installing anything."

        exit 0

    fi

elif [[ ! -e $env_path ]]; then

    echo "Conda does not seem to be installed at $env_path. Installing now."

    # set Linux/Darwin url
    if [[ `uname` == "Darwin" ]]; then
        echo "Detected Mac OS X."
        os_ver="MacOSX"
    else
        echo "Detected Linux."
        os_ver="Linux"
    fi

    url="http://repo.continuum.io/miniconda/Miniconda${python_base_ver}-latest-${os_ver}-x86_64.sh"

    # set install script name
    script_name="miniconda.sh"

    # download the installation script
    echo "Downloading Conda installation script."

    if [[ -e $script_name ]]; then
        rm $script_name
    fi

    curl $url -s -o $script_name 

    # create temporary conda installation
    echo "Creating Conda installation at $env_path."

    if [[ -e $env_path ]]; then
        rm -rf $env_path
    fi

    bash $script_name -b -f -p $env_path >> /dev/null

    rm $script_name

else

    # setup path and create environment
    echo "Conda seems to be installed already. Skipping installation."

fi

# Setup the environment

unset PYTHONHOME
unset PYTHONPATH

export PATH=$env_path:$PATH

echo "Python environment will be based on version $python_ver"

packages="python=$python_ver $packages"

$env_path/bin/conda create --quiet -y -n $env_name $packages >> /dev/null

if [[ $?==0 ]]; then
    echo "Finished creating Conda environment."
else
    echo "There was an error creating the Conda environment."
fi



