import React from "react";
import {
  AbsoluteFill,
  interpolate,
  spring,
  useCurrentFrame,
  useVideoConfig,
  Sequence,
  Easing,
} from "remotion";
import { AGENTS, Agent } from "./agents";

// ─── Theme ────────────────────────────────────────────────────────────────────

const BG = "#0f0f12";
const CARD = "#16161f";
const BORDER = "#2a2a3a";
const FG = "#e8e8f0";
const MUTED = "#6b6b88";
const PRIMARY = "#6366f1";

// ─── Helpers ──────────────────────────────────────────────────────────────────

function useSpr(frame: number, fps: number, delay = 0, damping = 18) {
  return spring({ frame: frame - delay, fps, config: { damping } });
}

function fadeIn(frame: number, start: number, duration = 20) {
  return interpolate(frame, [start, start + duration], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
}

function getAgentEmoji(id: string): string {
  const map: Record<string, string> = {
    sage: "🌿",
    marco: "🎯",
    maya: "📋",
    viktor: "⚡",
    luna: "✨",
    kai: "🤝",
  };
  return map[id] ?? "🤖";
}

// ─── Scene 1: Title ───────────────────────────────────────────────────────────

const TitleScene: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const logoScale = useSpr(frame, fps, 5, 14);
  const titleOpacity = fadeIn(frame, 15, 25);
  const subtitleOpacity = fadeIn(frame, 35, 25);
  const taglineOpacity = fadeIn(frame, 55, 25);

  const titleY = interpolate(frame, [15, 40], [30, 0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
    easing: Easing.out(Easing.cubic),
  });

  return (
    <AbsoluteFill
      style={{
        background: `radial-gradient(ellipse at 50% 40%, #1a1a2e 0%, ${BG} 70%)`,
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        justifyContent: "center",
      }}
    >
      {/* Glow orb */}
      <div
        style={{
          position: "absolute",
          width: 500,
          height: 500,
          borderRadius: "50%",
          background: `radial-gradient(circle, ${PRIMARY}22 0%, transparent 70%)`,
          top: "50%",
          left: "50%",
          transform: "translate(-50%, -60%)",
          opacity: interpolate(frame, [0, 40], [0, 1], {
            extrapolateLeft: "clamp",
            extrapolateRight: "clamp",
          }),
        }}
      />

      {/* Logo badge */}
      <div
        style={{
          transform: `scale(${logoScale})`,
          marginBottom: 32,
          background: `linear-gradient(135deg, ${PRIMARY}, #8b5cf6)`,
          borderRadius: 20,
          width: 72,
          height: 72,
          display: "flex",
          alignItems: "center",
          justifyContent: "center",
          boxShadow: `0 0 40px ${PRIMARY}66`,
        }}
      >
        <span style={{ fontSize: 36 }}>✦</span>
      </div>

      <div
        style={{
          opacity: titleOpacity,
          transform: `translateY(${titleY}px)`,
          textAlign: "center",
        }}
      >
        <div
          style={{
            fontSize: 72,
            fontWeight: 800,
            fontFamily: "system-ui, -apple-system, sans-serif",
            color: FG,
            letterSpacing: "-2px",
            lineHeight: 1.1,
          }}
        >
          Ikigai Team
        </div>
      </div>

      <div
        style={{
          opacity: subtitleOpacity,
          marginTop: 16,
          fontSize: 28,
          fontWeight: 500,
          fontFamily: "system-ui, -apple-system, sans-serif",
          color: PRIMARY,
          letterSpacing: "0.5px",
        }}
      >
        Your AI Dream Team
      </div>

      <div
        style={{
          opacity: taglineOpacity,
          marginTop: 20,
          fontSize: 18,
          fontFamily: "system-ui, -apple-system, sans-serif",
          color: MUTED,
          maxWidth: 480,
          textAlign: "center",
          lineHeight: 1.6,
        }}
      >
        6 AI agents with GTD, OKRs, Level 10 Life, and S3 governance built in.
      </div>

      {/* Floating agent dots */}
      {AGENTS.map((agent, i) => {
        const angle = (i / AGENTS.length) * Math.PI * 2;
        const radius = 260;
        const x = Math.cos(angle + frame * 0.01) * radius;
        const y = Math.sin(angle + frame * 0.01) * (radius * 0.4);
        const dotOpacity = fadeIn(frame, 20 + i * 8, 20);
        return (
          <div
            key={agent.id}
            style={{
              position: "absolute",
              width: 8,
              height: 8,
              borderRadius: "50%",
              background: agent.color,
              left: "50%",
              top: "50%",
              transform: `translate(calc(-50% + ${x}px), calc(-50% + ${y}px))`,
              opacity: dotOpacity * 0.7,
              boxShadow: `0 0 12px ${agent.color}`,
            }}
          />
        );
      })}
    </AbsoluteFill>
  );
};

// ─── Scene 2: Agent Card ──────────────────────────────────────────────────────

const AgentScene: React.FC<{ agent: Agent; index: number }> = ({
  agent,
  index,
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const cardScale = useSpr(frame, fps, 8, 16);
  const cardOpacity = fadeIn(frame, 8, 20);
  const nameOpacity = fadeIn(frame, 20, 20);
  const roleOpacity = fadeIn(frame, 28, 18);
  const descOpacity = fadeIn(frame, 36, 20);
  const respOpacities = [
    fadeIn(frame, 46, 18),
    fadeIn(frame, 56, 18),
    fadeIn(frame, 66, 18),
  ];
  const terminalOpacity = fadeIn(frame, 80, 25);
  const terminalScale = useSpr(frame, fps, 78, 20);

  const pillColor = agent.color + "33";
  const pillBorder = agent.color + "66";

  return (
    <AbsoluteFill
      style={{
        background: BG,
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
        padding: 60,
      }}
    >
      {/* Top accent bar */}
      <div
        style={{
          position: "absolute",
          top: 0,
          left: 0,
          right: 0,
          height: 4,
          background: `linear-gradient(90deg, transparent, ${agent.color}, transparent)`,
          opacity: cardOpacity,
        }}
      />

      <div
        style={{
          display: "flex",
          gap: 60,
          alignItems: "flex-start",
          width: "100%",
          maxWidth: 1100,
          opacity: cardOpacity,
          transform: `scale(${cardScale})`,
        }}
      >
        {/* Left: Avatar */}
        <div
          style={{
            display: "flex",
            flexDirection: "column",
            alignItems: "center",
            gap: 16,
            minWidth: 220,
          }}
        >
          <div
            style={{
              width: 160,
              height: 160,
              borderRadius: "50%",
              background: `linear-gradient(135deg, ${agent.color}33, ${agent.color}11)`,
              border: `3px solid ${agent.color}`,
              display: "flex",
              alignItems: "center",
              justifyContent: "center",
              boxShadow: `0 0 50px ${agent.color}44`,
              fontSize: 72,
            }}
          >
            {getAgentEmoji(agent.id)}
          </div>

          <div
            style={{
              padding: "6px 16px",
              borderRadius: 20,
              background: pillColor,
              border: `1px solid ${pillBorder}`,
              fontSize: 14,
              fontFamily: "monospace",
              color: agent.color,
              fontWeight: 600,
              letterSpacing: "2px",
              opacity: roleOpacity,
            }}
          >
            {agent.personality}
          </div>

          <div
            style={{
              fontSize: 13,
              color: MUTED,
              fontFamily: "monospace",
              opacity: roleOpacity,
            }}
          >
            Agent {index + 1} of {AGENTS.length}
          </div>
        </div>

        {/* Right: Content */}
        <div style={{ flex: 1 }}>
          <div
            style={{
              fontSize: 64,
              fontWeight: 800,
              fontFamily: "system-ui, -apple-system, sans-serif",
              color: FG,
              letterSpacing: "-1px",
              lineHeight: 1,
              opacity: nameOpacity,
            }}
          >
            {agent.name}
          </div>

          <div
            style={{
              fontSize: 22,
              fontWeight: 500,
              color: agent.color,
              marginTop: 8,
              opacity: roleOpacity,
              fontFamily: "system-ui, -apple-system, sans-serif",
            }}
          >
            {agent.role}
          </div>

          <div
            style={{
              fontSize: 17,
              color: MUTED,
              marginTop: 20,
              lineHeight: 1.65,
              opacity: descOpacity,
              fontFamily: "system-ui, -apple-system, sans-serif",
              maxWidth: 580,
            }}
          >
            {agent.description}
          </div>

          <div style={{ marginTop: 24, display: "flex", flexDirection: "column", gap: 10 }}>
            {agent.responsibilities.map((resp, i) => (
              <div
                key={i}
                style={{
                  display: "flex",
                  alignItems: "center",
                  gap: 12,
                  opacity: respOpacities[i] ?? 0,
                }}
              >
                <div
                  style={{
                    width: 20,
                    height: 20,
                    borderRadius: "50%",
                    background: agent.color,
                    display: "flex",
                    alignItems: "center",
                    justifyContent: "center",
                    flexShrink: 0,
                    fontSize: 11,
                    color: "#fff",
                    fontWeight: 700,
                  }}
                >
                  ✓
                </div>
                <div
                  style={{
                    fontSize: 16,
                    color: FG,
                    fontFamily: "system-ui, -apple-system, sans-serif",
                  }}
                >
                  {resp}
                </div>
              </div>
            ))}
          </div>

          <div
            style={{
              marginTop: 32,
              background: CARD,
              border: `1px solid ${BORDER}`,
              borderRadius: 12,
              padding: "14px 18px",
              fontFamily: "monospace",
              fontSize: 14,
              opacity: terminalOpacity,
              transform: `scale(${terminalScale})`,
              transformOrigin: "left center",
            }}
          >
            <span style={{ color: agent.color, fontWeight: 700 }}>
              {agent.name}:
            </span>
            <span style={{ color: FG, marginLeft: 10 }}>
              {agent.terminalMessage}
            </span>
          </div>
        </div>
      </div>
    </AbsoluteFill>
  );
};

// ─── Scene 3: Team Overview ───────────────────────────────────────────────────

const AgentMiniCard: React.FC<{ agent: Agent; delay: number }> = ({
  agent,
  delay,
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const cardSpr = useSpr(frame, fps, delay, 18);
  const cardOp = fadeIn(frame, delay, 20);

  return (
    <div
      style={{
        background: CARD,
        border: `1px solid ${BORDER}`,
        borderTop: `3px solid ${agent.color}`,
        borderRadius: 14,
        padding: "20px 22px",
        opacity: cardOp,
        transform: `scale(${cardSpr}) translateY(${interpolate(cardSpr, [0, 1], [20, 0])}px)`,
      }}
    >
      <div style={{ display: "flex", alignItems: "center", gap: 12, marginBottom: 10 }}>
        <div
          style={{
            width: 44,
            height: 44,
            borderRadius: "50%",
            background: agent.color + "22",
            border: `2px solid ${agent.color}66`,
            display: "flex",
            alignItems: "center",
            justifyContent: "center",
            fontSize: 22,
          }}
        >
          {getAgentEmoji(agent.id)}
        </div>
        <div>
          <div style={{ fontSize: 17, fontWeight: 700, color: FG, fontFamily: "system-ui, -apple-system, sans-serif" }}>
            {agent.name}
          </div>
          <div style={{ fontSize: 13, color: agent.color, fontFamily: "system-ui, -apple-system, sans-serif" }}>
            {agent.role}
          </div>
        </div>
      </div>
      <div style={{ fontSize: 13, color: MUTED, lineHeight: 1.5, fontFamily: "system-ui, -apple-system, sans-serif" }}>
        {agent.responsibilities[0]}
      </div>
    </div>
  );
};

const TeamScene: React.FC = () => {
  const frame = useCurrentFrame();

  const titleOpacity = fadeIn(frame, 5, 25);
  const titleY = interpolate(frame, [5, 30], [20, 0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
    easing: Easing.out(Easing.cubic),
  });

  return (
    <AbsoluteFill
      style={{
        background: BG,
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        justifyContent: "center",
        padding: 50,
      }}
    >
      <div
        style={{
          opacity: titleOpacity,
          transform: `translateY(${titleY}px)`,
          marginBottom: 40,
          textAlign: "center",
        }}
      >
        <div
          style={{
            fontSize: 42,
            fontWeight: 800,
            fontFamily: "system-ui, -apple-system, sans-serif",
            color: FG,
            letterSpacing: "-1px",
          }}
        >
          The Full Team
        </div>
        <div style={{ fontSize: 18, color: MUTED, marginTop: 8, fontFamily: "system-ui, -apple-system, sans-serif" }}>
          Every role covered. Zero micromanagement.
        </div>
      </div>

      <div
        style={{
          display: "grid",
          gridTemplateColumns: "repeat(3, 1fr)",
          gap: 20,
          width: "100%",
          maxWidth: 1000,
        }}
      >
        {AGENTS.map((agent, i) => (
          <AgentMiniCard key={agent.id} agent={agent} delay={15 + i * 8} />
        ))}
      </div>
    </AbsoluteFill>
  );
};

// ─── Scene 4: Terminal Collaboration ─────────────────────────────────────────

const TerminalScene: React.FC = () => {
  const frame = useCurrentFrame();

  const titleOpacity = fadeIn(frame, 5, 25);
  const windowOpacity = fadeIn(frame, 15, 20);

  const lines = [
    { agent: "Maya", color: "#6366f1", text: "Good morning. Starting daily review..." },
    { agent: "Sage", color: "#a855f7", text: "Energy check: you're at 8/10. Strong day ahead." },
    { agent: "Marco", color: "#f59e0b", text: "Q2 OKR check: Product launch on track for April 15." },
    { agent: "Viktor", color: "#10b981", text: "Deployed v2.3.0 to production. All tests passing." },
    { agent: "Luna", color: "#ec4899", text: "Your blog post got 1.2k views. Scheduling follow-up." },
    { agent: "Kai", color: "#f97316", text: "3 partnership leads to follow up. Coffee with Anna tomorrow." },
    { agent: "Maya", color: "#6366f1", text: "Daily briefing complete. You can focus now. ✓" },
  ];

  return (
    <AbsoluteFill
      style={{
        background: BG,
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        justifyContent: "center",
        padding: 60,
      }}
    >
      <div
        style={{
          opacity: titleOpacity,
          marginBottom: 32,
          textAlign: "center",
        }}
      >
        <div
          style={{
            fontSize: 38,
            fontWeight: 800,
            color: FG,
            fontFamily: "system-ui, -apple-system, sans-serif",
            letterSpacing: "-0.5px",
          }}
        >
          Your Morning Briefing
        </div>
        <div style={{ fontSize: 16, color: MUTED, marginTop: 8, fontFamily: "system-ui, -apple-system, sans-serif" }}>
          All agents working in sync, before you even open your laptop
        </div>
      </div>

      <div
        style={{
          opacity: windowOpacity,
          width: "100%",
          maxWidth: 820,
          background: CARD,
          border: `1px solid ${BORDER}`,
          borderRadius: 16,
          overflow: "hidden",
          boxShadow: "0 25px 60px rgba(0,0,0,0.5)",
        }}
      >
        {/* Title bar */}
        <div
          style={{
            display: "flex",
            alignItems: "center",
            gap: 8,
            padding: "12px 18px",
            borderBottom: `1px solid ${BORDER}`,
            background: "#1a1a27",
          }}
        >
          <div style={{ width: 12, height: 12, borderRadius: "50%", background: "#ff5f57" }} />
          <div style={{ width: 12, height: 12, borderRadius: "50%", background: "#febc2e" }} />
          <div style={{ width: 12, height: 12, borderRadius: "50%", background: "#28c840" }} />
          <span style={{ marginLeft: 12, fontSize: 13, color: MUTED, fontFamily: "monospace" }}>
            ikigai-team — daily-review
          </span>
        </div>

        {/* Lines */}
        <div style={{ padding: "20px 24px", display: "flex", flexDirection: "column", gap: 12 }}>
          {lines.map((line, i) => (
            <div
              key={i}
              style={{
                display: "flex",
                gap: 12,
                opacity: fadeIn(frame, 25 + i * 15, 15),
                fontFamily: "monospace",
                fontSize: 15,
                lineHeight: 1.5,
              }}
            >
              <span style={{ color: line.color, fontWeight: 700, minWidth: 60 }}>
                {line.agent}
              </span>
              <span style={{ color: FG + "cc" }}>{line.text}</span>
            </div>
          ))}

          {/* Blinking cursor */}
          <div
            style={{
              opacity: fadeIn(frame, 25 + lines.length * 15, 10) * (Math.floor(frame / 15) % 2 === 0 ? 1 : 0),
              color: PRIMARY,
              fontFamily: "monospace",
              fontSize: 16,
            }}
          >
            ▊
          </div>
        </div>
      </div>
    </AbsoluteFill>
  );
};

// ─── Scene 5: CTA ─────────────────────────────────────────────────────────────

const CTAScene: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const logoScale = useSpr(frame, fps, 5, 14);
  const titleOpacity = fadeIn(frame, 20, 25);
  const subtitleOpacity = fadeIn(frame, 38, 22);
  const urlOpacity = fadeIn(frame, 55, 22);
  const tagsOpacity = fadeIn(frame, 72, 22);

  return (
    <AbsoluteFill
      style={{
        background: `radial-gradient(ellipse at 50% 50%, #1a1a30 0%, ${BG} 65%)`,
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        justifyContent: "center",
      }}
    >
      <div
        style={{
          position: "absolute",
          width: 600,
          height: 600,
          borderRadius: "50%",
          background: `radial-gradient(circle, ${PRIMARY}18 0%, transparent 70%)`,
          top: "50%",
          left: "50%",
          transform: "translate(-50%, -50%)",
        }}
      />

      <div
        style={{
          transform: `scale(${logoScale})`,
          marginBottom: 28,
          background: `linear-gradient(135deg, ${PRIMARY}, #8b5cf6)`,
          borderRadius: 20,
          width: 72,
          height: 72,
          display: "flex",
          alignItems: "center",
          justifyContent: "center",
          boxShadow: `0 0 50px ${PRIMARY}66`,
        }}
      >
        <span style={{ fontSize: 36 }}>✦</span>
      </div>

      <div
        style={{
          opacity: titleOpacity,
          textAlign: "center",
          fontSize: 58,
          fontWeight: 800,
          fontFamily: "system-ui, -apple-system, sans-serif",
          color: FG,
          letterSpacing: "-1.5px",
          lineHeight: 1.1,
        }}
      >
        Start with a coaching
        <br />
        session, not a config file.
      </div>

      <div
        style={{
          opacity: subtitleOpacity,
          marginTop: 20,
          fontSize: 20,
          color: MUTED,
          fontFamily: "system-ui, -apple-system, sans-serif",
          textAlign: "center",
          maxWidth: 520,
          lineHeight: 1.6,
        }}
      >
        Discover your purpose, set your strategy, build your rhythm — then let
        the team handle the rest.
      </div>

      <div
        style={{
          opacity: urlOpacity,
          marginTop: 36,
          background: CARD,
          border: `1px solid ${PRIMARY}66`,
          borderRadius: 12,
          padding: "14px 28px",
          fontFamily: "monospace",
          fontSize: 18,
          color: PRIMARY,
          letterSpacing: "0.5px",
          boxShadow: `0 0 20px ${PRIMARY}33`,
        }}
      >
        github.com/razbakov/ikigai-team
      </div>

      <div
        style={{
          opacity: tagsOpacity,
          marginTop: 28,
          display: "flex",
          gap: 12,
          flexWrap: "wrap",
          justifyContent: "center",
        }}
      >
        {["GTD", "OKRs", "Level 10 Life", "S3 Governance", "6 AI Agents"].map(
          (tag) => (
            <div
              key={tag}
              style={{
                padding: "6px 14px",
                borderRadius: 20,
                background: PRIMARY + "18",
                border: `1px solid ${PRIMARY}44`,
                fontSize: 13,
                color: PRIMARY,
                fontFamily: "system-ui, -apple-system, sans-serif",
                fontWeight: 500,
              }}
            >
              {tag}
            </div>
          )
        )}
      </div>
    </AbsoluteFill>
  );
};

// ─── Composition timing ───────────────────────────────────────────────────────

const TITLE_DURATION = 100;
const AGENT_DURATION = 120;
const TEAM_DURATION = 110;
const TERMINAL_DURATION = 160;
const CTA_DURATION = 130;

export const totalDuration =
  TITLE_DURATION +
  AGENTS.length * AGENT_DURATION +
  TEAM_DURATION +
  TERMINAL_DURATION +
  CTA_DURATION;

// ─── Main Composition ─────────────────────────────────────────────────────────

export const IkigaiVideo: React.FC = () => {
  const agentStart = TITLE_DURATION;

  return (
    <>
      <Sequence from={0} durationInFrames={TITLE_DURATION}>
        <TitleScene />
      </Sequence>

      {AGENTS.map((agent, i) => (
        <Sequence
          key={agent.id}
          from={agentStart + i * AGENT_DURATION}
          durationInFrames={AGENT_DURATION}
        >
          <AgentScene agent={agent} index={i} />
        </Sequence>
      ))}

      <Sequence
        from={agentStart + AGENTS.length * AGENT_DURATION}
        durationInFrames={TEAM_DURATION}
      >
        <TeamScene />
      </Sequence>

      <Sequence
        from={agentStart + AGENTS.length * AGENT_DURATION + TEAM_DURATION}
        durationInFrames={TERMINAL_DURATION}
      >
        <TerminalScene />
      </Sequence>

      <Sequence
        from={agentStart + AGENTS.length * AGENT_DURATION + TEAM_DURATION + TERMINAL_DURATION}
        durationInFrames={CTA_DURATION}
      >
        <CTAScene />
      </Sequence>
    </>
  );
};
