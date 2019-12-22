# Notes

This is meant to be complementary to the git logs: I am not disciplined
enough to write fully descriptive commit messages.

December 22, 2019
-----------------

- Copied all original code from Thonny's repo.
- Removed everything dealing with packaging and installation, including
  setup.py; this project is meant to be run locally.
- Created local virtual environment, installing all original required packages.
- Renamed "thonny" to "ynnoht" everywhere.
- Removed support for most languages, keeping only French and English.
- Creating my own .bat files to update .pot files; Thonny seems to rely
  on a third-party package (Babel) to do this.

- Verified that I could start ynnoht successfully using

    python -m ynnoht

- Using pydeps, created a svg file (original_ynnoht.svg) that is very useful
  for visualizing all dependencies.
- Removed all mentions of Birdseye; created ynnoht2.svg
- Confirmed that everything still works as expected.

- Removed CircuitPython, esp, microbit, MicroPython
- Produced new graph file (ynnoht3.svg); significanly fewer files.
