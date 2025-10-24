#!/usr/bin/env python3
"""
Simple script to test GitHub API
Demonstrates basic GitHub API operations using the requests library
"""

import requests
import json
from typing import Optional, Dict, Any


class GitHubAPITester:
    """Class for testing GitHub API endpoints"""
    
    BASE_URL = "https://api.github.com"
    
    def __init__(self, token: Optional[str] = None):
        """
        Initialize GitHub API tester
        
        Args:
            token: Optional GitHub personal access token for authenticated requests
        """
        self.token = token
        self.headers = {
            "Accept": "application/vnd.github.v3+json"
        }
        if token:
            self.headers["Authorization"] = f"token {token}"
    
    def get_user(self, username: str) -> Dict[str, Any]:
        """
        Get information about a GitHub user
        
        Args:
            username: GitHub username
            
        Returns:
            User information as dictionary
        """
        url = f"{self.BASE_URL}/users/{username}"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()
    
    def get_repository(self, owner: str, repo: str) -> Dict[str, Any]:
        """
        Get information about a GitHub repository
        
        Args:
            owner: Repository owner
            repo: Repository name
            
        Returns:
            Repository information as dictionary
        """
        url = f"{self.BASE_URL}/repos/{owner}/{repo}"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()
    
    def list_repositories(self, username: str) -> list:
        """
        List repositories for a user
        
        Args:
            username: GitHub username
            
        Returns:
            List of repositories
        """
        url = f"{self.BASE_URL}/users/{username}/repos"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()
    
    def get_rate_limit(self) -> Dict[str, Any]:
        """
        Get current rate limit status
        
        Returns:
            Rate limit information
        """
        url = f"{self.BASE_URL}/rate_limit"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()


def main():
    """Main function to demonstrate API usage"""
    print("GitHub API Tester")
    print("=" * 50)
    
    # Initialize tester (without token for public API access)
    tester = GitHubAPITester()
    
    # Example: Get user information
    print("\n1. Getting user information for 'octocat':")
    try:
        user_info = tester.get_user("octocat")
        print(f"   Name: {user_info.get('name')}")
        print(f"   Login: {user_info.get('login')}")
        print(f"   Public Repos: {user_info.get('public_repos')}")
    except Exception as e:
        print(f"   Error: {e}")
    
    # Example: Get rate limit
    print("\n2. Checking rate limit:")
    try:
        rate_limit = tester.get_rate_limit()
        core_limit = rate_limit['resources']['core']
        print(f"   Limit: {core_limit['limit']}")
        print(f"   Remaining: {core_limit['remaining']}")
    except Exception as e:
        print(f"   Error: {e}")
    
    print("\n" + "=" * 50)
    print("Testing completed!")


if __name__ == "__main__":
    main()
