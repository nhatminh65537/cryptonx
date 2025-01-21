if [ ! -d "github-tools" ]; then
    mkdir github-tools
fi
cd github_tools

echo install lbc_toolkit
git clone https://github.com/josephsurin/lattice-based-cryptanalysis.git
cd lattice-based-cryptanalysis
pip install .
cd ..
