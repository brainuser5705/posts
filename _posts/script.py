from datetime import datetime

time = datetime.now().strftime("%H:%M")
date = datetime.now().strftime("%Y-%m-%d")

filename_input = input("Filename: ")
title_input = input("Title if different from filename: ")
if (not title_input):
    title_input = filename_input
tags_input = input("Tags (space-separated): ")

filename = date + "-" + "-".join(filename_input.split()) + ".md"

yaml_template= \
"""---
layout: post
title: {title}
date: {date} {time}
tags: {tags}
---
"""

with open(filename, "w") as file:
    yaml = yaml_template.format(
        title=title_input,
        date=date,
        time=time,
        tags=tags_input
    )
    file.write(yaml)
    file.write("\n")