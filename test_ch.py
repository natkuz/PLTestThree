from checkout import checkout, get_hash, getout
import yaml
import pytest

with open("config.yaml", encoding='UTF-8') as f:
    data = yaml.safe_load(f)


class TestChPositive:
    def test_step_one(self, make_folder, make_file):
        # test1
        assert checkout(f"cd {data.get('folder_in')}; 7z a {data.get('folder_out')}arch -t{data.get('type_arch')}",
                        "Everything is Ok"), "test1 FAIL"

    def test_step_two(self, make_folder, make_file):
        # test2
        assert checkout(f"cd {data.get('folder_in')}; 7z a {data.get('folder_out')}arch -t{data.get('type_arch')}", "")
        assert checkout(f"cd {data.get('folder_out')}; 7z d ./arch.7z file1", "Everything is Ok"), "test2 FAIL"

    def test_step_three(self, make_folder, make_file):
        # test3
        assert checkout(f"cd {data.get('folder_in')}; 7z a {data.get('folder_out')}arch", "")
        assert checkout(f"cd {data['folder_out']}; 7z l ./arch.7z", "Name"), "test3 FAIL"

    def test_step_four(self, make_folder, make_file):
        # test3
        assert checkout(f"cd {data.get('folder_in')}; 7z a {data.get('folder_out')}arch", "")
        assert checkout(f"cd {data['folder_out']}; 7z x ./arch.7z", "Everything is Ok"), "test4 FAIL"

    def test_step_five(self, make_folder, make_file):
        res1 = checkout(f"cd {data['folder_in']}; 7z h file2 -t{data.get('type_arch')}", "Everything is Ok")
        hs = get_hash(f"cd {data['folder_in']}; crc32 file2".upper())
        res2 = checkout(f"cd {data['folder_in']}; 7z h file2", hs)
        assert res1 and res2, "test5 FAIL"


if __name__ == '__main__':
    pytest.main(["-vv"])