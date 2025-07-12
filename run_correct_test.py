import os
import subprocess

def run_correct_test():
    """Run the correct bot for testing on @Alphahubhai"""
    print("🧪 Running CORRECT test on @Alphahubhai...")
    print("🔧 Using CORRECT email: sparshkumar510@gmail.com")
    
    # Import and run the correct bot
    from correct_github_bot import CorrectGitHubBot
    
    bot = CorrectGitHubBot()
    
    # Run with a shorter date range for testing (1 month)
    bot.run("2024-12-01", "2024-12-31")
    
    print("✅ Correct test completed!")
    print("🔗 Check your profile: https://github.com/Alphahubhai")

if __name__ == "__main__":
    run_correct_test() 