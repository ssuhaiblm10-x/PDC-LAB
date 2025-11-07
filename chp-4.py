
from mpi4py import MPI
import numpy

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()


senddata = (rank+1)*numpy.arange(size,dtype=int)
recvdata = numpy.empty(size,dtype=int)
comm.Alltoall(senddata,recvdata)


print(" process %s sending %s receiving %s"\
      %(rank , senddata , recvdata))
=================================================

from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
   variable_to_share = 100 
           
else:
   variable_to_share = None

variable_to_share = comm.bcast(variable_to_share, root=0)
print("process = %d" %rank + " variable shared  = %d " %variable_to_share)
=============================================================================

from mpi4py import MPI

comm=MPI.COMM_WORLD
rank = comm.rank
print("my rank is %i" % (rank))

if rank==1:
    data_send= "a"
    destination_process = 5
    source_process = 5

    data_received=comm.recv(source=source_process)
    comm.send(data_send,dest=destination_process)
    
    print ("sending data %s " %data_send + \
           "to process %d" %destination_process)
    print ("data received is = %s" %data_received)


     
if rank==5:
    data_send= "b"
    destination_process = 1
    source_process = 1

    comm.send(data_send,dest=destination_process)
    data_received=comm.recv(source=source_process)
    

    print ("sending data %s :" %data_send + \
           "to process %d" %destination_process)
    print ("data received is = %s" %data_received)
===========================================================

from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()
data = (rank+1)**2

data = comm.gather(data, root=0)
if rank == 0:
   print ("rank = %s " %rank +\
          "...receiving data to other process")
   for i in range(1,size):

      value = data[i]
      print(" process %s receiving %s from process %s"\
            %(rank , value , i))
==================================================

#hello.py
from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
print ("hello world from process ", rank)
====================================================

from mpi4py import MPI

comm=MPI.COMM_WORLD
rank = comm.rank
print("my rank is : " , rank)

if rank==0:
    data= 10000000
    destination_process = 4
    comm.send(data,dest=destination_process)
    print ("sending data %s " %data +\
           "to process %d" %destination_process)
   
if rank==1:
    destination_process = 8
    data= "hello"
    comm.send(data,dest=destination_process)
    print ("sending data %s :" %data + \
           "to process %d" %destination_process)
   

if rank==4:
    data=comm.recv(source=0)
    print ("data received is = %s" %data)
    
    
if rank==8:
    data1=comm.recv(source=1)
    print ("data1 received is = %s" %data1)
====================================================

import numpy
from mpi4py import MPI 
comm = MPI.COMM_WORLD 
size = comm.size 
rank = comm.rank


array_size = 10
recvdata = numpy.zeros(array_size,dtype=numpy.int)
senddata = (rank+1)*numpy.arange(array_size,dtype=numpy.int)

print(" process %s sending %s " %(rank , senddata))


comm.Reduce(senddata,recvdata,root=0,op=MPI.SUM)
print ('on task',rank,'after Reduce:    data = ',recvdata)
==================================================================

from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
   array_to_share = [1, 2, 3, 4 ,5 ,6 ,7, 8 ,9 ,10] 
           
else:
   array_to_share = None

recvbuf = comm.scatter(array_to_share, root=0)
print("process = %d" % rank + " variable shared  = %d " % recvbuf )
=====================================================================

from mpi4py import MPI
import numpy as np

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3
neighbour_processes = [0,0,0,0]
if __name__ == "__main__":
    comm = MPI.COMM_WORLD
    rank = comm.rank
    size = comm.size

    grid_row = int(np.floor(np.sqrt(comm.size)))
    grid_column = comm.size // grid_row

        
    if grid_row*grid_column > size:
        grid_column -= 1
    if grid_row*grid_column > size:
        grid_row -= 1

    if (rank == 0) :
        print("Building a %d x %d grid topology:"\
              % (grid_row, grid_column) )
               

    cartesian_communicator = \
                           comm.Create_cart( \
                               (grid_row, grid_column), \
                               periods=(True, True), reorder=True)
    my_mpi_row, my_mpi_col = \
                cartesian_communicator.Get_coords\
                ( cartesian_communicator.rank ) 


    neighbour_processes[UP], neighbour_processes[DOWN]\
                             = cartesian_communicator.Shift(0, 1)
    neighbour_processes[LEFT],  \
                               neighbour_processes[RIGHT]  = \
                               cartesian_communicator.Shift(1, 1)
    print ("Process = %s \
row = %s \
column = %s \n----> \nneighbour_processes[UP] = %s\n\
neighbour_processes[DOWN] = %s\n\
neighbour_processes[LEFT] =%s\nneighbour_processes[RIGHT]=%s\n" \
           %(rank, my_mpi_row, \
             my_mpi_col,neighbour_processes[UP], \
             neighbour_processes[DOWN], \
             neighbour_processes[LEFT] , \
             neighbour_processes[RIGHT]))
 
============================================================
