import streamlit as st
from datetime import datetime
import base64
import random

# Set up page config
st.set_page_config(page_title="For My Love ❤️", page_icon="💍", layout="centered")

# -----------------------------
# CSS & JS (All Effects + Responsive)
# -----------------------------
st.markdown("""
<style>

/* Hide Streamlit UI */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
[data-testid="stToolbar"] {display: none;}

/* Background moving gradient with image */
.stApp {
    background: linear-gradient(-45deg, #0f0c29, #302b63, #24243e, #1a1a2e), url('your_image.jpg');
    background-size: cover;
    background-position: center;
    animation: gradientMove 15s ease infinite;
    color: white;
}

/* Gradient animation */
@keyframes gradientMove {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

/* Glass card */
.glass {
    background: rgba(255, 255, 255, 0.08);
    padding: 40px;
    border-radius: 25px;
    backdrop-filter: blur(15px);
    box-shadow: 0px 0px 40px rgba(255, 105, 180, 0.4);
    text-align: center;
}

/* Buttons */
.stButton>button {
    background: linear-gradient(45deg, #ff4da6, #ff0066);
    color: white;
    border-radius: 25px;
    height: 3em;
    font-size: 18px;
    border: none;
    transition: 0.3s;
}
.stButton>button:hover { transform: scale(1.1); }

/* Chat bubbles */
.chat-left { background: #2d2d44; padding: 12px 18px; border-radius: 15px; margin: 10px 0; text-align: left; }
.chat-right { background: #ff0066; padding: 12px 18px; border-radius: 15px; margin: 10px 0; text-align: right; }

/* Typing animation */
.typewriter { overflow: hidden; border-right: .15em solid pink; white-space: nowrap; margin: 0 auto; letter-spacing: .05em; animation: typing 6s steps(60,end), blink .75s step-end infinite; }
@keyframes typing { from { width:0 } to { width:100% } }
@keyframes blink { from, to { border-color: transparent } 50% { border-color: pink; } }

/* Floating glowing hearts */
@keyframes floatHearts {0% {transform:translateY(0) scale(1); opacity:1;} 100% {transform:translateY(-100vh) scale(1.5); opacity:0;}}
.glow-heart { position: fixed; bottom:-10px; font-size:20px; animation: floatHearts 10s linear infinite; color:#ff4da6; text-shadow: 0 0 10px #ff4da6,0 0 20px #ff1a75; }
.glow-heart:nth-child(1) { left:15%; animation-duration: 8s; }
.glow-heart:nth-child(2) { left:35%; animation-duration: 12s; }
.glow-heart:nth-child(3) { left:60%; animation-duration: 10s; }
.glow-heart:nth-child(4) { left:80%; animation-duration: 14s; }

/* Stars */
.stars { position: fixed; width:100%; height:100%; background: transparent; overflow:hidden; top:0; left:0; z-index:-1; }
.stars::after { content:""; position:absolute; width:2px; height:2px; background:white; box-shadow:100px 200px white, 300px 400px white, 500px 100px white, 700px 300px white, 900px 500px white, 1200px 250px white, 1400px 450px white, 1600px 150px white; animation: twinkle 3s infinite alternate;}
@keyframes twinkle { from{opacity:0.3} to{opacity:1} }

/* Shooting star */
.shooting-star { position: fixed; width: 2px; height: 100px; background: linear-gradient(-45deg, white, transparent); opacity:0.8; transform: rotate(45deg); animation: shoot 1s linear forwards; z-index:9999; }
@keyframes shoot { 0% { transform: translate(0,0) rotate(45deg); opacity:1; } 100% { transform: translate(600px,600px) rotate(45deg); opacity:0; } }

/* 3D Ring */
.ring3d { font-size:90px; display:inline-block; animation: spin 3s linear infinite, glowRing 2s infinite alternate; }
@keyframes spin { from { transform: rotateY(0deg); } to { transform: rotateY(360deg); } }
@keyframes glowRing { from { text-shadow:0 0 10px gold;} to{ text-shadow:0 0 40px hotpink; } }

/* Intro screen */
#introScreen { position: fixed; top:0; left:0; width:100%; height:100%; background: radial-gradient(circle at center, #0f0c29, #000); color:white; display:flex; justify-content:center; align-items:center; flex-direction:column; z-index:99999; animation: fadeOut 3s ease 4s forwards; }
@keyframes fadeOut { to { opacity:0; visibility:hidden; } }
.intro-text { font-size:40px; letter-spacing:4px; animation: glow 2s infinite alternate; }
@keyframes glow { from{ text-shadow:0 0 10px pink;} to{ text-shadow:0 0 30px hotpink;} }

/* Mobile touch sparkles */
.sparkle { position: fixed; width:8px; height:8px; background:pink; border-radius:50%; pointer-events:none; animation:sparkleAnim 0.8s linear forwards; box-shadow:0 0 10px white,0 0 20px hotpink; }
@keyframes sparkleAnim { 0%{transform:scale(1);opacity:1;} 100%{transform:scale(3);opacity:0;} }

/* Rose petals */
.petal { position: fixed; top:-10px; font-size:20px; animation: fall 5s linear forwards; }

@keyframes fall { 0%{transform:translateY(0) rotate(0deg);opacity:1;} 100%{transform:translateY(100vh) rotate(360deg);opacity:0;} }

/* --------- Mobile Responsiveness --------- */
@media only screen and (max-width: 768px) {
    .glass { padding: 20px !important; border-radius: 15px !important; }
    h1 { font-size: 24px !important; }
    h2 { font-size: 22px !important; }
    h3 { font-size: 20px !important; }
    .stButton>button { font-size: 16px !important; height: 2.5em !important; }
    .glow-heart { font-size: 16px !important; }
    .ring3d { font-size: 60px !important; }
    .typewriter { font-size: 16px !important; }
    .intro-text { font-size: 28px !important; }
    .chat-left, .chat-right { font-size: 14px !important; padding: 10px 14px !important; }
    #clock { font-size: 18px !important; }
}

body, .stApp { overflow-x: hidden; }

</style>

<div class="stars"></div>
<div class="glow-heart">💖</div>
<div class="glow-heart">💗</div>
<div class="glow-heart">💘</div>
<div class="glow-heart">💞</div>

<div id="introScreen">
  <div class="intro-text">A Love Written in the Stars ✨</div>
</div>

<script>
function randomStar(){const star=document.createElement("div"); star.className="shooting-star"; star.style.left=Math.random()*window.innerWidth+"px"; star.style.top=Math.random()*window.innerHeight/2+"px"; document.body.appendChild(star); setTimeout(()=>star.remove(),1000);}
setInterval(randomStar,30000);

document.addEventListener("click",function(e){
  const sparkle=document.createElement("div");
  sparkle.className="sparkle";
  sparkle.style.left=e.pageX+"px";
  sparkle.style.top=e.pageY+"px";
  document.body.appendChild(sparkle);
  setTimeout(()=>sparkle.remove(),800);
});

function petalsFall(){for(let i=0;i<20;i++){const petal=document.createElement("div");petal.className="petal";petal.innerHTML="🌹";petal.style.left=Math.random()*window.innerWidth+"px";document.body.appendChild(petal);setTimeout(()=>petal.remove(),5000);}}
</script>
""", unsafe_allow_html=True)

# -----------------------------
# BACKGROUND MUSIC (fade-in)
# -----------------------------
try:
    with open("love_song.mp3","rb") as f:
        data=f.read()
        b64=base64.b64encode(data).decode()
    st.markdown(f"""
    <audio id="bgMusic" autoplay loop>
      <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
    </audio>
    <script>
    var audio = document.getElementById("bgMusic");
    audio.volume = 0;
    var fade = setInterval(function () {{
        if (audio.volume < 0.8) {{ audio.volume += 0.02; }} else {{ clearInterval(fade); }}
    }}, 200);
    </script>
    """, unsafe_allow_html=True)
except:
    pass

# -----------------------------
# SESSION STATE
# -----------------------------
if "page" not in st.session_state: st.session_state.page = "home"

# -----------------------------
# HOME PAGE
# -----------------------------
if st.session_state.page=="home":
    st.markdown('<div class="glass">', unsafe_allow_html=True)
    st.title("Miles Apart, One Heart ❤️")
    st.write("Even the night sky feels closer when I think of you.")
    if st.button("Enter Our Story 🌙"):
        st.session_state.page="countdown"
    st.markdown('</div>', unsafe_allow_html=True)

# -----------------------------
# COUNTDOWN PAGE
# -----------------------------
elif st.session_state.page=="countdown":
    meeting_date = datetime(2026,6,15,10,0,0) # CHANGE
    now = datetime.now()
    diff = meeting_date - now
    st.markdown('<div class="glass">', unsafe_allow_html=True)
    st.header("⏳ Countdown Until I Hold You")
    if diff.total_seconds()>0:
        st.write(f"{diff.days} days left until I finally see you.")
    else:
        st.write("You're here. And I'm never letting go.")
    if st.button("See Our Chat 💌"):
        st.session_state.page="chat"
    st.markdown('</div>', unsafe_allow_html=True)

# -----------------------------
# CHAT PAGE
# -----------------------------
elif st.session_state.page=="chat":
    st.markdown('<div class="glass">', unsafe_allow_html=True)
    st.header("Our Messages 💌")
    st.markdown('<div class="chat-left">I miss you…</div>', unsafe_allow_html=True)
    st.markdown('<div class="chat-right">I’m always right here.</div>', unsafe_allow_html=True)
    st.markdown('<div class="chat-left">Promise?</div>', unsafe_allow_html=True)
    st.markdown('<div class="chat-right">In every lifetime.</div>', unsafe_allow_html=True)
    if st.button("Read My Heart 💖"):
        st.session_state.page="letter"
    st.markdown('</div>', unsafe_allow_html=True)

# -----------------------------
# LOVE LETTER
# -----------------------------
elif st.session_state.page=="letter":
    st.markdown('<div class="glass">', unsafe_allow_html=True)
    st.header("My Love...")
    st.markdown("""
    <div class="typewriter">
    No distance, no timezone, no ocean could ever silence what I feel for you.
    You are my peace in chaos, my light in the dark, my forever.
    </div>
    """, unsafe_allow_html=True)
    if st.button("One Last Thing 💍"):
        st.session_state.page="proposal_lock"
    st.markdown('</div>', unsafe_allow_html=True)

# -----------------------------
# SECRET PASSWORD
# -----------------------------
elif st.session_state.page=="proposal_lock":
    st.markdown('<div class="glass">', unsafe_allow_html=True)
    st.header("🔐 One Last Secret")
    password = st.text_input("Enter the word that defines us...")
    if password.lower() == "forever":  # CHANGE
        st.session_state.page="proposal"
    elif password != "":
        st.error("That’s not our word… try again 💕")
    st.markdown('</div>', unsafe_allow_html=True)

# -----------------------------
# PROPOSAL PAGE
# -----------------------------
elif st.session_state.page=="proposal":
    st.markdown('<div class="glass">', unsafe_allow_html=True)
    st.title("Forever Starts Now 💍")
    if st.button("Yes. Always. ❤️"):
        st.markdown("<script>petalsFall(); triggerConfetti();</script>", unsafe_allow_html=True)
        st.markdown('<div class="ring3d">💍</div>', unsafe_allow_html=True)
        st.balloons()
        st.success("You just made my universe complete.")
    st.markdown('</div>', unsafe_allow_html=True)

# -----------------------------
# REAL-TIME CLOCK
# -----------------------------
st.markdown("""
<div id="clock" style="text-align:center; font-size:22px; margin-top:20px;"></div>
<script>
function updateClock() {
  var options = { timeZone:"Asia/Kolkata", hour:'2-digit', minute:'2-digit', second:'2-digit'};
  var time = new Date().toLocaleTimeString([], options);
  document.getElementById("clock").innerHTML = "Right now in your world… it’s "+time+" 💖<br>I’m thinking of you.";
}
setInterval(updateClock,1000); updateClock();
</script>
""", unsafe_allow_html=True)