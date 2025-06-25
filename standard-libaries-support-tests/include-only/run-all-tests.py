import subprocess
import re

test_scripts = [
    "test-with-cbmc.py",
    "test-with-goto-cc.py",
    "test-with-gcc.py",
    "test-with-clang.py"
]

result_file = "result.txt"
all_outputs = []
summaries = []

def extract_summary(output):
    # The summary starts at the line "Summary:" and includes all lines until no more lines or blank line after Per-standard support
    lines = output.splitlines()
    start_idx = None
    # Find line with "Summary:"
    for i, line in enumerate(lines):
        if line.strip() == "Summary:":
            start_idx = i
            break
    if start_idx is None:
        return "(No summary found)"

    # We want to capture lines from start_idx until the block ends.
    # Since the summary includes a blank line and then the "Per-standard support:" block, let's grab everything after start_idx.
    summary_lines = []
    for line in lines[start_idx:]:
        summary_lines.append(line)
    return "\n".join(summary_lines)

for script in test_scripts:
    print(f"Running {script}...")
    proc = subprocess.run(["python3", script], capture_output=True, text=True)
    output = proc.stdout
    all_outputs.append(f"===== Output from {script} =====\n{output}\n")
    summary = extract_summary(output)
    summaries.append(f"{script} summary:\n{summary}\n")

with open(result_file, "w") as f:
    # Write all summaries first
    f.write("===== SUMMARY OVERVIEW =====\n\n")
    for summary in summaries:
        f.write(summary)
        f.write("\n")

    # Then write all full outputs
    f.write("===== FULL OUTPUTS =====\n\n")
    for output in all_outputs:
        f.write(output)
        f.write("\n")

print(f"Results written to {result_file}")
