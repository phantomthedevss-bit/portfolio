import os, json
from datetime import datetime
from flask import Flask, request, jsonify, render_template_string, send_from_directory
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

CONTACT_EMAIL = "phantomthedev@proton.me"
MESSAGES_FILE = "messages.json"

if not os.path.exists(MESSAGES_FILE):
    with open(MESSAGES_FILE, "w") as f:
        json.dump([], f)

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>phantomthedev - Backend Engineer & Cybersecurity Specialist</title>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<style>
:root{
  --bg:#07080a; --card:#111317; --card2:#15181d; --border:#1e232b; --text:#e8e9ed; --muted:#9aa0ac; --accent:#00ff88; --accent2:#00e5ff; --accent-dark:#059669;
}
[data-theme="light"]{ --bg:#fafafb; --card:#ffffff; --card2:#ffffff; --border:#e5e7eb; --text:#111827; --muted:#6b7280; --accent:#059669; --accent2:#0891b2; }
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:'Inter',sans-serif;background:var(--bg);color:var(--text);line-height:1.6;transition:background .3s,color .3s;overflow-x:hidden}
h1,h2,h3{font-family:'Space Grotesk',sans-serif}
.mono{font-family:'JetBrains Mono',monospace}
.glass{background:var(--card);border:1px solid var(--border);backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px)}
.low-end .glass{backdrop-filter:none!important;-webkit-backdrop-filter:none!important;background:var(--card)!important}
.low-end *{animation:none!important;transition:none!important}
.container{max-width:1100px;margin:0 auto;padding:0 24px}
nav{position:sticky;top:0;z-index:100;background:rgba(7,8,10,.8);backdrop-filter:blur(20px);border-bottom:1px solid var(--border)}
[data-theme="light"] nav{background:rgba(250,250,251,.8)}
.low-end nav{backdrop-filter:none;background:var(--bg)}
.nav-inner{display:flex;align-items:center;justify-content:space-between;height:68px}
.logo{display:flex;align-items:center;gap:12px;font-weight:700;font-size:20px}
.logo-img{width:36px;height:36px;border-radius:50%;object-fit:cover;border:2px solid var(--accent)}
.dot{width:8px;height:8px;background:var(--accent);border-radius:50%;box-shadow:0 0 10px var(--accent);animation:pulse 2s infinite}
@keyframes pulse{0%,100%{opacity:1}50%{opacity:.5}}
.nav-links{display:flex;gap:24px;align-items:center}
.nav-links a{color:var(--muted);text-decoration:none;font-size:14px;font-weight:500;transition:.2s}
.nav-links a:hover{color:var(--text)}
.btn{padding:10px 20px;border-radius:10px;font-weight:600;font-size:14px;cursor:pointer;border:none;transition:.2s;text-decoration:none;display:inline-flex;align-items:center;gap:8px}
.btn-primary{background:var(--accent);color:#000}
.btn-primary:hover{transform:translateY(-1px);box-shadow:0 4px 20px rgba(0,255,136,.3)}
.btn-ghost{background:var(--card);border:1px solid var(--border);color:var(--text)}
.icon-btn{width:40px;height:40px;border-radius:10px;display:grid;place-items:center;background:var(--card);border:1px solid var(--border);cursor:pointer;font-size:18px}
.hero{padding:80px 0 60px;display:grid;grid-template-columns:1.1fr .9fr;gap:60px;align-items:center}
.hero h1{font-size:56px;line-height:.95;letter-spacing:-.03em;margin-bottom:16px}
.hero h1 span{background:linear-gradient(90deg,var(--accent),var(--accent2));-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.hero p{color:var(--muted);font-size:18px;margin-bottom:28px;max-width:520px}
.stats{display:flex;gap:24px;margin:24px 0}
.stat strong{font-size:24px;display:block}
.stat span{font-size:13px;color:var(--muted)}
.hero-img{position:relative}
.hero-img img{width:100%;max-width:380px;aspect-ratio:1;border-radius:24px;object-fit:cover;border:1px solid var(--border);box-shadow:0 20px 60px rgba(0,0,0,.3)}
.badge{position:absolute;bottom:-16px;left:20px;background:var(--card);border:1px solid var(--border);padding:10px 16px;border-radius:12px;display:flex;align-items:center;gap:10px;font-size:13px;box-shadow:0 8px 24px rgba(0,0,0,.2)}
.grid{display:grid;gap:20px}
.grid-2{grid-template-columns:repeat(2,1fr)}
.grid-3{grid-template-columns:repeat(3,1fr)}
.card{padding:24px;border-radius:16px}
.card h3{margin-bottom:8px}
.muted{color:var(--muted)}
.tag{display:inline-block;padding:4px 10px;border-radius:20px;background:var(--card2);border:1px solid var(--border);font-size:12px;margin:4px 4px 0 0}
.section{padding:60px 0}
.section h2{font-size:32px;margin-bottom:32px;letter-spacing:-.02em}
.form{display:grid;gap:16px}
.form input,.form select,.form textarea{width:100%;padding:12px 14px;border-radius:10px;background:var(--card);border:1px solid var(--border);color:var(--text);font-family:Inter;font-size:14px}
.form textarea{min-height:120px;resize:vertical}
.toast{position:fixed;bottom:24px;right:24px;background:var(--card);border:1px solid var(--border);padding:12px 18px;border-radius:12px;box-shadow:0 8px 24px rgba(0,0,0,.3);transform:translateY(100px);opacity:0;transition:.3s;z-index:999}
.toast.show{transform:translateY(0);opacity:1}
@media(max-width:900px){.hero{grid-template-columns:1fr}.grid-2,.grid-3{grid-template-columns:1fr}.nav-links{gap:12px}.hero h1{font-size:40px}}
</style>
</head>
<body data-theme="dark">
<nav>
<div class="container nav-inner">
<div class="logo"><img src="/static/images/formal.webp" class="logo-img" onerror="this.src='/static/images/original.jpg'"><span>phantomthedev</span><div class="dot"></div></div>
<div class="nav-links">
<a href="#projects">Projects</a>
<a href="#contact">Contact</a>
<button class="icon-btn" id="perfBtn" title="Performance mode for low-end devices">🐢</button>
<button class="icon-btn" id="themeBtn" title="Toggle light/dark">🌙</button>
<a class="btn btn-primary" href="mailto:phantomthedev@proton.me?subject=Hiring%20Inquiry">Hire Me</a>
</div>
</div>
</nav>

<div class="container">
<div class="hero">
<div>
<h1>Backend Engineer & <span>Cybersecurity Specialist</span></h1>
<p>I am <strong>Oreoluwa Olawale (phantomthedev)</strong>, based in Abuja, Nigeria. I build resilient Python applications, secure API infrastructure, and automated keep-alive systems for cloud platforms with Flask, Gunicorn and ethical hacking.</p>
<div class="stats">
<div class="stat"><strong>10+</strong><span>Tools Built</span></div>
<div class="stat"><strong>99.9%</strong><span>Uptime</span></div>
<div class="stat"><strong>Abuja</strong><span>Based</span></div>
</div>
<div style="display:flex;gap:12px;margin-top:12px">
<a class="btn btn-primary" href="#contact">Hire Me — phantomthedev@proton.me</a>
<a class="btn btn-ghost" href="https://github.com/phantomthedevss-bit" target="_blank">GitHub</a>
</div>
<div style="margin-top:20px" class="mono muted" style="font-size:13px">📧 phantomthedev@proton.me • 📞 +2349160352202 • 📍 Abuja</div>
</div>
<div class="hero-img">
<img id="heroImg" src="/static/images/formal.webp" onerror="this.src='/static/images/original.jpg'" alt="phantomthedev">
<div class="badge"><div class="dot"></div> Available for new projects • Response < 2h</div>
</div>
</div>

<div class="section" id="projects">
<h2>Projects — Live on Render Oregon</h2>
<div class="grid grid-2" id="projectsGrid">
<!-- Filled by JS from /api/projects backend -->
</div>
</div>

<div class="section">
<h2>Skills — Backend + Cybersecurity</h2>
<div class="grid grid-3">
<div class="card glass"><h3>Python & Flask 95%</h3><p class="muted">Backend APIs, Gunicorn, Threading, RPS control</p></div>
<div class="card glass"><h3>Cybersecurity 90%</h3><p class="muted">Pentesting, Nmap, Vuln scanning, Secure coding</p></div>
<div class="card glass"><h3>Render & DevOps 85%</h3><p class="muted">Deployment, Oregon region, Fix TemplateNotFound</p></div>
<div class="card glass"><h3>Ethical Hacking 85%</h3><p class="muted">Network security, Linux, Access control</p></div>
<div class="card glass"><h3>APIs 90%</h3><p class="muted">REST, High throughput, TikTok downloader</p></div>
<div class="card glass"><h3>Linux 80%</h3><p class="muted">Server management, Security hardening</p></div>
</div>
</div>

<div class="section" id="contact">
<h2>Hire Me — Backend & Security</h2>
<div class="grid grid-2">
<div class="card glass">
<h3>Contact Information</h3>
<p class="muted" style="margin:16px 0">Professional and formal — I reply within 2 hours.</p>
<div style="display:grid;gap:12px">
<a class="btn btn-ghost" href="mailto:phantomthedev@proton.me?subject=Hiring%20Inquiry">📧 phantomthedev@proton.me</a>
<a class="btn btn-ghost" href="tel:+2349160352202">📞 +2349160352202</a>
<a class="btn btn-ghost" href="https://github.com/phantomthedevss-bit" target="_blank">💻 github.com/phantomthedevss-bit</a>
<div class="btn btn-ghost">📍 Abuja, Nigeria • Remote Worldwide</div>
</div>
<div style="margin-top:20px;padding:16px;background:var(--card2);border-radius:12px;border:1px solid var(--border)">
<div class="mono" style="font-size:13px">Backend API: <span style="color:var(--accent)">/api/contact (POST)</span> — messages saved to server, mailto fallback</div>
</div>
</div>
<div class="card glass">
<h3>Send Message — Backend Powered</h3>
<form class="form" id="contactForm">
<input name="name" placeholder="Your name" required>
<input name="email" type="email" placeholder="your@email.com" required>
<select name="project"><option>Backend Development</option><option>Cybersecurity Audit</option><option>Render Deployment Fix</option><option>Bot Hosting</option><option>Other</option></select>
<select name="budget"><option>Budget: $50-$200</option><option>$200-$500</option><option>$500-$1000</option><option>$1000+</option></select>
<textarea name="message" placeholder="Tell me about your project..." required></textarea>
<button type="submit" class="btn btn-primary" style="width:100%;justify-content:center">Send via Backend API →</button>
<div class="muted" style="font-size:12px;text-align:center">Sends to server (/api/contact) + opens Proton Mail as fallback</div>
</form>
</div>
</div>
</div>
</div>

<div class="toast" id="toast"></div>

<script>
// Theme
const themeBtn = document.getElementById('themeBtn');
let theme = localStorage.getItem('theme') || 'dark';
document.body.setAttribute('data-theme', theme);
themeBtn.textContent = theme === 'dark' ? '🌙' : '☀️';
themeBtn.onclick = () => {
  theme = theme === 'dark' ? 'light' : 'dark';
  document.body.setAttribute('data-theme', theme);
  localStorage.setItem('theme', theme);
  themeBtn.textContent = theme === 'dark' ? '🌙' : '☀️';
};

// Performance / Low-end switch
const perfBtn = document.getElementById('perfBtn');
let perf = localStorage.getItem('perf') === 'on';
if(perf) document.body.classList.add('low-end');
perfBtn.textContent = perf ? '⚡' : '🐢';
perfBtn.title = perf ? 'Performance ON - minimal effects' : 'Performance OFF - enable if lagging';
perfBtn.onclick = () => {
  perf = !perf;
  document.body.classList.toggle('low-end', perf);
  localStorage.setItem('perf', perf ? 'on' : 'off');
  perfBtn.textContent = perf ? '⚡' : '🐢';
  toast(perf ? 'Performance mode ON - animations disabled' : 'Performance mode OFF - full effects');
};

// Auto-detect low-end
if(navigator.hardwareConcurrency && navigator.hardwareConcurrency <= 4 && !localStorage.getItem('perf')){
  setTimeout(()=>toast('Low-end device detected — tap 🐢 for performance mode if lagging'), 2000);
}

function toast(msg){
  const t = document.getElementById('toast');
  t.textContent = msg;
  t.classList.add('show');
  setTimeout(()=>t.classList.remove('show'), 3000);
}

// Load projects from backend API
fetch('/api/projects').then(r=>r.json()).then(projects=>{
  const grid = document.getElementById('projectsGrid');
  grid.innerHTML = projects.map(p=>`
    <div class="card glass">
      <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px">
        <h3>${p.name}</h3><span class="tag" style="background:${p.status==='live'?'#00ff88':'#f59e0b'};color:#000">${p.status}</span>
      </div>
      <p class="muted" style="margin-bottom:12px">${p.desc}</p>
      <div style="margin-bottom:16px">${p.tech.map(t=>`<span class="tag">${t}</span>`).join('')}</div>
      <div style="display:flex;gap:8px">
        ${p.url !== '#' ? `<a class="btn btn-primary" href="${p.url}" target="_blank" style="flex:1;justify-content:center">Live</a>` : ''}
        <a class="btn btn-ghost" href="${p.github}" target="_blank" style="flex:1;justify-content:center">GitHub</a>
      </div>
    </div>
  `).join('');
}).catch(()=>{
  document.getElementById('projectsGrid').innerHTML = '<div class="card glass"><p class="muted">Backend /api/projects loading...</p></div>';
});

// Contact form -> backend API + mailto fallback
document.getElementById('contactForm').onsubmit = async (e)=>{
  e.preventDefault();
  const fd = new FormData(e.target);
  const data = Object.fromEntries(fd.entries());
  const btn = e.target.querySelector('button');
  btn.textContent = 'Sending...';
  btn.disabled = true;

  try{
    const res = await fetch('/api/contact', {
      method:'POST',
      headers:{'Content-Type':'application/json'},
      body: JSON.stringify(data)
    });
    const out = await res.json();
    if(out.success){
      toast(out.message);
      // Mailto fallback
      window.location.href = out.mailto;
      e.target.reset();
    } else {
      toast('Error: ' + out.error);
      // Fallback mailto even on error
      const mailto = `mailto:phantomthedev@proton.me?subject=${encodeURIComponent(data.project + ' - Hiring')}&body=${encodeURIComponent(data.message + '\n\nFrom: ' + data.name + ' (' + data.email + ') Budget: ' + data.budget)}`;
      window.location.href = mailto;
    }
  }catch(err){
    toast('Backend offline, opening email...');
    const mailto = `mailto:phantomthedev@proton.me?subject=${encodeURIComponent(data.project)}&body=${encodeURIComponent(data.message + '\n\nFrom: ' + data.name)}`;
    window.location.href = mailto;
  } finally {
    btn.textContent = 'Send via Backend API →';
    btn.disabled = false;
  }
};
</script>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route("/api/projects")
def projects():
    return jsonify([
        {"id":"tt-downloader","name":"TT Downloader","url":"https://ttdownloader-hraw.onrender.com","github":"https://github.com/phantomthedevss-bit","desc":"High-throughput TikTok downloader API handling millions of requests","tech":["Python","Flask","Render","API"],"status":"live"},
        {"id":"render-keeper","name":"Render Keeper","url":"https://ddos-6g1d.onrender.com","github":"https://github.com/phantomthedevss-bit","desc":"Keep-alive system with precise RPS control (1-20 RPS) for 24/7 uptime","tech":["Python","Threading","Gunicorn"],"status":"live"},
        {"id":"load-tester","name":"Load Tester","url":"#","github":"https://github.com/phantomthedevss-bit","desc":"DDoS simulation & load testing with RPS metrics","tech":["Python","Requests","Security"],"status":"dev"},
        {"id":"sectools","name":"SecTools","url":"#","github":"https://github.com/phantomthedevss-bit","desc":"Cybersecurity toolkit - nmap automation, vuln scanner","tech":["Cybersecurity","Nmap","Pentesting"],"status":"dev"}
    ])

@app.route("/api/contact", methods=["POST"])
def contact():
    try:
        data = request.get_json()
        name = data.get("name","").strip()
        email = data.get("email","").strip()
        msg = data.get("message","").strip()
        if not name or not email or not msg:
            return jsonify({"success":False,"error":"Name, email, message required"}), 400
        
        entry = {
            "name": name, "email": email,
            "project": data.get("project",""), "budget": data.get("budget",""),
            "message": msg, "timestamp": datetime.now().isoformat(),
            "ip": request.remote_addr
        }
        with open(MESSAGES_FILE,"r") as f:
            messages = json.load(f)
        messages.append(entry)
        with open(MESSAGES_FILE,"w") as f:
            json.dump(messages, f, indent=2)
        
        print(f"[CONTACT] {name} <{email}> - {data.get('project')}")
        mailto = f"mailto:{CONTACT_EMAIL}?subject={data.get('project','Hiring')}&body={msg}%0A%0AFrom:%20{name}%20({email})"
        return jsonify({"success":True,"message":f"Message saved! I'll reply to {email} soon.","mailto":mailto})
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"success":False,"error":str(e)}), 500

@app.route("/health")
def health():
    return jsonify({"status":"ok","service":"phantomthedev portfolio","time":datetime.now().isoformat()})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    print(f"SERVER BOOTED - phantomthedev portfolio on port {port}")
    app.run(host="0.0.0.0", port=port)
