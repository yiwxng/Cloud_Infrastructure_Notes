# what are learn about system programming so far with this course and with my internship
1. We learned to work directly with memory - This course takes away more abstraction that higher level languages like Python, Where we don't have to worry about memory management. And now we have to use a functions like certain concepts and tools like pointers understanding how to terminate strings,  how many bytes a data type has, using malloc and understanding the live scope of different types of memories, understanding how the computer reads and writes text and other types of binary data, buffered i/o


2. gives us a glimpse about interacting with the operating system directly: over the span of this course we used a lot of system functions, like malloc, fork, all the system calls with reading files, signals, sockets. They are all functions in C that enable us the connects directly us the user and the OS. It takes the layer of obstruction away from the previous languages, like Python
    2.2 where we see the exact processes that's running on our computer, understanding the memories addresses, file descriptor 
    - The kernel is the only part of the system that can safely:
    - Manage memory
    - Create and destroy processes
    - Control I/O with devices, sockets, and files
    - Deliver signals and interrupts

3. everything is a file in linux, file descriptors

4. Touched on the idea of concurrency in process f



# Operating System Responsibilities — Summary Table

|  Aspect                 | Description                                                                 |
|--------------------------|---------------------------------------------------------------------------------|
| **Process Management**    | Handles creation, scheduling, and termination of processes                      |
| **Memory Management**     | Allocates RAM, handles paging, virtual memory, heap and stack                   |
| **File System**           | Manages file storage, retrieval, hierarchy, and access permissions              |
| **Device Management (I/O)**| Interfaces with hardware using device drivers (disk, keyboard, network, etc.)   |
| **CPU Scheduling**        | Chooses which process gets to use the CPU and when                             |
| **Permissions & Security**| Enforces access control via UIDs, GIDs, ACLs, and memory protection             |
| **Inter-Process Communication (IPC)** | Enables communication between processes (pipes, shared memory, sockets)     |
| **Networking**            | Implements network protocols (TCP/IP), socket management, and routing           |
| **System Call Interface** | Provides the entry point for programs to request OS services (`read()`, etc.)  |
| **Virtualization Support**| Isolates processes using containers (cgroups, namespaces) or VMs                |
| **User Interface (optional)**| CLI or GUI to allow human users to interact with the system                    |


## Process table 
The operating system has a process table where it keeps trucks of every process currently running. 
So a process table is a software in the OS colonel, it lives in Colonel memory, which is RAM. 
And it's it is used for scheduling, tracking and context switch.

## What is context switching?
It is when a OS switch the CPU from running one process to another. Essentially what it does is pause what process it was doing – save everything – and now resume or start process B.
A CPU can only run one process at a time per core, serve for when you have many applications running, with the operating system is actually doing contact, switching really fast between task.

## What does a process contain?
Each process has its own PID, appoint her to its memory map it status - Running, waiting, stopped, zombie. 
A list of open file descriptors, and other meta-data like parent PI.

### What are the status of a process?
Running, ready, sleeping, stopped, zombie, dead/reaped

| State           | Meaning |
|------------------|---------|
| **Running**      | Currently executing on the CPU |
| **Ready**        | Waiting to be scheduled (has everything it needs) |
| **Sleeping**     | Waiting for I/O (e.g. disk, network, user input) |
| **Stopped**      | Suspended (paused by signal, user, or debugger) |
| **Zombie**       | Process has terminated, but its parent hasn’t called `wait()` yet |
| **Dead / Reaped**| Fully cleaned up and removed from the process table |


## OS Responsibilities and Hierarcy (with chatgpt help)

```bash 

+----------------------------+   <- User Interface (Shell/GUI)
|       User Space           |
|   - Applications           |
|   - Libraries              |
+----------------------------+
|   System Call Interface    |   <- Bridge
+----------------------------+
|        Kernel Space        |
| - Process Manager          |
| - Memory Manager           |
| - File System              |
| - Device Drivers (I/O)     |
| - Scheduler                |
| - Network Stack            |
| - Security Manager         |
+----------------------------+
|       Hardware             |


```


## Source code to running process : Compiling, Process, C Preprocessor, Process Model rls 

1. preprocessor 
2. compiling 
3. 
compiling - 
is the abstraction that an operating system uses to represent and manage programs in execution (i.e., processes).

It’s the mental and structural framework that defines:

What a process is
What resources a process has
How processes behave
How the OS should manage them


## Process, Filesystem 

file systems contains the source code, lib, other tools that source code needs to become a process 


## Memory management 

### what is a memory leak ?
when a malloc-ed memory is not freed.

why is it a concern when the os will clean up the resources/ memory for each process when they are done?

Memory leak will be a problem if process calls malloc in a loop or many times. It will cause infinite asking of memory from the os, and heap will grow. which will cause the os 