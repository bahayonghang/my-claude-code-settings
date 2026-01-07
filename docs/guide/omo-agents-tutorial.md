# OMO Agents Tutorial

A comprehensive guide to using the multi-agent orchestration system inspired by [oh-my-opencode](https://github.com/code-yeongyu/oh-my-opencode).

## What is OMO Agents?

OMO Agents is a multi-agent collaboration system that brings the power of specialized AI agents working together. Instead of a single AI handling everything, different agents focus on what they do best:

- **Sisyphus** orchestrates complex tasks
- **Oracle** provides architectural guidance
- **Explore** searches your codebase
- **Librarian** researches external documentation
- **Frontend Engineer** creates beautiful UIs
- **Document Writer** produces technical documentation
- **Multimodal Looker** analyzes visual content

## Core Philosophy

The oh-my-opencode project demonstrates key principles:

1. **Specialization**: Each agent excels in their domain
2. **Delegation**: Route work to the right expert
3. **Parallelization**: Run independent tasks simultaneously
4. **Context Efficiency**: Keep main agent context lean by delegating exploration

## Installation

Install all OMO Agents skills:

::: code-group
```bash [Linux/macOS]
./install.sh install sisyphus oracle explore librarian frontend-engineer document-writer multimodal-looker omo-agents
```
```powershell [Windows]
.\install.ps1 install sisyphus oracle explore librarian frontend-engineer document-writer multimodal-looker omo-agents
```
:::

Or install everything:

::: code-group
```bash [Linux/macOS]
./install.sh install-all
```
```powershell [Windows]
.\install.ps1 install-all
```
:::

## Quick Start

### Method 1: Let Sisyphus Orchestrate

For complex tasks, just tell Sisyphus what you need:

```
@sisyphus Add a user review system to this e-commerce project
```

Sisyphus will:
1. Analyze the task and create a TODO list
2. Launch @explore to find existing relevant code
3. Consult @oracle for architecture decisions
4. Send @librarian to research best practices
5. Execute implementation with parallel tasks
6. Delegate UI work to @frontend-engineer
7. Have @document-writer update documentation

### Method 2: Direct Agent Calls

For specific needs, call agents directly:

```
@oracle Should I use Redux or Zustand for state management?

@explore Find all authentication-related code in this project

@librarian How does Next.js 14 handle Server Actions?

@frontend-engineer Create a subscription form with smooth animations

@document-writer Write API documentation for the user service

@multimodal-looker Analyze this error screenshot
```

## Agent Reference

### Sisyphus - The Orchestrator

**Best for**: Complex multi-step tasks, feature development, refactoring projects

**Workflow**:
1. **Phase 0**: Classify intent (simple Q&A vs complex task)
2. **Phase 1**: Assess codebase structure and patterns
3. **Phase 2A**: Explore and research (delegates to other agents)
4. **Phase 2B**: Execute with TODO tracking

**Example**:
```
@sisyphus Implement user authentication with JWT tokens
```

### Oracle - The Architect

**Best for**: Design decisions, code review, debugging guidance, tech selection

**Response style**: Direct recommendations with trade-off analysis

**Example**:
```
@oracle Review this authentication flow for security issues

@oracle Should we use microservices or monolith for this scale?
```

### Explore - The Scout

**Best for**: Finding code, tracing dependencies, understanding structure

**Tools used**: grep, glob, LSP, ast-grep, git log/blame

**Example**:
```
@explore Find where payment processing is handled

@explore Trace all usages of the UserService class
```

### Librarian - The Researcher

**Best for**: External documentation, OSS implementations, best practices

**Three modes**:
- TYPE A: Conceptual questions ("What is X?")
- TYPE B: Implementation reference ("How to implement X?")
- TYPE C: Context and history ("Why was X designed this way?")

**Example**:
```
@librarian How do other projects implement rate limiting?

@librarian What's the recommended way to handle form validation in React 19?
```

### Frontend Engineer - The UI Expert

**Best for**: Creating beautiful interfaces, animations, responsive design

**Principles**: Pixel-perfect, motion as soul, intuition-first

**Example**:
```
@frontend-engineer Create a dashboard card component with hover effects

@frontend-engineer Build a modal with smooth enter/exit animations
```

### Document Writer - The Technical Writer

**Best for**: README, API docs, architecture docs, JSDoc comments

**Document types**: README.md, API Reference, Architecture docs, User guides

**Example**:
```
@document-writer Write comprehensive API documentation for the auth module

@document-writer Add JSDoc comments to this service class
```

### Multimodal Looker - The Visual Analyst

**Best for**: Screenshots, PDFs, charts, architecture diagrams, design mockups

**Output**: Structured extraction of relevant information

**Example**:
```
@multimodal-looker What does this error screenshot show?

@multimodal-looker Extract the data from this chart
```

## Best Practices

### 1. Choose the Right Agent

| Need | Agent |
|------|-------|
| Complex feature development | @sisyphus |
| Architecture advice | @oracle |
| Find code in project | @explore |
| Research external docs | @librarian |
| Build UI components | @frontend-engineer |
| Write documentation | @document-writer |
| Analyze images/PDFs | @multimodal-looker |

### 2. Provide Good Context

**Bad**:
```
@explore find that function
```

**Good**:
```
@explore Find the payment processing function, likely in src/services/ or src/api/
```

### 3. Use Sisyphus for Uncertainty

When unsure which agent to use, start with Sisyphus:
```
@sisyphus I need to improve the performance of the user list page
```

Sisyphus will analyze and route to appropriate agents.

### 4. Combine Agents for Complex Tasks

For a feature like "Add user reviews":

1. `@sisyphus Add user review system` (orchestrates everything)

Or manually:
1. `@explore Find existing review or rating code`
2. `@oracle Design the review data model`
3. `@librarian Research review system patterns`
4. `@frontend-engineer Build the review UI`
5. `@document-writer Update API docs`

## Example Workflows

### Feature Development

```
User: @sisyphus Add dark mode support to the application

Sisyphus:
├── @explore → Find existing theme/styling code
├── @oracle → Recommend dark mode implementation approach
├── @librarian → Research CSS custom properties best practices
├── Execute: Create theme context and CSS variables
├── @frontend-engineer → Update components for dark mode
└── @document-writer → Document theme configuration
```

### Bug Investigation

```
User: @sisyphus Users report intermittent login failures

Sisyphus:
├── @explore → Find auth/login code paths
├── @oracle → Analyze potential failure points
├── @librarian → Check for known issues in auth libraries
└── Execute: Implement fix with proper error handling
```

### Code Refactoring

```
User: @sisyphus Refactor the user module to use repository pattern

Sisyphus:
├── @explore → Map all user-related files and dependencies
├── @oracle → Design repository interface
├── @librarian → Research repository pattern implementations
├── Execute: Refactor with TODO tracking
└── @document-writer → Update architecture documentation
```

## Tips and Tricks

1. **Parallel Execution**: Sisyphus runs independent tasks simultaneously—don't worry about ordering

2. **TODO Tracking**: Sisyphus maintains TODO lists for complex tasks—check progress anytime

3. **Context Efficiency**: Agents delegate exploration to keep context lean—trust the process

4. **Challenge Requests**: Sisyphus may question suboptimal approaches—consider the feedback

5. **Direct Calls for Speed**: For simple, specific needs, call agents directly instead of going through Sisyphus

## Troubleshooting

**Agent not responding as expected?**
- Provide more context about your project
- Be specific about what you need
- Try a different agent if the task doesn't match

**Sisyphus creating too many subtasks?**
- Break your request into smaller, focused tasks
- Use direct agent calls for simple needs

**Results not accurate?**
- Verify the agent has access to relevant files
- Provide file paths or code snippets as context
