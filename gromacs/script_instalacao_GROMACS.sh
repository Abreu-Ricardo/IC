
#sudo apt install gcc; sudo apt install g++;
#tar xfz gromacs-2021.4.tar.gz;

cd gromacs-2021.4;
mkdir build;
cd build;
cmake .. -DGMX_BUILD_OWN_FFTW=ON -DREGRESSIONTEST_DOWNLOAD=ON -DGMX_GPU=OpenCL; #-DGMX_GPU=ON;
make;
make check;
sudo make install;
source /usr/local/gromacs/bin/GMXRC;



## coisas extras que precisa
# Make e Cmake
# fftw - Biblioteca de transformacoes de Fourier
# libc-dev
## sudo apt update
## sudo apt install ocl-icd-opencl-dev
