export interface Agent {
  id: string;
  name: string;
  role: string;
  color: string;
  personality: string;
  description: string;
  responsibilities: string[];
  terminalMessage: string;
}

export const AGENTS: Agent[] = [
  {
    id: "sage",
    name: "Sage",
    role: "Personal Coach",
    color: "#a855f7",
    personality: "INFJ",
    description:
      "Sage watches out for you as a human. She tracks your energy, flags burnout risk, and helps you reconnect with purpose.",
    responsibilities: [
      "Energy & burnout monitoring",
      "Purpose & motivation alignment",
      "Level 10 Life assessment",
    ],
    terminalMessage:
      "Good morning. Your energy score is 7/10. Today's intention: focus on one key goal.",
  },
  {
    id: "marco",
    name: "Marco",
    role: "Head of Strategy",
    color: "#f59e0b",
    personality: "ENTJ",
    description:
      "Marco ensures you're building the right things. He defines OKRs, evaluates business models, and keeps your portfolio focused.",
    responsibilities: [
      "OKR setting & quarterly planning",
      "Business model validation",
      "Competitive analysis",
    ],
    terminalMessage: "Q2 OKR progress: 67%. Revenue target needs attention.",
  },
  {
    id: "maya",
    name: "Maya",
    role: "Chief of Staff",
    color: "#6366f1",
    personality: "ISTJ",
    description:
      "Maya keeps everything running. She owns your daily rhythm, manages your inbox, and ensures nothing falls through the cracks.",
    responsibilities: [
      "Daily standup & check-ins",
      "Inbox processing & GTD workflow",
      "Cross-agent task delegation",
    ],
    terminalMessage:
      "3 items in inbox, 2 meetings today. Top priority: product launch.",
  },
  {
    id: "viktor",
    name: "Viktor",
    role: "CTO",
    color: "#10b981",
    personality: "INTJ",
    description:
      "Viktor handles the technical side. He architects solutions, writes code, manages deployments, and keeps your codebase clean.",
    responsibilities: [
      "Architecture & code reviews",
      "CI/CD & deployment management",
      "Technical debt tracking",
    ],
    terminalMessage: "PR #47 passed all checks. Deploying to staging now.",
  },
  {
    id: "luna",
    name: "Luna",
    role: "Head of Content & Growth",
    color: "#ec4899",
    personality: "ENFP",
    description:
      "Luna turns your ideas into content that reaches people. She writes posts, manages social, and builds your public presence.",
    responsibilities: [
      "Blog posts & social media",
      "SEO optimization",
      "Brand voice & messaging",
    ],
    terminalMessage: "Blog post draft ready for review. SEO score: 92/100.",
  },
  {
    id: "kai",
    name: "Kai",
    role: "Community & Partnerships",
    color: "#f97316",
    personality: "ESFJ",
    description:
      "Kai builds your network and nurtures your community. He manages contacts, follows up after events, and opens doors to partnerships.",
    responsibilities: [
      "Contact management & follow-ups",
      "Community engagement",
      "Partnership outreach",
    ],
    terminalMessage:
      "3 new connection requests. Scheduled follow-up with 2 partners.",
  },
];
