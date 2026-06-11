"use client"
import { useState } from "react"
import { useRouter } from "next/navigation"
import { mockUsers, schools } from "../data/mockUsers"

function Signin() {
  const router = useRouter()

  const [selectedSchool, setSelectedSchool] = useState<number | "">("")
  const [email, setEmail]                   = useState("")
  const [password, setPassword]             = useState("")
  const [error, setError]                   = useState("")
  const [loading, setLoading]               = useState(false)

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault()
    setError("")
    setLoading(true)

    setTimeout(() => {
      const user = mockUsers.find(
        (u) =>
          u.email     === email &&
          u.password  === password &&
          u.school_id === Number(selectedSchool)
      )

      if (!user) {
        setError("Invalid school, email, or password.")
      } else if (!user.is_active) {
        setError("Your account is inactive. Contact your administrator.")
      } else {
        sessionStorage.setItem("mockUser", JSON.stringify(user))
        router.push("/dashboard")
      }

      setLoading(false)
    }, 800)
  }

  return (
    <div className="min-h-screen bg-[#0b0b0b] flex font-mono text-white overflow-hidden"
      style={{
        backgroundImage: `
          linear-gradient(rgba(163,230,53,0.04) 1px, transparent 1px),
          linear-gradient(90deg, rgba(163,230,53,0.04) 1px, transparent 1px)`,
        backgroundSize: "48px 48px"
      }}
    >

      {/* ── Left Panel ── */}
      <div className="w-[48%] flex flex-col justify-between gap-12 p-12 border-r border-[#1f1f1f]">

        {/* Logo */}
        <div className="flex items-center gap-3">
          <div className="w-9 h-9 bg-[#a3e635] rounded-md flex items-center justify-center text-black text-xs font-bold tracking-wide">
            KA
          </div>
          <div>
            <p className="text-xs tracking-[0.12em] uppercase text-white font-mono">
              Kognitiv Analytica
            </p>
            <p className="text-[9px] tracking-[0.18em] uppercase text-[#666] mt-0.5 font-mono">
              Data-driven system for advanced learning
            </p>
          </div>
        </div>

        {/* Tag pill */}
        <div className="inline-flex items-center gap-2 border border-[#1f1f1f] rounded-full px-4 py-1.5 text-[11px] text-[#666] tracking-widest w-fit font-mono">
          <span className="w-1.5 h-1.5 rounded-full bg-[#a3e635]"></span>
          Sovereign AI infrastructure for education
        </div>

        {/* Hero */}
        <div>
          <h1 className="text-[34px] font-bold leading-tight tracking-tight font-sans mb-4">
            The AI operating layer<br />
            for academic<br />
            institutions.
          </h1>
          <p className="text-sm text-[#666] leading-relaxed max-w-sm font-sans">
            Secure APIs and hosted infrastructure for universities,
            research institutions, and educational organisations — no
            internal AI infrastructure needed.
          </p>
        </div>

        {/* Stats */}
        <div className="flex gap-8">
          <div className="flex flex-col gap-1">
            <span className="text-[22px] font-bold text-[#a3e635] font-sans">200+</span>
            <span className="text-[11px] text-[#666] tracking-wider font-mono uppercase">Institutions</span>
          </div>
          <div className="flex flex-col gap-1">
            <span className="text-[22px] font-bold text-[#a3e635] font-sans">99.9%</span>
            <span className="text-[11px] text-[#666] tracking-wider font-mono uppercase">Uptime SLA</span>
          </div>
          <div className="flex flex-col gap-1">
            <span className="text-[22px] font-bold text-[#a3e635] font-sans">SOC 2</span>
            <span className="text-[11px] text-[#666] tracking-wider font-mono uppercase">Certified</span>
          </div>
        </div>

      </div>

      {/* ── Right Panel ── */}
      <div className="flex-1 flex items-center justify-center px-16 py-12 overflow-y-auto">
        <div className="w-full max-w-sm">

          <h3 className="text-2xl font-bold font-sans tracking-tight mb-1">
            Welcome back
          </h3>
          <p className="text-sm text-[#666] font-sans mb-7">
            Sign in to your Kognitiv Core account
          </p>

          {/* Test credentials hint */}
          <div className="bg-[#a3e635]/5 border border-[#a3e635]/20 rounded-md px-4 py-3 mb-6">
            <p className="text-[11px] text-[#a3e635] tracking-wider mb-2 font-mono">
              🧪 Test Credentials — password is: password123
            </p>
            {mockUsers.map((u) => (
              <p key={u.id} className="text-[11px] text-[#666] font-mono mb-1 leading-relaxed">
                <span className="text-white">
                  [{schools.find((s) => s.id === u.school_id)?.name}]
                </span>
                {" "}{u.email}{" "}
                <span className="text-[#a3e635]">· {u.role}</span>
                {!u.is_active && (
                  <span className="text-red-500"> · inactive</span>
                )}
              </p>
            ))}
          </div>

          <form onSubmit={handleSubmit} className="flex flex-col gap-4">

            {/* School */}
            <div className="flex flex-col gap-2">
              <label className="text-[11px] uppercase tracking-widest text-[#666] font-mono">
                School
              </label>
              <select
                className="w-full bg-[#111] border border-[#1f1f1f] rounded-md text-white text-sm px-3 py-3 outline-none font-mono focus:border-[#a3e635] transition-colors cursor-pointer appearance-none"
                value={selectedSchool}
                onChange={(e) => setSelectedSchool(Number(e.target.value))}
                required
              >
                <option value="">Select your school…</option>
                {schools.map((s) => (
                  <option key={s.id} value={s.id} className="bg-[#111]">
                    {s.name}
                  </option>
                ))}
              </select>
            </div>

            {/* Email */}
            <div className="flex flex-col gap-2">
              <label className="text-[11px] uppercase tracking-widest text-[#666] font-mono">
                Email Address
              </label>
              <input
                className="w-full bg-[#111] border border-[#1f1f1f] rounded-md text-white text-sm px-3 py-3 outline-none font-mono placeholder:text-[#666] focus:border-[#a3e635] transition-colors"
                type="email"
                placeholder="you@institution.ac.ke"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                required
              />
            </div>

            {/* Password */}
            <div className="flex flex-col gap-2">
              <label className="text-[11px] uppercase tracking-widest text-[#666] font-mono">
                Password
              </label>
              <input
                className="w-full bg-[#111] border border-[#1f1f1f] rounded-md text-white text-sm px-3 py-3 outline-none font-mono placeholder:text-[#666] focus:border-[#a3e635] transition-colors"
                type="password"
                placeholder="••••••••••••"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                required
              />
            </div>

            {/* Error */}
            {error && (
              <p className="text-red-500 text-xs font-mono bg-red-500/10 border border-red-500/25 rounded-md px-3 py-2">
                {error}
              </p>
            )}

            <button
              className="w-full bg-[#a3e635] text-black text-sm font-bold py-3 rounded-md uppercase tracking-widest font-mono hover:opacity-85 active:scale-[0.98] transition-all disabled:opacity-50 disabled:cursor-not-allowed"
              type="submit"
              disabled={loading}
            >
              {loading ? "Signing in…" : "Sign in →"}
            </button>

          </form>

          {/* Divider */}
          <div className="flex items-center gap-3 my-5">
            <span className="flex-1 h-px bg-[#1f1f1f]"></span>
            <span className="text-[11px] text-[#666] font-mono whitespace-nowrap">
              or continue with
            </span>
            <span className="flex-1 h-px bg-[#1f1f1f]"></span>
          </div>

          <button className="w-full bg-transparent border border-[#1f1f1f] rounded-md text-[#ccc] text-xs font-mono py-3 tracking-wider hover:border-[#444] transition-colors">
            Sign in with Google
          </button>

          <p className="text-center mt-6 text-xs text-[#666] font-sans">
            Don&apos;t have an account?{" "}
            <span
              className="text-[#a3e635] cursor-pointer hover:underline"
              onClick={() => router.push("/signup")}
            >
              Create one →
            </span>
          </p>

        </div>
      </div>
    </div>
  )
}

export default Signin