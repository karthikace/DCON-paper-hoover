# 📄 DCON26 Paper Hoover

> Because downloading 300 conference PDFs one-by-one is a punishment no engineer deserves.

## What is this?

A semi-automated Playwright script that logs into the DCON26 conference portal, browses every session, and vacuums up all the handout PDFs into tidy little folders - so you can pretend you'll read them later.

## The Workflow

```
You ➜ Add credentials ➜ Solve CAPTCHA like a good human ➜ Scroll to the bottom ➜ Go make coffee ☕
Script ➜ Opens 9000 tabs ➜ Downloads everything ➜ Cleans up empty folders ➜ Feels nothing
```

## Requirements

- Python 3.x
- A soul willing to solve one (1) CAPTCHA
- Functioning scroll wheel finger

```bash
pip install playwright
playwright install chromium
```

## Usage

1. Create a `credentials.txt` file in the project root:
   ```
   your.email@example.com
   your.password
   ```
2. Run it:
   ```bash
   python download_script.py
   ```
3. Solve the CAPTCHA when prompted. Yes, you - the robot couldn't do it. The irony is not lost on us.
   
5. **Scroll to the bottom of the session gallery to load all results, then press Enter.**
   
7. Watch the script middle click its way through every session like a caffeinated grad student at 2 AM.
   
9. Find your PDFs in the `Conference_Papers/` directory, organized by session title.

## FAQ

**Q: Is this legal?**

A: You're downloading papers you have legitimate access to. You're just... faster now.

**Q: Why is it not fully headless?**

A: CAPTCHA. Humanity's last stand against automation, and apparently it's working.

**Q: Will you read all these papers?**

A: No. But they'll look great in a folder.

## License

MIT - do whatever you want, just don't mass-email the authors asking for TL;DRs.
