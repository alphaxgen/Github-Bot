# 🎯 Clean GitHub Bot for @Alphahubhai

A clean, focused bot that creates realistic GitHub contributions for testing on @Alphahubhai account.

## 🧹 First: Clean Up Files

Before running the bot, clean up all unnecessary files:

```bash
python cleanup_files.py
```

**Date Range:** This script is configured to create commits from April 20th, 2024 (your account creation date) until July 1st, 2025.

## Getting Started

Follow these steps to bring your contribution graph to life:

1. **Clone this repository**
```bash
git clone https://github.com/Alphahubhai/Github-Bot.git
cd Github-Bot
```
```

This will remove all the old bot files and keep only the essential ones.

## 🎯 Features

### Realistic Random Patterns
- **Varied intensity**: Light green (1-3), medium green (4-8), dark green (9-15), very dark green (16-25)
- **Random gaps**: Realistic breaks (weekends, sick days, holidays)
- **No patterns**: Completely random but realistic
- **Weekend patterns**: Less activity on weekends but still some work

### Proper Git Configuration
- **Correct user**: Set to @Alphahubhai
- **Proper email**: Uses email associated with @Alphahubhai account
- **Clean repository**: Removes all existing commits
- **Correct dates**: Uses proper ISO date format

### Authentic Content
- **Multiple file types**: Python, Markdown, JSON, YAML
- **Realistic commit messages**: Professional, varied messages
- **Proper file structure**: Organized project structure

## 🚀 Quick Start

### Step 1: Clean Up Files
```bash
python cleanup_files.py
```

### Step 2: Run the Bot
```bash
python clean_github_bot.py
```

### Step 3: Check Results
Visit: https://github.com/Alphahubhai

## 📊 What You'll See

### Contribution Levels
- **Light green**: 1-3 commits (40% of active days)
- **Medium green**: 4-8 commits (30% of active days)  
- **Dark green**: 9-15 commits (20% of active days)
- **Very dark green**: 16-25 commits (10% of active days)
- **No green**: Skipped days (weekends, breaks)

### Random Patterns
- **Weekends**: 60% chance to skip, 40% chance to work
- **Weekdays**: 15% chance to skip, 85% chance to work
- **Varied intensity**: Some days light, some heavy
- **Natural gaps**: Realistic breaks in activity

## ⚠️ Important Notes

1. **Test account**: This bot is specifically for @Alphahubhai testing
2. **Clean start**: Removes all existing commits
3. **Proper dates**: Uses correct ISO date format
4. **Realistic patterns**: No obvious automation

## 🔧 Configuration

The bot is pre-configured for @Alphahubhai:
- **Git user**: Alphahubhai
- **Git email**: alphahubhai@gmail.com
- **Repository**: https://github.com/Alphahubhai/Github-Bot.git
- **Date range**: January 1, 2024 to July 1, 2025

## 📈 Expected Results

After running the bot, @Alphahubhai's GitHub profile will show:
- **Realistic green squares**: Varied intensity levels
- **Natural patterns**: No obvious automation
- **Professional appearance**: Looks like real development work
- **Random gaps**: Realistic breaks in activity

## 🎯 For Main Account (@alphaxgen)

Once testing on @Alphahubhai is successful, you can modify the bot for @alphaxgen:

1. Change the Git configuration in `clean_github_bot.py`
2. Update the repository URL
3. Run the same process

## ⚡ Troubleshooting

### No green squares appearing?
- Check Git configuration is correct
- Ensure repository exists on GitHub
- Verify you have push permissions

### Permission denied?
- Check your GitHub authentication
- Make sure you can push to the repository

### Wrong account?
- The bot is configured for @Alphahubhai
- Check the Git user and email settings

## 📋 Files

After cleanup, you'll have:
- `clean_github_bot.py` - Main bot
- `cleanup_files.py` - Cleanup script
- `README.md` - This file
- `LICENSE` - License file
- `main.py` - Simple main file
- `data.txt` - Data file

The bot will create a realistic, random contribution pattern that looks completely authentic!