#!/usr/bin/env python3
import http.server
import socketserver
import os
import re
from urllib.parse import urlparse
from pathlib import Path

class DynamicHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/' or self.path == '/index.html':
            self.serve_dynamic_page()
        else:
            # Serve static files normally
            super().do_GET()
    
    def serve_dynamic_page(self):
        try:
            # Load example.html content
            example_content = ""
            example_styles = ""
            
            if os.path.exists('example.html'):
                with open('example.html', 'r', encoding='utf-8') as f:
                    content = f.read()
                    
                # Extract styles from example.html
                style_match = re.search(r'<style>(.*?)</style>', content, re.DOTALL)
                if style_match:
                    example_styles = style_match.group(1)
                
                # Extract body content from example.html  
                body_match = re.search(r'<body[^>]*>(.*?)</body>', content, re.DOTALL)
                if body_match:
                    example_content = body_match.group(1)
                else:
                    # If no body tag, use everything between style tags and end
                    example_content = re.sub(r'<style>.*?</style>', '', content, flags=re.DOTALL)
                    example_content = re.sub(r'<!DOCTYPE html>.*?<head>.*?</head>', '', example_content, flags=re.DOTALL)
                    example_content = example_content.replace('<html>', '').replace('</html>', '')
                    example_content = example_content.replace('<body>', '').replace('</body>', '')
            
            # Process asset placeholders
            example_content = self.process_assets(example_content)
            
            # Create complete page with navigation and footer
            html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Yeez Landing Page</title>
    <style>
        body {{
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
            margin: 0;
            padding: 0;
            padding-top: 80px;
        }}
        
        .navbar {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 24px 16px;
            background-color: white;
            width: 100%;
            box-sizing: border-box;
            position: fixed;
            top: 0;
            left: 0;
            z-index: 1000;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
        }}
        
        .navbar-logo {{
            display: flex;
            align-items: center;
        }}
        
        .navbar-logo img {{
            height: 32px;
            width: auto;
            max-width: 120px;
        }}
        
        .navbar-auth {{
            color: #1f2937;
            font-weight: 500;
            font-size: 14px;
            text-decoration: none;
            cursor: pointer;
            transition: color 0.2s ease;
        }}
        
        .navbar-auth:hover {{
            color: #06b6d4;
        }}
        
        .page-footer {{
            padding: 24px 16px;
            border-top: 1px solid #e5e7eb;
            background-color: white;
            width: 100%;
            box-sizing: border-box;
        }}
        
        .footer-content {{
            max-width: 1280px;
            margin: 0 auto;
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 24px;
        }}
        
        .footer-link {{
            font-size: 12px;
            color: #6b7280;
            text-decoration: none;
            transition: color 0.2s ease;
        }}
        
        .footer-link:hover {{
            color: #374151;
        }}
        
        .footer-separator {{
            font-size: 12px;
            color: #d1d5db;
        }}
        
        {example_styles}
    </style>
</head>
<body>
    <!-- Navigation -->
    <nav class="navbar">
        <div class="navbar-logo">
            <img src="settings/navlogo.png" alt="YEEZ" />
        </div>
        <div>
            <a href="/auth/login" class="navbar-auth">Login / Sign Up</a>
        </div>
    </nav>

    <!-- Dynamic Content from example.html -->
    {example_content}

    <!-- Footer -->
    <footer class="page-footer">
        <div class="footer-content">
            <a href="/privacy" class="footer-link">Privacy Policy</a>
            <span class="footer-separator">•</span>
            <a href="/tos" class="footer-link">Terms of Service</a>
        </div>
    </footer>
</body>
</html>"""
            
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(html.encode('utf-8'))
            
        except Exception as e:
            print(f"Error serving page: {e}")
            self.send_error(500, f"Server Error: {e}")
    
    def process_assets(self, content):
        """Replace asset placeholders with actual files"""
        
        # Replace <logo> with actual logo
        logo_files = ['public/logo-example.png', 'settings/navlogo.png']
        for logo_file in logo_files:
            if os.path.exists(logo_file):
                content = re.sub(r'<logo([^>]*)>', f'<img src="{logo_file}"\\1>', content)
                break
        
        # Replace <banner> with actual banner
        banner_files = ['public/banner-example.png']
        for banner_file in banner_files:
            if os.path.exists(banner_file):
                content = re.sub(r'<banner([^>]*)>', f'<img src="{banner_file}"\\1>', content)
                break
        
        # Replace <video1>, <video2>, etc.
        video_pattern = r'<(video\d+)([^>]*)>'
        def replace_video(match):
            video_name = match.group(1)  # e.g., "video1"
            attrs = match.group(2)       # attributes
            
            # Check for video files with common extensions
            for ext in ['mp4', 'webm', 'ogg', 'avi', 'mov']:
                video_path = f'public/video/{video_name}.{ext}'
                if os.path.exists(video_path):
                    return f'<video src="{video_path}" controls{attrs}></video>'
            
            # Fallback: return placeholder
            return f'<div style="background: #f0f0f0; padding: 20px; text-align: center; border-radius: 8px;"{attrs}>Video: {video_name}</div>'
        
        content = re.sub(video_pattern, replace_video, content)
        
        # Replace <image1>, <image2>, etc.
        image_pattern = r'<(image\d+)([^>]*)>'
        def replace_image(match):
            image_name = match.group(1)  # e.g., "image1"
            attrs = match.group(2)       # attributes
            
            # Check for image files with common extensions
            for ext in ['png', 'jpg', 'jpeg', 'gif', 'svg', 'webp']:
                image_path = f'public/image/{image_name}.{ext}'
                if os.path.exists(image_path):
                    return f'<img src="{image_path}"{attrs}>'
            
            # Fallback: return placeholder
            return f'<div style="background: #e0e0e0; padding: 20px; text-align: center; border-radius: 8px;"{attrs}>Image: {image_name}</div>'
        
        content = re.sub(image_pattern, replace_image, content)
        
        return content

def run_server(port=8080):
    handler = DynamicHandler
    with socketserver.TCPServer(("", port), handler) as httpd:
        print(f"🚀 Server running at http://localhost:{port}")
        print(f"📄 Dynamically serving content from example.html")
        print(f"🔄 Edit example.html and refresh to see changes")
        print(f"⚡ Asset placeholders automatically replaced")
        print(f"🛑 Press Ctrl+C to stop")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n✅ Server stopped")

if __name__ == "__main__":
    run_server() 