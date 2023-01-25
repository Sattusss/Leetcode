class Solution:
  def kWeakestRows(self, mat: list[list[int]], k: int) -> list[int]:
    candidates = []

    for i, row in enumerate(mat):
      candidates.append([sum(row), i])

    candidates.sort(key=lambda c: (c[0], c[1]))

    return [i for _, i in candidates[:k]]