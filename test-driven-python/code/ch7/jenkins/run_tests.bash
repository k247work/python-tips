#!/bin/bash

# top_pathとvenv_pathの値は変更が必要
top_path=/xxx
code_path=${top_path}/code
venv_path=${top_path}/venv

tasks_proj_dir=${code_path}/$1
start_tests_dir=${code_path}/$2
results_dir=$3

# clickとPython3
# http://click.pocoo.org/5/python3/
export LC_ALL=en_US.utf-8
export LANG=en_US.utf-8

# 仮想環境
source ${venv_path}/bin/activate

# プロジェクトのインストール
pip install -e ${tasks_proj_dir}

# テストの実行
cd ${start_tests_dir}
pytest --junit-xml=${results_dir}/results.xml