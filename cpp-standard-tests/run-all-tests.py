import subprocess

test_scripts = [
    "test-with-cbmc.py",
    "test-with-goto-cc.py",
    "test-with-gcc.py",
    "test-with-clang.py"
]

result_file = "result.txt"
all_outputs = []
summaries = []

def extract_overview(output):
    # Find last occurrence of the line starting with === and take that line + all following lines
    lines = output.splitlines()
    start_idx = None
    for i in range(len(lines)-1, -1, -1):
        if lines[i].startswith("==="):
            start_idx = i
            break
    if start_idx is not None:
        return "\n".join(lines[start_idx:])
    else:
        return "(No overview found)"

for script in test_scripts:
    print(f"Running {script}...")
    proc = subprocess.run(["python3", script], capture_output=True, text=True)
    output = proc.stdout
    all_outputs.append(f"===== Output from {script} =====\n{output}\n")
    overview = extract_overview(output)
    summaries.append(f"{script} overview:\n{overview}\n")

# Now write to the result file
with open(result_file, "w") as f:
    # Write the overview summary at the top
    f.write("===== OVERVIEW SUMMARY =====\n\n")
    for summary in summaries:
        f.write(summary)
        f.write("\n")

    # Write all full outputs after the summary
    f.write("===== FULL OUTPUTS =====\n\n")
    for output in all_outputs:
        f.write(output)
        f.write("\n")

print(f"Results written to {result_file}")
