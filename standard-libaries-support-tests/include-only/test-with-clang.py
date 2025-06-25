import subprocess
from pathlib import Path
from collections import defaultdict

SRC_DIR = Path("src")

STANDARD_FLAGS = {
    # "cpp98": "-std=c++98",
    # "cpp03": "-std=c++03",
    # "cpp11": "-std=c++11",
    # "cpp14": "-std=c++14",
    # "cpp17": "-std=c++17",
    # "cpp20": "-std=c++20",
    # "cpp23": "-std=c++23",
    # "default": "",  
    "default": "-std=c++23",  
}

def find_cpp_files(src_dir):
    return [f for f in src_dir.rglob("*.cpp")]

def extract_standard_from_path(path):
    """
    Determines the standard for a given file path based on folder names.
    """
    parts = Path(path).parts
    # Recognize cppXX_headers folders (e.g. cpp11_14_headers)
    if "cpp98_03_headers" in parts:
        return "cpp03"
    if "cpp11_14_headers" in parts:
        return "cpp14"
    if "cpp17_headers" in parts:
        return "cpp17"
    if "cpp20_headers" in parts:
        return "cpp20"
    if "cpp23_headers" in parts:
        return "cpp23"
    # Recognize c_wrapper subfolders
    if "c_wrapper" in parts:
        # return "cpp11"
        idx = parts.index("c_wrapper")
        if len(parts) > idx + 1:
            sub = parts[idx + 1]
            if sub == "cpp98":
                return "cpp98"
            if sub == "cpp11":
                return "cpp11"
            # removed_in_cpp20 and others: default
            return "default"
    
    if "c_header" in parts:
        idx = parts.index("c_header")
        if len(parts) > idx + 1:
            sub = parts[idx + 1]
            if sub == "c11_additions":
                return "cpp11"
            if sub == "c23_additions":
                return "cpp23"
            if sub == "core_c_library":
                return "default"
    return "default"  # fallback

def extract_group_from_path(path):
    rel = Path(path).relative_to(SRC_DIR)
    if len(rel.parts) > 1:
        return rel.parts[0]
    return "."

def run_clang_on_file(file_path, std_flag):
    try:
        cmd = ["clang++"]
        if std_flag:
            cmd.append(std_flag)
        cmd += ["-o", "/dev/null", str(file_path)]
        result = subprocess.run(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=60
        )
        return result.returncode, result.stdout.decode(), result.stderr.decode()
    except subprocess.TimeoutExpired:
        return -999, "", "Timeout"

def main():
    cpp_files = find_cpp_files(SRC_DIR)
    results_by_group = defaultdict(list)
    standard_totals = defaultdict(int)
    standard_passed = defaultdict(int)

    for cpp_file in cpp_files:
        std = extract_standard_from_path(cpp_file)
        std_flag = STANDARD_FLAGS.get(std, STANDARD_FLAGS["default"])
        retcode, out, err = run_clang_on_file(cpp_file, std_flag)
        if retcode == 0:
            result = "PASS"
        elif retcode == -999:
            result = "TIMEOUT"
        else:
            result = "FAIL"
        flag_display = std_flag if std_flag else "(default)"
        group = extract_group_from_path(cpp_file)
        results_by_group[group].append((cpp_file, result, retcode, flag_display, std))

        standard_totals[std] += 1
        if result == "PASS":
            standard_passed[std] += 1

    print(f"{'File':<60} | {'Result':<10} | {'clang++ Return Code'} | {'Standard Flag'} | {'Group'}")
    print("-" * 120)
    for group in sorted(results_by_group):
        print(f"\nGroup: {group}")
        for cpp_file, result, retcode, flag_display, std in results_by_group[group]:
            print(f"{str(cpp_file):<60} | {result:<10} | {retcode:<17} | {flag_display:<18} | {group}")

    print("\nSummary:")
    total = sum(len(files) for files in results_by_group.values())
    passed = sum(1 for files in results_by_group.values() for _, r, _, _, _ in files if r == "PASS")
    failed = sum(1 for files in results_by_group.values() for _, r, _, _, _ in files if r == "FAIL")
    timeout = sum(1 for files in results_by_group.values() for _, r, _, _, _ in files if r == "TIMEOUT")
    print(f"Total: {total}, PASS: {passed}, FAIL: {failed}, TIMEOUT: {timeout}")

    print("\nPer-standard support:")
    def group_sort_key(g):
        if g == "c_header":
            return (0, g)
        if g == "c_wrapper":
            return (1, g)
        return (2, g)
    for group in sorted(results_by_group, key=group_sort_key):
        group_totals = defaultdict(int)
        group_passed = defaultdict(int)
        subgroups = defaultdict(list)
        for cpp_file, result, retcode, flag_display, std in results_by_group[group]:
            rel = Path(cpp_file).relative_to(SRC_DIR)
            if len(rel.parts) > 2:
                subgroups[rel.parts[1]].append((cpp_file, result, std))
            else:
                group_totals[std] += 1
                if result == "PASS":
                    group_passed[std] += 1

        if group == "c_wrapper":
            group_label = "C++ wrappers for C headers"
            subgroup_order = ["cpp98", "cpp11"]
            subgroup_display = {
                "cpp98": "added in cpp98",
                "cpp11": "added in cpp11"
            }
        elif group == "c_header":
            group_label = "C standard library headers"
            subgroup_order = ["core_c_library", "c11_additions", "c23_additions"]
            subgroup_display = {
                "core_c_library": "core C library",
                "c11_additions": "added in C11",
                "c23_additions": "added in C23"
            }
        else:
            group_label = group
            subgroup_order = []
            subgroup_display = {}

        total_group = sum(group_totals.values()) + sum(
            sum(1 for _, result, _ in subgroups[subgroup]) for subgroup in subgroups
        )
        passed_group = sum(group_passed.values()) + sum(
            sum(1 for _, result, _ in subgroups[subgroup] if result == "PASS") for subgroup in subgroups
        )
        if total_group > 0:
            print(f"{group_label}: {passed_group}/{total_group} supported")

        for subgroup in subgroup_order:
            if subgroup in subgroups:
                sub_totals = defaultdict(int)
                sub_passed = defaultdict(int)
                for _, result, std in subgroups[subgroup]:
                    sub_totals[std] += 1
                    if result == "PASS":
                        sub_passed[std] += 1
                total_sub = sum(sub_totals.values())
                passed_sub = sum(sub_passed.values())
                display_name = subgroup_display.get(subgroup, subgroup)
                print(f"    {display_name}: {passed_sub}/{total_sub} supported")
        for subgroup in sorted(subgroups):
            if subgroup not in subgroup_order:
                sub_totals = defaultdict(int)
                sub_passed = defaultdict(int)
                for _, result, std in subgroups[subgroup]:
                    sub_totals[std] += 1
                    if result == "PASS":
                        sub_passed[std] += 1
                total_sub = sum(sub_totals.values())
                passed_sub = sum(sub_passed.values())
                print(f"    {subgroup}: {passed_sub}/{total_sub} supported")

if __name__ == "__main__":
    main()