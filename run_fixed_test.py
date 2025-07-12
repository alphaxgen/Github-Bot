import os
import subprocess

def run_fixed_test():
    """Run the fixed bot for testing on @Alphahubhai"""
    print("🧪 Running FIXED test on @Alphahubhai...")
    print("🔧 Using CORRECT email address...")
    
    # Import and run the fixed bot
    from fixed_github_bot import FixedGitHubBot
    
    bot = FixedGitHubBot()
    
    # Run with a shorter date range for testing (1 month)
    bot.run("2024-12-01", "2024-12-31")
    
    print("✅ Fixed test completed!")
    print("🔗 Check your profile: https://github.com/Alphahubhai")

if __name__ == "__main__":
    run_fixed_test() 