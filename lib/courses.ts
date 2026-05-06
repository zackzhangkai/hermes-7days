import fs from 'fs'
import path from 'path'
import matter from 'gray-matter'

const contentDirectory = path.join(process.cwd(), 'content')

export interface Course {
  slug: string
  title: string
  description: string
  content: string
}

const courseSlugs = [
  'lesson1-intro',
  'lesson2-provider',
  'lesson3-memory',
  'lesson4-channel',
  'lesson5-skill',
  'lesson6-gateway',
  'lesson7-cron',
  'lesson8-deployment',
]

const courseTitles: Record<string, string> = {
  'lesson1-intro': 'Lesson 1: Hermes Agent 基础与环境搭建',
  'lesson2-provider': 'Lesson 2: Provider 配置与模型选择',
  'lesson3-memory': 'Lesson 3: Memory 持久化与跨会话记忆',
  'lesson4-channel': 'Lesson 4: Channel 消息通道配置',
  'lesson5-skill': 'Lesson 5: Skill 系统与自定义技能',
  'lesson6-gateway': 'Lesson 6: Gateway API 与 HTTP 接口',
  'lesson7-cron': 'Lesson 7: Cron 定时任务与自动化调度',
  'lesson8-deployment': 'Lesson 8: 生产部署与运维',
}

export function getAllCourses(): Course[] {
  return courseSlugs.map((slug) => {
    const fullPath = path.join(contentDirectory, `${slug}.md`)
    const fileContents = fs.readFileSync(fullPath, 'utf8')
    const { content } = matter(fileContents)

    return {
      slug,
      title: courseTitles[slug],
      description: getDescription(content),
      content,
    }
  })
}

export function getCourseBySlug(slug: string): Course | undefined {
  const courses = getAllCourses()
  return courses.find((course) => course.slug === slug)
}

function getDescription(content: string): string {
  const lines = content.split('\n')
  for (const line of lines) {
    if (line.startsWith('## ') && !line.includes('动手实战') && !line.includes('课后作业') && !line.includes('知识卡片') && !line.includes('下节预告') && !line.includes('课程总结')) {
      return line.replace('## ', '').trim()
    }
  }
  return ''
}