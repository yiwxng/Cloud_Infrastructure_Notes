# Shell Programming - Bash 

## 1. core of bash 

### 1.1 Interactive and non interactive shell 

### 1.2 local and env variable 

- local : exist only within the current shell  x=5
- env : inherited by child processes  export x=5

### 1.3 Quoting 
quotes mainly used for string, not needed for number 

- "  - expands variables in the a string, and should be used as good practice
- ' - doesnt exand variables, pass the string as it is, can be used in eval and awk 
- ` - expr `` pass what the numeric exp
- \ escape char - treat the next char literally
- ${} - When you want to use a variable value within a string or add other values to it
  - echo "${name:-Anonymous}"  # prints $name if set, else "Anonymous"
  - text="hello"
            echo "${text:1:2}"  # prints "el"


```bash 
USER=yi
echo "Hello, $USER"     # Hello, Yi

echo 'Hello, $USER'     # Hello, $USER
```


### 1.4 redirection 
- > overwrites if file exist
- < Read input from a file instead of keyboard
- >> doesn't Override and just append it to the end of the file
- &> Redirect, standard output and standard error to this file
- ordering


### 1.5 pipe  | 
- 

### 1.6 globbing * ? []
- * 
- ?
- []


## 2 Control flow 

### 2.1 : logic 
- if, 
- then , 
- elif, 
- else

### 2.2 condition
- []
- [[]]

### 2.3 test 

### 2.4 for, while, until 

### 2.5 case multi-branch 


## 3 CLI Tools

### 3.1 Show file content
- cat, 
- less, 
- head, 
- tail 

### 3.2 Search 
- grep 
- cut 
- awk 
- sed 

### 3.3 
- sort 
- uniq
- wc 
- tr 
- xargs 

### 3.4  
- find 
- locate 
- du 
- df 

### 3.5 exec, set, expr, eval

### 3.6 
- compare 
- num 
- files 
string 




## Process 

A process is a running instance of a program in a computer. It is managed by the operating system.

 each process has its own memory space, APID, and a file descriptor

How do we create processes?
fork()

What does this is when it is called a create a copy of the current line and always contents below as a child process of the current main process

return value of fork 

Do you return value of fork will be different for child and parent, for a child it would be zero and for parent it will be greater than zero. 
When a child process is created, it has a duplicate value of the parents data, but they are independent when things changes.

what are same and different?
No, the child’s PID is never the same as the parent’s.
It is a new unique PID assigned by the operating system.


## what controls the process? - Kernel 

kernel - A kernel is something that gives each running process its memory, stack, and storage…

| Kernel Role          | What It Means                                                                 |
|----------------------|--------------------------------------------------------------------------------|
| **Memory manager**   | Allocates memory/stack, enforces boundaries                                    |
| **I/O manager**      | Handles read/write operations via syscalls                                    |
| **Process manager**  | Starts/kills/suspends/resumes processes, assigns PIDs                         |
| **Signal dispatcher**| Delivers signals between system and processes                                 |
| **Security enforcer**| Controls file permissions, syscalls, isolation (namespaces/cgroups)           |
| **Device handler**   | Talks to actual hardware via device drivers                                   |


- Each **process** belongs to one or more **namespaces**.
  - These control what it can **see** (like its own PID list, file mounts, network, etc.)
  - Processes in different namespaces are **isolated from each other**.
  
- Each process is also assigned to one or more **cgroups**.
  - These control what it can **use** (CPU, memory, disk I/O, etc.)
  - Cgroups **do not isolate** — they just limit.

- A **tenant** is a user or team using a shared system.
- **Multitenancy** means multiple tenants share the same system but are isolated.
- In Kubernetes:
  - Each **namespace** can represent a tenant.
  - They share the same cluster, but have separate access, quotas, and policies.
- If you have **multiple clusters**, their namespaces are **completely separate**.

- A process belongs to one instance of each namespace type (e.g., one PID namespace, one NET namespace).
- Namespaces are **independent** — you can isolate or share each one separately.
- So yes:
  - One app can share some namespaces (e.g., NET)
  - And have private others (e.g., MNT, PID)
- Containers (and Pods) are built using flexible combinations of these namespace types.


- A **system service** is a background program that supports the OS or user applications.
- Examples you’ve probably used:
  - `NetworkManager` (Wi-Fi)
  - `cups` (printing)
  - `udev` (USB)
  - `docker` / `containerd` (containers)
- These services:
  - Are usually started by `systemd` or similar
  - Work with the kernel and other system components
  - Expose functionality to apps so they don't have to reimplement it

- The **S3 CSI driver** is like a system service in Kubernetes:
  - It runs in the background
  - It watches for storage requests
  - It uses FUSE to mount volumes from S3
  - It makes your app's life easier by managing the “infrastructure plumbing”


- `systemd` is the init system that starts up core services on Linux after boot.
- On your laptop or EC2 instance, `systemd` launches things like:
  - `NetworkManager`, `sshd`, `containerd`, `kubelet`

- In Kubernetes:
  - Add-ons like the S3 CSI driver are **not started by systemd**.
  - They are deployed as Pods and started by **Kubernetes (via the kubelet)**.
  - So they are more like cluster-native system services, managed by Kubernetes itself.

- You can think of them as "Kubernetes-managed system services" that are always present and run in the background.


####  What is a Child Process?
- Any new process created by a running program using `fork()`
- It can run **any program**: `ls`, `awk`, `bash`, compiled C code, etc.
- Gets a **copy** of the parent’s environment (variables, file descriptors) - read and write from the same source 
- Created implicitly in Bash when running commands, piping, backgrounding, etc.

#### What is a Subshell?
- A **child process** that runs a **new shell** (usually Bash)
- Created when you:
  - Use parentheses: `( ... )`
  - Run a new shell with `bash`, `bash -c`
  - Use some pipelines or backgrounded grouped commands

#### Relationship:
- All subshells are child processes
- Not all child processes are subshells

#### How Are They Created in Bash?

| Syntax                  | Creates Child Process | Subshell? |
|-------------------------|-----------------------|-----------|
| `ls`                    | ✅ Yes                | ❌ No     |
| `awk`                   | ✅ Yes                | ❌ No     |
| `( echo hi )`           | ✅ Yes                | ✅ Yes    |
| `bash`                  | ✅ Yes                | ✅ Yes    |
| `{ echo hi; }`          | ❌ No                 | ❌ No     |
| `source script.sh`      | ❌ No                 | ❌ No     |
| `command &`             | ✅ Yes                | ❌ No     |
| `echo hi | grep hi`     | ✅ Yes (both sides)   | ⛔ Depends* |

\* Each side of a pipeline usually runs in a separate child process. Some shells may run parts in subshells depending on context (e.g. loops inside pipelines).

#### Variable and Environment Behavior

| Scenario                            | Affects Parent Shell? |
|-------------------------------------|------------------------|
| Variable set in subshell `( ... )`  | ❌ No                 |
| Variable set in `{ ... }` block     | ✅ Yes                |
| Exported var + child process        | ✅ Available in child |
| Child var change → parent           | ❌ No (copy-only)     |

#### Use Subshells When:
- You want to isolate changes (`cd`, variables, etc.)
- You want to run code in background (`( sleep 5; echo done ) &`)
- You need to group commands but avoid side effects
- Running temporary shell configurations (e.g., `set -e`)
- When commands are automatically piped (each in its own process)

#### Use `{}` (Group, not Subshell) When:
- You want to keep changes (e.g., change directory or set a variable)
- You want to redirect output of multiple commands
  - Example: `{ echo hi; echo there; } > output.txt`

###  Summary Table

| Goal                         | Use `( ... )` | Use `{ ... }` |
|------------------------------|----------------|----------------|
| Isolate variable changes     | ✅ Yes         | ❌ No          |
| Preserve changes             | ❌ No          | ✅ Yes         |
| Background group of commands| ✅ Yes         | ✅ Yes         |
| Redirect multi-cmd output   | ✅ Yes         | ✅ Yes         |
| Implicitly used in pipelines| ✅ Often       | ❌ No          |

###  Examples

```bash
count=1
( count=99 )
echo $count  # → 1

count=1
{ count=99; }
echo $count  # → 99
```



#### Files vs File Descriptors

#### What is a File Descriptor?
- An integer that represents an open file within a process
- Managed by the OS
- Used to read from or write to files, pipes, sockets, etc.
- File descriptors 0, 1, and 2 are standard input, output, and error respectively
- File descriptors are **unbuffered I/O**; they communicate directly with the kernel

#### What is a File?
- A named resource on disk managed by the filesystem
- Persistent and shared across processes by name, not by file descriptor

#### Key Differences

| Concept         | File Descriptor                | File                         |
|----------------|--------------------------------|------------------------------|
| What it is     | Integer handle (0, 1, 2, ...)  | Persistent storage path      |
| Managed by     | OS, per process                | Filesystem                   |
| Scope          | Per-process                    | Global to the system         |
| Accessed via   | `read()`, `write()`, `dup()`   | `open()`, file path          |
| Inheritance    | Shared via `fork()`            | Shared by path               |

#### Can We Replace a File Descriptor With a File?
- Not directly. They are fundamentally different.
- But you can:
  - Open a file and get a new file descriptor: `fd = open("file.txt", O_WRONLY);`
  - Duplicate a file descriptor with `dup()` or `dup2()`
  - Use `freopen()` in C to redirect `stdin`, `stdout`, etc.

#### In Bash:

```bash
exec 3> output.txt   # open file and assign FD 3
echo "hello" >&3     # write to FD 3 → goes into output.txt
exec 3>&-            # close FD 3
```