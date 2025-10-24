# test
Repository untuk test GitHub API

## Deskripsi
Repository ini dibuat untuk testing dan eksplorasi GitHub API. Berisi contoh script Python yang mendemonstrasikan penggunaan dasar GitHub REST API.

## Fitur
- Mendapatkan informasi user GitHub
- Mendapatkan informasi repository
- Melihat daftar repository user
- Mengecek rate limit API

## Instalasi

1. Clone repository ini:
```bash
git clone https://github.com/satrimu/test.git
cd test
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Penggunaan

### Menjalankan script test:
```bash
python test_github_api.py
```

### Menggunakan dengan token (opsional):
Untuk akses API dengan rate limit lebih tinggi, gunakan GitHub personal access token:

```python
from test_github_api import GitHubAPITester

# Inisialisasi dengan token
tester = GitHubAPITester(token="your_github_token_here")

# Gunakan method yang tersedia
user_info = tester.get_user("octocat")
print(user_info)
```

## Contoh Penggunaan

```python
from test_github_api import GitHubAPITester

# Tanpa token (rate limit rendah)
tester = GitHubAPITester()

# Mendapatkan info user
user = tester.get_user("octocat")
print(f"User: {user['login']}, Repos: {user['public_repos']}")

# Mendapatkan info repository
repo = tester.get_repository("octocat", "Hello-World")
print(f"Repo: {repo['full_name']}, Stars: {repo['stargazers_count']}")

# List repositories
repos = tester.list_repositories("octocat")
for repo in repos[:5]:
    print(f"- {repo['name']}")

# Cek rate limit
rate_limit = tester.get_rate_limit()
print(f"API calls remaining: {rate_limit['resources']['core']['remaining']}")
```

## Dokumentasi API
Untuk informasi lebih lanjut tentang GitHub API, kunjungi:
- [GitHub REST API Documentation](https://docs.github.com/en/rest)
- [GitHub API v3](https://developer.github.com/v3/)

## Lisensi
Open source untuk keperluan testing dan pembelajaran
