FROM node:18-alpine

WORKDIR /app

# Install backend dependencies
COPY server/package*.json ./server/
RUN cd server && npm install --production

# Copy entire project
COPY . .

EXPOSE 3000

CMD ["node", "server/server.js"]
