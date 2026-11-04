#!/usr/bin/env python3
"""Validate the static site: local links, assets, in-page anchors, basic HTML sanity."""
import os, sys, re
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
strict = "--strict" in sys.argv

class P(HTMLParser):
    def __init__(self):
        super().__init__(); self.links=[]; self.ids=set(); self.title=None; self._in_title=False; self.h1=0; self.lang=None; self.imgs_noalt=0
    def handle_starttag(self, tag, attrs):
        a=dict(attrs)
        if tag=="html": self.lang=a.get("lang")
        if "id" in a: self.ids.add(a["id"])
        if tag in ("a","link") and a.get("href"): self.links.append(a["href"])
        if tag in ("img","script") and a.get("src"): self.links.append(a["src"])
        if tag=="img" and "alt" not in a: self.imgs_noalt+=1
        if tag=="title": self._in_title=True
        if tag=="h1": self.h1+=1
    def handle_endtag(self, tag):
        if tag=="title": self._in_title=False
    def handle_data(self, d):
        if self._in_title: self.title=(self.title or "")+d

pages={}
for dp,_,fs in os.walk(ROOT):
    if "/.git" in dp: continue
    for f in fs:
        if f.endswith(".html"):
            path=os.path.join(dp,f); p=P(); p.feed(open(path,encoding="utf-8").read()); pages[path]=p

errors=[]; drafts=0
for path,p in pages.items():
    rel=os.path.relpath(path,ROOT)
    if not p.title: errors.append(f"{rel}: missing <title>")
    if p.lang!="en": errors.append(f"{rel}: html lang missing")
    if p.h1!=1: errors.append(f"{rel}: expected exactly one <h1>, found {p.h1}")
    if p.imgs_noalt: errors.append(f"{rel}: {p.imgs_noalt} <img> without alt")
    src=open(path,encoding="utf-8").read()
    drafts+=src.count("Draft · needs owner confirmation")+src.count('class="todo"')
    for href in p.links:
        u=urlsplit(href)
        if u.scheme in ("http","https","mailto"): continue
        target=path if not u.path else os.path.normpath(os.path.join(os.path.dirname(path),unquote(u.path)))
        if os.path.isdir(target): target=os.path.join(target,"index.html")
        if not os.path.exists(target): errors.append(f"{rel}: broken link {href}"); continue
        if u.fragment:
            tp=pages.get(target)
            if tp is None: tp=P(); tp.feed(open(target,encoding="utf-8").read())
            if u.fragment not in tp.ids: errors.append(f"{rel}: missing anchor #{u.fragment} in {os.path.relpath(target,ROOT)}")

print(f"checked {len(pages)} pages; {drafts} draft/todo markers remain")
for e in errors: print("ERROR", e)
if errors or (strict and drafts): sys.exit(1)
print("OK")
