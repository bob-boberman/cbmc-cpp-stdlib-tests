# cbmc-cpp-stdlib-tests
Simple test cases for verifying CBMC’s C and C++ standard library header support in C++ programs.

I created these during my thesis work to check the current state of CBMC's C++ support without much optimization.


⚠️ **Note:**  
This is **not** a polished or comprehensive verification suite — it’s a rudimentary setup, and GitHub Copilot generated some of the code.  
I experimented a bit with compiler flags for optimization, but there’s likely still room for improvement; it should be sufficient to show a trend.

All programs are tested as C++ programs using the .cpp extension.

Here are the results for CBMC 6.6.0 (with GCC 15.1.1 and Clang 20.1.6 used for sanity checks):


## 📌 Import-Only Tests

In the corresponding test programs, the libraries are included but not used. For example:

```cpp 
#include <stdio.h>

int main() {}

```


### Overview

| Tool                 | Total | PASS | FAIL | TIMEOUT |
|-----------------------|-------|-------|-------|---------|
| **CBMC**              | 142   | 79    | 63    | 0       | 
| **goto-cc**           | 142   | 66    | 76    | 0       | 
| **GCC**               | 142   | 140   | 2     | 0       | 
| **Clang**             | 142   | 141   | 1     | 0       | 

### Per-standard support (Import Only)

| Standard                    | CBMC | goto-cc | GCC | Clang |
|-----------------------------|-------|---------|------|--------|
| C standard library headers   | 22/27 | 22/27  | 27/27 | 27/27 |
| -> core C library               | 15/18 | 15/18  | 18/18 | 18/18 |
| -> added in C11                 | 6/8   | 6/8    | 8/8   | 8/8   |
| -> added in C23                 | 1/1   | 1/1    | 1/1   | 1/1   |
| C++ wrappers for C headers   | 21/31 | 22/31  | 31/31 | 31/31 |
| -> added in cpp98               | 15/18 | 14/18  | 18/18 | 18/18 |
| -> added in cpp11               | 5/8   | 5/8    | 8/8   | 8/8   |
| -> removed_in_cpp20             | 1/5   | 3/5    | 5/5   | 5/5   |
| cpp11_14_headers             | 1/21  | 0/21   | 21/21 | 21/21 |
| cpp17_headers                | 8/8   | 0/8    | 7/8   | 8/8   |
| cpp20_headers                | 14/15 | 13/15  | 15/15 | 15/15 |
| cpp23_headers                | 8/9   | 8/9    | 8/9   | 8/9   |
| cpp98_03_headers             | 5/31  | 1/31   | 31/31 | 31/31 |

---

## 📌 Import + Usage Tests

Simple test programs are provided for the imported libraries, but they do not cover the full range of functionality. For example: 

```cpp 
#include <stdio.h>

int main() {
    printf("Test\n");
    return 0;
}

```

### Overview

| Tool                 | Total | PASS | FAIL | TIMEOUT 
|-----------------------|-------|-------|-------|---------
| **CBMC**              | 142   | 29    | 113   | 0       | 
| **goto-cc**           | 142   | 38    | 104   | 0       | 
| **GCC**               | 142   | 134   | 8     | 0       | 
| **Clang**             | 142   | 134   | 8     | 0       | 

### Per-standard support (Import + Usage)

| Standard                    | CBMC | goto-cc | GCC | Clang |
|-----------------------------|-------|---------|------|--------|
| C standard library headers   | 14/27 | 18/27  | 26/27 | 26/27 |
| -> C library               | 10/18 | 13/18  | 18/18 | 18/18 |
| -> added in C11                 | 4/8   | 5/8    | 7/8   | 7/8   |
| -> added in C23                 | 0/1   | 0/1    | 1/1   | 1/1   |
| C++ wrappers for C headers   | 13/31 | 19/31  | 29/31 | 29/31 |
| -> added in cpp98               | 9/18  | 13/18  | 18/18 | 18/18 |
| -> added in cpp11               | 3/8   | 4/8    | 7/8   | 7/8   |
| -> removed_in_cpp20             | 1/5   | 2/5    | 4/5   | 4/5   |
| cpp11_14_headers             | 0/21  | 0/21   | 21/21 | 21/21 |
| cpp17_headers                | 0/8   | 0/8    | 7/8   | 8/8   |
| cpp20_headers                | 1/15  | 1/15   | 14/15 | 14/15 |
| cpp23_headers                | 0/9   | 0/9    | 6/9   | 5/9   |
| cpp98_03_headers             | 1/31  | 0/31   | 31/31 | 31/31 |

---





