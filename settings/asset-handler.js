/**
 * Asset Handler - Manages dynamic asset loading
 * Replaces <logo> and <banner> placeholders with actual image paths
 */

class AssetHandler {
    constructor() {
        this.assets = {
            logo: 'public/logo-example.png',
            banner: 'public/banner-example.png'
        };
        
        // Common file extensions for different media types
        this.videoExtensions = ['mp4', 'webm', 'ogg', 'avi', 'mov'];
        this.imageExtensions = ['png', 'jpg', 'jpeg', 'gif', 'svg', 'webp'];
    }

    /**
     * Initialize asset replacement
     */
    init() {
        this.replacePlaceholders();
        this.replaceDynamicAssets();
        this.setupDynamicLoading();
    }

    /**
     * Replace placeholder tags with actual images
     */
    replacePlaceholders() {
        // Replace <logo> tags
        const logoPlaceholders = document.querySelectorAll('logo');
        logoPlaceholders.forEach(placeholder => {
            const img = this.createImageElement(this.assets.logo, 'Logo');
            // Copy any attributes from the placeholder
            this.copyAttributes(placeholder, img);
            placeholder.parentNode.replaceChild(img, placeholder);
        });

        // Replace <banner> tags
        const bannerPlaceholders = document.querySelectorAll('banner');
        bannerPlaceholders.forEach(placeholder => {
            const img = this.createImageElement(this.assets.banner, 'Banner');
            // Copy any attributes from the placeholder
            this.copyAttributes(placeholder, img);
            placeholder.parentNode.replaceChild(img, placeholder);
        });
    }

    /**
     * Create an image element with proper attributes
     */
    createImageElement(src, alt) {
        const img = document.createElement('img');
        img.src = src;
        img.alt = alt;
        img.style.maxWidth = '100%';
        img.style.height = 'auto';
        return img;
    }

    /**
     * Copy attributes from placeholder to new element
     */
    copyAttributes(from, to) {
        const attributes = from.attributes;
        for (let i = 0; i < attributes.length; i++) {
            const attr = attributes[i];
            to.setAttribute(attr.name, attr.value);
        }
    }

    /**
     * Replace dynamic video and image placeholders
     */
    async replaceDynamicAssets() {
        // Find all elements that match video pattern (video1, video2, etc.)
        const allElements = document.querySelectorAll('*');
        const videoElements = [];
        const imageElements = [];
        
        allElements.forEach(element => {
            const tagName = element.tagName.toLowerCase();
            if (tagName.match(/^video\d+$/)) {
                videoElements.push(element);
            } else if (tagName.match(/^image\d+$/)) {
                imageElements.push(element);
            }
        });
        
        // Replace video elements
        for (const element of videoElements) {
            await this.replaceVideoElement(element);
        }
        
        // Replace image elements
        for (const element of imageElements) {
            await this.replaceImageElement(element);
        }
    }

    /**
     * Replace a video element with actual video tag
     */
    async replaceVideoElement(element) {
        const videoName = element.tagName.toLowerCase(); // e.g., "video1"
        const videoPath = await this.findVideoFile(videoName);
        
        if (videoPath) {
            const video = document.createElement('video');
            video.src = videoPath;
            video.controls = true;
            video.style.maxWidth = '100%';
            video.style.height = 'auto';
            
            // Copy attributes from placeholder
            this.copyAttributes(element, video);
            
            // Replace the placeholder
            element.parentNode.replaceChild(video, element);
        }
    }

    /**
     * Replace an image element with actual img tag
     */
    async replaceImageElement(element) {
        const imageName = element.tagName.toLowerCase(); // e.g., "image1"
        const imagePath = await this.findImageFile(imageName);
        
        if (imagePath) {
            const img = document.createElement('img');
            img.src = imagePath;
            img.alt = imageName;
            img.style.maxWidth = '100%';
            img.style.height = 'auto';
            
            // Copy attributes from placeholder
            this.copyAttributes(element, img);
            
            // Replace the placeholder
            element.parentNode.replaceChild(img, element);
        }
    }

    /**
     * Find video file with common extensions
     */
    async findVideoFile(videoName) {
        for (const ext of this.videoExtensions) {
            const path = `public/video/${videoName}.${ext}`;
            if (await this.fileExists(path)) {
                return path;
            }
        }
        return null;
    }

    /**
     * Find image file with common extensions
     */
    async findImageFile(imageName) {
        for (const ext of this.imageExtensions) {
            const path = `public/image/${imageName}.${ext}`;
            if (await this.fileExists(path)) {
                return path;
            }
        }
        return null;
    }

    /**
     * Check if a file exists
     */
    async fileExists(path) {
        try {
            const response = await fetch(path, { method: 'HEAD' });
            return response.ok;
        } catch (error) {
            return false;
        }
    }

    /**
     * Setup dynamic loading for content that might be added later
     */
    setupDynamicLoading() {
        // Create a MutationObserver to watch for dynamically added content
        const observer = new MutationObserver((mutations) => {
            mutations.forEach((mutation) => {
                if (mutation.type === 'childList') {
                    mutation.addedNodes.forEach((node) => {
                        if (node.nodeType === Node.ELEMENT_NODE) {
                            // Check if the added node contains any placeholder tags
                            const logos = node.querySelectorAll ? node.querySelectorAll('logo') : [];
                            const banners = node.querySelectorAll ? node.querySelectorAll('banner') : [];
                            
                            // Check for dynamic video/image elements
                            const tagName = node.tagName ? node.tagName.toLowerCase() : '';
                            const isDynamicElement = tagName.match(/^(video|image)\d+$/);
                            
                            if (node.tagName === 'LOGO' || node.tagName === 'BANNER' || 
                                logos.length > 0 || banners.length > 0 || isDynamicElement) {
                                this.replacePlaceholders();
                                this.replaceDynamicAssets();
                            }
                        }
                    });
                }
            });
        });

        // Start observing
        observer.observe(document.body, {
            childList: true,
            subtree: true
        });
    }

    /**
     * Update asset paths dynamically
     */
    updateAsset(type, newPath) {
        if (this.assets.hasOwnProperty(type)) {
            this.assets[type] = newPath;
            // Re-run replacement for this asset type
            this.replacePlaceholders();
        }
    }

    /**
     * Get current asset path
     */
    getAsset(type) {
        return this.assets[type] || null;
    }
}

// Global asset handler instance
window.AssetHandler = AssetHandler;

// Auto-initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    window.assetHandler = new AssetHandler();
    window.assetHandler.init();
});

// Also provide a manual initialization function
window.initAssetHandler = function() {
    if (!window.assetHandler) {
        window.assetHandler = new AssetHandler();
    }
    window.assetHandler.init();
}; 