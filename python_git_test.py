import git

repo = git.Repo("./")

local_branches = repo.branches
remotes = repo.remotes

# Create Local/ remote

repo.git.checkout("-b", "test_branch_A", "test_branch_A")


pass
