import os
import subprocess

def run_goto_cc_on_file(file_path):
    """Run goto-cc on the given C++ file and return the result."""
    try:
        result = subprocess.run(['goto-cc', '-o', '/dev/null', file_path], capture_output=True, text=True)
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
        print(f"Running goto-cc on {cpp_path}...")
        stdout, stderr, returncode = run_goto_cc_on_file(cpp_path)
        results[cpp_file] = {
            'stdout': stdout,
            'stderr': stderr,
            'returncode': returncode
        }

    for file in ordered_cpp_files:
        output = results[file]
        print(f"\nResults for {file}:")
        print("STDOUT:")
        print(output['stdout'])
        print("STDERR:")
        print(output['stderr'])

    print("\n=== goto-cc Compilation Overview ===")
    for file in ordered_cpp_files:
        output = results[file]
        status = "PASS" if output['returncode'] == 0 else "FAIL"
        print(f"{file}: {status}")

if __name__ == "__main__":
    main()