from src.enterprise.repository_manager import RepositoryManager

repo = RepositoryManager()

print("Policies :", repo.total_policies())

print("Chunks :", repo.total_chunks())

print(repo.list_policies().head())

print(repo.list_chunks().head())