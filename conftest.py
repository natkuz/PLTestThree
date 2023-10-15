import pytest
import yaml
from checkout import checkout, getout
from datetime import datetime

with open("config.yaml", encoding='UTF-8') as f:
    data = yaml.safe_load(f)


@pytest.fixture()
def make_folder():
    yield checkout(f"mkdir -p {data.get('folder_in')} {data.get('folder_out')} {data.get('folder_fld')}", "")
    return checkout(f"rm -r {data.get('folder_in')} {data.get('folder_out')} {data.get('folder_fld')}", "")


@pytest.fixture()
def make_file():
    return checkout(f"cd {data.get('folder_in')}; touch file1 file2 file3", "")


@pytest.fixture(autouse=True)
def write_stat():
    yield
    stat = getout("cat /proc/loadavg")
    checkout(f"'time: {datetime.now().strftime('%H:%M:%S.%f')} count:{data.get('count')} size: {data.get('bs')} "
             f"load: {stat}' >> stat.txt", "")