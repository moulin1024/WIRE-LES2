################################################################################
# FC
################################################################################

FC = mpif90

################################################################################
# FFLAGS
################################################################################

FFLAGS = -O3 -Mpreprocess -mcmodel=medium
CUDA = -Mcuda -lcufft -ta=nvidia
PRECISION=-DDOUBLE
# debug
# -check bounds -debug all -traceback -fpe0 fp-stack-check -debug inline-debug-info -parallel-source-info=2 -warn all

# prof
# -pg

################################################################################
# LIBS
################################################################################

LIBS = -L/home/moulin/anaconda3/lib -lfftw3
# INC = #-I/opt/intel/compilers_and_libraries_2019.4.243/linux/mpi/intel64/include/
################################################################################
# OBJ, PROG
################################################################################

OBJ = precision.o dimen.o cufft_m.o derivative.o divergence.o div.o\
	  test.o \

PROG = wireles
all: build run
# --- compile ---
build:
	$(FC) $(FFLAGS) $(CUDA) $(PRECISION) -c ../../src/precision.cuf
	$(FC) $(FFLAGS) $(CUDA) $(PRECISION) -c ../common/dimen.cuf
	$(FC) $(FFLAGS) $(CUDA) $(PRECISION) -c ../../src/cufft_m.cuf
	$(FC) $(FFLAGS) $(CUDA) $(PRECISION) -c ../../src/derivative.cuf
	$(FC) $(FFLAGS) $(CUDA) $(PRECISION) -c ../../src/divergence.cuf
	$(FC) $(FFLAGS) $(CUDA) $(PRECISION) -c ../cpu_benchmark/div.f90
	$(FC) $(FFLAGS) $(CUDA) $(PRECISION) -c test.cuf
	$(FC) $(FFLAGS) $(CUDA) $(OBJ) -o $(PROG).run $(LIBS)

run:
	mpirun -np 2 ./wireles.run
		

clean:
	find . -type f -name '*.o' -delete
	find . -type f -name '*.mod' -delete
	find . -type f -name '*.run' -delete