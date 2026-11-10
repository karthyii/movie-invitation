
import streamlit as st
import streamlit.components.v1 as components

# Set up page configurations
st.set_page_config(page_title="A Special Message For Neethu ❤️", page_icon="💌", layout="centered")

# --- CUSTOM CSS FOR BALOONS ---
st.markdown("""
    <style>
    .reportview-container {
        background-color: #0e1117;
    }
    </style>
""", unsafe_allow_html=True)

# Main Title Headers (Static)
st.markdown("<h1 style='text-align: center; color: #ff4b4b;'>Oii Selfiee... 👀</h1>", unsafe_allow_html=True)

# Interactive Screen Box (Handles both states instantly)
html_code = """
<div id="questionScreen" style="text-align: center; font-family: sans-serif; color: white;">
    <h2 style='font-weight: normal; margin-bottom: 10px;'>നമുക്ക് ഒരു സിനിമ കാണാൻ പോയാലോ ? 🎬</h2>
    <h3 style='font-weight: normal; margin-bottom: 40px; color: #f0f2f6;'>നിനക്ക് എന്ത് തോന്നുന്നു ? 🌹</h3>
    
    <div style="display: flex; justify-content: center; align-items: center; height: 150px; position: relative; width: 100%;">
        <!-- Yes Button: Styled green, hides the question and shows success instantly -->
        <button id="yesBtn" onclick="showSuccess()" 
            style="
                padding: 15px 35px; 
                font-size: 20px; 
                background-color: #28a745; 
                color: white; 
                border: none; 
                border-radius: 10px; 
                cursor: pointer; 
                margin-right: 50px;
                font-weight: bold;
                box-shadow: 0px 4px 10px rgba(0,0,0,0.15);
            ">
            Yes! 💖
        </button>

        <!-- No Button: Moves away as soon as the mouse hovers over it -->
        <button id="noBtn" onmouseover="moveButton()" onclick="moveButton()" style="
                padding: 15px 35px; 
                font-size: 20px; 
                background-color: #dc3545; 
                color: white; 
                border: none; 
                border-radius: 10px; 
                position: absolute; 
                left: 55%;
                font-weight: bold;
                transition: all 0.1s ease;
                box-shadow: 0px 4px 10px rgba(0,0,0,0.15);
            ">
            No 💔
        </button>
    </div>
</div>

<!-- Success Screen: Hidden by default, appears instantly when Yes is clicked -->
<div id="successScreen" style="display: none; text-align: center; font-family: sans-serif; animation: fadeIn 0.5s;">
    <h1 style='color: #ff4b4b; font-size: 40px; margin-bottom: 10px;'>Yayyy! ❤️🥰</h1>
    <h3 style='color: white; font-weight: normal; margin-bottom: 20px;'>അപ്പോ ഓക്കെ, എന്നാ പോവാം ല്ലേ 😍</h3>
    <p style='font-size: 60px; margin: 0;'>💖 👩‍❤️‍👨 💍</p>
</div>

<script>
    function showSuccess() {
        // Toggle display states instantly
        document.getElementById('questionScreen').style.display = 'none';
        document.getElementById('successScreen').style.display = 'block';
    }

    function moveButton() {
        var btn = document.getElementById('noBtn');
        
        // Generate positions constrained to container boundaries
        var x = Math.random() * (window.innerWidth - 160);
        var y = Math.random() * 100;
        
        if (x < 10) x = 10;
        
        btn.style.position = 'absolute';
        btn.style.left = x + 'px';
        btn.style.top = y + 'px';
    }
</script>

<style>
@keyframes fadeIn {
    from { opacity: 0; transform: scale(0.95); }
    to { opacity: 1; transform: scale(1); }
}
</style>
"""

# Render the interface block safely
components.html(html_code, height=400)
