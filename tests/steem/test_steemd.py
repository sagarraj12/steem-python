from funcy.colls import pluck
from steem.steemd import Steemd


def test_ensured_block_ranges():
    """ Post should load correctly if passed a dict or string identifier. """
    s = Steemd()
    assert list(pluck('block_num', s.get_blocks_range(1000, 2000))) == list(
        range(1000, 2000))

    # for fuzzing in s.get_block_range_ensured() use:
    # degraded_results = [x for x in results if x['block_num'] %
    #     random.choice(range(1, 10)) != 0]
