import streamlit as st
from datetime import datetime
import base64

# Set up page config
st.set_page_config(page_title="For My Love ❤️", page_icon="💍", layout="centered")

# -----------------------------
# CSS & JS (Enhanced Animations)
# -----------------------------
st.markdown("""
<style>
/* Hide Streamlit UI */
#MainMenu, footer, header, [data-testid="stToolbar"] {visibility: hidden; display: none;}

/* Background moving gradient */
.stApp {
    background: linear-gradient(-45deg, #0f0c29, #302b63, #24243e, #1a1a2e);
    background-size: 400% 400%;
    animation: gradientMove 15s ease infinite;
    color: white;
}

@keyframes gradientMove {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

/* Glass card */
.glass {
    background: rgba(255, 255, 255, 0.1);
    padding: 30px;
    border-radius: 20px;
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 255, 255, 0.1);
    box-shadow: 0 8px 32px 0 rgba(255, 105, 180, 0.3);
    text-align: center;
    margin-top: 20px;
}

/* Custom Buttons */
div.stButton > button {
    background: linear-gradient(45deg, #ff4da6, #ff0066);
    color: white;
    border-radius: 50px;
    padding: 10px 25px;
    border: none;
    transition: 0.3s;
    width: 100%;
}
div.stButton > button:hover { transform: translateY(-3px); box-shadow: 0 10px 20px rgba(255, 0, 102, 0.4); }

/* Typewriter */
.typewriter {
    font-family: 'Courier New', Courier, monospace;
    overflow: hidden; 
    border-right: .15em solid #ff4da6;
    white-space: normal;
    margin: 0 auto;
    animation: typing 4s steps(40, end), blink-caret .75s step-end infinite;
}

/* Floating Elements */
.glow-heart { position: fixed; bottom:-10px; font-size:20px; animation: float 10s linear infinite; color:#ff4da6; opacity: 0.6; z-index: -1; }
@keyframes float { 0% {transform:translateY(0) rotate(0deg);} 100% {transform:translateY(-110vh) rotate(360deg);} }

.ring3d { font-size: 80px; animation: spin 4s linear infinite; display: inline-block; }
@keyframes spin { from {transform: rotateY(0deg);} to {transform: rotateY(360deg);} }

</style>

<script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js"></script>
<script>
function petalsFall() {
    var duration = 5 * 1000;
    var animationEnd = Date.now() + duration;
    var defaults = { startVelocity: 30, spread: 360, ticks: 60, zIndex: 0 };
    function randomInRange(min, max) { return Math.random() * (max - min) + min; }
    var interval = setInterval(function() {
        var timeLeft = animationEnd - Date.now();
        if (timeLeft <= 0) { return clearInterval(interval); }
        var particleCount = 50 * (timeLeft / duration);
        confetti(Object.assign({}, defaults, { particleCount, origin: { x: randomInRange(0.1, 0.3), y: Math.random() - 0.2 } }));
        confetti(Object.assign({}, defaults, { particleCount, origin: { x: randomInRange(0.7, 0.9), y: Math.random() - 0.2 } }));
    }, 250);
}
</script>
""", unsafe_allow_html=True)

# -----------------------------
# AUDIO HANDLER
# -----------------------------
# Note: Place 'love_song.mp3' in the same folder as this script.
try:
    with open("love_song.mp3", "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        st.sidebar.markdown(f"""
        <audio id="bgMusic" loop>
          <source src="https://github.com/sanjaybhujel/my-love/blob/main/music.mp3;base64,{b64}" type="audio/mp3">
        </audio>
        <p style="color: pink; font-size: 12px;">🎵 Music is ready</p>
        """, unsafe_allow_html=True)
        if st.sidebar.button("Play/Pause Music"):
            st.sidebar.markdown("<script>var audio = window.parent.document.getElementById('bgMusic'); if (audio.paused) { audio.play(); } else { audio.pause(); }</script>", unsafe_allow_html=True)
except FileNotFoundError:
    st.sidebar.write("🎵 Add 'love_song.mp3' to play music!")

# -----------------------------
# APP LOGIC
# -----------------------------
if "page" not in st.session_state:
    st.session_state.page = "home"

def go_to(page_name):
    st.session_state.page = page_name

# Navigation
if st.session_state.page == "home":
    st.markdown('<div class="glass">', unsafe_allow_html=True)
    st.title("Miles Apart, One Heart ❤️")
    st.write("Even the night sky feels closer when I think of you.")
    if st.button("Enter Our Story 🌙"): go_to("countdown")
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.page == "countdown":
    # Set your specific date here
    meeting_date = datetime(2026, 6, 15, 10, 0) 
    diff = meeting_date - datetime.now()
    
    st.markdown('<div class="glass">', unsafe_allow_html=True)
    st.header("⏳ The Countdown")
    if diff.total_seconds() > 0:
        st.subheader(f"{diff.days} Days : {diff.seconds//3600} Hours")
        st.write("Until I finally hold you in my arms.")
    else:
        st.write("The wait is over. I'm yours.")
    if st.button("See Our Chat 💌"): go_to("chat")
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.page == "chat":
    st.markdown('<div class="glass">', unsafe_allow_html=True)
    st.header("Our Messages 💌")
    st.info("I miss you...")
    st.success("I'm always right here.")
    st.info("Promise?")
    st.success("In every lifetime.")
    if st.button("Read My Heart 💖"): go_to("letter")
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.page == "letter":
    st.markdown('<div class="glass">', unsafe_allow_html=True)
    st.header("My Love...")
    st.markdown('<p class="typewriter">No distance, no timezone, and no ocean could ever silence what I feel for you. You are my peace in the chaos, my light in the dark, and my forever.</p>', unsafe_allow_html=True)
    if st.button("One Last Thing 💍"): go_to("lock")
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.page == "lock":
    st.markdown('<div class="glass">', unsafe_allow_html=True)
    st.header("🔐 Our Secret")
    pwd = st.text_input("Enter the word that defines us...", type="password")
    if pwd.lower() == "forever":
        go_to("proposal")
        st.rerun()
    elif pwd != "":
        st.error("Not quite... think of our promise. 💕")
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.page == "proposal":
    st.markdown('<div class="glass">', unsafe_allow_html=True)
    st.title("Forever Starts Now 💍")
    if st.button("Yes. Always. ❤️"):
        st.balloons()
        st.markdown("<script>petalsFall();</script>", unsafe_allow_html=True)
        st.markdown('<div class="ring3d">💍</div>', unsafe_allow_html=True)
        st.success("You just made my universe complete.")
    st.markdown('</div>', unsafe_allow_html=True)

# Footer Clock
st.markdown("""
<div id="clock" style="text-align:center; font-size:16px; margin-top:30px; color: #ffb3d9;"></div>
<script>
function updateClock() {
    var options = { timeZone:"Asia/Kolkata", hour:'2-digit', minute:'2-digit' };
    var time = new Date().toLocaleTimeString([], options);
    document.getElementById("clock").innerHTML = "Thinking of you at " + time + " 💖";
}
setInterval(updateClock, 1000); updateClock();
</script>
""", unsafe_allow_html=True)

