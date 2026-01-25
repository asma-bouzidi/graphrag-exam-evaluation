# --------------------
# Base image
# --------------------
FROM node:20-alpine AS base
WORKDIR /app

# --------------------
# Dependencies stage
# --------------------
FROM base AS deps
COPY package.json package-lock.json ./
RUN npm ci

# --------------------
# Build stage
# --------------------
FROM base AS builder
WORKDIR /app

COPY --from=deps /app/node_modules ./node_modules
COPY . .
RUN npm run build

# --------------------
# Production stage
# --------------------
FROM node:20-alpine AS runner
WORKDIR /app

ENV NODE_ENV=production
ENV PORT=3000
ENV HOSTNAME=0.0.0.0

# Copy only what is needed to run
COPY --from=builder /app/.next ./.next
COPY --from=builder /app/public ./public
COPY --from=builder /app/package.json ./package.json
COPY --from=builder /app/node_modules ./node_modules
COPY --from=builder /app/next.config.js ./next.config.js

EXPOSE 3000

CMD ["npm", "start"]
