from requester import call
import mock


@mock.patch("requester.requests.get")
def test_call(rg):
    from collections import namedtuple
    Response = namedtuple('Response', 'status_code')
    response = Response(status_code=200)
    rg.return_value = response
    x = call('http://localhost:9000/abc')
    # print(type(x))
    # print(x.__dict__)
    assert x == 200
