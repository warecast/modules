import os
import re

# regex patterns
reject_pattern = r"(^|\n)reject"
hostname_pattern = r"(^|\n)hostname ="
tag_pattern = r"(^|\n)tag ="

# replacements
reject_replacement = "REJECT-TINYGIF"
hostname_replacement = "hostname = %APPEND%"
tag_replacement = ""

# iterate over files in the directory
for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".conf"):
            file_path = os.path.join(root, file)

            # read file content
            with open(file_path, "r") as f:
                content = f.read()

            # make modifications using regex
            content = re.sub(reject_pattern, reject_replacement, content, flags=re.IGNORECASE)
            content = re.sub(hostname_pattern, hostname_replacement, content, flags=re.IGNORECASE)
            content = re.sub(tag_pattern, tag_replacement, content, flags=re.IGNORECASE)

            # write modified content to file
            with open(file_path, "w") as f:
                f.write(content)
