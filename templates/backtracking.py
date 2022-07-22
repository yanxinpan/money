def find_solution(candiate):
    raise NotImplementedError


def is_valid(candidate):
    raise NotImplementedError


def place(candidate):
    raise NotImplementedError


def remove(candidate):
    raise NotImplementedError


def output(candidate):
    raise NotImplementedError


def backtracking(candidate):
    if find_solution(candidate):
        output(candidate)
        return
    for n in candidate.next:
        place(n)
        backtracking(n)
        remove(n)
