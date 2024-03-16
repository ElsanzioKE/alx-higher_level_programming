#!/bin/bash
# check if there are any changes to commit
if ! git diff-index --quiet HEAD --; then
    # Add all changes
    git add .

    # Commit changes with a default commit message
    git commit -m "Auto commit at $(date)"

    # Push changes to the remote repository
    git push origin master
else
    echo "No changes to commit."
fi

