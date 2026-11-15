"""Regenerate the beginner's source reference using Python's own syntax parser."""

import ast
import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

PURPOSES = {
    "app/streamlit_app.py": "The visible demo: upload, detect, read, show evidence, review, and export a batch.",
    "riskgate/calibration.py": "Learn and use a small model that estimates whether a complete OCR answer is correct.",
    "riskgate/config.py": "Keep shared file paths and experiment settings in one place.",
    "riskgate/contracts.py": "Define the fields in a labelled example and an OCR result.",
    "riskgate/data.py": "Load labels, keep related images together, and crop plate rectangles.",
    "riskgate/features.py": "Turn the crop and OCR result into six numbers for calibration.",
    "riskgate/grammar.py": "Check whether characters resemble a plate format; this cannot verify a real registration.",
    "riskgate/metrics.py": "Measure exact text matches, character errors, calibration, and error versus coverage.",
    "riskgate/router.py": "Choose validation thresholds and accept, escalate, or review a reading.",
    "riskgate/stability.py": "Run two transformed-image reads and veto acceptance when either disagrees.",
    "riskgate/engines/easyocr_engine.py": "Adapt EasyOCR output to the common EngineResult format and order text boxes.",
    "riskgate/engines/fastplate_engine.py": "Load the local ONNX plate reader and adapt its output.",
    "scripts/baseline_v2.py": "Compare readers on labelled crops and record predictions and features.",
    "scripts/detector.py": "Prepare YOLO box labels, fine-tune the detector, and measure box overlap.",
    "scripts/eval_end_to_end.py": "Evaluate full photos, counting missed plates as failed text readings.",
    "scripts/eval_router.py": "Fit calibration, choose validation thresholds, and evaluate the saved policy.",
    "scripts/eval_stability.py": "Compare the original policy with the optional veto on the existing demo gallery.",
    "scripts/explain_code.py": "Generate this line reference from the actual source and record source fingerprints.",
    "scripts/import_extra_detection.py": "Screen the additional box-only source and add eligible photos to detector training.",
    "scripts/label_tool.py": "Support manual inspection of proposed labels.",
    "scripts/package_submission.py": "Build the portable academic demo ZIP from an explicit list of folders and assets.",
    "scripts/plot_results.py": "Draw charts from saved experiment results.",
    "scripts/prepare_gallery.py": "Copy selected original demo scenes and write their gallery manifest.",
    "scripts/prepare_indian.py": "Read the main dataset, group related examples, and prepare labels and splits.",
}


def expression(node: ast.AST) -> str:
    """Translate common Python expressions into short, concrete reading instructions."""
    if isinstance(node, ast.Call):
        name = ast.unparse(node.func)
        actions = {"normalize": "uppercase the text and remove characters outside A–Z and 0–9",
                   "predict": "calculate the correctness estimate using the saved calibration model",
                   "plate_features": "extract the six input signals from the crop and OCR result",
                   "route": "apply the format and confidence acceptance rules",
                   "check_stability": "read resized and brightened copies and compare with the original text",
                   "apply_veto": "change an accepted answer to review if the stability check failed",
                   "classify": "check the plate format", "fit": "learn the calibration parameters",
                   "normalize": "uppercase the text and keep only letters A–Z and digits 0–9"}
        if name in actions:
            return actions[name]
        return f"call `{name}` with the inputs shown to obtain its result"
    if isinstance(node, ast.Constant):
        return f"use the fixed value `{repr(node.value)}`" if not isinstance(node.value, str) or len(node.value) < 100 else "use this fixed text block (presentation content, not model logic)"
    if isinstance(node, ast.Dict):
        return "build a dictionary: each key names the value stored beside it"
    if isinstance(node, (ast.ListComp, ast.DictComp, ast.SetComp, ast.GeneratorExp)):
        return "build or iterate values using the inline `for` loop and any `if` filter shown"
    if isinstance(node, ast.Subscript):
        return f"look up or slice `{ast.unparse(node.value)}` using the index or range in brackets"
    if isinstance(node, ast.IfExp):
        return f"choose the first value if `{ast.unparse(node.test)}` is true, otherwise choose the value after `else`"
    if isinstance(node, ast.Compare):
        return f"check whether `{ast.unparse(node)}` is true"
    if isinstance(node, ast.BinOp):
        return f"calculate `{ast.unparse(node)}`; `/` divides, `*` multiplies, and paths use `/` to join folders"
    if isinstance(node, ast.Tuple):
        return "collect the values in order (a tuple), which can also be unpacked into separate names"
    return f"evaluate `{ast.unparse(node)}` using the values currently in memory"


def explanation(node: ast.AST) -> str:
    if isinstance(node, (ast.Import, ast.ImportFrom)):
        return f"Make the named library tools available here: `{ast.unparse(node)}`. Importing a project module makes its reusable functions accessible."
    if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
        doc = ast.get_docstring(node)
        return f"Define `{node.name}`; its indented body runs when called. " + (doc.splitlines()[0] if doc else "Inputs are in parentheses; the return annotation describes the expected output type.")
    if isinstance(node, ast.ClassDef):
        return f"Define the `{node.name}` object type, grouping its data and methods."
    if isinstance(node, (ast.Assign, ast.AnnAssign)):
        targets = ', '.join(ast.unparse(t) for t in node.targets) if isinstance(node, ast.Assign) else ast.unparse(node.target)
        return f"Store the result in `{targets}`: {expression(node.value)}." if node.value else f"Declare the expected type of `{targets}`."
    if isinstance(node, ast.AugAssign):
        return f"Update `{ast.unparse(node.target)}` using the operation shown and the new value."
    if isinstance(node, ast.Return):
        return "Finish this function and " + (expression(node.value) + "; send that result to its caller." if node.value else "send back no value (`None`).")
    if isinstance(node, ast.If):
        return f"Run the indented branch only when `{ast.unparse(node.test)}` is true."
    if isinstance(node, ast.For):
        return f"For each item from `{ast.unparse(node.iter)}`, name it `{ast.unparse(node.target)}` and run the indented body."
    if isinstance(node, ast.With):
        return "Enter the shown context: an open file is closed afterwards; a Streamlit context places widgets inside that panel."
    if isinstance(node, ast.Assert):
        return f"Check `{ast.unparse(node.test)}`. If false, stop with an assertion error: the tested expectation failed."
    if isinstance(node, ast.Raise):
        return "Stop this operation with the shown exception and message, rather than silently continuing."
    if isinstance(node, ast.Try):
        return "Try the indented work; matching failures are handled by the later `except` branch."
    if isinstance(node, ast.ExceptHandler):
        return "Handle the specified exception types using the indented recovery code."
    if isinstance(node, ast.Continue):
        return "Skip the rest of this loop iteration and move to the next item."
    if isinstance(node, ast.Expr):
        return expression(node.value).capitalize() + "."
    return "Continue the enclosing Python statement using the syntax shown."


def main() -> None:
    paths = sorted(path for folder in ("riskgate", "app", "scripts", "tests")
                   for path in (ROOT / folder).rglob("*.py"))
    output = ["# Every Python source line explained", "",
              "Read [FACULTY_EXPLANATION.md](FACULTY_EXPLANATION.md) first for the system and mathematics.", "",
              "This is a generated syntax companion, not a claim that model weights or third-party library internals are explained line by line. Every physical line of our Python source, including tests and this generator, appears below. Long statements are explained at their first line; following lines identify the statement they continue. Source fingerprints let you detect an outdated guide. Regenerate with `./venv/bin/python -m scripts.explain_code`.", "",
              "Python basics: indentation groups instructions. `=` stores a value; `==` compares values. A function is a named recipe. A class describes an object. A dictionary holds named values. A list holds ordered values. `None` means missing. `True`/`False` are yes/no. Type hints document expected values; they do not enforce them automatically. An array stores image pixel numbers. `image[y1:y2, x1:x2]` selects rows then columns; the ending coordinates are excluded.", ""]
    for path in paths:
        source = path.read_text()
        relative = path.relative_to(ROOT).as_posix()
        tree = ast.parse(source)
        statements = [node for node in ast.walk(tree) if isinstance(node, (ast.stmt, ast.ExceptHandler))]
        output += [f"## {relative}", "", PURPOSES.get(relative, "Automated checks for the named component." if relative.startswith("tests/") else "Package marker: allows this folder to hold importable modules."), "",
                   f"Source SHA-256: `{hashlib.sha256(source.encode()).hexdigest()}`", ""]
        for number, line in enumerate(source.splitlines(), 1):
            containing = [node for node in statements if node.lineno <= number <= getattr(node, "end_lineno", node.lineno)]
            containing.sort(key=lambda node: (getattr(node, "end_lineno", node.lineno) - node.lineno, -node.lineno))
            node = containing[0] if containing else None
            stripped = line.strip()
            if not stripped:
                note = "Blank line: separates ideas for readability; performs no action."
            elif stripped.startswith("#"):
                note = "Comment for the reader; Python does not execute it. " + stripped[1:].strip()
            elif node is not None and node.lineno == number:
                note = explanation(node)
            elif stripped.startswith("else:"):
                note = "Run this branch when the associated condition was false."
            elif node is not None:
                note = f"Continuation of the statement starting at line {node.lineno}; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation."
            else:
                note = "Decorator or syntax belonging to the following definition; modifies how that definition is used (for example, caching)."
            output += [f"**Line {number}**", "```python", line, "```", note, ""]
        if not source:
            output += ["Empty package marker; there are no executable lines.", ""]
    for filename in ("requirements.txt", "Makefile", ".gitignore", ".streamlit/config.toml", "presentation/presentation.html"):
        output += [f"## {filename}", "", "Supporting configuration or presentation source; not part of neural inference.", ""]
        for number, line in enumerate((ROOT / filename).read_text().splitlines(), 1):
            stripped = line.strip()
            if not stripped:
                note = "Blank line for readability."
            elif filename == "requirements.txt":
                note = f"Install the Python package `{stripped}`. Brackets request optional extras; no version is pinned."
            elif filename == ".gitignore":
                note = f"Exclude paths matching `{stripped}` from ordinary Git tracking; this does not delete existing files."
            elif filename == "Makefile":
                note = "Declare a command target (or run its indented shell recipe). `check` runs the tests through the project's virtual environment. `.PHONY` ensures a same-named file cannot suppress the command."
            elif filename.endswith("toml"):
                note = "Start a settings section with brackets, or assign the shown setting. Theme settings control appearance; maxUploadSize sets Streamlit's per-file upload limit in MB."
            elif "<section" in line:
                note = "Define one presentation slide. The visible headings, paragraphs, numbers, links, and image references on this line make up its content. Class names select the appearance rules in the style block."
            elif "<script>" in line:
                note = "Keep the current slide index; collect slides; move within valid bounds, toggle the active class, update the counter, and listen for left/right/space keys. preventDefault stops space from scrolling."
            elif "{" in line and "}" in line:
                note = "CSS appearance rules: selectors before braces choose elements; name:value declarations set their layout, size, colors, spacing, or print behaviour. They do not process plate images."
            elif "<div class=" in line:
                note = "Render navigation controls and the slide counter; the arrow buttons call move with minus or plus one."
            else:
                note = "HTML document structure or metadata: opening tags begin an element, closing tags end it; meta tags configure text encoding and viewport; style holds appearance rules."
            output += [f"**Line {number}**", "```text", line, "```", note, ""]
    (ROOT / "docs/CODE_WALKTHROUGH.md").write_text('\n'.join(output))
    print(f"Explained {len(paths)} Python files")


if __name__ == "__main__":
    main()
