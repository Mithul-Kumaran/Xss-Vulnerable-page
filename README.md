# 🚨 XSS Vulnerability Demo Page

> **⚠️ Warning:** This is an **intentionally vulnerable** web page created for **educational and testing purposes**.  
> **Do not** deploy this in a production environment!

---

## 🎯 Purpose
This page demonstrates a **Reflected Cross-Site Scripting (XSS)** vulnerability by directly injecting user input into the DOM without sanitization.

---

## 📜 How It Works
1. **User Input** is collected via a form (`GET` request).
2. The entered value is retrieved from the URL query string using JavaScript.
3. The value is **directly inserted into the page using `innerHTML`**.
4. Malicious payloads entered in the input will execute as JavaScript.

---

## 🧩 Vulnerable Code Snippet

```html
<!-- Output box (vulnerable to XSS) -->
<div id="output"></div>

<script>
  window.addEventListener('DOMContentLoaded', () => {
    const params = new URLSearchParams(window.location.search);
    const username = params.get("username");

    if (username) {
      const output = document.getElementById("output");
      output.style.display = "block";
      // ❌ Intentionally vulnerable to XSS
      output.innerHTML = "You entered: " + username;
    }
  });
</script>
