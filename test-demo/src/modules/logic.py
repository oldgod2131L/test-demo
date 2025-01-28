
def is_valid_move(board, x, y):
    """檢查某位置是否為有效的落子位置。"""
    return 0 <= x < len(board) and 0 <= y < len(board[0]) and board[x][y] == "."

def check_win(board, x, y, player):
    """檢查是否當前玩家勝利。"""
    directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
    n = len(board)
    for dx, dy in directions:
        count = 1
        # 檢查正方向
        i, j = x + dx, y + dy
        while 0 <= i < n and 0 <= j < n and board[i][j] == player:
            count += 1
            i, j = i + dx, j + dy
        # 檢查反方向
        i, j = x - dx, y - dy
        while 0 <= i < n and 0 <= j < n and board[i][j] == player:
            count += 1
            i, j = i - dx, j - dy
        if count >= 5:
            return True
    return False
