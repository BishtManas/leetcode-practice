#!/bin/bash

start_date="2025-11-07"
end_date="2025-12-15"

current_date="$start_date"

while [ "$(date -d "$current_date" +%s)" -le "$(date -d "$end_date" +%s)" ]
do
    for i in {1..5}
    do
        echo "- Update on $current_date commit $i" >> README.md

        git add README.md

        hour=$((9 + i))

        GIT_AUTHOR_DATE="$current_date $hour:00:00" \
        GIT_COMMITTER_DATE="$current_date $hour:00:00" \
        git commit -m "README update $i - $current_date"
    done

    current_date=$(date -I -d "$current_date + 1 day")
done
