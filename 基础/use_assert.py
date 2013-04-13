def test(n):
    assert n>4     #如果assert 后面的为真在则不报错，否则AssertionError错误

test(10)   #不报错

test(2)   #报AssertionError错误