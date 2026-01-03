<#
.SYNOPSIS
    Claude/Codex Skills & Config Manager for Windows (PowerShell)
.DESCRIPTION
    Manages installation of Claude/Codex skills and configuration.
    Ported from install.sh
.PARAMETER Target
    Target platform: 'claude' (default) or 'codex'
#>

param(
    [string]$Command,
    [ValidateSet("claude", "codex")]
    [string]$Target = "claude",
    [string[]]$RemainingArgs
)

# Configuration
$ErrorActionPreference = "Stop"
$ScriptDir = $PSScriptRoot
$SkillsDir = Join-Path $ScriptDir "skills"
$PromptsDir = Join-Path $ScriptDir "prompts"

# Claude paths
$GlobalClaudeDir = Join-Path $HOME ".claude"
$GlobalClaudeSkillsDir = Join-Path $GlobalClaudeDir "skills"
$GlobalClaudeMd = Join-Path $GlobalClaudeDir "CLAUDE.md"
$LocalClaudeMd = Join-Path $PromptsDir "CLAUDE.md"

# Codex paths
$GlobalCodexDir = Join-Path $HOME ".codex"
$GlobalCodexSkillsDir = Join-Path $GlobalCodexDir "skills"

# Helper Functions
function Write-Info { param([string]$Message) Write-Host "[INFO] $Message" -ForegroundColor Blue }
function Write-Success { param([string]$Message) Write-Host "[SUCCESS] $Message" -ForegroundColor Green }
function Write-Warn { param([string]$Message) Write-Host "[WARN] $Message" -ForegroundColor Yellow }
function Write-Error { param([string]$Message) Write-Host "[ERROR] $Message" -ForegroundColor Red }

function Get-TargetBaseDir {
    if ($Target -eq "codex") {
        return $GlobalCodexDir
    }
    return $GlobalClaudeDir
}

function Get-TargetSkillsDir {
    if ($Target -eq "codex") {
        return $GlobalCodexSkillsDir
    }
    return $GlobalClaudeSkillsDir
}

function Ensure-GlobalDir {
    $baseDir = Get-TargetBaseDir
    $skillsDir = Get-TargetSkillsDir

    if (-not (Test-Path $baseDir)) {
        Write-Info "Creating $baseDir"
        New-Item -ItemType Directory -Path $baseDir -Force | Out-Null
    }
    if (-not (Test-Path $skillsDir)) {
        Write-Info "Creating $skillsDir"
        New-Item -ItemType Directory -Path $skillsDir -Force | Out-Null
    }
}

function Get-SkillDescription {
    param([string]$Path)
    $mdPath = Join-Path $Path "SKILL.md"
    if (Test-Path $mdPath) {
        $content = Get-Content $mdPath -ErrorAction SilentlyContinue
        $descLine = $content | Select-String -Pattern "^description:" | Select-Object -First 1
        if ($descLine) {
            return ($descLine.ToString() -replace "^description:\s*", "").Trim()
        }
    }
    return $null
}

function List-Skills {
    $targetSkillsDir = Get-TargetSkillsDir
    Write-Host "`n=== Available Skills in Repository (Target: $Target) ===" -ForegroundColor Blue

    if (-not (Test-Path $SkillsDir)) {
        Write-Error "Skills directory not found: $SkillsDir"
        return
    }

    $skills = Get-ChildItem -Path $SkillsDir -Directory
    if ($skills.Count -eq 0) {
        Write-Warn "No skills found in $SkillsDir"
        return
    }

    $count = 0
    foreach ($skill in $skills) {
        $count++
        Write-Host "`n[$count] $($skill.Name)" -ForegroundColor Green
        
        $desc = Get-SkillDescription -Path $skill.FullName
        if ($desc) {
            Write-Host "    Description: $desc"
        }

        $installedPath = Join-Path $targetSkillsDir $skill.Name
        if (Test-Path $installedPath) {
            Write-Host "    Status: Already installed" -ForegroundColor Yellow
        } else {
            Write-Host "    Status: Not installed" -ForegroundColor Red
        }
    }
    Write-Host ""
}

function List-Installed {
    $targetSkillsDir = Get-TargetSkillsDir
    Write-Host "`n=== Installed Skills (Target: $Target) ===" -ForegroundColor Blue

    if (-not (Test-Path $targetSkillsDir)) {
        Write-Warn "Skills directory does not exist: $targetSkillsDir"
        return
    }

    $installed = Get-ChildItem -Path $targetSkillsDir -Directory
    if ($installed.Count -eq 0) {
        Write-Warn "No skills installed"
        Write-Host ""
        return
    }

    foreach ($skill in $installed) {
        Write-Host "• $($skill.Name)" -ForegroundColor Green
        
        $repoPath = Join-Path $SkillsDir $skill.Name
        if (Test-Path $repoPath) {
            Write-Host "  Source: This repository"
        } else {
            Write-Host "  Source: External"
        }
    }
    Write-Host ""
}

function Install-Skill {
    param([string]$SkillName)

    $skillSrc = Join-Path $SkillsDir $SkillName
    $targetSkillsDir = Get-TargetSkillsDir
    $skillDst = Join-Path $targetSkillsDir $SkillName

    if (-not (Test-Path $skillSrc)) {
        Write-Error "Skill not found: $SkillName"
        return $false
    }

    Ensure-GlobalDir

    if (Test-Path $skillDst) {
        Write-Warn "Skill '$SkillName' already exists. Overwriting..."
        Remove-Item -Path $skillDst -Recurse -Force
    }

    Write-Info "Installing skill: $SkillName (to $Target)"
    Copy-Item -Path $skillSrc -Destination $skillDst -Recurse -Force
    Write-Success "Installed: $SkillName -> $skillDst"
    return $true
}

function Install-All-Skills {
    Write-Host "`n=== Installing All Skills (Target: $Target) ===`n" -ForegroundColor Blue

    if (-not (Test-Path $SkillsDir)) {
        Write-Error "Skills directory not found: $SkillsDir"
        return
    }

    $count = 0
    $failed = 0
    $skills = Get-ChildItem -Path $SkillsDir -Directory

    foreach ($skill in $skills) {
        if (Install-Skill -SkillName $skill.Name) {
            $count++
        } else {
            $failed++
        }
    }

    Write-Host ""
    Write-Success "Installed $count skills to $Target"
    if ($failed -gt 0) {
        Write-Error "Failed to install $failed skills"
    }
}

function Install-Interactive {
    List-Skills
    
    Write-Host "Select skills to install (space-separated numbers, or 'all'):" -ForegroundColor Blue -NoNewline
    $selection = Read-Host " "

    if ($selection -eq "all") {
        Install-All-Skills
        return
    }

    $skills = @(Get-ChildItem -Path $SkillsDir -Directory)
    $count = 0
    
    $indices = $selection -split "\s+"
    foreach ($idxStr in $indices) {
        if ($idxStr -match "^\d+$") {
            $idx = [int]$idxStr - 1
            if ($idx -ge 0 -and $idx -lt $skills.Count) {
                if (Install-Skill -SkillName $skills[$idx].Name) {
                    $count++
                }
            } else {
                Write-Warn "Invalid selection number: $idxStr"
            }
        } else {
            if (-not [string]::IsNullOrWhiteSpace($idxStr)) {
                Write-Warn "Invalid input: $idxStr"
            }
        }
    }

    Write-Host ""
    Write-Success "Installed $count skills to $Target"
}

function Update-Global-Prompt {
    if (-not (Test-Path $LocalClaudeMd)) {
        Write-Error "Local CLAUDE.md not found: $LocalClaudeMd"
        return
    }

    Ensure-GlobalDir

    if (Test-Path $GlobalClaudeMd) {
        $timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
        $backup = "$GlobalClaudeMd.backup.$timestamp"
        Write-Info "Backing up existing CLAUDE.md to: $backup"
        Copy-Item -Path $GlobalClaudeMd -Destination $backup -Force
    }

    Write-Info "Copying $LocalClaudeMd -> $GlobalClaudeMd"
    Copy-Item -Path $LocalClaudeMd -Destination $GlobalClaudeMd -Force
    Write-Success "Global CLAUDE.md updated successfully"
}

function Diff-Prompt {
    if (-not (Test-Path $LocalClaudeMd)) {
        Write-Error "Local CLAUDE.md not found: $LocalClaudeMd"
        return
    }

    if (-not (Test-Path $GlobalClaudeMd)) {
        Write-Warn "Global CLAUDE.md does not exist yet"
        return
    }

    Write-Host "`n=== Diff: Local vs Global CLAUDE.md ===`n" -ForegroundColor Blue
    
    # Try to use git diff if available, otherwise Compare-Object
    if (Get-Command git -ErrorAction SilentlyContinue) {
        git diff --no-index "$GlobalClaudeMd" "$LocalClaudeMd"
    } else {
        # Fallback to simple comparison
        if (Get-Command fc -ErrorAction SilentlyContinue) {
            fc "$GlobalClaudeMd" "$LocalClaudeMd"
        } else {
            Compare-Object (Get-Content $GlobalClaudeMd) (Get-Content $LocalClaudeMd)
        }
    }
}

function Show-Usage {
    Write-Host "Claude/Codex Skills & Config Manager (PowerShell)" -ForegroundColor Blue
    Write-Host ""
    Write-Host "Usage: .\install.ps1 [-Target claude|codex] [COMMAND] [OPTIONS]"
    Write-Host ""
    Write-Host "Commands:"
    Write-Host "  list              List all available skills in repository"
    Write-Host "  installed         List currently installed skills"
    Write-Host "  install [SKILL]   Install specific skill(s) (space-separated)"
    Write-Host "  install-all       Install all skills from repository"
    Write-Host "  interactive       Interactive skill selection and installation"
    Write-Host "  prompt-update     Update global CLAUDE.md with local version"
    Write-Host "  prompt-diff       Show diff between local and global CLAUDE.md"
    Write-Host "  help              Show this help message"
    Write-Host ""
    Write-Host "Options:"
    Write-Host "  -Target claude    Install to ~/.claude/skills (default)"
    Write-Host "  -Target codex     Install to ~/.codex/skills"
    Write-Host ""
    Write-Host "Examples:"
    Write-Host "  .\install.ps1 list"
    Write-Host "  .\install.ps1 -Target codex list"
    Write-Host "  .\install.ps1 install codex frontend-design"
    Write-Host "  .\install.ps1 -Target codex install-all"
    Write-Host "  .\install.ps1 interactive"
    Write-Host ""
    Write-Host "Environment:"
    Write-Host "  Repository:   $ScriptDir"
    Write-Host "  Claude dir:   $GlobalClaudeDir"
    Write-Host "  Codex dir:    $GlobalCodexDir"
}

# Main Logic
if ([string]::IsNullOrWhiteSpace($Command)) {
    Show-Usage
    exit 0
}

switch ($Command) {
    "list" { List-Skills }
    "installed" { List-Installed }
    "install" { 
        if ($RemainingArgs.Count -eq 0) {
            Write-Error "Please specify skill name(s)"
            exit 1
        }
        foreach ($skill in $RemainingArgs) {
            Install-Skill -SkillName $skill
        }
    }
    "install-all" { Install-All-Skills }
    "interactive" { Install-Interactive }
    "prompt-update" { Update-Global-Prompt }
    "prompt-diff" { Diff-Prompt }
    "help" { Show-Usage }
    "-h" { Show-Usage }
    "--help" { Show-Usage }
    default {
        Write-Error "Unknown command: $Command"
        Show-Usage
        exit 1
    }
}
