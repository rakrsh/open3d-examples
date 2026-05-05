import os
import subprocess
import sys
import threading
import tkinter as tk
from pathlib import Path
from tkinter import messagebox, ttk

ROOT = Path(__file__).resolve().parent
SCRIPT_DIRS = [ROOT / "src"/ "scripts" / "mesh", ROOT / "src" / "scripts" / "point_cloud"]


def get_example_scripts():
    examples = []
    for category_dir in SCRIPT_DIRS:
        if not category_dir.exists():
            continue
        category = category_dir.name
        for script_path in sorted(category_dir.glob("*.py")):
            examples.append((f"{category}/{script_path.name}", script_path))
    return examples


class VisualizationLauncher(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Open3D Examples Launcher")
        self.geometry("680x520")
        self.resizable(True, True)

        self.examples = get_example_scripts()
        self.process = None

        self._build_ui()

    def _build_ui(self):
        frame = ttk.Frame(self, padding=12)
        frame.pack(fill=tk.BOTH, expand=True)

        title = ttk.Label(frame, text="Open3D Example Visualizer", font=(None, 16, "bold"))
        title.pack(anchor=tk.W, pady=(0, 12))

        list_frame = ttk.Frame(frame)
        list_frame.pack(fill=tk.BOTH, expand=True)

        scrollbar = ttk.Scrollbar(list_frame, orient=tk.VERTICAL)
        self.examples_list = tk.Listbox(
            list_frame,
            yscrollcommand=scrollbar.set,
            font=(None, 11),
            selectmode=tk.SINGLE,
            activestyle="dotbox",
            exportselection=False,
        )
        scrollbar.config(command=self.examples_list.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.examples_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        for name, _ in self.examples:
            self.examples_list.insert(tk.END, name)

        button_frame = ttk.Frame(frame)
        button_frame.pack(fill=tk.X, pady=(12, 0))

        run_button = ttk.Button(button_frame, text="Run Selected Example", command=self.run_selected_example)
        run_button.pack(side=tk.LEFT)

        refresh_button = ttk.Button(button_frame, text="Refresh List", command=self.refresh_examples)
        refresh_button.pack(side=tk.LEFT, padx=(8, 0))

        self.status_var = tk.StringVar(value="Select an example and click Run.")
        status_label = ttk.Label(frame, textvariable=self.status_var, relief=tk.SUNKEN, anchor=tk.W)
        status_label.pack(fill=tk.X, pady=(12, 0))

        output_label = ttk.Label(frame, text="Example output:")
        output_label.pack(anchor=tk.W, pady=(12, 0))

        output_frame = ttk.Frame(frame)
        output_frame.pack(fill=tk.BOTH, expand=True)

        self.output_text = tk.Text(output_frame, height=12, wrap=tk.NONE, state=tk.DISABLED)
        self.output_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        output_scroll_y = ttk.Scrollbar(output_frame, orient=tk.VERTICAL, command=self.output_text.yview)
        output_scroll_y.pack(side=tk.RIGHT, fill=tk.Y)
        self.output_text.configure(yscrollcommand=output_scroll_y.set)

    def refresh_examples(self):
        self.examples = get_example_scripts()
        self.examples_list.delete(0, tk.END)
        for name, _ in self.examples:
            self.examples_list.insert(tk.END, name)
        self.status_var.set("Example list refreshed.")

    def run_selected_example(self):
        selection = self.examples_list.curselection()
        if not selection:
            messagebox.showwarning("No Example Selected", "Please select an example to run.")
            return

        index = selection[0]
        script_name, script_path = self.examples[index]

        if self.process is not None and self.process.poll() is None:
            messagebox.showinfo("Example Running", "An example is already running. Close it before starting another.")
            return

        self.status_var.set(f"Running {script_name}...")
        self._append_output(f">>> Launching {script_name}\n")
        self.process = subprocess.Popen(
            [sys.executable, str(script_path)],
            cwd=str(ROOT),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            bufsize=1,
        )

        threading.Thread(target=self._capture_process_output, daemon=True).start()

    def _capture_process_output(self):
        assert self.process is not None
        for stream_name, stream in (("stdout", self.process.stdout), ("stderr", self.process.stderr)):
            threading.Thread(target=self._read_stream, args=(stream_name, stream), daemon=True).start()

        self.process.wait()
        code = self.process.returncode
        status = "Finished" if code == 0 else f"Exited with code {code}"
        self.status_var.set(status)
        self._append_output(f"<<< {status}\n")

    def _read_stream(self, stream_name, stream):
        for line in stream:
            self._append_output(line)

    def _append_output(self, text):
        self.output_text.configure(state=tk.NORMAL)
        self.output_text.insert(tk.END, text)
        self.output_text.see(tk.END)
        self.output_text.configure(state=tk.DISABLED)


if __name__ == "__main__":
    app = VisualizationLauncher()
    app.mainloop()
