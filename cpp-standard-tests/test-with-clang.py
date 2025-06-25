import os
import subprocess

STANDARD_FLAGS = {
    "cpp98_test.cpp": "-std=c++98",
    "cpp11_test.cpp": "-std=c++11",
    "cpp17_test.cpp": "-std=c++17",
    "cpp20_test.cpp": "-std=c++20",
    "cpp23_test.cpp": "-std=c++23",
}

def run_clang_on_file(file_path, std_flag):
    """Run clang++ on the given C++ file and return the result."""
    try:
        result = subprocess.run(['clang++', std_flag, '-o', '/dev/null', file_path], capture_output=True, text=True)
        return result.stdout, result.stderr, result.returncode
    except Exception as e:
        return None, str(e), -1

def main():
    src_dir = "src"
    cpp_files = [f for f in os.listdir(src_dir) if f.endswith('.cpp')]

    cpp_order = [
        "cpp98_test.cpp",
        "cpp11_test.cpp",
        "cpp17_test.cpp",
        "cpp20_test.cpp",
        "cpp23_test.cpp"
    ]
    ordered_cpp_files = [f for f in cpp_order if f in cpp_files] + [f for f in cpp_files if f not in cpp_order]

    results = {}

    for cpp_file in ordered_cpp_files:
        cpp_path = os.path.join(src_dir, cpp_file)
        std_flag = STANDARD_FLAGS.get(cpp_file, "-std=c++20")  # Default to c++20 if unknown
        print(f"Running clang++ {std_flag} on {cpp_path}...")
        stdout, stderr, returncode = run_clang_on_file(cpp_path, std_flag)
        results[cpp_file] = {
            'stdout': stdout,
            'stderr': stderr,
            'returncode': returncode,
            'std_flag': std_flag
        }

    for file in ordered_cpp_files:
        output = results[file]
        print(f"\nResults for {file} [{output['std_flag']}] :")
        print("STDOUT:")
        print(output['stdout'])
        print("STDERR:")
        print(output['stderr'])

    print("\n=== clang++ Compilation Overview ===")
    for file in ordered_cpp_files:
        output = results[file]
        status = "PASS" if output['returncode'] == 0 else "FAIL"
        print(f"{file} [{output['std_flag']}]: {status}")

if __name__ == "__main__":
    main()