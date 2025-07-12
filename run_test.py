import os
import subprocess

def run_test():
    """Run the clean bot for testing on @Alphahubhai"""
    print("🧪 Running test on @Alphahubhai...")
    
    # Import and run the clean bot
    from clean_github_bot import CleanGitHubBot
    
    bot = CleanGitHubBot()
    
    # Run with a shorter date range for testing (1 month)
    bot.run("2024-12-01", "2024-12-31")
    
    print("✅ Test completed!")
    print("🔗 Check your profile: https://github.com/Alphahubhai")

if __name__ == "__main__":
    run_test() 