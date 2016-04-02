import mock


@mock.patch("requester.requests.get")
def test_call(rg):
    from requester import call
    from collections import namedtuple
    Response = namedtuple('Response', 'status_code')
    response = Response(status_code=200)
    rg.return_value = response
    url = 'http://localhost:9000/abc'
    x = call(url)
    rg.assert_called_with(url, timeout=2)
    assert x == 200
