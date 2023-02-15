from pathlib import Path

from invoke import task


@task
def sta(c, contest):
    c.run(f"acc new {contest}")
    with c.cd(f"{contest}/a"):
        c.run("code -r main.py")


@task
def test(c, dir):
    # _pypyInit(c)
    with c.cd(f"{dir}"):
        cmd = "oj t -c 'pypy3 main.py' -d ./tests/"
        c.run("pwd")
        print("cmd:", cmd)
        c.run(cmd)


@task
def testpy(c, dir):
    with c.cd(f"{dir}"):
        cmd = "oj t -c 'python main.py' -d ./tests/"
        c.run("pwd")
        print("cmd:", cmd)
        c.run(cmd)


@task
def sb(c, dir, conf=None):
    test(c, dir)
    ct, _ = _getContest(c)
    conf = conf if conf else ct + dir
    with c.cd(f"{dir}"):
        print(
            "cmd:",
            cmd := f"echo {conf} | acc s main.py -- --guess-python-interpreter pypy",
        )
        c.run(cmd)


@task
def sbpy(c, dir, conf=None):
    testpy(c, dir)
    ct, _ = _getContest(c)
    conf = conf if conf else ct + dir
    with c.cd(f"{dir}"):
        print("cmd:", cmd := f"echo {conf} | acc s")
        c.run(cmd)


@task
def cd(c, dir):
    c.run("pwd")
    with c.cd(f"{dir}"):
        c.run("pwd")
        c.run("code -r main.py")


def _pypyInit(c):
    c.run("pyenv versions")
    c.run("pyenv shell pypy3.6-7.3.0")


def _getContest(c):
    contest = Path(c.run("pwd").stdout.strip()).name
    return (contest[:3], contest[3:])


def _getTasks(c):
    path = Path(c.run("pwd").stdout.strip())
    tasks = sorted([d.name for d in path.iterdir() if d.is_dir()])
    return tasks
