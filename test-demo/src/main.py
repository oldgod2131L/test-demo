import random
from modules.board import create_board, print_board
from modules.logic import is_valid_move, check_win


def check_who_is_win(people):
    "輸入 people 名稱，顯示 people 勝利"
    if people == "玩家":
        print(f"恭喜 {people} 獲勝！")
    else:
        print(f"恭喜 {people} 獲勝！")
    


def evaluate_position(board, x, y, player):
    """計算某位置的得分，包含進攻與防守策略。"""
    directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
    score = 0
    opponent = "X" if player == "O" else "O"

    for dx, dy in directions:
        player_count = 0
        opponent_count = 0
        empty_count = 0

        # 正方向
        i, j = x + dx, y + dy
        while 0 <= i < len(board) and 0 <= j < len(board[0]):
            if board[i][j] == player:
                player_count += 1
            elif board[i][j] == ".":
                empty_count += 1
                break
            else:
                break
            i, j = i + dx, j + dy

        # 反方向
        i, j = x - dx, y - dy
        while 0 <= i < len(board) and 0 <= j < len(board[0]):
            if board[i][j] == player:
                player_count += 1
            elif board[i][j] == ".":
                empty_count += 1
                break
            else:
                break
            i, j = i - dx, j - dy

        # 防守與進攻分析（對手）
        i, j = x + dx, y + dy
        while 0 <= i < len(board) and 0 <= j < len(board[0]):
            if board[i][j] == opponent:
                opponent_count += 1
            elif board[i][j] == ".":
                break
            else:
                break
            i, j = i + dx, j + dy

        i, j = x - dx, y - dy
        while 0 <= i < len(board) and 0 <= j < len(board[0]):
            if board[i][j] == opponent:
                opponent_count += 1
            elif board[i][j] == ".":
                break
            else:
                break
            i, j = i - dx, j - dy

        # 計分規則
        if player_count >= 4:  # 確保自己五連
            score += 100000
        elif opponent_count >= 4:  # 阻止對手五連
            score += 50000
        elif opponent_count == 3 and empty_count > 1:  # 阻止對手三連
            score += 15000
        elif opponent_count == 3 and empty_count > 0:  # 阻止對手三連
            score += 10000
        elif player_count == 3 and empty_count > 1:
            score += 13000  # 三連進攻
        elif player_count == 3 and empty_count > 0:
            score += 8000  # 三連進攻
        elif opponent_count == 2 and empty_count > 1:  # 阻止對手雙連
            score += 5000
        elif opponent_count == 2 and empty_count > 0:  # 阻止對手雙連
            score += 1000
        elif player_count == 2 and empty_count > 1:
            score += 3000  # 雙連進攻
        elif player_count == 2 and empty_count > 0:
            score += 800  # 雙連進攻
        elif opponent_count == 1 and empty_count > 1:  # 阻止對手一連
            score += 500
        elif opponent_count == 1 and empty_count > 0:  # 阻止對手一連
            score += 300
        
    return score

def computer_move_optimized(board, player):
    """優化電腦 AI，選擇最佳得分的位置。"""
    best_score = -1
    best_move = None

    for x in range(len(board)):
        for y in range(len(board[0])):
            if board[x][y] == ".":
                score = evaluate_position(board, x, y, player)
                if score > best_score:
                    best_score = score
                    best_move = (x, y)

    return best_move

def play_gobang():
    """主函數，運行五子棋遊戲（優化 AI）。"""
    size = 15
    board = create_board(size)
    players = ["玩家 (X)", "電腦 (O)"]
    symbols = ["X", "O"]
    current_player = 0  # 0 表示玩家，1 表示電腦

    print("歡迎來到五子棋遊戲！")
    print("棋盤大小為 15x15，玩家與電腦交替落子，玩家輸入格式為: 行 列 (例如: 7 7)")
    print_board(board)

    while True:
        if current_player == 0:
            print(f"{players[current_player]} 的回合")
            try:
                x, y = map(int, input("請輸入坐標 (行 列): ").split())
                x, y = x - 1, y - 1  # 轉為 0 索引
                if not is_valid_move(board, x, y):
                    print("無效的落子位置，請重新輸入！")
                    continue
            except ValueError:
                print("輸入格式錯誤，請輸入兩個整數 (行 列)！")
                continue
        else:
            print(f"{players[current_player]} 的回合 (AI)")
            move = computer_move_optimized(board, symbols[current_player])
            if move is None:
                print("棋盤已滿，平局！")
                break
            x, y = move

        board[x][y] = symbols[current_player]
        print_board(board)

        if check_win(board, x, y, symbols[current_player]):
            print(f"恭喜 {players[current_player]} 獲勝！")
            break

        current_player = 1 - current_player  # 切換玩家

if __name__ == "__main__":
    play_gobang()
