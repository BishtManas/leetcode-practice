def simplifyPath(path: str) -> str:
    stack = []
    parts = path.split('/')

    for part in parts:
        if part == '' or part == '.':
            continue
        elif part == '..':
            if stack:
                stack.pop()
        else:
            stack.append(part)

    return "/" + "/".join(stack)


# Example test cases
if __name__ == "__main__":
    paths = [
        "/home/",
        "/home//foo/",
        "/home/user/Documents/../Pictures",
        "/../",
        "/.../a/../b/c/../d/./"
    ]
    for p in paths:
        print(f"Input: {p}\nOutput: {simplifyPath(p)}\n")
