# Automated Conda setup

Michelle L. Gill  
2016/07/26  
Regularly updated Gist located [here](https://gist.github.com/mlgill/4302c24ad1c8999577fd2f6cd03d8d2b/edit).

This bash script will download and setup a Conda environment on Mac OS X or Linux using a specified Python version (2.7, 3.4, 3.5) and packages. The Conda installation path and environment name can also be specified. All settings are input at the beginning of the script (see below).

If the Conda directory exists and can be determined to be a Conda installation, a new environment will be created. If the directory does not appear to be a Conda installation, the script will quit.

To run the script, set the variables below, make it executable with `chmod +x setup_conda.sh` and run the script from the command line with `./setup_conda.sh`.


```bash
# set environment path--use $HOME, not ~, if you want to use absolute path
env_path="$HOME/miniconda"

# set environment name
# NOTE: there's not an easy way to determine if an existing environment
# has the same name. Conda itself will throw an error during installation
# of second environment.
env_name="datasci"

# set python version: 2.7 3.4 3.5 etc
python_ver=2.7

# set packages to be installed (do not list python itself)
packages="numpy scipy matplotlib seaborn pandas statsmodels jupyter notebook nbconvert dill sqlalchemy BeautifulSoup4 html5lib lxml"
```