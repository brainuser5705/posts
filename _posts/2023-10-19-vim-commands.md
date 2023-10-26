---
layout: post
title: Vim Commands
date: 2023-10-19 23:06
tags: c
---

List of Vim commands to make development easier

# Commands

- **redo**: CTRL + r
- **undo**: U
- **copy and paste**: x or v or dd, then p
- **indent and unindent**: `=` and `<`

# .vimrc settings

- [`set textwidth=x`](https://stackoverflow.com/questions/3033423/vim-command-to-restructure-force-text-to-80-columns): autoindent once line is at `x` characters
- [different types of wrapping](https://stackoverflow.com/questions/36950231/auto-wrap-lines-in-vim-without-inserting-newlines)


# Vim multi-window editing

- **`:new [file]` (hori), `:vnew [file]`** : open new window
- **`:e [file]`** : edit new file in current window
- change editing window: `CTRL + w + w`

- open file in right vertical split: `:set splitright`

[source](https://www.baeldung.com/linux/vim-windows#:~:text=The%20Ctrl%2Bw%20%2Bs%20and,use%20Ctrl%2Bw%20%2Bn.)