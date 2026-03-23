---
description: Compile chapters into a DOCX file
---

Compile the manuscript to DOCX.

## Check prerequisites

1. Check if `chapters/` has any `.md` files. If empty, stop and tell user there's nothing to compile.
2. Check if Python is available: `python --version` or `python3 --version`
3. Check if python-docx is installed: `python -c "import docx"` — if not, run `pip install python-docx`

## Run converter

```bash
python "${CLAUDE_PLUGIN_ROOT}/converter/chapters_to_docx.py"
```

The converter:
- Reads all `chapters/*.md` in alphabetical order
- Outputs to `versions/[title]_vNN.docx` (auto-increments version number)

## After compile

Tell user:
- Output file path
- Chapter count and total words included
- If any chapters were skipped (non-standard filenames)

If the converter fails:
- Show the error
- Check if `versions/` directory exists (create if not)
- Check file permissions
- Do not attempt to write DOCX manually
