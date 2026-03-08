def solution(todo_list, finished):
        return [todo_list[idx] for idx in range(len(finished)) if finished[idx] == False ]
