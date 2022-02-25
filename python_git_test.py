import git

br_name = "master"

repo = git.Repo("./")

# branches = repo.branches
# remotes = repo.remotes
# origin = remotes["origin"]
# Create Local/ remote


# remote_refs = list(repo.remotes['origin'].refs)
remotes = [r.name for r in repo.remotes.origin.refs]
if f"origin/{br_name}" not in remotes:
    repo.git.checkout("-b", br_name)
    repo.git.push("--set-upstream", "origin", br_name)


branches = [b.name for b in repo.branches]
if br_name not in branches:
    repo.git.checkout("-b", br_name, f"origin/{br_name}")


# repo.git.checkout(br_name)

repo.git.add("-A")

repo.git.commit("-m update")

repo.remotes.origin.push()
