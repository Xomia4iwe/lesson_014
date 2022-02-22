# -*- coding: utf-8 -*-

# Прибежал менеджер и сказал что нужно срочно просчитать протокол турнира по боулингу в файле tournament.txt
#
# Пример записи из лога турнира
#   ### Tour 1
#   Алексей	35612/----2/8-6/3/4/
#   Татьяна	62334/6/4/44X361/X
#   Давид	--8/--8/4/8/-224----
#   Павел	----15623113-95/7/26
#   Роман	7/428/--4-533/34811/
#   winner is .........
#
# Нужно сформировать выходной файл tournament_result.txt c записями вида
#   ### Tour 1
#   Алексей	35612/----2/8-6/3/4/    98
#   Татьяна	62334/6/4/44X361/X      131
#   Давид	--8/--8/4/8/-224----    68
#   Павел	----15623113-95/7/26    69
#   Роман	7/428/--4-533/34811/    94
#   winner is Татьяна

# Код обаботки файла расположить отдельном модуле, модуль bowling использовать для получения количества очков
# одного участника. Если захочется изменить содержимое модуля bowling - тесты должны помочь.
#
# Из текущего файла сделать консольный скрипт для формирования файла с результатами турнира.
# Параметры скрипта: --input <файл протокола турнира> и --output <файл результатов турнира>

# Усложненное задание (делать по желанию)
#
# После обработки протокола турнира вывести на консоль рейтинг игроков в виде таблицы:
#
# +----------+------------------+--------------+
# | Игрок    |  сыграно матчей  |  всего побед |
# +----------+------------------+--------------+
# | Татьяна  |        99        |      23      |
# ...
# | Алексей  |        20        |       5      |
# +----------+------------------+--------------+


from bowling import Bowling


class TournamentInfo:

    def __init__(self, input_file, output_file='tournament_result.txt'):
        self.input_file = input_file
        self.output_file = output_file
        self.winner = []
        self.name_count_game = {}
        self.name_count_win = {}

    def game_info(self):
        with open(self.input_file, mode='r', encoding='utf-8') as file:
            for line in file:
                line = line.strip('\n')
                try:
                    if '\t' in line:
                        line = line.split('\t')
                        name = line[0]
                        score = line[1]
                        bowling_game = Bowling()
                        bowling_game.get_score(score)
                        digit_score = bowling_game.total_score
                        new_line = f'{name}\t{score}\t{digit_score}'
                        self.write_to_file(new_line)
                        self.winner_info(name, digit_score)
                        self.count_game(name)
                    elif 'winner is' in line:
                        winner_line = f'winner is {self.winner[0]}'
                        self.write_to_file(winner_line)
                        self.count_win(self.winner[0])
                        self.winner.clear()
                    else:
                        self.write_to_file(line)
                except ValueError as exc:
                    new_line = f'{name}\t{score}\t{exc.args}'
                    self.write_to_file(new_line)

                except IndexError:
                    new_line = f'{name}\t{score}\t(Количество бросков во фрейме не хватает ' \
                               f'для корректного подсчета очков.)'
                    self.write_to_file(new_line)

    def winner_info(self, name, total_score):
        if not self.winner:
            self.winner.append(name)
            self.winner.append(total_score)
        elif self.winner[1] < total_score:
            self.winner.clear()
            self.winner.append(name)
            self.winner.append(total_score)

    def count_game(self, name):
        if name in self.name_count_game:
            self.name_count_game[name] += 1
        else:
            self.name_count_game[name] = 1

    def count_win(self, name):
        if name in self.name_count_win:
            self.name_count_win[name] += 1
        else:
            self.name_count_win[name] = 1

    def write_to_file(self, result_line):
        with open(self.output_file, mode='a+', encoding='utf-8') as file:
            file.write(f'{result_line}\n')

    def write_on_console(self):
        format_chars = ['+', '-', 'Игрок', 'сыграно матчей', 'всего побед']
        head_line = f'{format_chars[0]:-<11}{format_chars[0]:-<19}{format_chars[0]:-<15}{format_chars[0]}'
        words_line = f'|{format_chars[2]:^10}|{format_chars[3]:^18}|{format_chars[4]:^14}|'
        print(head_line)
        print(words_line)
        print(head_line)
        for key, value in self.name_count_game.items():
            win_size = self.name_count_win[key]
            line = f'|{key:^10}|{value:^18}|{win_size:^14}|'
            print(line)
        print(head_line)


if __name__ == "__main__":
    A = TournamentInfo('tournament.txt', 'out_tournament.txt')
    A.game_info()
    A.write_on_console()
