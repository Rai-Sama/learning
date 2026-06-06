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

            for raw_path in "${paths[@]}"; do
                clean_path="$(echo "$raw_path" | xargs)"   # trim spaces

                # Skip empty or malformed entries
                [[ -z "$clean_path" ]] && continue

                full_path="$BASE_DIR/$clean_path"
                full_path=$(echo "$full_path" | sed 's:/\+:/:g')

                mkdir -p "$full_path"
                cp -f "$file" "$full_path/$(basename "$file")"
                echo "Copied '$file' → '$full_path/$(basename "$file")'"
            done
        fi
    done < "$file"
}

# Watch directory for new/updated files
inotifywait -m -e close_write,moved_to --format "%w%f" "$SOURCE_DIR" | while read file; do
    if [[ "$file" =~ \.py$|\.txt$ ]]; then
        process_file "$file"
    fi
done

