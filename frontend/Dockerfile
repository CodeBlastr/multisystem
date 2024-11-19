# Use Node.js LTS as the base image
FROM node:16-alpine

# Set the working directory
WORKDIR /app

# Copy package.json and yarn.lock first
COPY package.json ./

# Install dependencies
RUN yarn install

# Add node_modules/.bin to PATH
ENV PATH /app/node_modules/.bin:$PATH

# Copy the rest of the application
COPY . .

# Expose the development server port
EXPOSE 3000

# Use development mode by default
CMD ["sh", "-c", "yarn dev"]
