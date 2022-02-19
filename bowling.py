#!/usr/bin/env python3

class FrameError(Exception):
    """Неверное количество фреймов!"""
    pass


class ResultError(Exception):
    """Неверное количество очков в фрейме!"""
    pass


class IncorrectEntryError(Exception):
    """Неверная запись результата"""
    pass


def get_score(game_result):
    score = 0
    for frame_result in game_result:
        if frame_result not in 'X/123456789-':
            raise IncorrectEntryError('Неверная запись результата!')

    game_result = game_result.replace('X', 'XX')

    if len(game_result) // 2 != 10:
        raise FrameError('Неверное количество фреймов!')

    game_result = [game_result[x:x + 2] for x in range(0, len(game_result), 2)]
    print(game_result)

    for frame_result in game_result:
        if frame_result == '//' or frame_result[0] == '/':
            raise IncorrectEntryError('Неверная запись результата! Присутствуют лишние символы!')
        elif frame_result == 'XX':
            score += 20
        elif frame_result[0].isdigit():
            if frame_result[1].isdigit():
                if int(frame_result[0]) + int(frame_result[1]) > 10:
                    raise ResultError('Неверное количество очков в фрейме!')
                else:
                    score += int(frame_result[0]) + int(frame_result[1])
            else:
                if frame_result[1] == '/':
                    score += 15
                else:
                    score += int(frame_result[0])
        else:
            if frame_result[0] == '-':
                if frame_result[1].isdigit():
                    score += int(frame_result[1])
                elif frame_result[1] == '/':
                    score += 15
    return print(score)



if __name__ == "__main__":
    get_score('X1/253/X5572811/X')
