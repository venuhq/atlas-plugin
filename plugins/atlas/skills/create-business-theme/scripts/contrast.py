#!/usr/bin/env python3
"""Print WCAG contrast ratio for two six-digit hex colors (standard library only)."""
import argparse
import re


def luminance(value):
    if not re.fullmatch(r"#?[0-9a-fA-F]{6}", value):
        raise ValueError("Colors must have six hexadecimal digits, optionally prefixed by #")
    value = value.lstrip("#")
    channels = [int(value[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    linear = [c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4 for c in channels]
    return sum(c * weight for c, weight in zip(linear, (0.2126, 0.7152, 0.0722)))


def contrast(a, b):
    light, dark = sorted((luminance(a), luminance(b)), reverse=True)
    return (light + 0.05) / (dark + 0.05)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("foreground")
    parser.add_argument("background")
    args = parser.parse_args()
    try:
        ratio = contrast(args.foreground, args.background)
    except ValueError as error:
        parser.error(str(error))
    print(f"{ratio:.4f}:1 — {'PASS' if ratio >= 4.5 else 'FAIL'} (4.5:1 threshold)")
