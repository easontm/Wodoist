from src.woxqueryparser import WoxQueryParser as wqp
from src.result import CreateProjectResult

def test_parse():
    query = 'np this is a #test'
    v = wqp.parse(query)
    assert CreateProjectResult(query).name == v[0].name
