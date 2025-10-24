"""
Example usage of GitHub API tester
Shows various ways to use the GitHubAPITester class
"""

from test_github_api import GitHubAPITester


def example_basic_usage():
    """Example: Basic usage without authentication"""
    print("Example 1: Basic Usage (No Authentication)")
    print("-" * 50)
    
    tester = GitHubAPITester()
    
    try:
        # Get user information
        user = tester.get_user("torvalds")
        print(f"Username: {user['login']}")
        print(f"Name: {user.get('name', 'N/A')}")
        print(f"Public Repos: {user['public_repos']}")
        print(f"Followers: {user['followers']}")
    except Exception as e:
        print(f"Error: {e}")
    
    print()


def example_with_token():
    """Example: Usage with authentication token"""
    print("Example 2: With Authentication Token")
    print("-" * 50)
    
    # Replace with your actual token
    token = "your_github_token_here"
    tester = GitHubAPITester(token=token)
    
    try:
        # Get repository information
        repo = tester.get_repository("octocat", "Hello-World")
        print(f"Repository: {repo['full_name']}")
        print(f"Description: {repo['description']}")
        print(f"Stars: {repo['stargazers_count']}")
        print(f"Forks: {repo['forks_count']}")
        print(f"Language: {repo['language']}")
    except Exception as e:
        print(f"Error: {e}")
    
    print()


def example_list_repos():
    """Example: List user repositories"""
    print("Example 3: List User Repositories")
    print("-" * 50)
    
    tester = GitHubAPITester()
    
    try:
        repos = tester.list_repositories("github")
        print(f"Found {len(repos)} repositories")
        print("\nFirst 5 repositories:")
        for repo in repos[:5]:
            print(f"  - {repo['name']}: {repo.get('description', 'No description')}")
    except Exception as e:
        print(f"Error: {e}")
    
    print()


def example_rate_limit():
    """Example: Check rate limit"""
    print("Example 4: Check API Rate Limit")
    print("-" * 50)
    
    tester = GitHubAPITester()
    
    try:
        rate_info = tester.get_rate_limit()
        core = rate_info['resources']['core']
        search = rate_info['resources']['search']
        
        print(f"Core API:")
        print(f"  Limit: {core['limit']}")
        print(f"  Remaining: {core['remaining']}")
        print(f"  Reset: {core['reset']}")
        
        print(f"\nSearch API:")
        print(f"  Limit: {search['limit']}")
        print(f"  Remaining: {search['remaining']}")
    except Exception as e:
        print(f"Error: {e}")
    
    print()


if __name__ == "__main__":
    print("GitHub API Examples")
    print("=" * 50)
    print()
    
    # Run examples
    example_basic_usage()
    # example_with_token()  # Uncomment and add token to use
    # example_list_repos()  # Uncomment to use
    # example_rate_limit()  # Uncomment to use
    
    print("=" * 50)
    print("Examples completed!")
    print("\nNote: Some examples may fail due to API rate limits.")
    print("Use a GitHub personal access token for higher rate limits.")
