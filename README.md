# 🧬 Reverse Engineering & Binary Patching

This repository is a collection of scripts and experiments for **reverse engineering** and **binary patching** of ELF executables, with a focus on understanding runtime validation and message tampering. Tasks are solved using static analysis, binary manipulation, and custom assembly patching.

---

## 🔍 Project Scope

The project is divided into two main sections:

### Q1: Message Validation & Patching
- Validate binary-encoded messages using a custom validator.
- Apply minimal byte-level patches to message files to make them pass validation.
- Patch the validation binary itself to always return success.

### Q2: Executable Behavior Modification
- Patch ELF binary `readfile` to:
  - Interpret `#!` lines as shell commands.
  - Print all other lines as-is.
- Implemented using inline x86 assembly and position-independent patching.

---

## 🧱 Directory Structure

```
reverse-engineering-patching/
├── q1/
│   ├── msgcheck               # Binary that validates messages
│   ├── *.msg                  # Input message files
│   ├── *.py                   # Scripts to analyze/fix/patch messages or binary
│   └── *.txt                  # Written answers or observations
├── q2/
│   ├── readfile               # Target binary to patch
│   ├── patch1.asm             # Assembly patch 1
│   ├── patch2.asm             # Assembly patch 2
│   ├── q2.py                  # Python patching tool using `infosec` module
│   └── *.txt                  # Explanations or writeups
├── smoketest.py              # Validates solutions across Q1 & Q2
```

---

## 🛠️ Usage

### 🔧 Run a Patch Script (Q1)

```bash
python3 q1/q1b.py q1/02.msg
./q1/msgcheck q1/02.msg.fixed
```

### 🧪 Run Smoke Tests

```bash
python3 smoketest.py
```

This will:
- Validate message integrity.
- Test patched messages.
- Confirm that binary patches produce correct behavior.

### 🔨 Patch Binaries (Q2)

```bash
python3 q2/q2.py q2/readfile
chmod +x q2/readfile.patched
./q2/readfile.patched q2/1.txt
```

---

## 🧠 Requirements

- Python 3.8+
- `infosec` module for patching helpers
- GCC/Make (if rebuilding/testing patched binaries)

---

## 🎯 Learning Objectives

- Understand binary layout and patching with offsets.
- Perform byte-wise mutation to bypass validation.
- Use `infosec.core.assemble` for assembling and injecting shellcode.
- Work with ELF internals and dynamic instruction patching.

---

## 📜 License

For educational use only.

---

## 👨‍💻 Author

Created by [mati1mati1](https://github.com/mati1mati1) — Reverse engineering enthusiast.
