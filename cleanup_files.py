import os
import shutil

def cleanup_files():
    """Remove unnecessary files and keep only essential ones"""
    print("🧹 Cleaning up unnecessary files...")
    
    # Files to keep
    keep_files = [
        'clean_github_bot.py',
        'cleanup_files.py',
        'README.md',
        'LICENSE',
        'main.py',
        'data.txt'
    ]
    
    # Directories to remove
    remove_dirs = [
        'src',
        'tests', 
        'docs',
        'config',
        'scripts',
        '__pycache__'
    ]
    
    # Files to remove
    remove_files = [
        'advanced_github_bot.py',
        'comprehensive_github_bot.py',
        'flexible_github_bot.py',
        'simple_github_bot.py',
        'realistic_github_bot.py',
        'test_accounts.py',
        'check_github_config.py',
        'cleanup.py',
        'setup_complete_bot.py',
        'github_setup_guide.md',
        'USAGE_GUIDE.md',
        'app.py',
        'config.py',
        'server.py',
        'utils.py',
        'package.json',
        'requirements.txt',
        'Dockerfile',
        '.env.example'
    ]
    
    # Remove directories
    for dir_name in remove_dirs:
        if os.path.exists(dir_name):
            try:
                shutil.rmtree(dir_name)
                print(f"✅ Removed directory: {dir_name}")
            except Exception as e:
                print(f"❌ Failed to remove {dir_name}: {e}")
    
    # Remove files
    for file_name in remove_files:
        if os.path.exists(file_name):
            try:
                os.remove(file_name)
                print(f"✅ Removed file: {file_name}")
            except Exception as e:
                print(f"❌ Failed to remove {file_name}: {e}")
    
    print("\n✅ Cleanup completed!")
    print("📁 Remaining files:")
    for file in os.listdir('.'):
        if os.path.isfile(file):
            print(f"  - {file}")

if __name__ == "__main__":
    cleanup_files() 