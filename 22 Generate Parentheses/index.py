from typing import List

def generate_parenthesis(n: int) -> List[str]:
    result = []

    def backtrack(current: str, open_count: int, close_count: int):
        if len(current) == 2 * n:
            result.append(current)
            return

        if open_count < n:
            backtrack(current + "(", open_count + 1, close_count)

        if close_count < open_count:
            backtrack(current + ")", open_count, close_count + 1)

    backtrack("", 0, 0)
    return result


if __name__ == "__main__":
    print("n = 3 →", generate_parenthesis(3))
    print("n = 1 →", generate_parenthesis(1))
    print("n = 4 →", generate_parenthesis(4))
