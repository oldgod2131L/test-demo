## 專門 render 畫面


def create_board(size=15):
    """創建一個五子棋棋盤。"""
    return [["." for _ in range(size)] for _ in range(size)]

def print_board(board):
    """打印棋盤，並加上數字座標標示。"""
    size = len(board)
    # 打印列座標
    print(" "+"".join(f"{i+1:2}" for i in range(size)))
    for idx, row in enumerate(board):
        # 打印行座標和棋盤內容
        print(f"{idx+1:2}" + " ".join(row))
    print()