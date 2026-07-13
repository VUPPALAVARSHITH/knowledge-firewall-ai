from src.enterprise.managers.repository_manager import RepositoryManager

repo = RepositoryManager()

print("Policies")
print(repo.list_policies().columns.tolist())

print()

print("Chunks")
print(repo.list_chunks().columns.tolist())