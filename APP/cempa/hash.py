from hashlib import md5
from pandas import DataFrame
from pandas.util import hash_pandas_object


def generate_file_md5(filename: str, blocksize=2 ** 20) -> str:
    m = md5()
    with open(filename, "rb") as f:
        while True:
            buf = f.read(blocksize)
            if not buf:
                break
            m.update(buf)
    return m.hexdigest()


def data_frame2hash(name: str, df: DataFrame) -> str:
    m = md5()
    for i in hash_pandas_object(df):
        m.update(str(i).encode("utf-8"))
    return f"{name}_{m.hexdigest()}"
