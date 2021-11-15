"""
This file changes all SVGs in the CWD to remove colons from non-urls. This is useful because in chromium-based browsers there is a bug where embedded SVG IDs cannot contain colons or everything will break
"""
import os
import re

for root, dirs, files in os.walk("/"):
    for file in files:
        if file.endswith(".svg"):
            with open(os.path.join(root, file)) as f:
                svg = f.read()
                svg = re.sub(r':(?!\/)', "", svg)
            with open(os.path.join(root, file), "w") as f:
                f.write(svg)
