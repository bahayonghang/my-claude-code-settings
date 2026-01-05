import { defineConfig } from 'vitepress'

export default defineConfig({
  title: 'MyClaude Skills',
  description: 'Claude Code 技能和提示词集合',
  
  locales: {
    root: {
      label: 'English',
      lang: 'en',
      themeConfig: {
        nav: [
          { text: 'Guide', link: '/guide/' },
          { text: 'Skills', link: '/skills/' },
          { text: 'GitHub', link: 'https://github.com/anthropics/my-claude-skills' }
        ],
        sidebar: {
          '/guide/': [
            {
              text: 'Getting Started',
              items: [
                { text: 'Introduction', link: '/guide/' },
                { text: 'Installation', link: '/guide/installation' },
                { text: 'Commands', link: '/guide/commands' }
              ]
            },
            {
              text: 'Advanced',
              items: [
                { text: 'Creating Skills', link: '/guide/creating-skills' },
                { text: 'Prompts', link: '/guide/prompts' }
              ]
            }
          ],
          '/skills/': [
            {
              text: 'Skills',
              items: [
                { text: 'Overview', link: '/skills/' },
                { text: 'article-cover', link: '/skills/article-cover' },
                { text: 'codex', link: '/skills/codex' },
                { text: 'excalidraw', link: '/skills/excalidraw' },
                { text: 'frontend-design', link: '/skills/frontend-design' },
                { text: 'gemini-image', link: '/skills/gemini-image' },
                { text: 'research', link: '/skills/research' },
                { text: 'spec-interview', link: '/skills/spec-interview' },
                { text: 'tech-blog', link: '/skills/tech-blog' },
                { text: 'tech-design-doc', link: '/skills/tech-design-doc' }
              ]
            }
          ]
        }
      }
    },
    zh: {
      label: '中文',
      lang: 'zh-CN',
      link: '/zh/',
      themeConfig: {
        nav: [
          { text: '指南', link: '/zh/guide/' },
          { text: '技能', link: '/zh/skills/' },
          { text: 'GitHub', link: 'https://github.com/anthropics/my-claude-skills' }
        ],
        sidebar: {
          '/zh/guide/': [
            {
              text: '快速开始',
              items: [
                { text: '简介', link: '/zh/guide/' },
                { text: '安装', link: '/zh/guide/installation' },
                { text: '命令', link: '/zh/guide/commands' }
              ]
            },
            {
              text: '进阶',
              items: [
                { text: '创建技能', link: '/zh/guide/creating-skills' },
                { text: '提示词', link: '/zh/guide/prompts' }
              ]
            }
          ],
          '/zh/skills/': [
            {
              text: '技能列表',
              items: [
                { text: '概览', link: '/zh/skills/' },
                { text: 'article-cover', link: '/zh/skills/article-cover' },
                { text: 'codex', link: '/zh/skills/codex' },
                { text: 'excalidraw', link: '/zh/skills/excalidraw' },
                { text: 'frontend-design', link: '/zh/skills/frontend-design' },
                { text: 'gemini-image', link: '/zh/skills/gemini-image' },
                { text: 'research', link: '/zh/skills/research' },
                { text: 'spec-interview', link: '/zh/skills/spec-interview' },
                { text: 'tech-blog', link: '/zh/skills/tech-blog' },
                { text: 'tech-design-doc', link: '/zh/skills/tech-design-doc' }
              ]
            }
          ]
        }
      }
    }
  },

  themeConfig: {
    logo: '/logo.svg',
    socialLinks: [
      { icon: 'github', link: 'https://github.com/anthropics/my-claude-skills' }
    ],
    footer: {
      message: 'Released under the MIT License.',
      copyright: 'Copyright © 2024-present'
    },
    search: {
      provider: 'local'
    }
  }
})
