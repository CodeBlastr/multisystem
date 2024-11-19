# Use Node.js base image for development
FROM node:18-alpine

WORKDIR /app

# Copy only the package files for dependency installation
COPY package.json yarn.lock ./

# Install dependencies
RUN yarn install

# Copy the rest of the app's source code
COPY . .

# Expose the port used by the React development server
EXPOSE 3000

# Set polling for file changes (useful in Docker)
ENV CHOKIDAR_USEPOLLING=true

# Run the React development server
CMD ["yarn", "start"]
