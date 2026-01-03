#!/usr/bin/env bash

set -euo pipefail

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Paths
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILLS_DIR="${SCRIPT_DIR}/skills"
PROMPTS_DIR="${SCRIPT_DIR}/prompts"
GLOBAL_CLAUDE_DIR="${HOME}/.claude"
GLOBAL_SKILLS_DIR="${GLOBAL_CLAUDE_DIR}/skills"
GLOBAL_CLAUDE_MD="${GLOBAL_CLAUDE_DIR}/CLAUDE.md"
LOCAL_CLAUDE_MD="${PROMPTS_DIR}/CLAUDE.md"

# Codex paths
GLOBAL_CODEX_DIR="${HOME}/.codex"
GLOBAL_CODEX_SKILLS_DIR="${GLOBAL_CODEX_DIR}/skills"

# Target selection (claude or codex)
TARGET="claude"

# Print functions
info() { echo -e "${BLUE}[INFO]${NC} $*"; }
success() { echo -e "${GREEN}[SUCCESS]${NC} $*"; }
warn() { echo -e "${YELLOW}[WARN]${NC} $*"; }
error() { echo -e "${RED}[ERROR]${NC} $*"; }

# Get target skills directory based on TARGET
get_target_skills_dir() {
    if [[ "${TARGET}" == "codex" ]]; then
        echo "${GLOBAL_CODEX_SKILLS_DIR}"
    else
        echo "${GLOBAL_SKILLS_DIR}"
    fi
}

# Get target base directory based on TARGET
get_target_base_dir() {
    if [[ "${TARGET}" == "codex" ]]; then
        echo "${GLOBAL_CODEX_DIR}"
    else
        echo "${GLOBAL_CLAUDE_DIR}"
    fi
}

# Ensure global directory exists
ensure_global_dir() {
    local base_dir=$(get_target_base_dir)
    local skills_dir=$(get_target_skills_dir)

    if [[ ! -d "${base_dir}" ]]; then
        info "Creating ${base_dir}"
        mkdir -p "${base_dir}"
    fi
    if [[ ! -d "${skills_dir}" ]]; then
        info "Creating ${skills_dir}"
        mkdir -p "${skills_dir}"
    fi
}

# List available skills in repository
list_skills() {
    local target_skills_dir=$(get_target_skills_dir)
    echo -e "\n${BLUE}=== Available Skills in Repository (Target: ${TARGET}) ===${NC}"

    if [[ ! -d "${SKILLS_DIR}" ]]; then
        error "Skills directory not found: ${SKILLS_DIR}"
        return 1
    fi

    local count=0
    for skill_path in "${SKILLS_DIR}"/*; do
        if [[ -d "${skill_path}" ]]; then
            local skill_name=$(basename "${skill_path}")
            local skill_md="${skill_path}/SKILL.md"

            count=$((count + 1))
            echo -e "\n${GREEN}[$count] ${skill_name}${NC}"

            if [[ -f "${skill_md}" ]]; then
                # Extract description from SKILL.md
                local desc=$(grep -E "^description:" "${skill_md}" | sed 's/description: *//' | head -1 || true)
                if [[ -n "${desc}" ]]; then
                    echo "    Description: ${desc}"
                fi
            fi

            # Check if already installed
            if [[ -d "${target_skills_dir}/${skill_name}" ]]; then
                echo -e "    Status: ${YELLOW}Already installed${NC}"
            else
                echo -e "    Status: ${RED}Not installed${NC}"
            fi
        fi
    done

    if [[ $count -eq 0 ]]; then
        warn "No skills found in ${SKILLS_DIR}"
    fi
    echo ""
}

# List installed skills
list_installed() {
    local target_skills_dir=$(get_target_skills_dir)
    echo -e "\n${BLUE}=== Installed Skills (Target: ${TARGET}) ===${NC}"

    if [[ ! -d "${target_skills_dir}" ]]; then
        warn "Skills directory does not exist: ${target_skills_dir}"
        return 0
    fi

    local count=0
    for skill_path in "${target_skills_dir}"/*; do
        if [[ -d "${skill_path}" ]]; then
            local skill_name=$(basename "${skill_path}")
            count=$((count + 1))
            echo -e "${GREEN}• ${skill_name}${NC}"

            # Check if from this repo
            if [[ -d "${SKILLS_DIR}/${skill_name}" ]]; then
                echo "  Source: This repository"
            else
                echo "  Source: External"
            fi
        fi
    done

    if [[ $count -eq 0 ]]; then
        warn "No skills installed"
    fi
    echo ""
}

# Install single skill
install_skill() {
    local skill_name=$1
    local skill_src="${SKILLS_DIR}/${skill_name}"
    local target_skills_dir=$(get_target_skills_dir)
    local skill_dst="${target_skills_dir}/${skill_name}"

    if [[ ! -d "${skill_src}" ]]; then
        error "Skill not found: ${skill_name}"
        return 1
    fi

    ensure_global_dir

    if [[ -d "${skill_dst}" ]]; then
        warn "Skill '${skill_name}' already exists. Overwriting..."
        rm -rf "${skill_dst}"
    fi

    info "Installing skill: ${skill_name} (to ${TARGET})"
    cp -r "${skill_src}" "${skill_dst}"
    success "Installed: ${skill_name} → ${skill_dst}"
}

# Install all skills
install_all_skills() {
    echo -e "\n${BLUE}=== Installing All Skills (Target: ${TARGET}) ===${NC}\n"

    if [[ ! -d "${SKILLS_DIR}" ]]; then
        error "Skills directory not found: ${SKILLS_DIR}"
        return 1
    fi

    local count=0
    local failed=0

    for skill_path in "${SKILLS_DIR}"/*; do
        if [[ -d "${skill_path}" ]]; then
            local skill_name=$(basename "${skill_path}")
            if install_skill "${skill_name}"; then
                count=$((count + 1))
            else
                failed=$((failed + 1))
            fi
        fi
    done

    echo ""
    success "Installed ${count} skills to ${TARGET}"
    if [[ $failed -gt 0 ]]; then
        error "Failed to install ${failed} skills"
    fi
}

# Interactive skill selection
install_interactive() {
    list_skills

    echo -e "${BLUE}Select skills to install (space-separated numbers, or 'all'):${NC}"
    read -r selection

    if [[ "${selection}" == "all" ]]; then
        install_all_skills
        return
    fi

    # Build array of available skills
    local skills=()
    for skill_path in "${SKILLS_DIR}"/*; do
        if [[ -d "${skill_path}" ]]; then
            skills+=("$(basename "${skill_path}")")
        fi
    done

    # Parse selection
    local count=0
    for num in ${selection}; do
        if [[ "${num}" =~ ^[0-9]+$ ]] && [[ $num -ge 1 ]] && [[ $num -le ${#skills[@]} ]]; then
            local idx=$((num - 1))
            if install_skill "${skills[$idx]}"; then
                count=$((count + 1))
            fi
        else
            warn "Invalid selection: ${num}"
        fi
    done

    echo ""
    success "Installed ${count} skills to ${TARGET}"
}

# Update global CLAUDE.md
update_global_prompt() {
    if [[ ! -f "${LOCAL_CLAUDE_MD}" ]]; then
        error "Local CLAUDE.md not found: ${LOCAL_CLAUDE_MD}"
        return 1
    fi

    ensure_global_dir

    # Backup existing if present
    if [[ -f "${GLOBAL_CLAUDE_MD}" ]]; then
        local backup="${GLOBAL_CLAUDE_MD}.backup.$(date +%Y%m%d_%H%M%S)"
        info "Backing up existing CLAUDE.md to: ${backup}"
        cp "${GLOBAL_CLAUDE_MD}" "${backup}"
    fi

    info "Copying ${LOCAL_CLAUDE_MD} → ${GLOBAL_CLAUDE_MD}"
    cp "${LOCAL_CLAUDE_MD}" "${GLOBAL_CLAUDE_MD}"
    success "Global CLAUDE.md updated successfully"
}

# Show diff between local and global CLAUDE.md
diff_prompt() {
    if [[ ! -f "${LOCAL_CLAUDE_MD}" ]]; then
        error "Local CLAUDE.md not found: ${LOCAL_CLAUDE_MD}"
        return 1
    fi

    if [[ ! -f "${GLOBAL_CLAUDE_MD}" ]]; then
        warn "Global CLAUDE.md does not exist yet"
        return 0
    fi

    echo -e "\n${BLUE}=== Diff: Local vs Global CLAUDE.md ===${NC}\n"
    diff -u "${GLOBAL_CLAUDE_MD}" "${LOCAL_CLAUDE_MD}" || true
}

# Print usage
usage() {
    cat << EOF
${BLUE}Claude/Codex Skills & Config Manager${NC}

Usage: $0 [COMMAND] [OPTIONS]

Commands:
  list              List all available skills in repository
  installed         List currently installed skills
  install [SKILL]   Install specific skill(s) (space-separated)
  install-all       Install all skills from repository
  interactive       Interactive skill selection and installation
  prompt-update     Update global CLAUDE.md with local version
  prompt-diff       Show diff between local and global CLAUDE.md
  help              Show this help message

Options:
  --target=claude   Install to ~/.claude/skills (default)
  --target=codex    Install to ~/.codex/skills

Examples:
  $0 list                                    # Show available skills (Claude)
  $0 --target=codex list                     # Show available skills (Codex)
  $0 install codex frontend-design           # Install specific skills to Claude
  $0 --target=codex install-all              # Install all skills to Codex
  $0 interactive                             # Interactive mode (Claude)
  $0 --target=codex interactive              # Interactive mode (Codex)
  $0 prompt-update                           # Update global CLAUDE.md

Environment:
  Repository:   ${SCRIPT_DIR}
  Claude dir:   ${GLOBAL_CLAUDE_DIR}
  Codex dir:    ${GLOBAL_CODEX_DIR}
EOF
}

# Main logic
main() {
    # Parse --target option
    while [[ $# -gt 0 ]]; do
        case "$1" in
            --target=claude)
                TARGET="claude"
                shift
                ;;
            --target=codex)
                TARGET="codex"
                shift
                ;;
            --target=*)
                error "Invalid target: ${1#--target=}. Use 'claude' or 'codex'."
                exit 1
                ;;
            *)
                break
                ;;
        esac
    done

    if [[ $# -eq 0 ]]; then
        usage
        exit 0
    fi

    case "$1" in
        list)
            list_skills
            ;;
        installed)
            list_installed
            ;;
        install)
            shift
            if [[ $# -eq 0 ]]; then
                error "Please specify skill name(s)"
                exit 1
            fi
            ensure_global_dir
            for skill in "$@"; do
                install_skill "${skill}"
            done
            ;;
        install-all)
            install_all_skills
            ;;
        interactive)
            install_interactive
            ;;
        prompt-update)
            update_global_prompt
            ;;
        prompt-diff)
            diff_prompt
            ;;
        help|--help|-h)
            usage
            ;;
        *)
            error "Unknown command: $1"
            echo ""
            usage
            exit 1
            ;;
    esac
}

main "$@"
