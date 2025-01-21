venv_folder="cryptonx-venv"
sage_version="9.8"
python="python"

if [ "$1" = "-h" ]; then
    echo "Usage: sh ./build-venv.sh [-f]"
    echo "  -f: Force the removal of the existing virtual environment folder"
    exit 0
fi

if [ -d $venv_folder ]; then
    if [ "$1" = "-f" ]; then
        echo "Removing existing folder $venv_folder"
        rm -rf $venv_folder
    else
        echo "The folder $venv_folder already exists. Please remove it before running this script."
        exit 1
    fi
fi

if ! [ -x "$(command -v python)" ]; then
    if ! [ -x "$(command -v python3)" ]; then
        echo "Python is not installed. Please install Python 3.6 or higher:"
        echo "  sudo apt-get install python3"
        exit 1
    else
        python="python3"
    fi
fi

if ! [ -x "$(command -v $python -m venv)" ]; then
    echo "Python venv is not installed. Please install python3-venv:"
    echo "  sudo apt-get install python3-venv"
    exit 1
fi

echo "Installing system packages (enter your password if prompted)"
sudo apt-get update
sudo apt-get install bc binutils bzip2 ca-certificates cliquer cmake curl \
        ecl eclib-tools fflas-ffpack flex g++ gap gcc gengetopt gfan gfortran \
        glpk-utils gmp-ecm lcalc libatomic-ops-dev libboost-dev \
        libbraiding-dev libbrial-dev libbrial-groebner-dev libbz2-dev \
        libcdd-dev libcdd-tools libcliquer-dev libcurl4-openssl-dev libec-dev \
        libecm-dev libffi-dev libflint-dev libfplll-dev libfreetype-dev \
        libgap-dev libgc-dev libgd-dev libgf2x-dev libgiac-dev libgivaro-dev \
        libglpk-dev libgmp-dev libgsl-dev libhomfly-dev libiml-dev \
        liblfunction-dev liblinbox-dev liblrcalc-dev liblzma-dev libm4ri-dev \
        libm4rie-dev libmpc-dev libmpfi-dev libmpfr-dev libncurses5-dev \
        libntl-dev libopenblas-dev libpari-dev libplanarity-dev libppl-dev \
        libprimecount-dev libprimesieve-dev libpython3-dev libqhull-dev \
        libreadline-dev librw-dev libsingular4-dev libsqlite3-dev libssl-dev \
        libsuitesparse-dev libsymmetrica2-dev libz-dev libzmq3-dev m4 make \
        maxima maxima-sage meson nauty ninja-build openssl palp pari-doc \
        pari-elldata pari-galdata pari-galpol pari-gp2c pari-seadata patch \
        patchelf perl pkg-config planarity ppl-dev python3 python3-setuptools \
        python3-venv qhull-bin singular singular-doc sqlite3 sympow tachyon \
        tar texinfo tox xcas xz-utils

echo "Creating virtual environment $venv_folder"
$python -m venv $venv_folder

echo "Activating virtual environment"
. $venv_folder/bin/activate

echo "Check activated virtual environment"
pip list

echo "Installing Python packages"
pip install -r requirements.txt

echo "Installing SageMath $sage_version"
sh install-sage.sh $sage_version

echo "Upgrading pip"
pip install --upgrade pip

echo "Installing github_tools"
sh install-tools.sh