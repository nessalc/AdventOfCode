# day10.py

with open('input10.txt') as fp:
    navigation_code = list(map(str.strip, fp.readlines()))

open_chunk_chars_score = {')': 1, ']': 2, '}': 3, '>': 4}
close_chunk_chars_score = {')': 3, ']': 57, '}': 1197, '>': 25137}

syntax_error_score = 0
syntax_repair_scores = []
for code_line in navigation_code:
    stack = []
    for c in code_line:
        if c == '(':
            stack.append(')')
        elif c == '[':
            stack.append(']')
        elif c == '{':
            stack.append('}')
        elif c == '<':
            stack.append('>')
        elif c == stack[-1]:
            stack.pop()
        else:
            syntax_error_score += close_chunk_chars_score[c]
            break
    else:
        current_syntax_repair_score = 0
        for c in stack[::-1]:
            current_syntax_repair_score *= 5
            current_syntax_repair_score += open_chunk_chars_score[c]
        syntax_repair_scores.append(current_syntax_repair_score)
syntax_repair_scores.sort()

print(syntax_error_score)
print(syntax_repair_scores[len(syntax_repair_scores)//2])
