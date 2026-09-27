import os
import sys
import time
import re
import socket
import subprocess

# Ensure UTF-8 output if possible, otherwise fallback gracefully
if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

def pr(msg=""):
    print(msg, flush=True)

def is_port_in_use(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('127.0.0.1', port)) == 0

def copy_to_clipboard(text):
    try:
        p = subprocess.Popen(['clip'], stdin=subprocess.PIPE, shell=True)
        p.communicate(input=text.strip().encode('utf-8'))
    except Exception:
        pass

def main():
    pr("\n" + "="*70)
    pr("   TERA PULSE - Live Prototype WhatsApp Link Generator")
    pr("="*70)
    
    proj_dir = os.path.dirname(os.path.abspath(__file__))
    cloudflared_path = os.path.join(proj_dir, "cloudflared.exe")
    venv_python = os.path.join(proj_dir, "venv", "Scripts", "python.exe")
    
    if os.path.exists(venv_python):
        py_bin = venv_python
    else:
        py_bin = sys.executable

    if not os.path.exists(cloudflared_path):
        pr(f"[!] Error: {cloudflared_path} not found!")
        sys.exit(1)

    flask_proc = None
    if not is_port_in_use(5000):
        pr("[1/2] Local server start ho raha hai...")
        app_script = os.path.join(proj_dir, "web", "app.py")
        flask_proc = subprocess.Popen(
            [py_bin, app_script],
            cwd=proj_dir,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        # Wait for port 5000 to be open
        server_ready = False
        for _ in range(40):
            if is_port_in_use(5000):
                server_ready = True
                break
            time.sleep(0.5)
        
        if not server_ready:
            pr("[!] Local server start hone me dikkat aayi. Check requirements.")
            if flask_proc: flask_proc.terminate()
            return
        pr("      Local server active on http://127.0.0.1:5000")
    else:
        pr("[1/2] Local server pehle se port 5000 par running hai.")

    pr("[2/2] Public Cloudflare link generate ho rahi hai (5-10 sec)...")
    cf_cmd = [cloudflared_path, "tunnel", "--url", "http://127.0.0.1:5000"]
    cf_proc = subprocess.Popen(
        cf_cmd,
        cwd=proj_dir,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        bufsize=1,
        encoding="utf-8",
        errors="replace"
    )

    tunnel_url = None
    pattern = re.compile(r"https://[a-zA-Z0-9-]+\.trycloudflare\.com")

    for line in cf_proc.stdout:
        match = pattern.search(line)
        if match:
            tunnel_url = match.group(0)
            break

    if not tunnel_url:
        pr("[!] Link generate karne me problem aayi. Internet connection check karein.")
        if flask_proc: flask_proc.terminate()
        cf_proc.terminate()
        return

    # Auto copy to clipboard
    copy_to_clipboard(tunnel_url)

    pr("\n" + "#"*70)
    pr("  >>> LINK TAYYAR HAI! (Direct Clipboard pe Copy ho chuki hai!) <<<")
    pr("#"*70)
    pr(f"\n      LINK: {tunnel_url}\n")
    pr("#"*70)
    pr("  * WhatsApp me jao aur bas Ctrl + V (Paste) karke send kar do!")
    pr("  * DHYAN RAKHEIN: Jab tak ye terminal khula rahega, link chalegi.")
    pr("  * Band karne ke liye keyboard par Ctrl + C dabayein.")
    pr("#"*70 + "\n")

    try:
        cf_proc.wait()
    except KeyboardInterrupt:
        pr("\nStopping server & link...")
    finally:
        cf_proc.terminate()
        if flask_proc:
            flask_proc.terminate()
        pr("Link closed successfully.")

if __name__ == "__main__":
    main()
