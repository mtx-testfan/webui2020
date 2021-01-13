import pytest
import time
import subprocess

if __name__ == '__main__':
    tmp = time.strftime('%Y%m%d_%H%M%S')
    pytest.main(['-sv', './case/test_cart.py', '--alluredir=./reports/mtx', '--clean-alluredir'])
    # subprocess.call('allure generate ./reports/mtx -o ./reports/html/' + tmp, shell=True)
    subprocess.call('allure generate ./reports/mtx -o ./reports/html/ --clean', shell=True)