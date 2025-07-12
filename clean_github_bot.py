import os
import random
import datetime
import subprocess

class CleanGitHubBot:
    def __init__(self):
        self.file_types = [
            'main.py', 'utils.py', 'config.py', 'app.py',
            'src/main.py', 'src/utils.py', 'src/config.py',
            'docs/README.md', 'docs/API.md',
            'config/settings.json', 'config/database.yml'
        ]
    
    def setup_git_config(self):
        """Setup proper Git configuration for @Alphahubhai"""
        print("🔧 Setting up Git configuration...")
        
        # Set Git user for @Alphahubhai
        os.system('git config user.name "Alphahubhai"')
        os.system('git config user.email "alphahubhai@gmail.com"')  # Use the email associated with @Alphahubhai
        
        print("✅ Git configuration set for @Alphahubhai")
        return True
    
    def setup_repository(self):
        """Setup repository for @Alphahubhai"""
        print("🔄 Setting up repository for @Alphahubhai...")
        
        # Set the correct repository URL
        repo_url = "https://github.com/Alphahubhai/Github-Bot.git"
        os.system(f'git remote set-url origin {repo_url}')
        
        # Test connection
        try:
            result = subprocess.run(['git', 'remote', 'get-url', 'origin'], 
                                  capture_output=True, text=True)
            print(f"✅ Repository: {result.stdout.strip()}")
            return True
        except:
            print("❌ Failed to setup repository")
            return False
    
    def clean_repository(self):
        """Remove all existing commits and start fresh"""
        print("🧹 Cleaning repository...")
        
        # Force delete all commits and start fresh
        os.system('git checkout --orphan temp_branch')
        os.system('git add -A')
        os.system('git commit -m "Initial commit"')
        os.system('git branch -D main')
        os.system('git branch -m main')
        os.system('git push -f origin main')
        
        print("✅ Repository cleaned up")
    
    def generate_realistic_pattern(self, start_date: datetime.date, end_date: datetime.date):
        """Generate realistic random pattern with varied intensity"""
        pattern = []
        current_date = start_date
        
        print(f"📊 Generating commits from {start_date} to {end_date}")
        
        while current_date <= end_date:
            # Random decision: skip day or create commits
            if self._should_skip_day(current_date):
                current_date += datetime.timedelta(days=1)
                continue
            
            # Generate random number of commits (0-20)
            commits = self._get_random_commit_count(current_date)
            if commits > 0:
                pattern.append((current_date, commits))
            
            current_date += datetime.timedelta(days=1)
        
        print(f"✅ Will create commits for {len(pattern)} active days")
        return pattern
    
    def _should_skip_day(self, date: datetime.date) -> bool:
        """Randomly skip days to create realistic gaps"""
        weekday = date.weekday()
        
        # Weekend patterns - more likely to skip
        if weekday in [5, 6]:  # Weekend
            return random.random() < 0.6  # 60% chance to skip weekends
        
        # Weekday patterns - less likely to skip
        if weekday in [0, 1, 2, 3, 4]:  # Weekdays
            return random.random() < 0.15  # 15% chance to skip weekdays
        
        return False
    
    def _get_random_commit_count(self, date: datetime.date) -> int:
        """Get random commit count with varied intensity"""
        weekday = date.weekday()
        
        # Different patterns for different days
        if weekday in [0, 1, 2, 3, 4]:  # Weekdays
            # Random distribution: some days light, some medium, some heavy
            rand = random.random()
            if rand < 0.4:  # 40% chance - light activity
                return random.randint(1, 3)
            elif rand < 0.7:  # 30% chance - medium activity
                return random.randint(4, 8)
            elif rand < 0.9:  # 20% chance - heavy activity
                return random.randint(9, 15)
            else:  # 10% chance - very heavy activity
                return random.randint(16, 25)
        
        else:  # Weekends
            # Weekend work is less common but still happens
            if random.random() < 0.7:  # 70% chance no work
                return 0
            else:
                return random.randint(1, 8)
    
    def create_commit(self, date: datetime.date, commit_count: int):
        """Create realistic commits for a given date"""
        for i in range(commit_count):
            # Choose a random file
            file_path = random.choice(self.file_types)
            
            # Create directory if needed
            dir_path = os.path.dirname(file_path)
            if dir_path:
                os.makedirs(dir_path, exist_ok=True)
            
            # Generate content
            content = self._generate_file_content(file_path)
            
            # Write to file
            with open(file_path, 'w') as f:
                f.write(content)
            
            # Stage and commit
            os.system(f'git add {file_path}')
            
            # Generate commit message
            commit_msg = self._generate_commit_message(file_path)
            
            # Use proper ISO date format with random time
            hour = random.randint(9, 18)  # Work hours
            minute = random.randint(0, 59)
            second = random.randint(0, 59)
            iso_date = f"{date.strftime('%Y-%m-%d')} {hour:02d}:{minute:02d}:{second:02d}"
            
            # Create commit with proper date
            os.system(f'git commit --date="{iso_date}" -m "{commit_msg}"')
    
    def _generate_file_content(self, file_path: str) -> str:
        """Generate realistic file content"""
        file_name = os.path.basename(file_path)
        
        if file_path.endswith('.py'):
            return f'''import os
import sys

def main():
    """Main function for {file_name}"""
    print("Hello from {file_name}")
    
    # Configuration
    config = {{
        "debug": True,
        "timeout": 30
    }}
    
    return True

if __name__ == "__main__":
    main()
'''
        elif file_path.endswith('.md'):
            return f'''# {file_name.replace('.md', '').title()}

This is documentation for {file_name}.

## Features

- Feature 1: Core functionality
- Feature 2: Advanced options
- Feature 3: Integration support

## Usage

```bash
# Example usage
python {file_name.replace('.md', '.py')}
```

## Contributing

Please read the contributing guidelines.

## License

MIT License
'''
        elif file_path.endswith('.json'):
            return f'''{{
  "name": "{file_name.replace('.json', '')}",
  "version": "1.0.0",
  "description": "Configuration for {file_name}",
  "author": "Alphahubhai",
  "settings": {{
    "debug": true,
    "timeout": 30,
    "max_retries": 3,
    "database": {{
      "host": "localhost",
      "port": 5432
    }}
  }}
}}'''
        elif file_path.endswith('.yml'):
            return f'''# {file_name}
# Configuration file

database:
  host: localhost
  port: 5432
  name: myapp
  user: admin

logging:
  level: INFO
  format: "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
  file: "app.log"

server:
  port: 8000
  host: "0.0.0.0"
'''
        else:
            return f"# {file_name}\n\nGenerated content for {file_name}\n\nThis file contains configuration and utilities."
    
    def _generate_commit_message(self, file_path: str) -> str:
        """Generate realistic commit message"""
        file_name = os.path.basename(file_path)
        
        messages = [
            f"Update {file_name}",
            f"Fix bug in {file_name}",
            f"Add feature to {file_name}",
            f"Refactor {file_name}",
            f"Improve {file_name}",
            f"Update documentation in {file_name}",
            f"Fix formatting in {file_name}",
            f"Add tests for {file_name}",
            f"Optimize {file_name}",
            f"Clean up {file_name}",
            f"Fix linting issues in {file_name}",
            f"Update configuration in {file_name}",
            f"Add error handling to {file_name}",
            f"Improve performance in {file_name}",
            f"Update dependencies in {file_name}",
            f"Enhance {file_name}",
            f"Restructure {file_name}",
            f"Add new functionality to {file_name}",
            f"Fix security issue in {file_name}",
            f"Update API in {file_name}"
        ]
        
        return random.choice(messages)
    
    def run(self, start_date_str: str = "2024-01-01", end_date_str: str = "2025-07-01"):
        """Run the clean bot"""
        print("🎯 Clean GitHub Bot for @Alphahubhai")
        print("=" * 50)
        
        # Setup Git configuration
        if not self.setup_git_config():
            print("❌ Failed to setup Git configuration")
            return
        
        # Setup repository
        if not self.setup_repository():
            print("❌ Failed to setup repository")
            return
        
        # Clean repository
        self.clean_repository()
        
        # Parse dates
        start_date = datetime.datetime.strptime(start_date_str, "%Y-%m-%d").date()
        end_date = datetime.datetime.strptime(end_date_str, "%Y-%m-%d").date()
        
        print(f"📅 Date range: {start_date} to {end_date}")
        
        # Generate pattern
        pattern = self.generate_realistic_pattern(start_date, end_date)
        
        # Create commits
        total_commits = 0
        for i, (date, commit_count) in enumerate(pattern):
            print(f"📅 {date}: {commit_count} commits ({i+1}/{len(pattern)})")
            self.create_commit(date, commit_count)
            total_commits += commit_count
            
            # Push every 100 commits to avoid overwhelming
            if total_commits % 100 == 0:
                print(f"🚀 Pushing batch of commits...")
                os.system('git push origin main')
        
        # Final push
        print("🚀 Pushing final commits to GitHub...")
        os.system('git push origin main')
        
        print(f"✅ Done! Created {total_commits} commits for @Alphahubhai")
        print(f"🔗 Check your profile: https://github.com/Alphahubhai")

def main():
    """Main function"""
    print("🎯 Clean GitHub Bot")
    print("=" * 50)
    print("This will create realistic commits for @Alphahubhai")
    print("Testing phase - will create varied green squares")
    
    confirm = input("\nContinue? (y/n): ").strip().lower()
    
    if confirm == 'y':
        bot = CleanGitHubBot()
        bot.run()
    else:
        print("❌ Cancelled")

if __name__ == "__main__":
    main() 