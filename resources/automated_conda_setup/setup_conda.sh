#!/usr/bin/env bash

# Michelle L. Gill
# 2016/07/26
# https://gist.github.com/mlgill/4302c24ad1c8999577fd2f6cd03d8d2b

# set environment path--use $HOME, not ~, if you want to use absolute path
# otherwise the path will be relative to the current path.
env_path="$HOME/miniconda"

# set environment name
# NOTE: there's not an easy way to determine if an existing environment
# has the same name. Conda itself will throw an error during installation
# of second environment.
env_name="datasci"

# set python version: 2.7, 3.4, 3.5, etc
python_ver=2.7

# set packages to be installed (do not list python itself)
# be sure to name/spell them exactly as Conda does or installation will fail
packages="numpy scipy matplotlib seaborn pandas statsmodels jupyter notebook nbconvert dill sqlalchemy BeautifulSoup4 html5lib lxml"

################# USER SET VARIABLES ABOVE THIS LINE #####################

# get python major version (2 or 3)
python_base_ver=`echo $python_ver | cut -d'.' -f1`

echo "Using Python $python_ver."

if [[ ! -d $env_path ]]; then

    echo "Conda does not seem to be installed at $env_path. Installing now."

    # set Linux/Darwin url
    if [[ `uname` == "Darwin" ]]; then
        echo "Detected Mac OS X."
        os_ver="MacOSX"
    else
        echo "Detected Linux."
        os_ver="Linux"
    fi
    url="http://repo.continuum.io/miniconda/Miniconda$python_base_ver-latest-$os_ver-x86_64.sh"

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

elif [[ -e $env_path/bin/conda ]]; then

    unset PYTHONHOME
    unset PYTHONPATH

    # setup path and create environment
    echo "Conda seems to be installed already. Skipping installation."

    export PATH=$env_path:$PATH

    packages="python=$python_ver $packages"
    $env_path/bin/conda create --quiet -y -n $env_name $packages >> /dev/null
    
    if [[ $? == 0 ]]; then
        echo "Finished creating Conda environment."
    else
        echo "There was an error creating the Conda environment."
    fi

else

    # the destination directory exists but does not seem to a Conda installation
    # don't want to risk overwriting files, so time to bail...

    echo "The directory $env_path exists but it does not seem to be a Conda installation."
    echo "Quitting without installing anything."
    echo "Please delete or move this directory before installing."

fi


