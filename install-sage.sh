option="-v"
sage_version="9.8"

if [ "$1" = "-h" ]; then
    echo "Usage: $0 <sage_version> to specify a version"
    exit 0
fi

if [ $# = 0 ]; then
    echo "Use default version 9.8"
    echo "Usage: $0 <sage_version> to specify a version"
else
    sage_version=$1
fi

pip install $option sage_conf==$sage_version
pip install $option $(sage-config SAGE_SPKG_WHEELS)/*.whl sage_setup==$sage_version
pip install $option --no-build-isolation sagemath-standard==$sage_version
