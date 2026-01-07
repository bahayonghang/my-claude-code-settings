#!/usr/bin/env python3
import os
import sys
import shutil
import argparse
import datetime
from pathlib import Path
from dataclasses import dataclass
from typing import Optional, List
from enum import Enum

# --- Data Models for TUI ---
class SkillStatus(Enum):
    """Installation status of a skill."""
    INSTALLED = "installed"
    NOT_INSTALLED = "not_installed"
    EXTERNAL = "external"

@dataclass
class SkillInfo:
    """Structured information about a skill."""
    name: str
    description: Optional[str] = None
    status: SkillStatus = SkillStatus.NOT_INSTALLED
    source_path: Optional[Path] = None
    target_path: Optional[Path] = None

@dataclass
class InstallationResult:
    """Result of an installation operation."""
    success: bool
    skill_name: str
    source_path: Path
    target_path: Path
    message: str
    error: Optional[str] = None

# --- Colors & Styles (Standard ANSI) ---
class Colors:
    HEADER = '\033[95m'
    INFO = '\033[94m'
    SUCCESS = '\033[92m'
    WARN = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

def log_info(msg): print(f"{Colors.INFO}[INFO] {Colors.ENDC} {msg}")
def log_success(msg): print(f"{Colors.SUCCESS}[SUCCESS] {Colors.ENDC} {msg}")
def log_warn(msg): print(f"{Colors.WARN}[WARN] {Colors.ENDC} {msg}")
def log_error(msg): print(f"{Colors.FAIL}[ERROR] {Colors.ENDC} {msg}")

# --- Configuration ---
SCRIPT_DIR = Path(__file__).parent.absolute()
SKILLS_SRC_DIR = SCRIPT_DIR / "skills"
PROMPTS_SRC_DIR = SCRIPT_DIR / "prompts"
COMMANDS_SRC_DIR = SCRIPT_DIR / "commands"
HOME_DIR = Path.home()

TARGET_CONFIG = {
    "claude": {
        "base": HOME_DIR / ".claude",
        "skills": HOME_DIR / ".claude" / "skills",
        "commands": HOME_DIR / ".claude" / "commands",
        "prompt": HOME_DIR / ".claude" / "CLAUDE.md"
    },
    "codex": {
        "base": HOME_DIR / ".codex",
        "skills": HOME_DIR / ".codex" / "skills",
        "commands": HOME_DIR / ".codex" / "prompts",
        "prompt": None
    },
    "gemini": {
        "base": HOME_DIR / ".gemini",
        "skills": HOME_DIR / ".gemini" / "skills",
        "commands": HOME_DIR / ".gemini" / "commands",
        "prompt": None
    }
}

class SkillManager:
    def __init__(self, target):
        self.target = target
        self.config = TARGET_CONFIG[target]
        self.target_skills_dir = self.config["skills"]
        self.target_commands_dir = self.config["commands"]

    def ensure_dirs(self):
        self.config["base"].mkdir(parents=True, exist_ok=True)
        self.target_skills_dir.mkdir(parents=True, exist_ok=True)
        self.target_commands_dir.mkdir(parents=True, exist_ok=True)

    def get_skill_description(self, skill_path):
        skill_md = skill_path / "SKILL.md"
        if skill_md.exists():
            with open(skill_md, 'r', encoding='utf-8') as f:
                for line in f:
                    if line.startswith("description:"):
                        return line.replace("description:", "").strip()
        return None

    def list_available(self):
        print(f"\n{Colors.HEADER}=== Available Skills in Repository (Target: {self.target}) ==={Colors.ENDC}")
        if not SKILLS_SRC_DIR.exists():
            log_error(f"Skills directory not found: {SKILLS_SRC_DIR}")
            return

        skills = sorted([d for d in SKILLS_SRC_DIR.iterdir() if d.is_dir()])
        for i, skill in enumerate(skills, 1):
            desc = self.get_skill_description(skill)
            status = f"{Colors.SUCCESS}Installed{Colors.ENDC}" if (self.target_skills_dir / skill.name).exists() else f"{Colors.FAIL}Not installed{Colors.ENDC}"
            print(f"\n[{i}] {Colors.BOLD}{skill.name}{Colors.ENDC}")
            if desc: print(f"    Description: {desc}")
            print(f"    Status: {status}")

    def list_installed(self):
        print(f"\n{Colors.HEADER}=== Installed Skills (Target: {self.target}) ==={Colors.ENDC}")
        if not self.target_skills_dir.exists():
            log_warn("No skills directory found.")
            return

        installed = sorted([d for d in self.target_skills_dir.iterdir() if d.is_dir()])
        if not installed:
            log_warn("No skills installed.")
            return

        for skill in installed:
            source = "This repository" if (SKILLS_SRC_DIR / skill.name).exists() else "External"
            print(f" • {Colors.SUCCESS}{skill.name}{Colors.ENDC} ({source})")

    def install_skill(self, skill_name, quiet=False):
        src = SKILLS_SRC_DIR / skill_name
        dst = self.target_skills_dir / skill_name

        if not src.exists():
            log_error(f"Skill not found in repository: {skill_name}")
            return False

        self.ensure_dirs()
        if dst.exists():
            if not quiet: log_warn(f"Overwriting existing skill: {skill_name}")
            shutil.rmtree(dst)

        shutil.copytree(src, dst)
        if not quiet: log_success(f"Installed: {skill_name} -> {dst}")
        return True

    def install_commands(self):
        log_info(f"Installing commands for {self.target}...")
        self.ensure_dirs()
        
        # Determine source directory based on target
        if self.target == "gemini":
            src_cmd_dir = COMMANDS_SRC_DIR / "gemini"
        else:
            # Claude and Codex share commands from 'claude' folder
            src_cmd_dir = COMMANDS_SRC_DIR / "claude"
            
        if not src_cmd_dir.exists():
            log_warn(f"No specific commands found for target {self.target} in {src_cmd_dir}")
            return

        # Copy contents to target_commands_dir
        try:
            # shutil.copytree requires the destination dir to not exist for Python < 3.8 if dirs_exist_ok is not used
            # We use dirs_exist_ok=True (Python 3.8+) to allow merging/overwriting
            shutil.copytree(src_cmd_dir, self.target_commands_dir, dirs_exist_ok=True)
            
            log_success(f"Installed commands to {self.target_commands_dir}")
            if self.target == "codex":
                log_info(f"Note: For Codex, commands are installed as prompts in {self.target_commands_dir}")
        except Exception as e:
            log_error(f"Failed to install commands: {e}")

    def install_all(self):
        log_info(f"Installing all skills to {self.target}...")
        skills = sorted([d.name for d in SKILLS_SRC_DIR.iterdir() if d.is_dir()])
        count = 0
        for name in skills:
            if self.install_skill(name, quiet=True):
                count += 1
        log_success(f"Finished! Installed {count} skills.")
        
        # Also install commands
        self.install_commands()

    def interactive(self):
        self.list_available()
        skills = sorted([d.name for d in SKILLS_SRC_DIR.iterdir() if d.is_dir()])
        try:
            val = input(f"\n{Colors.INFO}Select numbers to install (space-separated, or 'all'):{Colors.ENDC} ").strip()
        except EOFError:
            return
        
        if val.lower() == 'all':
            self.install_all()
            return

        count = 0
        for idx_str in val.split():
            try:
                idx = int(idx_str) - 1
                if 0 <= idx < len(skills):
                    if self.install_skill(skills[idx]):
                        count += 1
                else:
                    log_warn(f"Invalid index: {idx_str}")
            except ValueError:
                log_warn(f"Skipping invalid input: {idx_str}")
        log_success(f"Finished! Installed {count} skills.")

    def prompt_update(self):
        if self.target != "claude":
            log_error("prompt-update is only supported for 'claude' target.")
            return

        local_md = PROMPTS_SRC_DIR / "CLAUDE.md"
        global_md = self.config["prompt"]

        if not local_md.exists():
            log_error(f"Local CLAUDE.md not found: {local_md}")
            return

        self.ensure_dirs()
        if global_md.exists():
            timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
            backup = global_md.parent / f"CLAUDE.md.backup.{timestamp}"
            log_info(f"Backing up existing CLAUDE.md to {backup.name}")
            shutil.copy2(global_md, backup)

        shutil.copy2(local_md, global_md)
        log_success(f"Global CLAUDE.md updated successfully.")

    def prompt_diff(self):
        if self.target != "claude":
            log_error("prompt-diff is only supported for 'claude' target.")
            return

        local_md = PROMPTS_SRC_DIR / "CLAUDE.md"
        global_md = self.config["prompt"]

        if not local_md.exists():
            log_error(f"Local CLAUDE.md not found: {local_md}")
            return

        if not global_md.exists():
            log_warn("Global CLAUDE.md does not exist.")
            return

        import difflib
        with open(local_md, 'r', encoding='utf-8') as f1, open(global_md, 'r', encoding='utf-8') as f2:
            diff = difflib.unified_diff(
                f2.readlines(), f1.readlines(),
                fromfile='Global CLAUDE.md', tofile='Local CLAUDE.md'
            )
            for line in diff:
                sys.stdout.write(line)

def main():
    parser = argparse.ArgumentParser(description="Unified Skills & Config Manager")
    parser.add_argument("command", choices=["list", "installed", "install", "install-all", "install-commands", "interactive", "prompt-update", "prompt-diff"], help="Command to execute")
    parser.add_argument("skills", nargs="*", help="Skill names to install (for 'install' command)")
    parser.add_argument("--target", choices=["claude", "codex", "gemini"], default="claude", help="Target platform (default: claude)")

    args = parser.parse_args()
    mgr = SkillManager(args.target)

    if args.command == "list": mgr.list_available()
    elif args.command == "installed": mgr.list_installed()
    elif args.command == "install":
        if not args.skills:
            log_error("Please specify at least one skill name.")
        else:
            for s in args.skills: mgr.install_skill(s)
    elif args.command == "install-all": mgr.install_all()
    elif args.command == "install-commands": mgr.install_commands()
    elif args.command == "interactive": mgr.interactive()
    elif args.command == "prompt-update": mgr.prompt_update()
    elif args.command == "prompt-diff": mgr.prompt_diff()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nAborted by user.")
        sys.exit(0)
