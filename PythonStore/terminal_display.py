import sys

import arabic_reshaper
from bidi.algorithm import get_display


def configure_terminal():
    """استخدم UTF-8 لقراءة وكتابة النص العربي في الطرفية."""
    for stream in (sys.stdin, sys.stdout):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8")


def print_terminal(text=""):
    """تشكيل النص العربي وعرضه باتجاه القراءة الصحيح."""
    shaped_text = arabic_reshaper.reshape(str(text))
    print(get_display(shaped_text))


def input_terminal(prompt=""):
    """عرض المطالبة بالعربية مع قراءة إدخال المستخدم."""
    shaped_prompt = arabic_reshaper.reshape(str(prompt))
    return input(get_display(shaped_prompt))
