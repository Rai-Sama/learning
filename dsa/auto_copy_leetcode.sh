#!/usr/bin/env bash

SOURCE_DIR="$HOME/everything/learning/dsa/leetcode_sols"
BASE_DIR="$HOME/everything/learning/dsa"

process_file() {
    local file="$1"

    # Wait briefly for file write completion (handles atomic saves)
    for i in {1..5}; do
        [[ -s "$file" ]] && break
        sleep 0.2
    done

    [[ -f "$file" && -s "$file" ]] || return  # skip if not ready

    while IFS= read -r line; do
        if [[ "$line" =~ ^[[:space:]]*#\ Anshuman\ --\ (.*) ]]; then
            comment_path="${BASH_REMATCH[1]}"
            IFS='--' read -ra paths <<< "$comment_path"

            # Extract the parent folder name (e.g., "3310.remove-methods-from-project")
            # This turns solution.py into a nicely named file for study folders
            local problem_name
            problem_name=$(basename "$(dirname "$file")")

            for raw_path in "${paths[@]}"; do
                clean_path="$(echo "$raw_path" | xargs)"   # trim spaces

                # Skip empty or malformed entries or unedited TODOs
                [[ -z "$clean_path" || "$clean_path" == "TODO_PATH_1" ]] && continue

                full_path="$BASE_DIR/$clean_path"
                full_path=$(echo "$full_path" | sed 's:/\+:/:g')

                mkdir -p "$full_path"
                
                # Copy and rename the file!
                cp -f "$file" "$full_path/${problem_name}.py"
                echo "Copied '$file' → '$full_path/${problem_name}.py'"
            
            done
        fi
    done < "$file"
}

# Watch directory RECURSIVELY (-r) for new/updated files
inotifywait -r -m -e close_write,moved_to --format "%w%f" "$SOURCE_DIR" | while read file; do
    if [[ "$file" =~ solution\.py$ ]]; then
        process_file "$file"
    fi
done
