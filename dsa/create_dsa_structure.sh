#!/bin/bash

# Base directory
BASE_DIR=~/everything/learning/dsa

# Define main folders
MAIN_DIRS=(
  "arrays"
  "bit_manipulation"
  "dp"
  "graphs"
  "greedy"
  "searching"
  "sorting"
  "strings"
  "trees"
  "recursion_backtracking"
  "math"
  "patterns"
  "templates"
)

# Define subdirectories for data_structures
DATA_STRUCTURES=(
  "linked_list"
  "stack"
  "queue"
  "heap"
  "hash_map"
  "trie"
  "segment_tree"
)

# Create base directory
echo "Creating base directory: $BASE_DIR"
mkdir -p "$BASE_DIR"

# Create main topic directories
echo "Creating main topic directories..."
for dir in "${MAIN_DIRS[@]}"; do
  mkdir -p "$BASE_DIR/$dir"
  echo "# ${dir//_/ }" > "$BASE_DIR/$dir/README.md"
done

# Create data_structures subfolders
echo "Creating data_structures and subfolders..."
for ds in "${DATA_STRUCTURES[@]}"; do
  mkdir -p "$BASE_DIR/data_structures/$ds/problems"
  echo "# ${ds//_/ }" > "$BASE_DIR/data_structures/$ds/README.md"
  echo "# Problems related to ${ds//_/ }" > "$BASE_DIR/data_structures/$ds/problems/README.md"
done

# Create top-level README
cat <<EOF > "$BASE_DIR/README.md"
# DSA Practice Repository

This directory contains categorized practice problems, implementations, and notes for Data Structures and Algorithms.

## Folder Overview
- \`arrays/\`: Array-based problems
- \`bit_manipulation/\`: Bitwise operations and tricks
- \`data_structures/\`: Implementations of fundamental data structures
- \`dp/\`: Dynamic programming patterns and problems
- \`graphs/\`: Traversal, shortest path, and connectivity problems
- \`greedy/\`: Greedy algorithms and proofs
- \`searching/\`: Binary search and variations
- \`sorting/\`: Sorting algorithms and analysis
- \`strings/\`: String algorithms and pattern matching
- \`trees/\`: Binary trees, BSTs, and tree-based problems
- \`recursion_backtracking/\`: Recursive and backtracking approaches
- \`math/\`: Number theory, combinatorics, and modular arithmetic
- \`patterns/\`: Problem-solving patterns (sliding window, two pointers, etc.)
- \`templates/\`: Common algorithm and DS code snippets

Created automatically via \`create_dsa_structure.sh\`.
EOF

echo "✅ Folder structure created successfully at: $BASE_DIR"
