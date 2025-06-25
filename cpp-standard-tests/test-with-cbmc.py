import os
import subprocess

CBMC_STANDARD_FLAGS = {
    "cpp98_test.cpp": "--cpp98",
    "cpp03_test.cpp": "--cpp03",
    "cpp11_test.cpp": "--cpp11",
    # For cpp17, cpp20, cpp23, CBMC does not support a flag, so use default (cpp98)
}

def run_cbmc_on_file(file_path, std_flag):
    """Run CBMC on the given C++ file and return the result."""
    try:
        cmd = ['cbmc']
        if std_flag:
            cmd.append(std_flag)
        cmd.append(file_path)
        result = subprocess.run(cmd, capture_output=True, text=True)
        return result.stdout, result.stderr, result.returncode
    except Exception as e:
        return None, str(e), -1

def main():
    src_dir = "src"
    cpp_files = [f for f in os.listdir(src_dir) if f.endswith('.cpp')]

    # Order files by C++ standard version if possible
    cpp_order = [
        "cpp98_test.cpp",
        "cpp03_test.cpp",
        "cpp11_test.cpp",
        "cpp17_test.cpp",
        "cpp20_test.cpp",
        "cpp23_test.cpp"
    ]
    # Add any other .cpp files not in the list at the end
    ordered_cpp_files = [f for f in cpp_order if f in cpp_files] + [f for f in cpp_files if f not in cpp_order]

    results = {}

    for cpp_file in ordered_cpp_files:
        cpp_path = os.path.join(src_dir, cpp_file)
        std_flag = CBMC_STANDARD_FLAGS.get(cpp_file, None)
        print(f"Running CBMC {'('+std_flag+')' if std_flag else '(default)'} on {cpp_path}...")
        stdout, stderr, returncode = run_cbmc_on_file(cpp_path, std_flag)
        results[cpp_file] = {
            'stdout': stdout,
            'stderr': stderr,
            'returncode': returncode,
            'std_flag': std_flag if std_flag else "(default)"
        }

    # Output results
    for file in ordered_cpp_files:
        output = results[file]
        print(f"\nResults for {file} [{output['std_flag']}] :")
        print("STDOUT:")
        print(output['stdout'])
        print("STDERR:")
        print(output['stderr'])

    # Evaluation overview
    print("\n=== CBMC Compilation Overview ===")
    for file in ordered_cpp_files:
        output = results[file]
        status = "PASS" if output['returncode'] == 0 else "FAIL"
        print(f"{file} [{output['std_flag']}]: {status}")

if __name__ == "__main__":
    main()