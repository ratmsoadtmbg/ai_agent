import os
import subprocess

def run_python_file(working_directory, file):
    wd_path = os.path.abspath(working_directory)
    full_path = os.path.abspath(os.path.join(wd_path, file))
    try:
        if not full_path.startswith(wd_path):
            return f'Error: Cannot execute "{file}" as it is outside the permitted working directory'
        if not os.path.exists(full_path):
            return f'Error: File "{file}" not found.'
        if not file.endswith(".py"):
            return f'Error: "{file}" is not a Python file.'
        runtime = subprocess.run(["python", f"{full_path}"], timeout=30, capture_output=True, cwd=wd_path)
        if len(runtime.stdout) == 0 and len(runtime.stderr) == 0:
            return "No output produced."
        if runtime.returncode != 0:
            return f'STDOUT: {runtime.stdout.decode("utf-8")}\nSTDERR: {runtime.stderr.decode("utf-8")}\nProcess exited with code {runtime.returncode}'
        return f'STDOUT: {runtime.stdout.decode("utf-8")}\nSTDERR: {runtime.stderr.decode("utf-8")}'

    except Exception as e:
        return f"Error: executing Python file: {e}"