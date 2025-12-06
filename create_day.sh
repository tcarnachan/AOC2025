#!/bin/bash

source .env
input="$(curl -s -b session=$SESSION https://adventofcode.com/2025/day/$1/input)"
printf "%s" "$input" > res/day$1.txt

echo "with open('res/day$1.txt') as f:
    lines = f.read().splitlines()" >> src/day$1.py