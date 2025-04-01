import sys
import os
from contextlib import nullcontext

import pytest

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from library import  Library
from book import  Book

def test_add_book():
    l=Library()
    b=Book("duplikatim2","yona# sapir")
    after_add=len(l.books)
    l.add_book(b)
    before_add=len(l.books)
    assert  after_add+1==before_add

def test_add_book_with_empty_author():
    with pytest.raises(ValueError, match="Title and author must not be empty."):
        Book("Valid Title", "")

def add_user():
    l = Library()
    try:
        (l.add_user(""))
    except ValueError as e:
       assert e.__eq__("Username must not be empty.")


def test_check_out_book():
    l=Library()
    b=Book("hjk","vbb")
    l.add_book(b)
    l.add_user("yael")
    l.check_out_book("yael",b)
    assert b.is_checked_out==True

def search_books():
    l = Library()
    b = Book("hjk", "vbb")
    l.add_book(b)
    book = l.search_books(b)
    assert b==book

