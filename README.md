# Eclipse Landing Page System 🌙

A powerful, dynamic landing page system designed for creating beautiful community pages on the Yeez platform. This system features automatic asset management, hot-reload development, and a modern design framework.

## 🚀 Quick Start

### Prerequisites
- Python 3.6+
- A web browser
- Basic HTML/CSS knowledge

### 1. Clone or Download
```bash
git clone <your-repo-url>
cd eclipse
```

### 2. Start the Development Server
```bash
python3 server.py
```

The server will start at `http://localhost:8080` with:
- 🚀 Live development server
- 📄 Dynamic HTML serving
- 🔄 Hot-reload (edit files and refresh to see changes)
- ⚡ Automatic asset placeholder replacement

## 📁 Project Structure

```
eclipse/
├── example.html          # Main landing page template
├── server.py            # Python development server
├── package-lock.json    # Dependencies (if needed)
├── public/              # Public assets directory
│   ├── image/           # Images (.jpg, .png, .svg, .gif)
│   ├── video/           # Videos (.mp4, .webm, .mov)
│   ├── logo-example.png # Logo placeholder
│   └── banner-example.png # Banner placeholder
└── settings/
    ├── asset-handler.js  # Automatic asset management
    ├── nav-footer.html   # Navigation/footer templates
    └── navlogo.png       # Navigation logo
```

## 🎨 Creating Your Community Landing Page

### Step 1: Edit the HTML Template

1. **Copy the template:**
   ```bash
   cp example.html my-community.html
   ```

2. **Update community information:**
   ```html
   <!-- Replace these with your community details -->
   <h1>Your Community Name</h1>
   <p class="subtitle">Your Community Tagline</p>
   <p>Your community description here...</p>
   ```

3. **Customize sections:**
   - Hero section with community intro
   - Skills/features your community offers
   - Testimonials from community members
   - Call-to-action buttons

### Step 2: Update Server Configuration

Edit `server.py` to serve your new HTML file:

```python
# Change this line in server.py
HTML_FILE = 'my-community.html'  # Instead of 'example.html'
```

## 🖼️ Asset Management System

The system includes a powerful automatic asset management system that replaces placeholder tags with actual files.

### Static Assets (Fixed Names)

```html
<!-- These automatically map to files in your directories -->
<logo>         <!-- → settings/navlogo.png or public/logo-example.png -->
<banner>       <!-- → public/banner-example.png -->
```

### Dynamic Assets (Auto-Discovery)

```html
<!-- These automatically find files with matching names -->
<image1>       <!-- → public/image/image1.jpg (or .png, .svg, etc.) -->
<image2>       <!-- → public/image/image2.png -->
<video1>       <!-- → public/video/video1.mp4 (or .webm, .mov, etc.) -->
```

### Supported File Types

**Images**: `.png`, `.jpg`, `.jpeg`, `.gif`, `.svg`, `.webp`  
**Videos**: `.mp4`, `.webm`, `.ogg`, `.avi`, `.mov`

### Adding Your Assets

1. **Add images to `public/image/`:**
   ```
   public/image/
   ├── team-photo.jpg      # Use as <image1>
   ├── product-demo.png    # Use as <image2>
   └── founder-avatar.jpg  # Use as <image3>
   ```

2. **Add videos to `public/video/`:**
   ```
   public/video/
   ├── intro-video.mp4     # Use as <video1>
   └── testimonial.webm    # Use as <video2>
   ```

3. **Use in HTML:**
   ```html
   <image1 style="width: 300px; border-radius: 10px;">  
   <video1 style="width: 100%; height: auto;">
   ```

## 🎯 Customizing for Your Community

### 1. Branding
```html
<!-- Update logo and community name -->
<logo style="width: 80px; height: 80px;">
<h1>Your Community Name</h1>
<p class="subtitle">Your Community Mission</p>
```

### 2. Community Description
```html
<p>
  Your community is a [description] for [target audience] looking to [main benefit]. 
  Our goal is to [mission statement].
</p>
```

### 3. Skills/Features Section
```html
<div class="hero-stat">
    <span class="hero-stat-icon">🎯</span>
    <div class="hero-stat-label">Your Skill</div>
    <div class="hero-stat-desc">What members will learn</div>
</div>
```

### 4. Founder/Leader Section
```html
<a href="https://instagram.com/yourhandle" class="founder">
    <image2 class="founder-avatar"></image2>
    By Your Name - Your Title
</a>
```

### 5. Call-to-Action Buttons
```html
<a href="https://yeez.app/auth/signup" class="cta-button">
    Join Your Community
</a>
```

## 🛠️ Development Workflow

### 1. Start Development Server
```bash
python3 server.py
```

### 2. Edit Your Files
- Modify HTML in real-time
- Add new assets to `public/` directories  
- Update styles in the `<style>` section

### 3. Live Preview
- Visit `http://localhost:8080`
- Refresh browser to see changes
- Assets are automatically replaced

### 4. Deploy
When ready, your HTML file can be deployed to any web server or hosting platform.

## 🎨 Design System

The template uses a modern, clean design system with:

### Colors
- **Primary Text**: `#0f172a` (dark slate)
- **Secondary Text**: `#64748b` (slate gray)  
- **Borders**: `#e2e8f0` (light gray)
- **Backgrounds**: `#ffffff` (white) and gradients

### Typography
- **Font**: Inter (system fallback)
- **Headers**: Bold, modern sizing
- **Body**: Clean, readable text

### Components
- **Cards**: Clean white cards with subtle shadows
- **Buttons**: Modern with hover effects and icons
- **Grid**: Responsive layouts that work on all devices

## 📱 Mobile Responsive

The template is fully responsive and includes:
- Mobile-first design approach
- Flexible grid layouts
- Touch-friendly buttons
- Optimized typography for all screen sizes

## 🔧 Advanced Customization

### Custom Styling
Add your own CSS in the `<style>` section:

```css
/* Add your custom styles */
.my-custom-section {
    background: linear-gradient(135deg, #your-colors);
    padding: 60px 0;
}
```

### JavaScript Features
The asset handler runs automatically, but you can extend it:

```javascript
// Access the asset handler
window.assetHandler.updateAsset('logo', 'path/to/new-logo.png');
```

### Server Customization
Modify `server.py` for:
- Different ports: `PORT = 3000`
- Custom HTML files: `HTML_FILE = 'your-page.html'`
- Additional routes or features

## 🌟 Examples

Check out `example.html` for a complete implementation featuring:
- Eclipse Clipping Academy branding
- Professional hero section
- Skills showcase
- Video integration
- Testimonials
- Modern call-to-action

## 🤝 Contributing

Feel free to:
- Submit improvements
- Report bugs
- Share your community pages
- Suggest new features

## 📄 License

This template system is designed for creating Yeez community landing pages. Customize it for your community and help grow the creator economy! 

---

**Ready to build your community landing page?** Start with `python3 server.py` and begin customizing! 🚀
