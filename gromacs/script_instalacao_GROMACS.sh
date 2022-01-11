
#sudo apt install gcc; sudo apt install g++;
#tar xfz gromacs-2021.4.tar.gz;

cd gromacs-2021.4;
mkdir build;
cd build;
cmake .. -DGMX_BUILD_OWN_FFTW=ON -DREGRESSIONTEST_DOWNLOAD=ON -DGMX_GPU=ON -DGMX_GPU=OpenCL GMX_USE_RDTSCP=ON; #-DGMX_GPU=ON;
make;
make check;
sudo make install;
source /usr/local/gromacs/bin/GMXRC;

# Habilita a GPU
# -DGMX_GPU=ON

# Especifica o tipo de API para a GPU
# -DGMX_GPU=OpenCL

# Quando a CPU pode medir tempos melhores do que o especificado por padrao
# GMX_USE_RDTSCP=ON

## coisas extras que precisa
# Make e Cmake
# fftw - Biblioteca de transformacoes de Fourier
# libc-dev
## sudo apt update
## sudo apt install ocl-icd-opencl-dev
