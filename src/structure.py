# box: np.array([Lx, Ly, Lz])
# n_cell: 各方向のセル数（直方体格子を想定）
import numpy as np


def fcc_positions(a, n_cell):
    bases = np.array(
        [
            [0.0, 0.0, 0.0],
            [0.0, 0.5, 0.5],
            [0.5, 0.0, 0.5],
            [0.5, 0.5, 0.0],
        ]
    )

    N = 4 * n_cell**3
    pos = np.zeros((N, 3), dtype=float)

    idx = 0
    for ix in range(n_cell):
        for iy in range(n_cell):
            for iz in range(n_cell):
                R0 = np.array([ix, iy, iz], dtype=float)  # セル原点(格子単位)
                # 4基底を追加（必ず 0<=座標<box に収める）
                p = (R0 + bases) * a  # 各成分で a を掛ける（ベクトル）
                pos[idx : idx + 4] = p
                idx += 4

    # 念のため丸め誤差をラップ
    return pos
