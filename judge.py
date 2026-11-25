"""D03: 책장 10회 넘김 시험 결과의 합격 여부를 판정한다.

MuJoCo 실행·센서 측정·CSV 기록은 이 파일의 역할이 아니다.
"""

from math import isfinite
from collections.abc import Sequence


def judge_episode(
    turned_pages: Sequence[int],
    elapsed_s: Sequence[float],
    book_falls: int = 0,
    joint_limit_violations: int = 0,
) -> bool:
    """R-01~R-03, R-05를 모두 만족한 10회 시험이면 True.

    turned_pages[i]: i번째 입력으로 실제 넘어간 종이 장수 (1만 시도 성공, 0과 2 이상은 실패)
    elapsed_s[i]: i번째 입력의 시작부터 종료/실패 확정까지 소요한 초
    """
    if not isinstance(turned_pages, (list, tuple)) or not isinstance(elapsed_s, (list, tuple)):
        return False
    if len(turned_pages) != 10 or len(elapsed_s) != 10:
        return False
    if any(type(n) is not int or n < 0 for n in turned_pages):
        return False
    if any(type(t) not in (int, float) or not isfinite(t) or t < 0 for t in elapsed_s):
        return False
    if type(book_falls) is not int or book_falls < 0:
        return False
    if type(joint_limit_violations) is not int or joint_limit_violations < 0:
        return False

    return (
        sum(n == 1 for n in turned_pages) >= 9
        and all(n <= 1 for n in turned_pages)
        and all(t <= 15.0 for t in elapsed_s)
        and book_falls == 0
        and joint_limit_violations == 0
    )
