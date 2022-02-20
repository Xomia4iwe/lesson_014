#!/usr/bin/env python3


class State:

    def strike(self):
        pass

    def spare(self):
        pass

    @staticmethod
    def count(char):
        if char == '-':
            return 0
        if char != '0':
            return int(char)
        else:
            raise ValueError('Промах записывается как: -!!!!')


class FirstShotState(State):

    def strike(self):
        return 20

    def spare(self):
        raise ValueError('Не правильная запись, в первом броске фрейма не может быть: spare!!!!')


class SecondShotState(State):

    def strike(self):
        raise ValueError('Не правильная запись, во втором броске фрейма не может быть: strike!!!!')

    def spare(self):
        return 15


class Bowling:

    def __init__(self):
        self.state = None
        self.i = 0
        self.frame_count = 0
        self.total_score = 0

    def change_state(self, state):
        self.state = state

    def char_state(self, char):
        if char == 'X':
            self.total_score += self.state.strike()
        elif char == '/':
            self.total_score += self.state.spare()
        else:
            if char.isdigit() or char == '-':
                self.total_score += self.state.count(char)
            else:
                raise ValueError('Вы ввели неверный символ!!!')

    def split_on_frame(self, game_result):
        frame = game_result[self.i] + game_result[self.i + 1] if game_result[self.i] != 'X' else game_result[self.i]
        self.frame_count += 1
        if self.frame_count > 10:
            raise ValueError('Нельзя играть больше 10 фреймов')
        yield frame
        self.i += 1 if len(frame) == 2 else 0

    def get_score(self, game_result):
        while self.i < len(game_result):
            frame_generation = self.split_on_frame(game_result)
            for frame in frame_generation:
                if len(frame) == 1:
                    self.change_state(FirstShotState())
                    self.char_state(frame[0])
                elif frame[1] == '/' and frame[0].isdigit() and frame[0] != '0':
                    self.change_state(SecondShotState())
                    self.char_state(frame[1])
                else:
                    if frame[0].isdigit() and frame[1].isdigit():
                        if int(frame[0]) + int(frame[1]) >= 10:
                            raise ValueError('Сумма очков за два броска не должна превышать или быть равной 10 ' +
                                             'очкам...здесь должен быть спэр!!!')
                    self.change_state(FirstShotState())
                    self.char_state(frame[0])
                    self.change_state(SecondShotState())
                    self.char_state(frame[1])
                self.i += 1
        if self.frame_count < 10:
            raise ValueError('Сыграно меньше 10 фрэймов, запись game_result ошибочна!!!')


if __name__ == "__main__":
    A = Bowling()
    A.get_score(game_result='--8/--8/4/8/-224----')
    print(A.total_score)
