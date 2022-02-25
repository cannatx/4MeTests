import git

br_name = "master"

repo = git.Repo("./")

# branches = repo.branches
try:
    repo.git.checkout(br_name)
except:
    repo.git.fetch()
    remotes = [r.name for r in repo.remotes.origin.refs]
    if f"origin/{br_name}" not in remotes:
        repo.git.checkout("-b", br_name)
        repo.git.push("--set-upstream", "origin", br_name)

    branches = [b.name for b in repo.branches]
    if br_name not in branches:
        repo.git.checkout("-b", br_name, f"origin/{br_name}")

    repo.git.checkout(br_name)

try:
    repo.git.add("-A")
    repo.git.commit(f"-m uodate on {br_name}")
    # repo.remotes.origin.push()
    repo.git.push("origin", br_name)
except Exception as e:
    if "nothing to commit" in list(e):
        pass
    else:
        print(e)
