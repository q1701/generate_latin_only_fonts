# -*- coding: utf-8 -*-
import sys
import os
import fontforge


def _clear_glyphs_except_latin(font):
    codepoints = [(0x0020, 0x002F),  # ASCII punctuation and symbols（ASCII句読点と記号）
                  (0x0030, 0x0039),  # ASCII digits（ASCII数字）
                  (0x003A, 0x0040),  # ASCII punctuation and symbols（ASCII句読点と記号）
                  (0x0041, 0x005A),  # Uppercase Latin alphabet（大文字ラテン・アルファベット）
                  (0x005B, 0x0060),  # ASCII punctuation and symbols（ASCII句読点と記号）
                  (0x0061, 0x007A),  # Lowercase Latin alphabet（小文字ラテン・アルファベット）
                  (0x007B, 0x007E)]  # ASCII punctuation and symbols（ASCII句読点と記号）
    font.selection.all()
    for codepoint in codepoints:
        first, last, = codepoint
        font.selection.select(('less', 'ranges', 'unicode'), first, last)
    font.clear()


def generate_latin_only_font(src_file, dest_dir):
    if not os.path.exists(src_file):
        raise Exception('File not found: \'' + src_file + '\'')
    if not os.path.exists(dest_dir):
        os.mkdir(dest_dir)
    if not os.path.isdir(dest_dir):
        raise Exception('\'' + dest_dir + '\' must be a directory')
    font = fontforge.open(src_file)
    _clear_glyphs_except_latin(font)
    dest_file = os.path.basename(src_file)
    font.generate(os.path.join(dest_dir, dest_file))
    font.close()


if __name__ == '__main__':
    if len(sys.argv) <= 2:
        print('Usage: ' + sys.argv[0] + ' <source font file(s)> <destination directory>')
    else:
        for src_file in sys.argv[1:-1]:
            generate_latin_only_font(src_file, sys.argv[-1])
