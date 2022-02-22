from Tournament import TournamentInfo
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--input', type=str, help='Введите путь к файлу протокола турнира', required=True)
parser.add_argument('--output', type=str, help='Введите путь к файлу результатов турнира')
args = parser.parse_args()

if __name__ == '__main__':
    tournament = TournamentInfo(args.input, args.output)
    tournament.game_info()
    tournament.write_on_console()