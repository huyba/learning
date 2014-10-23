CC      = CC
COPT    = -g -O2

MPICH2_PATH=/usr/local/mpich2
INCLUDE = -I. -I$(MPICH2_PATH)/include

LIBS    = -L$(MPICH2_PATH)/lib -l mpi

CFLAGS  = $(COPT) $(INCLUDE)

LD      = $(CC)
LDFLAGS = $(COPT) $(INCLUDE)

all: main.x

%.x: %.o
	$(LD) $(LDFLAGS) $< $(LIBS) -o $@

%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@
