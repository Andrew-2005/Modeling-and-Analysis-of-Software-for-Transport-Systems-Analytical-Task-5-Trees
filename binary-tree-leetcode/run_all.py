import subprocess
import sys
from pathlib import Path


TASK_FILES = (
    "task1_same_tree.py",
    "task2_symmetric_tree.py",
    "task3_invert_tree.py",
    "task4_kth_smallest_bst.py",
    "task5_serialize_deserialize.py",
    "task6_max_path_sum.py",
    "task7_camera.py",
    "task8_vertical_traversal.py",
    "task9_recover_preorder.py",
)


# Запускає приклади кожної задачі й повертає код помилки, якщо є збій.
def main():
    project_dir = Path(__file__).resolve().parent
    failed = False
    for filename in TASK_FILES:
        result = subprocess.run(
            [sys.executable, "-E", "-B", str(project_dir / filename)],
            capture_output=True,
            text=True,
        )
        passed = result.returncode == 0 and result.stdout.strip() == "OK"
        if passed:
            print(f"{filename}: OK")
        else:
            print(f"{filename}: FAIL")
            for output in (result.stdout, result.stderr):
                if output:
                    print(output.rstrip())
            failed = True
    return int(failed)


if __name__ == "__main__":
    raise SystemExit(main())
