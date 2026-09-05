#!/usr/bin/env python3
"""
将图片中心裁剪到目标比例，避免生图时被拉伸压缩。

用法:
    python3 crop_to_ratio.py <input_path> <output_path> --ratio <宽:高>

示例:
    python3 crop_to_ratio.py input.jpg output.jpg --ratio 9:19.5
    python3 crop_to_ratio.py input.jpg output.jpg --ratio 3:4
"""

import argparse
from PIL import Image


def crop_to_ratio(input_path: str, output_path: str, ratio_str: str):
    im = Image.open(input_path).convert("RGB")
    w, h = im.size

    parts = ratio_str.split(":")
    target_w = float(parts[0])
    target_h = float(parts[1])
    target_ratio = target_w / target_h

    current_ratio = w / h

    if abs(current_ratio - target_ratio) < 0.01:
        im.save(output_path, quality=95)
        print(f"比例接近，直接保存: {w}x{h} -> {output_path}")
        return

    if current_ratio > target_ratio:
        new_w = int(h * target_ratio)
        left = (w - new_w) // 2
        right = left + new_w
        cropped = im.crop((left, 0, right, h))
    else:
        new_h = int(w / target_ratio)
        top = (h - new_h) // 2
        bottom = top + new_h
        cropped = im.crop((0, top, w, bottom))

    cropped.save(output_path, quality=95)
    print(f"已裁剪: {w}x{h} (比例 {current_ratio:.3f}) -> {cropped.size} (比例 {target_ratio:.3f})")
    print(f"输出: {output_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="中心裁剪图片到目标比例")
    parser.add_argument("input_path", help="输入图片路径")
    parser.add_argument("output_path", help="输出图片路径")
    parser.add_argument("--ratio", required=True, help="目标比例，如 9:19.5 或 3:4")
    args = parser.parse_args()
    crop_to_ratio(args.input_path, args.output_path, args.ratio)
