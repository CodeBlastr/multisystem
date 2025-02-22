# Use a lightweight Node.js-based image
FROM node:18-slim

WORKDIR /app

# Copy a simple HTML file to serve
RUN echo '<!DOCTYPE html><html lang="en"><head><title>Hello Frontend</title></head><body><h1>Hello from Frontend!</h1></body></html>' > /app/index.html

# Install a lightweight HTTP server
RUN npm install -g serve

# Use "serve" to serve the static file
CMD ["serve", "-s", ".", "-l", "3000"]
