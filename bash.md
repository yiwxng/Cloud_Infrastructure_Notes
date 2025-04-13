# Shell Programming - Bash 

## 1. core of bash 

### 1.1 Interactive and non interactive shell 

### 1.2 local and env variable 




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

