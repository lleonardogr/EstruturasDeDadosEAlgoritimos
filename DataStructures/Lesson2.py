import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    found_files = []
    if path is None:
        return None

    def find_files(current_path):
        for entry in os.listdir(current_path):
            entry_path = os.path.join(current_path, entry)

            if os.path.isdir(entry_path):
                find_files(entry_path)
            elif entry.endswith(suffix):
                found_files.append(entry_path)

    find_files(path)
    return found_files

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1
# Test Case normal
assert len(find_files(".c","testdir")) == 4

# Test Case 2 
# Test Case null
assert find_files(".txt","testdir") == []

# Test Case 3
# Test large values
assert find_files("."+"A"*(10**6),"testdir") == []