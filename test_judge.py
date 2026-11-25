"""3일차 D03: 책장 10장 연속 넘김의 성공·경계·실패 판정 테스트."""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from judge import judge_episode

OK = [1] * 10
TIMES = [12.0] * 10


def test_T01_nine_successes_pass():
    assert judge_episode([1] * 9 + [0], TIMES)


def test_T02_ten_successes_pass():
    assert judge_episode(OK, TIMES)


def test_T03_only_eight_successes_fail():
    assert not judge_episode([1] * 8 + [0, 0], TIMES)


def test_T04_two_pages_in_one_command_fail():
    assert not judge_episode([1] * 9 + [2], TIMES)


def test_T05_zero_is_failed_trial_but_nine_of_ten_pass():
    assert judge_episode([0] + [1] * 9, TIMES)


def test_T06_exactly_fifteen_seconds_pass():
    assert judge_episode(OK, [15.0] * 10)


def test_T07_exceeds_fifteen_seconds_fail():
    assert not judge_episode(OK, [12.0] * 9 + [15.01])


def test_T09_book_falls_fail():
    assert not judge_episode(OK, TIMES, book_falls=1)


def test_T10_joint_limit_violation_fail():
    assert not judge_episode(OK, TIMES, joint_limit_violations=1)


def test_wrong_trial_count_fail():
    assert not judge_episode(OK[:9], TIMES[:9])
    assert not judge_episode(OK + [1], TIMES + [12.0])


def test_invalid_page_counts_fail():
    assert not judge_episode([1] * 9 + [-1], TIMES)
    assert not judge_episode([1] * 9 + [1.0], TIMES)
    assert not judge_episode([1] * 9 + [True], TIMES)


def test_invalid_time_fail():
    assert not judge_episode(OK, [12.0] * 9 + [float('nan')])
    assert not judge_episode(OK, [12.0] * 9 + [float('inf')])
    assert not judge_episode(OK, [12.0] * 9 + [-0.1])
    assert not judge_episode(OK, [12.0] * 9 + [True])


def test_invalid_safety_counts_fail():
    assert not judge_episode(OK, TIMES, book_falls=-1)
    assert not judge_episode(OK, TIMES, joint_limit_violations=True)


def test_zero_pages_does_not_count_as_success():
    # 0장은 성공이 아니므로 2회 이상 0장이면 전체 9/10 기준에서 탈락.
    assert not judge_episode([0, 0] + [1] * 8, TIMES)


def test_all_zero_pages_fail():
    assert not judge_episode([0] * 10, TIMES)
