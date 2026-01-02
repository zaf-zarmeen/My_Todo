#!/bin/bash
# Demo script to show Todo CLI App functionality

echo "=== Todo CLI App Demonstration ==="
echo ""

# Test 1: View empty list
echo "Test 1: View empty task list"
echo -e "2\n0" | uv run python src/main.py
echo ""

# Test 2: Add a task
echo "Test 2: Add tasks"
printf "1\nBuy groceries\nMilk, eggs, and bread\n2\n0\n" | uv run python src/main.py

echo ""
echo "=== All tests completed! ==="
