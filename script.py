import datetime
import subprocess
import os
import sys

keywords = 'Function return type'
start_date = '2017-10-02'
end_date = '2018-01-26'

init_path = '/home/travis/.cargo/bin/'
cmd = [init_path + 'rustc', os.path.abspath('test.rs')]
toolchain_type = 'nightly'
last_date = start_date

def middle_date(start_date, end_date):
    start = datetime.datetime.strptime(start_date, '%Y-%m-%d')
    end = datetime.datetime.strptime(end_date, '%Y-%m-%d')
    mid = start + (end - start) / 2
    return str(mid.date())


def output_has_keywords(cmd, capture):
    output = subprocess.run(cmd,
                            stderr=subprocess.PIPE,
                            stdout=subprocess.PIPE)

    stdout = output.stdout.decode('utf-8')
    stderr = output.stderr.decode('utf-8')

    return capture in stderr or capture in stdout


def set_default_toolchain(toolchain):
    cmd = [init_path + 'rustup', 'default', toolchain]
    output = subprocess.run(cmd,
                            stderr=subprocess.PIPE,
                            stdout=subprocess.PIPE)
    subprocess.run([init_path + 'rustc', '-vV'])
    return output.stdout


mid_date = middle_date(start_date, end_date)
toolchain = '{0}-{1}'.format(toolchain_type, mid_date)

subprocess.run(['bash', 'rustup.sh', '-y', '--default-toolchain', toolchain])

while not last_date == mid_date:
    last_date = mid_date
    if output_has_keywords(cmd, keywords):
        end_date = mid_date
    else:
        start_date = mid_date

    mid_date = middle_date(start_date, end_date)
    toolchain = '{0}-{1}'.format(toolchain_type, mid_date)

    print('\nSetting defaults: ' + toolchain)
    set_default_toolchain(toolchain)
