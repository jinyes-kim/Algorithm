def solution(skill, skill_trees):
    answer = len(skill_trees)

    for letters in skill_trees:
        dummy = []
        for alphabet in letters:
            if alphabet not in skill:
                continue
            if alphabet == skill[0]:
                dummy.append(alphabet)
            else:
                pivot = skill.index(alphabet) - 1
                if skill[pivot] not in dummy:
                    answer -= 1
                    break
                else:
                    dummy.append(alphabet)

    return answer