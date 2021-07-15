
" 基础配置
set nocompatible                " don't bother with vi compatibility
set autoread                    " reload files when changed on disk, i.e. via `git checkout`
set nobackup                    " do not keep a backup file
set noerrorbells                " don't beep

" 编码设置
set encoding=utf-8
set termencoding=utf-8          " 终端使用的编码方式

" 界面显示
set ruler                       " show current row and column number
set number                      " show line numbers
set showcmd                     " display incomplete commands
set showmode                    " display current modes

" 缩进配置
set expandtab                   " expand tabs to spaces
set smarttab                    " 插入 Tab 时使用 shiftwidth
set tabstop=2                   " 按下 Tab 键时，缩进的空格个数
set shiftwidth=2                " 执行Vim普通模式下的缩进操作 ( << 和 >> 命令 )时缩进的列数
set autoindent                  " 新增加的行和前一行具有相同的缩进形式
set smartindent                 " 每一行都有相同的缩进量，直到遇到右大括号 (}) 取消缩进形式
set shiftround                  " 缩进列数对齐到 shiftwidth 值的整数倍

" 光标位置
" set cursorcolumn
set cursorline

" 搜索配置 
set hlsearch                    " highlight searches "
set incsearch                   " do incremental searching, search as you type "
set ignorecase                  " ignore case when searching "
set smartcase                   " no ignorecase if Uppercase char present "

" 语法高亮
syntax enable

" 文件类型
filetype on
filetype plugin on
